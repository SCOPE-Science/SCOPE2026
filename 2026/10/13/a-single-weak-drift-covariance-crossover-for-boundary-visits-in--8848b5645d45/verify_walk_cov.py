"""Independent exact finite-state and asymptotic checks for an absorbing walk.

Run with Python 3.10+ and its standard library:
    python verify_walk_cov.py
These checks supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
from math import exp


def solve(matrix, rhs):
    n = len(rhs)
    a = [list(matrix[k]) + [rhs[k]] for k in range(n)]
    for k in range(n):
        pivot = next(j for j in range(k, n) if a[j][k] != 0)
        a[k], a[pivot] = a[pivot], a[k]
        scale = a[k][k]
        a[k] = [x/scale for x in a[k]]
        for j in range(n):
            if j != k and a[j][k]:
                c = a[j][k]
                a[j] = [x - c*y for x, y in zip(a[j], a[k])]
    return [a[k][-1] for k in range(n)]


def exact_check(m, p):
    q = 1-p
    a = [[F(int(i == j)) for j in range(m-1)] for i in range(m-1)]
    qmat = [[F(0) for _ in range(m-1)] for _ in range(m-1)]
    for i in range(1, m):
        if i > 1: qmat[i-1][i-2] = q
        if i < m-1: qmat[i-1][i] = p
    for j in range(m-1):
        for k in range(m-1): a[j][k] -= qmat[j][k]
    ones = [F(1)] * (m-1)
    e1 = [F(int(j == 0)) for j in range(m-1)]
    t = solve(a, ones)
    v = solve(a, e1)
    rhs = [F(int(j == 0)) + sum(qmat[j][k]*v[k] for k in range(m-1))
           + F(int(j == 0))*sum(qmat[j][k]*t[k] for k in range(m-1))
           for j in range(m-1)]
    w = solve(a, rhs)
    g2e = solve(a, v)
    n_checks = 0
    for i in range(1, m):
        cov = w[i-1] - t[i-1]*v[i-1]
        formula = v[i-1]*(t[0]-t[i-1]) + g2e[i-1]-v[i-1]
        assert cov == formula, (m, p, i, cov, formula)
        if p == q:
            gformula = F(2*(m-i), m)
            tformula = F(i*(m-i))
        else:
            r = q/p
            d = p-q
            gformula = (r**(i-1)-r**(m-1))/(p*(1-r**m))
            tformula = (m*(1-r**i)/(1-r**m)-i)/d
        assert v[i-1] == gformula
        assert t[i-1] == tformula
        n_checks += 3
    return n_checks


def exact_finite_cov_float(m, i, b):
    if b == 0:
        g = lambda a, k: 2*min(a, k)*(m-max(a, k))/m
        t = lambda a: a*(m-a)
    else:
        r = exp(-b/m)
        p = 1/(1+r)
        d = (1-r)/(1+r)
        R = r**m
        def g(a,k):
            if a<=k:
                return (1-r**a)*(1-r**(m-k))/(d*(1-R))
            return (1-r**k)*(r**(a-k)-r**(m-k))/(d*(1-R))
        t = lambda a: (m*(1-r**a)/(1-R)-a)/d
    gi1 = g(i,1)
    g2i1 = sum(g(i,k)*g(k,1) for k in range(1,m))
    return (gi1*(t(1)-t(i))+g2i1-gi1)/m


def limit_value(i, b):
    if b == 0: return 2-2*i/3
    R = exp(-b)
    return 4*(((2*i-1)+R)*(1-R)-b*((i-1)+(i+1)*R))/(b*(1-R)**2)


def H(i,b):
    r = exp(-b)
    return ((2*i-1)+r)*(1-r)-b*((i-1)+(i+1)*r)


def root2():
    lo, hi = 1.0, 2.0
    for _ in range(70):
        mid = (lo+hi)/2
        if H(2,mid)>0: lo=mid
        else: hi=mid
    assert 1.49888421886733 < (lo+hi)/2 < 1.49888421886736
    return (lo+hi)/2


def main():
    count=0
    for m in range(3,11):
        for p in (F(1,3),F(1,2),F(2,3),F(3,4)):
            count += exact_check(m,p)
    for b in (0, 0.3, 1, 1.5, 2.5, 4):
        for i in range(1,6):
            a = exact_finite_cov_float(4800,i,b)
            e = limit_value(i,b)
            assert abs(a-e) < 0.075, (i,b,a,e)
            count += 1
    z=root2()
    for b in (.2,1,z-.00001,z+.00001,3,8):
        for i in range(1,8):
            sg=H(i,b)
            if i==1: assert sg>0
            if i>=3: assert sg<0
            if i==2 and b<z: assert sg>0
            if i==2 and b>z: assert sg<0
            count+=1
    print('VERIFY_OK exact_finite_independent_conditions=%d asymptotic_sign_root=%0.14f' %(count,z))


if __name__ == '__main__':
    main()
