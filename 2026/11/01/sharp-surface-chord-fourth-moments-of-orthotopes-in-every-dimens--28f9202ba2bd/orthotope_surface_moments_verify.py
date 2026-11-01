"""Independent rational face-pair checks of surface chord moments on orthotopes.

Run: python3 orthotope_surface_moments_verify.py
All exact arithmetic uses the Python standard library.
"""
from fractions import Fraction as F
from random import Random


def summary(a):
    d = len(a)
    T = sum((1 / v for v in a), F(0))
    B = sum((v * v for v in a), F(0))
    p1 = sum(a, F(0))
    C = sum((v**3 for v in a), F(0)) / T
    E = sum((v**4 for v in a), F(0))
    R = p1 / T
    Q = B + 2 * R
    K = F(1) + (F(7, 5)*E + F(28, 5)*C - 2*R*R + 4*B/(T*T))/(Q*Q)
    kmin = F(1) + F(1, d) + F(2*(d-1), 5*(d+2)**2)
    anis = sum(((v*v/B - F(1,d))**2 for v in a), F(0))
    stability = F(2*d*d,5*(d+2)**2)*anis
    return T, K, kmin, stability, F(2,3)*Q, K*(F(2,3)*Q)**2


def separate_face_pairs(a):
    d = len(a)
    T = sum((1 / v for v in a), F(0))
    weights = [(1/v)/T for v in a]
    ed2, ed4 = F(0), F(0)
    for i in range(d):
        for j in range(d):
            z2, z4 = [], []
            for k, v in enumerate(a):
                x2 = v*v if k == i else v*v/3
                x4 = v**4 if k == i else v**4/5
                y2 = v*v if k == j else v*v/3
                y4 = v**4 if k == j else v**4/5
                z2.append(x2 + y2)
                z4.append(x4 + y4 + 6*x2*y2)
            m2 = sum(z2, F(0))
            m4 = sum(z4, F(0)) + 2*sum((z2[k]*z2[l] for k in range(d) for l in range(k+1,d)), F(0))
            ed2 += weights[i]*weights[j]*m2
            ed4 += weights[i]*weights[j]*m4
    return ed2, ed4


def run():
    rng = Random(142857)
    exact = 0
    for d in range(4,9):
        for j in range(12):
            vals = [F(rng.randint(1, 9), rng.randint(1, 6)) for _ in range(d)]
            _, K, kmin, st, ed2, ed4 = summary(vals)
            direct2, direct4 = separate_face_pairs(vals)
            assert ed2 == direct2 and ed4 == direct4
            assert K == direct4/direct2**2
            assert kmin <= K < F(12,5)
            assert K-kmin >= st
            exact += 5
        equal = [F(3,2)]*d
        assert summary(equal)[1] == summary(equal)[2]
        exact += 1
        assert summary(equal)[1] > summary(equal+[F(3,2)])[1]
        exact += 1
        for L in [10**3,10**5]:
            K = summary([F(L)]+[F(1)]*(d-1))[1]
            assert K < F(12,5) and F(12,5)-K < F(10,d+0) / F(L)
            exact += 1
    print(f'VERIFY_OK exact_fractional_checks={exact} dimensions=4..8')

if __name__ == '__main__':
    run()
