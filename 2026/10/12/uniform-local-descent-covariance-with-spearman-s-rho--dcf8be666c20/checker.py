from fractions import Fraction
from itertools import permutations
from math import comb

def stats_for_n(n):
    rows = []
    for p in permutations(range(1, n+1)):
        I = [int(p[i] > p[i+1]) for i in range(n-1)]
        A = sum(I)
        D = sum((p[j]-(j+1))**2 for j in range(n))
        R = Fraction(1) - Fraction(6*D, n*(n*n-1))
        rows.append((I, A, D, R))
    N = len(rows)

    ED = sum((Fraction(D) for _,_,D,_ in rows), Fraction(0))/N
    ER = sum((R for *_,R in rows), Fraction(0))/N
    EA = sum((Fraction(A) for _,A,_,_ in rows), Fraction(0))/N
    assert ER == 0

    local_checks = 0
    for i in range(n-1):
        EI = sum((Fraction(I[i]) for I,_,_,_ in rows), Fraction(0))/N
        assert EI == Fraction(1,2)

        EID = sum((Fraction(I[i]*D) for I,_,D,_ in rows), Fraction(0))/N
        covD = EID - EI*ED
        assert covD == Fraction(n+1, 6)
        local_checks += 1

        EIR = sum((Fraction(I[i])*R for I,_,_,R in rows), Fraction(0))/N
        covR = EIR - EI*ER
        assert covR == -Fraction(1, n*(n-1))
        local_checks += 1

        desc = [R for I,_,_,R in rows if I[i]]
        asc = [R for I,_,_,R in rows if not I[i]]
        assert sum(desc, Fraction(0))/len(desc) == -Fraction(2, n*(n-1))
        local_checks += 1
        assert sum(asc, Fraction(0))/len(asc) == Fraction(2, n*(n-1))
        local_checks += 1

    EAD = sum((Fraction(A*D) for _,A,D,_ in rows), Fraction(0))/N
    EAR = sum((Fraction(A)*R for _,A,_,R in rows), Fraction(0))/N
    covAD = EAD - EA*ED
    covAR = EAR - EA*ER
    assert covAD == Fraction(n*n-1, 6)
    assert covAR == -Fraction(1, n)

    EA2 = sum((Fraction(A*A) for _,A,_,_ in rows), Fraction(0))/N
    ER2 = sum((R*R for *_,R in rows), Fraction(0))/N
    varA = EA2 - EA*EA
    varR = ER2 - ER*ER
    assert varA == Fraction(n+1, 12)
    assert varR == Fraction(1, n-1)

    corr2 = covAR*covAR/(varA*varR)
    target_corr2 = Fraction(12*(n-1), n*n*(n+1))
    assert corr2 == target_corr2
    return N, local_checks, 5

def conditional_pair_checks(max_n=500):
    checks = 0
    for n in range(2, max_n+1):
        pairs = [(a,b) for a in range(1,n+1) for b in range(a+1,n+1)]
        den = len(pairs)
        emin = Fraction(sum(a for a,b in pairs), den)
        emax = Fraction(sum(b for a,b in pairs), den)
        assert emin == Fraction(n+1,3)
        assert emax == Fraction(2*(n+1),3)
        checks += 2

        mu = Fraction(n+1,2)
        for i in range(1,n):
            shift = i*(emax-mu) + (i+1)*(emin-mu)
            assert shift == -Fraction(n+1,6)
            checks += 1
    return checks

def run():
    perms = 0
    local = 0
    global_checks = 0
    for n in range(2,10):
        a,b,c = stats_for_n(n)
        perms += a
        local += b
        global_checks += c
    pair_checks = conditional_pair_checks()
    print("VERIFY_OK")
    print(f"permutations_checked={perms}")
    print(f"local_formula_checks={local}")
    print(f"global_formula_checks={global_checks}")
    print(f"conditional_pair_checks={pair_checks}")
    print("max_pair_n=500")

if __name__ == "__main__":
    run()
