from fractions import Fraction
from itertools import permutations

def cycles(p):
    n = len(p)
    seen = [False] * n
    c = 0
    for i in range(n):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j] - 1
    return c

def H(n, power=1):
    return sum((Fraction(1, j**power) for j in range(1, n+1)), Fraction(0))

def arrays(n):
    return [
        [[(i-j)**2 for j in range(1,n+1)] for i in range(1,n+1)],
        [[i*j + 2*i - 3*j for j in range(1,n+1)] for i in range(1,n+1)],
        [[1 if i == j else 0 for j in range(1,n+1)] for i in range(1,n+1)],
        [[(2*i + 5*j + i*j) % 11 - 5 for j in range(1,n+1)] for i in range(1,n+1)],
    ]

def trace_formula(A):
    n = len(A)
    diag = sum(A[i][i] for i in range(n))
    total = sum(sum(row) for row in A)
    return Fraction(diag, n) - Fraction(total, n*n)

def run():
    perms_checked = 0
    global_checks = 0
    conditional_checks = 0
    array_checks = 0

    for n in range(2, 10):
        rows = []
        for p in permutations(range(1, n+1)):
            C = cycles(p)
            D = sum((p[i]-(i+1))**2 for i in range(n))
            R = Fraction(1) - Fraction(6*D, n*(n*n-1))
            K = n - C
            rows.append((p,C,D,R,K))
        N = len(rows)
        perms_checked += N

        EC = sum((Fraction(C) for _,C,_,_,_ in rows), Fraction(0))/N
        ED = sum((Fraction(D) for _,_,D,_,_ in rows), Fraction(0))/N
        ER = sum((R for _,_,_,R,_ in rows), Fraction(0))/N
        EK = sum((Fraction(K) for _,_,_,_,K in rows), Fraction(0))/N
        EC2 = sum((Fraction(C*C) for _,C,_,_,_ in rows), Fraction(0))/N
        ER2 = sum((R*R for _,_,_,R,_ in rows), Fraction(0))/N
        ECD = sum((Fraction(C*D) for _,C,D,_,_ in rows), Fraction(0))/N
        ECR = sum((Fraction(C)*R for _,C,_,R,_ in rows), Fraction(0))/N
        EKR = sum((Fraction(K)*R for _,_,_,R,K in rows), Fraction(0))/N

        assert EC == H(n)
        global_checks += 1
        varC = EC2 - EC*EC
        assert varC == H(n) - H(n,2)
        global_checks += 1
        covCD = ECD - EC*ED
        assert covCD == -Fraction(n*n-1, 6)
        global_checks += 1
        covCR = ECR - EC*ER
        assert covCR == Fraction(1,n)
        global_checks += 1
        covKR = EKR - EK*ER
        assert covKR == -Fraction(1,n)
        global_checks += 1
        varR = ER2 - ER*ER
        assert varR == Fraction(1,n-1)
        global_checks += 1
        corr2 = covKR*covKR/(varC*varR)
        assert corr2 == Fraction(n-1, n*n)/(H(n)-H(n,2))
        global_checks += 1

        if n <= 8:
            for i in range(n):
                for j in range(1,n+1):
                    subset = [C for p,C,_,_,_ in rows if p[i] == j]
                    mean = sum((Fraction(C) for C in subset), Fraction(0))/len(subset)
                    target = (Fraction(1) + H(n-1)) if j == i+1 else H(n-1)
                    assert mean == target
                    conditional_checks += 1

            for A in arrays(n):
                EX = Fraction(0)
                ECX = Fraction(0)
                for p,C,_,_,_ in rows:
                    X = sum(A[i][p[i]-1] for i in range(n))
                    EX += Fraction(X)
                    ECX += Fraction(C*X)
                EX /= N
                ECX /= N
                cov = ECX - EC*EX
                assert cov == trace_formula(A)
                array_checks += 1

    print("VERIFY_OK")
    print(f"permutations_checked={perms_checked}")
    print(f"global_formula_checks={global_checks}")
    print(f"conditional_entry_checks={conditional_checks}")
    print(f"general_array_checks={array_checks}")
    print("max_exhaustive_n=9")

if __name__ == "__main__":
    run()
