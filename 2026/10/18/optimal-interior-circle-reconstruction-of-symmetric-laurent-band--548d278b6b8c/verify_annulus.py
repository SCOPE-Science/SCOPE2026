"""Finite numerical checks of the annular Laurent sampling identities.

Only corroborates identities: the all-parameter assertions are proved analytically.
Uses Python standard library exclusively.
"""
import math


def moments(a, b, j):
    if j == -1:
        return 2.0 * math.log(b / a) / (b*b - a*a)
    return (b**(2*j+2) - a**(2*j+2)) / ((j+1)*(b*b-a*a))


def data(a, b, n):
    m = {j: moments(a, b, j) for j in range(-n, n+1)}
    r = math.exp((math.log(m[n])-math.log(m[-n]))/(4*n))
    lam = {j: r**(2*j)/m[j] for j in m}
    expected_min = 1.0/math.sqrt(m[n]*m[-n])
    assert a < r < b
    assert math.isclose(lam[-n], lam[n], rel_tol=5e-10)
    assert math.isclose(min(lam.values()), expected_min, rel_tol=5e-10)
    gap = max(m[n]**((j+n)/(2*n)) * m[-n]**((n-j)/(2*n)) / m[j] for j in m)
    cond2 = max(lam.values())/min(lam.values())
    assert math.isclose(cond2, gap, rel_tol=5e-10)
    for factor in [0.91, 0.97, 1.03, 1.09]:
        other = r*factor
        if not a < other < b:
            continue
        sl = [other**(2*j)/m[j] for j in m]
        assert min(sl) < expected_min + 1e-10
        assert max(sl)/min(sl) >= cond2 - 1e-10
    for j in range(-n+1,n):
        assert m[j]**2 < m[j-1]*m[j+1] + 1e-9 * m[j]**2
    return r, math.sqrt(cond2), max(lam, key=lam.get)


def run():
    for a,b in [(0.3,1.0),(0.7,1.0),(0.8,2.0)]:
        for n in [1,2,3,4,5,8,12,20]:
            r,k,j = data(a,b,n)
            print(f"a={a} b={b} N={n} r={r:.10g} kappa={k:.10g} max_index={j}")
        for n in [50,100]:
            r,k,j = data(a,b,n)
            expected = math.exp(0.5*n*math.log(b/a))/math.sqrt(2*n*math.log(b/a))
            assert 0.88 < k/expected < 1.12
            assert j == -1
            print(f"asymptotic N={n} ratio={k/expected:.10g}")
    print('ALL NUMERICAL CHECKS PASSED; NOT AN INFINITE CERTIFICATE')


if __name__ == '__main__':
    run()
