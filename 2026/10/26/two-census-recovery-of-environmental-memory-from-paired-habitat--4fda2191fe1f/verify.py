"""Exact-rational verification of two-patch Markov-weather occupancy identities.

Run using Python 3.10+ (standard library only): python verify.py
"""
import json
from fractions import Fraction as F

STATES = [(s, x, y) for s in (-1, 1) for x in (0, 1) for y in (0, 1)]

def solve(a, b):
    a = [[F(z) for z in row] + [F(bi)] for row, bi in zip(a, b)]
    n = len(a)
    for c in range(n):
        k = next(i for i in range(c, n) if a[i][c])
        a[c], a[k] = a[k], a[c]
        z = a[c][c]
        a[c] = [w/z for w in a[c]]
        for r in range(n):
            if r != c:
                z = a[r][c]
                if z:
                    a[r] = [v-z*w for v,w in zip(a[r], a[c])]
    return [a[i][-1] for i in range(n)]

def distribution(p, a, lam, rho):
    assert 0 < p-a < p+a < 1 and 0 <= lam < 1 and -1 < rho < 1
    P=[]
    for old in STATES:
        row=[]
        for new in STATES:
            sw,x,y=old
            tw,u,v=new
            z=(1+rho*sw*tw)/2
            pp=p+a*tw
            for previous, following in ((x,u),(y,v)):
                prob=lam*previous+(1-lam)*pp
                z*=prob if following else 1-prob
            row.append(z)
        assert sum(row) == 1
        P.append(row)
    # Solve stationary row vector pi: pi P = pi.
    matrix = [[P[j][i] - (1 if i == j else 0) for j in range(8)] for i in range(7)]
    matrix.append([F(1)]*8)
    pi=solve(matrix, [F(0)]*7+[F(1)])
    assert all(z > 0 for z in pi) and sum(pi) == 1
    assert all(sum(pi[i]*P[i][j] for i in range(8))==pi[j] for j in range(8))
    return P, pi

def check(p,a,lam,rho):
    P,pi=distribution(p,a,lam,rho)
    mean=sum(pi[i]*STATES[i][1] for i in range(8))
    var=mean*(1-mean)
    c0=sum(pi[i]*STATES[i][1]*STATES[i][2] for i in range(8))-mean**2
    c1=sum(pi[i]*P[i][j]*STATES[i][1]*STATES[j][2] for i in range(8) for j in range(8))-mean**2
    a1=sum(pi[i]*P[i][j]*STATES[i][1]*STATES[j][1] for i in range(8) for j in range(8))-mean**2
    assert mean == p
    assert c0 == a*a*(1-lam)*(1+lam*rho)/((1+lam)*(1-lam*rho))
    assert c1 == c0*(lam+rho)/(1+lam*rho)
    assert a1-c1 == lam*(var-c0)
    L=(a1-c1)/(var-c0)
    q=c1/c0
    R=(q-L)/(1-L*q)
    aa2=c0*(1+L)*(1-L*R)/((1-L)*(1+L*R))
    assert (L,R,aa2)==(lam,rho,a*a)
    return [str(x) for x in (mean,c0,c1,a1)]

def q(a,b):return F(a,b)

cases=[
    (q(2,5),q(1,5),q(2,3),q(1,3)),
    (q(1,2),q(1,5),q(1,2),q(-2,7)),
    (q(1,2),q(1,10),q(0,1),q(0,1)),
    (q(3,5),q(1,8),q(1,4),q(-3,5)),
    (q(1,3),q(1,6),q(3,4),q(3,4)),
    (q(3,4),q(1,8),q(4,5),q(-4,5)),
    (q(1,4),q(1,10),q(0,1),q(3,5)),
    (q(1,2),q(1,4),q(1,3),q(0,1)),
    (q(3,7),q(1,9),q(7,8),q(1,8)),
    (q(3,5),q(1,5),q(2,5),q(-1,5)),
    (q(1,2),q(1,6),q(5,6),q(1,6)),
    (q(2,3),q(1,4),q(1,6),q(5,6)),
]
observed=[check(*case) for case in cases]
# A one-date law for 2 binary exchangeable patches is determined by p and c0.
_, pi1 = distribution(q(1,2),q(1,5),q(1,2),q(-2,7))
_, pi2 = distribution(q(1,2),q(1,10),q(0,1),q(0,1))

def marginal(pi):
    return tuple(sum(pi[i] for i,(_,x,y) in enumerate(STATES) if (x,y)==(u,v))
                 for u in (0,1) for v in (0,1))
assert marginal(pi1) == marginal(pi2) == (q(13,50),q(6,25),q(6,25),q(13,50))
print(json.dumps({"status":"PASS", "exact_arithmetic":True,
    "parameter_cases":len(cases),"transition_entries_checked":len(cases)*64,
    "mean_and_covariance_comparisons":len(cases)*4,
    "reconstruction_cases":len(cases),
    "example_parameters":["2/5","1/5","2/3","1/3"],
    "example_observable_moments":observed[0],
    "one_date_aliasing_marginal":[str(x) for x in marginal(pi1)],
    "scope":"finite exact checks; analytical theorem requires separate proof"},
    sort_keys=True))
