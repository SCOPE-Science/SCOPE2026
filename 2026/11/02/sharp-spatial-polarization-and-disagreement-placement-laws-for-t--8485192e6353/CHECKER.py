"""Exact finite consistency tests for the two-anchor cycle theorem.

Standard library only. Reconstructs equilibria by rational Gaussian elimination;
finite tests are checks, not substitutes for the all-size analytic proof.
"""
from fractions import Fraction as F
from math import isclose, sqrt

checks = 0

def solve(A, b):
    global checks
    n = len(A)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for j in range(n):
        piv = next((i for i in range(j, n) if M[i][j]), None)
        assert piv is not None
        M[j], M[piv] = M[piv], M[j]
        z = M[j][j]
        M[j] = [v / z for v in M[j]]
        for i in range(n):
            if i != j:
                z = M[i][j]
                if z:
                    M[i] = [M[i][s] - z * M[j][s] for s in range(n + 1)]
    checks += 1
    return [row[-1] for row in M]

def state(n, d, k):
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        L[i][i] += 1
        L[j][j] += 1
        L[i][j] -= 1
        L[j][i] -= 1
    L[0][0] += k
    L[d][d] += k
    b = [F(0)] * n
    b[0] = k
    return solve(L, b)

for n in range(4, 20):
    m = n // 2
    gs = [F(1,d) + F(1,n-d) for d in range(1,m+1)]
    assert all(gs[i] > gs[i+1] for i in range(m-1)); checks += 1
    for k in (F(1,7), F(1), F(4), F(23,2), F(31), F(100)):
        ds=[]; ps=[]
        for d in range(1,m+1):
            g=gs[d-1]
            x=state(n,d,k)
            mid=sum(x)/n
            Delta=k/(k+2*g)
            energy=sum((x[i]-x[(i+1)%n])**2 for i in range(n))
            polar=sum((z-mid)**2 for z in x)
            assert mid==F(1,2);checks+=1
            assert x[0]-x[d]==Delta;checks+=1
            assert energy==g*Delta**2;checks+=1
            assert polar==(n+2*g)*Delta**2/12;checks+=1
            assert all(F(0)<z<F(1) for z in x);checks+=1
            ds.append(energy);ps.append(polar)
        for j in range(m-1):
            ge = 2*sqrt(float(gs[j]*gs[j+1]))
            gv = n+sqrt(float((n+2*gs[j])*(n+2*gs[j+1])))
            assert (ds[j] > ds[j+1]) == (float(k)>ge);checks+=1
            assert (ps[j] > ps[j+1]) == (float(k)>gv);checks+=1
        assert min(range(m),key=lambda j: ds[j]) in (0,m-1);checks+=1
        assert min(range(m),key=lambda j: ps[j]) in (0,m-1);checks+=1
    for j in range(m-1):
        gh, gl=gs[j],gs[j+1]
        ke=2*sqrt(float(gh*gl))
        kv=n+sqrt(float((n+2*gh)*(n+2*gl)))
        E=lambda g,k:float(g)/(1+2*float(g)/k)**2
        V=lambda g,k:(n+2*float(g))/12/(1+2*float(g)/k)**2
        assert isclose(E(gh,ke),E(gl,ke),rel_tol=1e-12,abs_tol=1e-12);checks+=1
        assert isclose(V(gh,kv),V(gl,kv),rel_tol=1e-12,abs_tol=1e-12);checks+=1

n,k=12,F(4)
x1=state(n,1,k);x6=state(n,6,k)
E=lambda x:sum((x[i]-x[(i+1)%n])**2 for i in range(n))
P=lambda x:sum((z-sum(x)/n)**2 for z in x)
assert E(x1)==F(132,289);checks+=1
assert E(x6)==F(12,49);checks+=1
assert P(x1)==F(143,289);checks+=1
assert P(x6)==F(38,49);checks+=1
assert E(x1)>E(x6) and P(x1)<P(x6);checks+=1
print(f"PASS {checks} exact-rational and threshold checks")
