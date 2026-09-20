from fractions import Fraction

def verify(q):
    # q is prime. Enumerate U,V in F_q and the first q indicators.
    total_R = 0
    b = q - 1

    # Pairwise joint-success counts.
    for i in range(q):
        for j in range(i + 1, q):
            both = 0
            for U in range(q):
                for V in range(q):
                    bi = ((U + i * V) % q == 0)
                    bj = ((U + j * V) % q == 0)
                    both += int(bi and bj)
            assert both == 1  # probability 1/q^2

    for U in range(q):
        for V in range(q):
            S = 0
            R = None
            for i in range(q):
                B = int((U + i * V) % q == 0)
                X = 1 + (2 * q - 1) * B
                S += X
                if S > b:
                    R = S - b
                    break
            assert R is not None
            total_R += R

    enumerated = Fraction(total_R, q * q)
    formula = Fraction(3 * q * q - 2 * q + 3, 2 * q)
    mean_x = Fraction(3 * q - 1, q)
    mean_x2 = Fraction(4 * q * q + q - 1, q)
    lorden_rhs = mean_x2 / mean_x
    gap = enumerated - lorden_rhs
    gap_formula = Fraction((q - 1) * (q * q - 10 * q + 3), 2 * q * (3 * q - 1))

    assert enumerated == formula
    assert gap == gap_formula
    return enumerated, lorden_rhs, gap

for q in (11, 13, 31):
    er, rhs, gap = verify(q)
    print(q, er, rhs, gap, float(er / rhs))
