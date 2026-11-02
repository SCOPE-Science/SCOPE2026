"""Independent finite consistency tests for a retained-bath Poisson-reset Langevin pair.

Uses standard Python only; analytical proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def mat_exp(A, t):
    # Scaling and squaring, direct Taylor matrix series (not eigenvalue formula).
    n = max(0, int((max(sum(abs(x) for x in row) for row in A) * t) / 0.4) + 1)
    n = min(n, 20)
    scale = (2 ** n)
    Z = [[0.0, 0.0], [0.0, 0.0]]
    term = [[1.0, 0.0], [0.0, 1.0]]
    for k in range(55):
        for i in range(2):
            for j in range(2):
                Z[i][j] += term[i][j]
        term = mm(term, [[A[i][j] * t / scale / (k + 1) for j in range(2)] for i in range(2)])
        if max(abs(x) for row in term for x in row) < 2e-18:
            break
    for _ in range(n):
        Z = mm(Z, Z)
    return Z


def independent_cov(r, g):
    # Solve the moment system by elimination; exact rational arithmetic.
    # c=b+1, a=(2b+2)/(2+r), (r+1/g)b-a/g=1.
    b = (F(1) + F(2)/(g * (2+r))) / (r + F(1)/g - F(2)/(g*(2+r)))
    a = (2*b + 2)/(2+r)
    return [[a, b], [b, b+1]]


def check_close(a, b, eps=2e-8):
    assert isclose(float(a), float(b), rel_tol=eps, abs_tol=eps), (a, b)


def main():
    tests = 0
    for r in (F(1, 5), F(1, 2), F(1), F(2), F(5)):
        for g in (F(1, 4), F(1, 2), F(1), F(3), F(8)):
            C = independent_cov(r, g)
            a, b, c = C[0][0], C[0][1], C[1][1]
            assert -(2+r)*a + 2*b + 2 == 0
            assert c - (1+r+1/g)*b + a/g == 0
            assert b-c+1 == 0
            tests += 3
            Af = [[-float(1+r), 1.], [float(1/g), -float(1/g)]]
            A = [[-(1+r), F(1)], [1/g, -1/g]]
            AC = mm(A, C)
            AA = mm(A, A)
            AAC = mm(AA, C)
            d1 = AC[0][1] - AC[1][0]
            d2 = AAC[0][1] - AAC[1][0]
            s = r+1+1/g
            p = r/g
            check_close(d1, -F(2)/(g*(r+2)+1)); tests+=1
            check_close(d2, -s*d1); tests+=1
            sinv = -d2/d1
            uinv = -(sinv+1)*d1/2
            rinv = sinv-1-uinv
            assert uinv == 1/g and rinv == r
            tests += 2
            hprime = AC[0][0]
            rinvprobe = -2*(hprime+1)/a
            ginvprobe = (2-rinvprobe*a)/(rinvprobe*a*(rinvprobe+2)-2*(rinvprobe+1))
            assert rinvprobe == r and ginvprobe == g
            tests += 2
            sf=float(s)
            disc=sqrt(sf*sf-4*float(p))
            lplus=(-sf+disc)/2
            lminus=(-sf-disc)/2
            assert lminus < lplus < 0
            tstar=log(lminus/lplus)/(lplus-lminus)
            def analytical(t):
                return float(d1)*(exp(lplus*t)-exp(lminus*t))/(lplus-lminus)
            for t in (0.01, 0.11, 0.75, 2.0, tstar, 1.12*tstar):
                E=mat_exp(Af,t)
                K=mm(E,[[float(x) for x in row] for row in C])
                direct=K[0][1]-K[1][0]
                check_close(direct, analytical(t)); tests += 1
                assert direct < 0
                tests += 1
            assert analytical(tstar) < analytical(tstar * 0.94)
            assert analytical(tstar) < analytical(tstar * 1.06)
            tests += 2
    print('PASS:',tests,'exact-rational and independent matrix-exponential checks')

if __name__ == '__main__':
    main()
