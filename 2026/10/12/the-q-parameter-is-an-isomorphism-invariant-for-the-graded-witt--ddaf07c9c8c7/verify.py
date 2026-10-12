#!/usr/bin/env python3
from fractions import Fraction as F


def c(q, lam, n, m):
    return (lam + F(m) + (F(1)-q)*F(n))/q

# Every member has the same Witt commutator.
for q in [F(-3), F(-1), F(1,2), F(2), F(5,2), F(4)]:
    if q in (0,1):
        continue
    for lam in [F(-2), F(0), F(3,2)]:
        for n in range(-4,5):
            for m in range(-4,5):
                assert c(q,lam,n,m)-c(q,lam,m,n) == F(m-n)

# Multiplicativity for Phi_{eps,a} after cancelling a^(m+n):
def iso_identity(q,lam,qp,mu,eps,n,m):
    lhs = F(eps)*c(q,lam,n,m)
    rhs = c(qp,mu,eps*n,eps*m)
    return lhs == rhs

qs = [F(-3),F(-2),F(-1),F(1,2),F(2),F(3),F(5,2)]
lams = [F(-2),F(-1),F(0),F(1),F(3,2),F(2)]
probe = [(0,0),(0,1),(1,0),(1,2),(-2,3)]
for q in qs:
    for qp in qs:
        for lam in lams:
            for mu in lams:
                for eps in (-1,1):
                    ok = all(iso_identity(q,lam,qp,mu,eps,n,m) for n,m in probe)
                    predicted = (q == qp and mu == eps*lam)
                    assert ok == predicted, (q,lam,qp,mu,eps)

# Converse on a wider index box.
for q in qs:
    for lam in lams:
        for eps in (-1,1):
            mu = eps*lam
            for n in range(-6,7):
                for m in range(-6,7):
                    assert iso_identity(q,lam,q,mu,eps,n,m)

# Automorphism sign condition for a fixed algebra.
for lam in lams:
    allowed = [eps for eps in (-1,1) if eps*lam == lam]
    assert allowed == ([-1,1] if lam == 0 else [1])

# Semidirect action: reflection conjugates scale a to a^{-1}.
# Pair action is Phi_(eps,a)(W_n)=eps*a^n W_(eps*n).
def compose(p1,p2):
    e1,a1=p1; e2,a2=p2
    # Phi(e1,a1) o Phi(e2,a2)
    return (e1*e2, a1**e2 * a2)
for a in [F(2),F(3,2),F(-3)]:
    r=(-1,F(1)); s=(1,a)
    x=compose(compose(r,s),r)
    assert x == (1, F(1,1)/a)

print('CHECK_OK')
