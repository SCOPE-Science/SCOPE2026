#!/usr/bin/env python3
"""Independent exact and numerical checks for a BDF2 logarithmic-memory CQ sign theorem."""
from fractions import Fraction as Q
import cmath, math

def p_exact(s, N):
    c = Q(3,2)+s
    p = [Q(2), Q(2)/c]
    for k in range(2,N+1):
        p.append((Q(2)/c)*p[-1] - (Q(1)/(2*c))*p[-2])
    return p[:N+1]

def cq_exact(a,b,h,N):
    pa=p_exact(h*a,N); pb=p_exact(h*b,N)
    return [(pa[n]-pb[n])/n for n in range(1,N+1)]

def independent_recurrence_log_coeff(a,b,h,N):
    # Let U = delta(zeta)+h*b, V = delta(zeta)+h*a.
    # W'=U'/U - V'/V. Series quotient computed without factored roots.
    def q_series(s):
        u=[Q(3,2)+h*s,Q(-2),Q(1,2)]
        q=[]
        for n in range(N):
            uder = u[n+1]*(n+1) if n+1<len(u) else Q(0)
            rest = sum(u[k]*q[n-k] for k in range(1,min(n,2)+1))
            q.append((uder-rest)/u[0])
        return q
    qb=q_series(b);qa=q_series(a)
    return [(qb[n-1]-qa[n-1])/n for n in range(1,N+1)]

# Distinct rational cases including below, exactly at, and above critical threshold.
cases=[(Q(1,4),Q(4),Q(1)),(Q(1,2),Q(4),Q(1)),(Q(1),Q(4),Q(1)),
       (Q(0),Q(20),Q(7)),(Q(1,8),Q(2),Q(3)),(Q(3),Q(7),Q(1,4))]
for a,b,h in cases:
    aa=cq_exact(a,b,h,45)
    bb=independent_recurrence_log_coeff(a,b,h,45)
    assert aa==bb, (a,b,h)
    if a*h<=Q(1,2): assert all(w>0 for w in aa)
    else:
        assert any(w<0 for w in aa)
        assert any(w>0 for w in aa)
print('PASS: six rational cases; exact independent polynomial quotient agrees through coefficient 45.')

# Infinite analytical trigonometric formula verified numerically over high-order terms.
for a,b,h in [(0.25,40,1),(0.5,20,1),(1,2,1),(2,10,1),(1,8,0.25)]:
    def lp(s):
        q=cmath.sqrt(1-2*s)/2
        return (1/(2*(1-q)),1/(2*(1+q)))
    la=lp(a*h); lb=lp(b*h)
    pa=[la[0]**n+la[1]**n for n in range(1,151)]
    pb=[lb[0]**n+lb[1]**n for n in range(1,151)]
    vals=[(pa[n]-pb[n]).real/(n+1) for n in range(150)]
    assert max(abs((pa[n]-pb[n]).imag) for n in range(150)) < 1e-12
    if a*h<=0.5: assert all(x>0 for x in vals if abs(x)>1e-150)
    else:
        assert sum(x>0 for x in vals[:80])>3 and sum(x<0 for x in vals[:80])>3
print('PASS: complex factor check over five cases and 150 coefficients each.')

# Exact witness with sign-indefiniteness and a positive slow rate.
positive=cq_exact(Q(1,4),Q(4),Q(1),24)
negative=cq_exact(Q(1),Q(2),Q(1),24)
print('slow-window first 12 weights =', list(map(str,positive[:12])))
print('fast-window first negative index =', next(i+1 for i,w in enumerate(negative) if w<0))
print('fast-window first 12 signs =', ''.join('+' if w>0 else '-' if w<0 else '0' for w in negative[:12]))
print('CHECKER PASS')
