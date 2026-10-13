from fractions import Fraction
from itertools import permutations

def closed(n):
    EF = Fraction(n*n - 1, 3)
    ED = Fraction(n*(n*n - 1), 6)
    VF = Fraction((n+1)*(2*n*n+7), 45)
    VD = Fraction(n*n*(n-1)*(n+1)*(n+1), 36)
    CFD = Fraction(n*(n+1)*(n*n+1), 30)
    CFR = -Fraction(n*n+1, 5*(n-1))
    VR = Fraction(1, n-1)
    corr2 = Fraction(9*(n*n+1)*(n*n+1),
                     5*(n-1)*(n+1)*(2*n*n+7))
    return EF, ED, VF, VD, CFD, CFR, VR, corr2

def brute(n):
    count = 0
    sF = sD = sF2 = sD2 = sFD = 0
    for p in permutations(range(1, n+1)):
        F = sum(abs(i+1-p[i]) for i in range(n))
        D = sum((i+1-p[i])**2 for i in range(n))
        count += 1
        sF += F
        sD += D
        sF2 += F*F
        sD2 += D*D
        sFD += F*D
    EF = Fraction(sF, count)
    ED = Fraction(sD, count)
    VF = Fraction(sF2, count) - EF*EF
    VD = Fraction(sD2, count) - ED*ED
    CFD = Fraction(sFD, count) - EF*ED
    scale = Fraction(-6, n*(n*n-1))
    CFR = scale*CFD
    VR = scale*scale*VD
    corr2 = CFR*CFR/(VF*VR)
    return EF, ED, VF, VD, CFD, CFR, VR, corr2, count

def centered_inner(n):
    A = [[Fraction((i-j)**2) for j in range(1,n+1)]
         for i in range(1,n+1)]
    B = [[Fraction(abs(i-j)) for j in range(1,n+1)]
         for i in range(1,n+1)]

    def dc(M):
        row = [sum(r, Fraction(0))/n for r in M]
        col = [sum(M[i][j] for i in range(n))/n
               for j in range(n)]
        grand = sum(row, Fraction(0))/n
        return [[M[i][j]-row[i]-col[j]+grand
                 for j in range(n)] for i in range(n)]

    Ac = dc(A)
    Bc = dc(B)
    ab = sum((Ac[i][j]*Bc[i][j]
              for i in range(n) for j in range(n)),
             Fraction(0))/(n-1)
    aa = sum((Ac[i][j]*Ac[i][j]
              for i in range(n) for j in range(n)),
             Fraction(0))/(n-1)
    bb = sum((Bc[i][j]*Bc[i][j]
              for i in range(n) for j in range(n)),
             Fraction(0))/(n-1)
    return ab, aa, bb

def run():
    permutations_checked = 0
    brute_assertions = 0
    for n in range(2,10):
        b = brute(n)
        c = closed(n)
        permutations_checked += b[-1]
        for got, want in zip(b[:-1], c):
            assert got == want
            brute_assertions += 1

    matrix_assertions = 0
    for n in range(2,61):
        ab, aa, bb = centered_inner(n)
        _, _, VF, VD, CFD, _, _, _ = closed(n)
        assert ab == CFD
        matrix_assertions += 1
        assert aa == VD
        matrix_assertions += 1
        assert bb == VF
        matrix_assertions += 1

    print("VERIFY_OK")
    print(f"permutations_checked={permutations_checked}")
    print(f"brute_formula_assertions={brute_assertions}")
    print("matrix_dimensions_checked=59")
    print(f"matrix_formula_assertions={matrix_assertions}")

if __name__ == "__main__":
    run()
