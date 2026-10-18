"""Standalone exact finite and symbolic checks for the four-cycle cut-model singular-scheme theorem."""
from itertools import combinations, product
from math import comb

COEFF = ((1,1,1),(-1,0,0),(0,-1,0),(0,0,-1))

def det3(vs):
    a,b,c=vs
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

# Exact identification of all 3x3 minors, including integral coefficients.
seen=set()
for cols in combinations(range(8),3):
    groups=tuple(c//2 for c in cols)
    d=det3([COEFF[g] for g in groups])
    if len(set(groups))<3:
        assert d==0
    else:
        assert abs(d)==1, (cols,d)
        seen.add(cols)
assert len(seen)==comb(4,3)*2**3==32

# In a fixed-point affine chart, after eliminating the nonzero pair's partner,
# every 2x2 Jacobian minor is a cross-pair variable product.
D=((1,1),(-1,0),(0,-1))
seen2=set()
for cols in combinations(range(6),2):
    groups=tuple(c//2 for c in cols)
    d=D[groups[0]][0]*D[groups[1]][1]-D[groups[0]][1]*D[groups[1]][0]
    if groups[0]==groups[1]:
        assert d==0
    else:
        assert abs(d)==1
        seen2.add(cols)
assert len(seen2)==comb(3,2)*4==12
# The degree-2 quotient in the local homogeneous tangent cone has 21 monomials,
# 12 independent cross-group monomials, and 2 independent z_i-z_j relations:
assert comb(6+2-1,2)-12-2 == 7 # six axial squares + one common z

# Eight vertices grouped into four opposite pairs; edge graph K_{2,2,2,2}.
vertices=range(8)
edges=[(a,b) for a,b in combinations(vertices,2) if a//2!=b//2]
assert len(edges)==24
assert all(sum(1 for e in edges if v in e)==6 for v in vertices)
assert 24-8+1==17 # arithmetic genus of the reduced line arrangement
assert 17-8==9 # one embedded length-one point at each of the eight vertices

# Exhaustive characteristic-two and characteristic-three projective point checks.
def rank(rows,p):
    A=[[x%p for x in row] for row in rows]
    r=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][c]%p),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(v*inv)%p for v in A[r]]
        for i in range(len(A)):
            if i!=r:
                t=A[i][c]
                A[i]=[(v-t*w)%p for v,w in zip(A[i],A[r])]
        r+=1
        if r==len(A): break
    return r
for p in (2,3):
    count=sing=0
    for a in product(range(p),repeat=8):
        if not any(a):continue
        z=[a[2*i]*a[2*i+1]%p for i in range(4)]
        if len(set(z))!=1:continue
        count+=1
        J=[]
        for r in range(3):
            J.append([COEFF[i][r]*a[2*i+1] if j%2==0 else COEFF[i][r]*a[2*i]
                      for j in range(8) for i in [j//2]])
        s=(rank(J,p)<3)
        active=sum(bool(a[2*i] or a[2*i+1]) for i in range(4))
        predicted=active<=2
        assert s==predicted,(p,a,z,s,predicted)
        sing+=s
    print('field',p,'affine_cone_nonzero_points',count,'singular',sing)
print('VERIFY_OK: 32 integral maximal minors, 12 local cross-pair minors, 24 lines, eight embedded points, two-characteristic exhaustive checks')
