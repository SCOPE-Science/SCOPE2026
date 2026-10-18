"""Reproducibility checks for finite-cycle resetting occupation noise.

Standard library only. Exact rational linear algebra for independent Markov
and Green resolvent derivations; numerical checks for hyperbolic identity.
"""
from fractions import Fraction as F
from math import sin, pi, sqrt, tanh, acosh, cosh, sinh


def solve(A, b):
    n = len(b)
    a = [list(map(F, A[i])) + [F(b[i])] for i in range(n)]
    for j in range(n):
        z = next(i for i in range(j, n) if a[i][j])
        a[j], a[z] = a[z], a[j]
        fac = a[j][j]
        a[j] = [x / fac for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                fac = a[i][j]
                a[i] = [a[i][k] - fac * a[j][k] for k in range(n+1)]
    return [a[i][-1] for i in range(n)]


def generators(n, r):
    Q = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        Q[i][(i-1) % n] += 1
        Q[i][(i+1) % n] += 1
        if i != 0:
            Q[i][0] += r
        Q[i][i] = -sum(Q[i][j] for j in range(n) if j != i)
    return Q


def exact_independent(n, r):
    Q = generators(n, r)
    A = [[Q[i][j] for i in range(n)] for j in range(n)]
    A[-1] = [F(1) for i in range(n)]
    b = [F(0)] * (n-1) + [F(1)]
    pi_vec = solve(A, b)
    assert all(x > 0 for x in pi_vec)
    p = pi_vec[0]
    f = [F(int(i==0)) - p for i in range(n)]
    A = [[-Q[i][j] for j in range(n)] for i in range(n)]
    A[0] = [F(int(j==0)) for j in range(n)]
    f[0] = 0
    u = solve(A, f)
    # Centering means contribution from the deleted first equation vanishes.
    v = 2 * p * (u[0] - sum(pi_vec[i] * u[i] for i in range(n)))
    # Independent resolvent for reset-free symmetric walk:
    M = [[F(2)*F(i==j) - F(j == (i-1)%n) - F(j == (i+1)%n) + (r if i==j else 0)
           for j in range(n)] for i in range(n)]
    g = solve(M, [F(int(i==0)) for i in range(n)])
    p2 = r*g[0]
    dp = g[0] - r * sum(x*x for x in g)
    v2 = 2*p2*dp
    assert p == p2, (n, r, p, p2)
    assert v == v2, (n, r, v, v2)
    return p, v


def spectral(n,r):
    ls = [4*sin(pi*k/n)**2 for k in range(n)]
    p = sum(r/(r+x) for x in ls)/n
    dp = sum(x/(r+x)**2 for x in ls[1:])/n
    return p, 2*p*dp


def hyperbolic(n,r):
    t = acosh(1+r/2)/2
    p = tanh(t)/tanh(n*t)
    # derivative dp/dr via p times log derivative
    dp = p * (1/(2*sinh(2*t)**2)-n/(2*sinh(2*t)*sinh(2*n*t)))
    return p, 2*p*dp


def checks():
    count = 0
    for n in range(3, 13):
        for r in [F(1,7),F(1,2),F(7,3)]:
            p, v = exact_independent(n,r)
            p_spec, v_spec = spectral(n,float(r))
            p_hyp, v_hyp = hyperbolic(n,float(r))
            assert abs(float(p)-p_spec)<2e-12
            assert abs(float(v)-v_spec)<2e-12
            assert abs(float(p)-p_hyp)<2e-12
            assert abs(float(v)-v_hyp)<2e-12
            assert F(0)<v<F(4,1)/(r+4)**2
            if n==3:
                assert v == 4*(r+1)/(r+3)**3
            count += 1
    # Complete r->0 moments via exact discrete Green sums and symbolic sums
    for n in range(3,71):
        sm1=sum(1/(4*sin(pi*k/n)**2) for k in range(1,n))
        sm2=sum(1/(4*sin(pi*k/n)**2)**2 for k in range(1,n))
        assert abs(sm1-(n*n-1)/12)<2e-9
        assert abs(sm2-(n**4+10*n*n-11)/720)<2e-7
    # Uniform upper envelope and sharpening as n grows
    for n in [4,5,10,25,100,400,2000]:
        r=1/n
        p, v=hyperbolic(n,r)
        assert v < 4/(r+4)**2
    n=2000
    _,v=hyperbolic(n,1/n)
    assert .244<v<.25
    print('PASS: 30 independent exact finite-chain generator/resolvent comparisons;')
    print('      30 spectral and hyperbolic comparisons; 68 reciprocal-eigenvalue')
    print('      trigonometric identities; finite-boundary and large-cycle probes.')
    print('      For n=2000 and reset rate 1/n: V=',format(v,'.12g'))

if __name__ == '__main__':
    checks()
