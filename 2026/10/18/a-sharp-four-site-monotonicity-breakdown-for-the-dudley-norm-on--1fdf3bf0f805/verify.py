"""Exact four-site dual bounded-Lipschitz phase-law checks; stdlib only."""
from fractions import Fraction as Q
from itertools import combinations, product

# The reflection-antisymmetric potentials are (-a,-b,b,a).
I = ((Q(1), Q(0)), (Q(-1), Q(0)), (Q(0), Q(1)), (Q(0), Q(-1)))
J = ((Q(1), Q(-1)), (Q(-1), Q(1)), (Q(0), Q(2)), (Q(0), Q(-2)))
H = tuple((u[0]+v[0],u[1]+v[1]) for u,v in product(I,J))

def vertices():
    res=set()
    for (u,v),(w,z) in combinations(H,2):
        d=u*z-w*v
        if not d: continue
        a,b=(z-v)/d,(u-w)/d
        if all(p*a+q*b<=1 for p,q in H): res.add((a,b))
    return sorted(res)

wanted=sorted([(Q(3,5),Q(1,5)),(Q(-3,5),Q(-1,5)),
               (Q(1,3),Q(-1,3)),(Q(-1,3),Q(1,3)),
               (Q(1,3),Q(1,3)),(Q(-1,3),Q(-1,3))])
V=vertices()
assert V==wanted,(V,wanted)
assert len(H)==16

def N(a,b): return max(abs(a),abs(b))+max(abs(a-b),2*abs(b))
assert all(N(a,b)==1 for a,b in V)

def claimed(t): return max((4-2*t)/3,(4+2*t)/5)

def brute(t): return max(2*(a+(t-1)*b) for a,b in V)

for i in range(1,40):
    t=Q(i,40)
    assert brute(t)==claimed(t),(t,brute(t),claimed(t))
    # The two sign patterns are normalized extreme potentials.
    assert N(Q(1,3),Q(-1,3))==1
    assert N(Q(3,5),Q(1,5))==1
    assert 2*(Q(1,3)+(t-1)*Q(-1,3))==(4-2*t)/3
    assert 2*(Q(3,5)+(t-1)*Q(1,5))==(4+2*t)/5
    # Checking the affine transport-flux identity for test potentials.
    for a,b in V:
        f=(-a,-b,b,a)
        mu=(-1,1-t,t-1,1)
        assert sum(s*x for s,x in zip(mu,f))==2*(a+(t-1)*b)
        assert N(a,b)==max(abs(x) for x in f)+max(abs(f[j+1]-f[j]) for j in range(3))
    mono=max(Q(1), (4+2*t)/5)
    if t<Q(1,2): assert claimed(t)>mono
    elif t>=Q(1,2): assert claimed(t)==(4+2*t)/5
assert (4-2*Q(1,2))/3==(4+2*Q(1,2))/5==1
print('PASS exact vertices=6, exact symbolic branches, 39 rational parameter cases, transport identities, monotonicity threshold')
