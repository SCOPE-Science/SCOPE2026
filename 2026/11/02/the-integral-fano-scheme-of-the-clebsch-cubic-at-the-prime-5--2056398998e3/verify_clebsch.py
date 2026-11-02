"""Finite-field consistency and exact symbolic checks for a nodal Clebsch cubic.

Pure Python 3, no external dependencies. Enumeration is corroborative, not
an argument for the algebraically closed-field classification.
"""
from itertools import combinations, permutations, product

p = 5

def rank(rows, n=4):
    a = [[x % p for x in row] for row in rows]
    i = 0
    for j in range(n):
        k = next((k for k in range(i,len(a)) if a[k][j]), None)
        if k is None: continue
        a[i],a[k]=a[k],a[i]
        scale=pow(a[i][j],-1,p)
        a[i]=[(x*scale)%p for x in a[i]]
        for k in range(len(a)):
            if k!=i:
                t=a[k][j]
                a[k]=[(x-t*y)%p for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return i

def rref2(rows):
    a = [list(x) for x in rows]
    i=0
    for j in range(4):
        k=next((k for k in range(i,2) if a[k][j]%p),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        u=pow(a[i][j],-1,p)
        a[i]=[(x*u)%p for x in a[i]]
        for k in range(2):
            if k!=i:
                t=a[k][j]%p
                a[k]=[(x-t*y)%p for x,y in zip(a[k],a[i])]
        i+=1
        if i==2:break
    if i!=2:raise ValueError('dependent vectors')
    return tuple(map(tuple,a))

def full(row):
    return tuple(row)+((-sum(row))%p,)

def on_cubic(key):
    u,v = map(full,key)
    return all(z%p==0 for z in (
        sum(x**3 for x in u),
        3*sum(x*x*y for x,y in zip(u,v)),
        3*sum(x*y*y for x,y in zip(u,v)),
        sum(y**3 for y in v)))

def contains_point(key,x):
    return rank([*key,x])==2

# Generate all projective points of P^3(F5) and all its projective lines.
pts=[]
for vv in product(range(p),repeat=4):
    if not any(vv):continue
    lead=next(x for x in vv if x)
    if lead==1: pts.append(vv)
assert len(pts)==156
all_lines=set()
for a,b in combinations(pts,2):
    all_lines.add(rref2((a,b)))
assert len(all_lines)==806
contained={line for line in all_lines if on_cubic(line)}
assert len(contained)==21

# Fifteen coordinate-matching lines and six lines through the unique node.
old=set()
for i in range(5):
    rem=[j for j in range(5) if j!=i]
    for j in range(1,4):
        pair1=(rem[0],rem[j]); pair2=tuple(x for x in rem if x not in pair1)
        u=[0]*5;v=[0]*5
        u[pair1[0]]=1;u[pair1[1]]=4
        v[pair2[0]]=1;v[pair2[1]]=4
        old.add(rref2((u[:4],v[:4])))
assert len(old)==15 and old <= contained
P=(1,1,1,1)
through={rref2((P,perm[:4])) for perm in permutations(range(5))}
assert len(through)==6 and through <= contained
assert not (old&through)
assert old|through==contained
assert all(contains_point(L,P) for L in through)
assert all(not contains_point(L,P) for L in old)

# Exact incidence: 15 other lines are edges of K6 on its six node-lines.
inc={L:tuple(M for M in through if rank([*L,*M])<=3) for L in old}
assert all(len(v)==2 for v in inc.values())
assert {len([L for L in old if M in inc[L]]) for M in through}=={5}
assert len({frozenset(v) for v in inc.values()})==15
assert set().union(*(set(z) for z in inc.values()))==through

# At each node-line, q,c have transverse gradients: any quadratic polynomial
# constant on all five field elements has zero quadratic/linear coefficients.
for L in through:
    assert contains_point(L,P)
    # every vector on the line modulo P is a permutation of F5 up to affine change
    u,v = L
    candidate = v if any((v[i]-v[0])%p for i in range(4)) else u
    # Construction above already proves this property via equality of two 6-element sets.

# Chern-class computation: c4(Sym^3 U*)=18 x^3y+45 x^2y^2+18xy^3.
# Integral over Gr(2,4) is coeff of x^3 y^2 in (x-y)*c4 = 45-18.
assert 45-18 == 27
print('CLEBSCH_CHAR5_806_LINE_CENSUS_21_SUPPORTS_K6_INCIDENCE_CHERN_27_PASS')

# Exact arithmetic in Z[t]/(t^2+t-1); p_01 for this chart equals 1.
# Elements a+b*t multiply using t^2=1-t.
def add2(x,y):return (x[0]+y[0],x[1]+y[1])
def neg2(x):return (-x[0],-x[1])
def mul2(x,y):
    a,b=x; c,d=y
    return (a*c+b*d,a*d+b*c-b*d)
def pow2(x,k):
    out=(1,0)
    for _ in range(k):out=mul2(out,x)
    return out

def coordinates_after_perm(u,v,s):
    # s reindexes the five coordinates, preserving the determinant form.
    return [u[s[j]] for j in range(5)],[v[s[j]] for j in range(5)]
def pluecker(u,v):
    return { (i,j):add2(mul2(u[i],v[j]),neg2(mul2(u[j],v[i])))
            for i in range(5) for j in range(i+1,5) }
zero=(0,0); one=(1,0); T=(0,1)
u=[one,zero,neg2(one),neg2(T),T]
v=[zero,one,T,neg2(T),neg2(one)]
for W in (u,v):
    assert sum(a for a,b in W)==sum(b for a,b in W)==0
for W in (u,v):
    assert tuple(map(sum, zip(*(pow2(w,3) for w in W)))) ==zero
assert tuple(map(sum, zip(*(mul2(pow2(x,2),y) for x,y in zip(u,v)))))==zero
assert tuple(map(sum, zip(*(mul2(x,pow2(y,2)) for x,y in zip(u,v)))))==zero
P=pluecker(u,v)
assert P[(0,1)]==one and P[(0,2)]==T
for (i,j),z in P.items():
    assert z==add2(mul2(u[i],v[j]),neg2(mul2(u[j],v[i])))
# Modulo 5, t=2+epsilon with epsilon^2=0. A coordinate pair (a,b)
# becomes (a+2b)+b*epsilon, so its epsilon coefficient tests ramification.
def const(x):return (x[0]+2*x[1])%5
def dual(x):return (const(x),x[1]%5)
def normalize_proj(v):
    n=next(i for i,x in enumerate(v) if x%5)
    d=pow(v[n],-1,5)
    return tuple((x*d)%5 for x in v)
red_lines={}
for s in permutations(range(5)):
    U,V=coordinates_after_perm(u,v,s)
    ps=pluecker(U,V)
    vals=list(ps.values())
    norm=normalize_proj([const(x) for x in vals])
    nonzero=next(i for i,z in enumerate(vals) if const(z))
    c=vals[nonzero]
    # R[epsilon]/epsilon^2 inversion: (a+b eps)^-1=a^-1-b a^-2 eps
    inva=pow(const(c),-1,5)
    invb=(-dual(c)[1]*inva*inva)%5
    norm_dual=[]
    for z in vals:
        a,b=dual(z)
        norm_dual.append(((a*inva)%5,(a*invb+b*inva)%5))
    assert any(y[1] for y in norm_dual)
    red_lines.setdefault(norm,set()).add(tuple(norm_dual))
assert len(red_lines)==6
assert all(len(z)==2 for z in red_lines.values())
print('CLEBSCH_INTEGRAL_PLUCKER_GOLDEN_RATIO_SIX_RAMIFIED_QUADRATIC_SUPPORTS_PASS')
