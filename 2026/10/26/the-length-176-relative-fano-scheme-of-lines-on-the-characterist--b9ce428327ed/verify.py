"""Exact finite-field and infinitesimal checks for the characteristic-three quartic pencil.

This reproduces finite enumerations and local Jacobian calculations. The
all-parameters statements require the separate algebraic proof.
"""
from itertools import combinations, product
from collections import Counter

# F9 = F3[i]/(i^2+1), encoded 3*x+y for x+y*i.
ADD = [[0]*9 for _ in range(9)]
MUL = [[0]*9 for _ in range(9)]
for a,b in product(range(9), repeat=2):
    x,y=divmod(a,3); z,w=divmod(b,3)
    ADD[a][b] = 3*((x+z)%3)+(y+w)%3
    MUL[a][b] = 3*((x*z+2*y*w)%3)+(x*w+y*z)%3
ZERO,ONE = 0,3
NEG = [next(b for b in range(9) if ADD[a][b]==0) for a in range(9)]
def sm(a,b):return ADD[a][b]
def mu(a,b):return MUL[a][b]
def minus(a,b):return sm(a,NEG[b])
def pw(a,k):
    s=ONE
    for _ in range(k): s=mu(s,a)
    return s
def inv(a):
    assert a!=ZERO
    return pw(a,7)

def all_rref_lines():
    for j,k in combinations(range(4),2):
        spots=[(r,c) for r,p in enumerate((j,k)) for c in range(p+1,4) if c not in (j,k)]
        for vv in product(range(9), repeat=len(spots)):
            rs=[[ZERO]*4 for _ in range(2)]
            rs[0][j]=rs[1][k]=ONE
            for (r,c),v in zip(spots,vv):rs[r][c]=v
            yield tuple(map(tuple,rs))

def quartic_coeff(a,b,lam):
    c=[ZERO]*5
    for x,y in zip(a,b):
        for j,t in [(0,pw(x,4)),(1,mu(pw(x,3),y)),(3,mu(x,pw(y,3))),(4,pw(y,4))]:
            c[j]=sm(c[j],t)
    prod=[ONE]
    for x,y in zip(a,b):
        nxt=[ZERO]*(len(prod)+1)
        for j,z in enumerate(prod):
            nxt[j]=sm(nxt[j],mu(z,x));nxt[j+1]=sm(nxt[j+1],mu(z,y))
        prod=nxt
    return tuple(sm(c[j],mu(lam,prod[j])) for j in range(5))

def middle_product(a,b):
    v=ZERO
    for js in combinations(range(4),2):
        z=ONE
        for j in range(4):z=mu(z,b[j] if j in js else a[j])
        v=sm(v,z)
    return v

def solve4(A,b):
    v=[list(A[j])+[b[j]] for j in range(4)]
    for j in range(4):
        pivot=next((r for r in range(j,4) if v[r][j]!=ZERO),None)
        assert pivot is not None
        v[j],v[pivot]=v[pivot],v[j]
        z=inv(v[j][j]);v[j]=[mu(z,t) for t in v[j]]
        for r in range(4):
            if r!=j:
                z=v[r][j]
                v[r]=[minus(v[r][t],mu(z,v[j][t])) for t in range(5)]
    return tuple(v[j][-1] for j in range(4))

lines=[l for l in all_rref_lines() if quartic_coeff(*l,ZERO)==(ZERO,)*5]
assert len(lines)==112
counts=Counter(middle_product(*l)==ZERO for l in lines)
assert counts=={True:64,False:48},counts
mus=[x for x in range(9) if pw(x,4)==ONE]
assert len(mus)==4
exceptional=set()
for alpha,beta,zeta in product(mus,repeat=3):
    a,b,c,d=alpha,beta,mu(alpha,zeta),NEG[mu(beta,zeta)]
    l=((ONE,ZERO,a,b),(ZERO,ONE,c,d))
    assert quartic_coeff(*l,ZERO)==(ZERO,)*5
    assert middle_product(*l)==ZERO
    exceptional.add(l)
    # Linearize A,B,C,D at lambda=0.
    J=[(pw(a,3),pw(b,3),ZERO,ZERO),
       (ZERO,ZERO,pw(c,3),pw(d,3)),
       (ZERO,ZERO,pw(a,3),pw(b,3)),
       (pw(c,3),pw(d,3),ZERO,ZERO)]
    deriv=solve4(J,(ZERO,ZERO,NEG[mu(a,b)],NEG[mu(c,d)]))
    ap,bp,cp,dp=deriv
    hp=sm(sm(mu(ap,d),mu(a,dp)),sm(mu(bp,c),mu(b,cp)))
    assert hp==pw(mu(a,b),2) and hp!=ZERO
assert len(exceptional)==64
assert exceptional.issubset(set(lines))
# Independent finite-field evidence for every lambda in F9.
for lam in range(1,9):
    assert not any(quartic_coeff(*l,lam)==(ZERO,)*5 for l in all_rref_lines())
print('VERIFY_OK: 112 Fermat lines; 48 reduced and 64 double relative-Fano points;')
print('           64 distinct nonzero first Hensel obstructions;')
print('           no lines for 8 nonzero parameters over F9.')
