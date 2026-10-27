"""Exact finite checks for the ProxSPS scalar phase-boundary formulas.

Uses only Python's standard library; this illustrates, but does not replace,
the analytic proof in RESULT.md.
"""
from fractions import Fraction as Q

def step(x, a, lam):
    d = 1 + a*lam
    g = x-1
    if g == 0:
        return x/d
    loss = g*g/2
    tau0 = (d*loss-a*lam*g*x)/(g*g)
    tau = min(a, max(Q(0), tau0))
    return (x-tau*g)/d

def check(lam, a):
    d = 1+a*lam
    c = (2*a-1-a*lam)/(2*a-1+a*lam)
    star = 1/(1+lam)
    left = (1+a)/(1+a+2*a*lam)
    right = (1+a+a*lam)/(1+a+2*a*lam)
    if a > 2/(1-lam):
        assert Q(0)<left<c<star<right<1
        assert step(left,a,lam)==right
        assert step(right,a,lam)==left
        assert step(star,a,lam)==star
        m = (1-a)/(2*d)
        assert m == (Q(1,2))*((1-a)/d)
    elif a == 2/(1-lam):
        assert c == (3-lam)/(3*(1+lam))
        u=(1+c)/2
        for x in (c, (c+star)/2,star,(star+u)/2,u):
            assert step(step(x,a,lam),a,lam)==x
        assert u==(3+lam)/(3*(1+lam))
    else:
        assert abs((1-a)/d)<1
    return (left,right)

for lam, a in ((Q(1,5),Q(2)),(Q(1,5),Q(5,2)),(Q(1,5),Q(3)),
               (Q(2,5),Q(5)),(Q(3,5),Q(6)),(Q(1,10),Q(4))):
    check(lam,a)
# Full exact-cycle witness in the strictly attractive window.
lam,a=Q(1,5),Q(3)
left,right=check(lam,a)
assert (left,right)==(Q(10,13),Q(23,26))
assert (1-a)/(2*(1+a*lam))==Q(-5,8)
assert step(left,a,lam)==right and step(right,a,lam)==left
# Unregularized benchmark: truncation is always a half-step when a>=1/2.
x=Q(9,10)
for a in (Q(1,2),Q(2),Q(100)):
    assert step(x,a,Q(0))==(x+1)/2
print('VERIFY_OK; exact fractions, both cycle orientations, critical band and stable/unstable examples')
