#!/usr/bin/env python3
"""Reproducible finite-field and exact-integer checks for a classical cubic polar map.
The accompanying proof covers all odd characteristics and the infinite-field degree claim.
This script checks polynomial identities and independently enumerates sample projective base loci.
"""
from itertools import combinations, product
from collections import Counter

N=5
ZERO=(0,)*N

def mon(*inds):
    a=[0]*N
    for i in inds:a[i]+=1
    return tuple(a)
def add(*ps):
    r=Counter()
    for p in ps:
        for k,v in p.items():r[k]+=v
    return {k:v for k,v in r.items() if v}
def scale(p,k):return {a:k*v for a,v in p.items() if k*v}
def mul(p,q):
    r=Counter()
    for a,ca in p.items():
      for b,cb in q.items():r[tuple(x+y for x,y in zip(a,b))]+=ca*cb
    return {k:v for k,v in r.items() if v}
def diff(p,i):
    r=Counter()
    for a,c in p.items():
        if a[i]:
            b=list(a);b[i]-=1;r[tuple(b)]+=c*a[i]
    return {k:v for k,v in r.items() if v}
def poly_eq(p,q):return add(p,scale(q,-1))=={}

def ev(poly,x,p):
    return sum(c*__import__('math').prod(pow(xi,ai,p) for xi,ai in zip(x,a)) for a,c in poly.items())%p

vars=[{mon(i):1} for i in range(N)]
s=add(*vars)
e2=add(*[mul(vars[i],vars[j]) for i,j in combinations(range(N),2)])
e3=add(*[mul(mul(vars[i],vars[j]),vars[k]) for i,j,k in combinations(range(N),3)])
F=add(e3,scale(mul(s,e2),-1))
qs=[add(mul(vars[i],vars[i]),scale(mul(s,s),-1)) for i in range(N)]
assert all(poly_eq(diff(F,i),qs[i]) for i in range(N))
assert poly_eq(scale(F,3),add(*[{mon(i,i,i):1} for i in range(N)],scale(mul(mul(s,s),s),-1)))
print('INTEGER_GRADIENT_IDENTITY_OK')

# The sixth symmetric coordinate is x5=-s. Transposition of x0 and x5
# induces x0 -> -s and leaves the remaining first-five coordinates intact.
def substitute(p, repl):
    ans={}
    for a,c in p.items():
        term={ZERO:c}
        for i,ex in enumerate(a):
            for _ in range(ex):term=mul(term,repl[i])
        ans=add(ans,term)
    return ans
assert poly_eq(substitute(F,[scale(s,-1)]+vars[1:]),F)
print('INTEGRAL_SIX_LABEL_SYMMETRY_OK')


def rank_mod(mat,p):
    a=[[v%p for v in row] for row in mat]
    r=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,p)
        a[r]=[(inv*v)%p for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                coef=a[i][j]
                a[i]=[(v-coef*w)%p for v,w in zip(a[i],a[r])]
        r+=1
    return r

def normalized_pts(p):
    # Each projective point has a unique representative whose first nonzero coordinate is 1.
    for lead in range(N):
        for tail in product(range(p),repeat=N-lead-1):
            yield (0,)*lead+(1,)+tail

def hessian_at(x,p):
    z=sum(x)%p
    return [[(2*x[i] if i==j else 0)-2*z for j in range(N)] for i in range(N)]

for p,count in [(3,11),(5,10),(7,10)]:
    base=[x for x in normalized_pts(p) if all(ev(q,x,p)==0 for q in qs)]
    assert len(base)==count,(p,len(base),base)
    in_cubic=[x for x in base if ev(F,x,p)==0]
    assert len(in_cubic)==10,(p,in_cubic)
    assert all(rank_mod(hessian_at(x,p),p)==4 for x in base)
    if p==3:
        extra=[x for x in base if ev(F,x,p)]
        assert extra==[(1,1,1,1,1)]
        assert ev(F,extra[0],3)==2
    else:assert all(ev(F,x,p)==0 for x in base)
    print(f'CHAR_{p}_BASE_POINTS={len(base)} CUBIC_NODES={len(in_cubic)} HESSIAN_RANK=4')

# All odd characteristics: x=(1,1,1,1,-4) satisfies s=0,
# so Hessian is diagonal and has integer determinant -128.
x=[1,1,1,1,-4]
assert sum(x)==0
def det_int(a):
    from itertools import permutations
    total=0
    for perm in permutations(range(len(a))):
        inv=sum(perm[i]>perm[j] for i in range(len(a)) for j in range(i+1,len(a)))
        v=1
        for i,j in enumerate(perm):v*=a[i][j]
        total+=(-1 if inv%2 else 1)*v
    return total
H=[[2*x[i]*(i==j)-2*sum(x) for j in range(N)] for i in range(N)]
assert det_int(H)==-128
assert det_int(H)%3 and det_int(H)%5 and det_int(H)%7
print('GENERIC_HESSIAN_DETERMINANT_WITNESS=-128')
print('POLAR_DEGREE_FROM_BEZOUT: odd_characteristic_other_than_3=6; characteristic_3=5')
print('VERIFY_OK')
