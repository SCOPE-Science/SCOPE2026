"""Exact arithmetic for two characteristic-two Weddle quartics over F_16.
Only Python's standard library is required.
Field integer encoding: bit i is coefficient of theta^i; theta^4=theta+1.
"""
from itertools import product, permutations, combinations
from math import comb

Q = 16
IRR = 0b10011

def mult(x, y):
    z = 0
    while y:
        if y & 1:
            z ^= x
        y >>= 1
        x <<= 1
        if x & Q:
            x ^= IRR
    return z

def power(x, n):
    v = 1
    while n:
        if n & 1:
            v = mult(v, x)
        x = mult(x, x)
        n >>= 1
    return v

def inv(x):
    assert x
    return power(x, 14)

def determinant(matrix):
    # Characteristic two: permanent equals determinant.
    out = 0
    for perm in permutations(range(len(matrix))):
        z = 1
        for i, j in enumerate(perm):
            z = mult(z, matrix[i][j])
        out ^= z
    return out

def matrix_at(a, b, c, d, x, y, z, w):
    return [
        [mult(a, mult(y, mult(z, w))), x, 1, a],
        [mult(b, mult(x, mult(z, w))), y, 1, b],
        [mult(c, mult(x, mult(y, w))), z, 1, c],
        [mult(d, mult(x, mult(y, z))), w, 1, d],
    ]

def dense_poly(a, b, c, d):
    # Independent coefficient expansion of the polynomial determinant.
    # Entry: (field coefficient, homogeneous exponent vector).
    zeros = (0, 0, 0, 0)
    mat = [
        [(a, (0,1,1,1)),(1,(1,0,0,0)),(1,zeros),(a,zeros)],
        [(b, (1,0,1,1)),(1,(0,1,0,0)),(1,zeros),(b,zeros)],
        [(c, (1,1,0,1)),(1,(0,0,1,0)),(1,zeros),(c,zeros)],
        [(d, (1,1,1,0)),(1,(0,0,0,1)),(1,zeros),(d,zeros)],
    ]
    out = {}
    for perm in permutations(range(4)):
        coeff, exp = 1, [0,0,0,0]
        for i,j in enumerate(perm):
            t,e = mat[i][j]
            coeff = mult(coeff,t)
            for k in range(4):exp[k] += e[k]
        e = tuple(exp)
        out[e] = out.get(e,0) ^ coeff
    return {e:v for e,v in out.items() if v}

def eval_poly(p,coords):
    accum = 0
    powers = [[1,x,mult(x,x),power(x,3),power(x,4)] for x in coords]
    for exp,coeff in p.items():
        val=coeff
        for j,e in enumerate(exp):val=mult(val,powers[j][e])
        accum ^= val
    return accum

def projective_points():
    for first in range(4):
        for suffix in product(range(Q),repeat=3-first):
            yield (0,)*first+(1,)+suffix

def local_coeffs(p,point):
    # Homogeneous polynomial in x,y,z,w; affine local coordinates
    # x=A+u,y=B+v,z=C+r,w=D. Extract degree >= 2.
    A,B,C,D=point
    out={}
    for exp,coeff in p.items():
        start=mult(coeff,power(D,exp[3]))
        options=[]
        for e,t in zip(exp[:3],(A,B,C)):
            options.append([(k,mult(comb(e,k)%2,power(t,e-k)))
                            for k in range(e+1) if comb(e,k)%2])
        for triple in product(*options):
            ex=tuple(e for e,_ in triple)
            value=start
            for _,t in triple:value=mult(value,t)
            out[ex]=out.get(ex,0)^value
    return {e:v for e,v in out.items() if v}

def poly2_mul(p,r):
    out={}
    for (i,j),c in p.items():
        for (k,l),d in r.items():
            idx=(i+k,j+l)
            out[idx]=out.get(idx,0)^mult(c,d)
    return {e:v for e,v in out.items() if v}

def cubic_on_tangent(local):
    assert all(v==0 for e,v in local.items() if sum(e)<2)
    assert all(not(v) for e,v in local.items() if sum(e)==2 and e not in [(2,0,0),(0,2,0),(0,0,2)])
    tangent=[power(local.get(e,0),8) for e in [(2,0,0),(0,2,0),(0,0,2)]]
    assert tangent[0] # true in the two examples
    # Solve L(u,v,r)=0 by v=s, r=t.
    l0=inv(tangent[0])
    linear=[{(1,0):mult(tangent[1],l0),(0,1):mult(tangent[2],l0)},
            {(1,0):1}, {(0,1):1}]
    res={}
    for (i,j,k),coeff in local.items():
        if i+j+k!=3:continue
        term={(0,0):coeff}
        for degree,lin in zip((i,j,k),linear):
            for _ in range(degree):term=poly2_mul(term,lin)
        for e,v in term.items():res[e]=res.get(e,0)^v
    coeffs=[res.get((3,0),0),res.get((2,1),0),res.get((1,2),0),res.get((0,3),0)]
    A,B,C,D=coeffs
    roots=[(1,t) for t in range(Q) if A^mult(B,t)^mult(C,mult(t,t))^mult(D,power(t,3))==0]
    if D==0:roots.append((0,1))
    return tangent,coeffs,roots

def check_general_position(parameters):
    a,b,c,d=parameters
    points=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,1,1,1),tuple(parameters)]
    for indices in combinations(range(6),4):
        m=[[points[j][i] for j in indices] for i in range(4)]
        assert determinant(m)!=0,(indices,parameters)

def run(parameters,expected_W,expected_tangent,expected_binary,expected_N):
    check_general_position(parameters)
    p=dense_poly(*parameters)
    assert len(p)>=12
    point=tuple(power(x,8) for x in parameters)
    assert eval_poly(p,point)==0
    local=local_coeffs(p,point)
    tangent,binary,roots=cubic_on_tangent(local)
    assert tangent==expected_tangent,(tangent,expected_tangent)
    assert binary==expected_binary,(binary,expected_binary)
    assert len(roots)==expected_N,(roots,expected_N)
    count_det=count_poly=0
    for coords in projective_points():
        val_det=determinant(matrix_at(*parameters,*coords))
        val_poly=eval_poly(p,coords)
        assert val_det==val_poly,(parameters,coords)
        count_det += val_det==0
        count_poly += val_poly==0
    assert count_det==count_poly==expected_W
    # The geometric minimal resolution has six rational A1 fibers and a D4
    # fiber with one central component and N rational arms; see mathematical proof.
    resolution_points=count_det+16*(6+1+len(roots))
    print('PARAMETERS',parameters,'W_POINTS',count_det,'D4_ARMS_RATIONAL',len(roots),
          'BINARY_CUBIC',binary,'TANGENT',tangent,'ROOTS',roots,
          'RESOLUTION_POINTS',resolution_points)
    return resolution_points

if __name__=='__main__':
    x=run((1,8,2,7),417,[11,11,14],[2,4,3,9],1)
    y=run((3,11,1,15),449,[9,2,2],[0,4,2,0],3)
    assert (x,y)==(545,609)
    assert y==16**2+22*16+1
    print('VERIFY_OK')
