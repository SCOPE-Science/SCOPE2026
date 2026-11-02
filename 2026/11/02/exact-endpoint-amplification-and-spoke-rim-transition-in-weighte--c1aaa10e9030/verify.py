"""Exact independent grounded-Laplacian checks for conductance-weighted wheels."""
from fractions import Fraction as F
from math import sqrt


def inverse(a):
    n = len(a)
    x = [[F(v) for v in row] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if x[i][k])
        x[k], x[pivot] = x[pivot], x[k]
        den = x[k][k]
        x[k] = [z / den for z in x[k]]
        for i in range(n):
            if i != k and x[i][k]:
                scale = x[i][k]
                x[i] = [z - scale * w for z, w in zip(x[i], x[k])]
    return [row[n:] for row in x]


def check_one(n, root_a):
    a = root_a**2
    k = [[a+2 if i == j else (-1 if ((i-j)%n in (1,n-1)) else 0)
          for j in range(n)] for i in range(n)]
    g = inverse(k)
    # Build C^(1/2) B from scratch: grounded spokes of conductance a,
    # unit-conductance rims. Projection is B K^-1 B^T.
    b = [[root_a*int(j==i) for j in range(n)] for i in range(n)]
    b += [[F(int(j==i)-int(j==(i+1)%n)) for j in range(n)] for i in range(n)]
    x = [[sum(bi[u]*g[u][v] for u in range(n)) for v in range(n)] for bi in b]
    p = [[sum(xi[v]*bj[v] for v in range(n)) for bj in b] for xi in x]
    rows = [sum(abs(y) for y in pi) for pi in p]
    g0,gm = g[0][0],g[0][n//2]
    S = 1+2*root_a*(g0-gm)
    R = 2*root_a*(g0-gm)+4*(g0-g[0][1])
    assert R == 2-2*a*g0+2*root_a*(g0-gm)
    assert R-S == 1-2*a*g0
    assert all(t==S for t in rows[:n]), (n,a,'spoke',rows[:n],S)
    assert all(t==R for t in rows[n:]), (n,a,'rim',rows[n:],R)
    assert max(rows)==max(S,R)
    assert all(p[i][j]==p[j][i] for i in range(2*n) for j in range(2*n))
    assert sum(p[i][i] for i in range(2*n))==n
    if n<=7:
        assert all(sum(p[i][u]*p[u][j] for u in range(2*n))==p[i][j]
                   for i in range(2*n) for j in range(2*n))
    af=float(a); rho=(af+2-sqrt(af*(af+4)))/2
    closed=(rho**(n//2)+rho**(n-n//2))/(sqrt(af*(af+4))*(1-rho**n))
    assert abs(float(gm)-closed)<2e-11
    return max(S,R),F(a*g0)


if __name__=='__main__':
    roots=[F(1,4),F(1,2),F(1),F(3,2),F(2),F(4)]
    cases=0
    for n in range(3,16):
        ratios=[]
        for t in roots:
            z,h=check_one(n,t)
            ratios.append(h)
            cases+=1
        assert all(ratios[i]<ratios[i+1] for i in range(len(ratios)-1))
    assert check_one(3,F(1))[0]==F(3,2)
    assert check_one(4,F(1))[0]==F(26,15)
    assert check_one(5,F(1))[0]==F(20,11)
    assert check_one(6,F(1))[0]==F(19,10)
    assert check_one(7,F(1))[0]==F(56,29)
    print('VERIFY_OK exact_weighted_profiles=%d graph_sizes=3..15 conductance_sqrt=%s' % (cases,roots))
    print('unit_case_norms=',[str(check_one(n,F(1))[0]) for n in range(3,11)])
