"""Exact finite checks for a saddle-node recurrence identity.

Uses only Python's standard library. The mathematical conclusions for
unbounded time and arbitrary real parameters require the accompanying proof.
"""
from fractions import Fraction as Q
from itertools import product


def fmap(state, alpha, sigma, delta):
    x, y, z = state
    return (delta*z + alpha-sigma*y+x*x, x, y)


def height(state, sigma, delta):
    x, y, z = state
    return x+(delta-sigma)*y+delta*z


def check(state, alpha, sigma, delta):
    kappa = delta-sigma-Q(1)
    fold = kappa*kappa/Q(4)
    eps = alpha-fold
    assert (height(fmap(state,alpha,sigma,delta),sigma,delta)
            - height(state,sigma,delta)
            == (state[0]+kappa/Q(2))**2+eps)

checks=0
for d,s,a,x,y,z in product((Q(0),Q(1,4),Q(3,4)),
                            (Q(-1,2),Q(0),Q(2,3)),
                            (Q(-1,8),Q(0),Q(1,8)),
                            (Q(-3,5),Q(0),Q(2,3)),
                            (Q(-2,3),Q(4,7)),
                            (Q(-1,4),Q(1,2))):
    check((x,y,z),a,s,d)
    checks+=1

for d in (Q(0),Q(1,5),Q(1,2),Q(4,5)):
    for s in (Q(-2,5),Q(0),Q(3,5)):
        k=d-s-Q(1)
        fold=k*k/Q(4)
        root=-k/Q(2)
        assert fmap((root,root,root),fold,s,d)==(root,root,root)
        checks+=1
        for a in (fold-Q(1,9), fold, fold+Q(1,9)):
            state=(Q(1,3),Q(-1,4),Q(2,5))
            for j in range(4):
                check(state,a,s,d)
                state=fmap(state,a,s,d)
                checks+=1

# Test the exact below-fold pair when the discriminant is a rational square.
for d in (Q(1,5),Q(1,2),Q(4,5)):
    for s in (Q(-2,5),Q(0),Q(3,5)):
        k=d-s-Q(1)
        alpha=k*k/Q(4)-Q(1,9)
        for root in (-k/Q(2)-Q(1,3),-k/Q(2)+Q(1,3)):
            assert fmap((root,root,root),alpha,s,d)==(root,root,root)
            checks+=1

print(f"PASS: {checks} exact rational identity/fixed-point checks")
