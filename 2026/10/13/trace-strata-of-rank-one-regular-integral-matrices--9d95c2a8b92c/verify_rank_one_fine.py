from math import gcd

# Finite sanity checks for the residue-class formulas in the accompanying proof.
# These checks do not prove the infinite theorem.

def units_mod(n):
    if n == 1:
        return [0]
    return [a for a in range(n) if gcd(a, n) == 1]

def sign_orbits(n):
    U = set(units_mod(n))
    out = []
    while U:
        a = min(U)
        orb = {a, (-a) % n} if n > 1 else {0}
        out.append(tuple(sorted(orb)))
        U -= orb
    return out

special = []
for n in range(1, 101):
    orbs = sign_orbits(n)
    expected = 1 if n <= 2 else len(units_mod(n)) // 2
    assert len(orbs) == expected
    fine_orb = {1 % n, (-1) % n} if n > 1 else {0}
    all_fine = all(set(o) == fine_orb for o in orbs)
    if all_fine:
        special.append(n)
assert special == [1, 2, 3, 4, 6]

# Check the upper-triangular conjugation formula on a bounded parameter box.
# P^{-1} B(t,b) P = B(t, eps*t*m + eps*delta*b).
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

for t in range(-8,9):
    for b in range(-8,9):
        for eps in (-1,1):
            for delta in (-1,1):
                for m in range(-3,4):
                    B = [[t,b],[0,0]]
                    P = [[eps,m],[0,delta]]
                    Pinv = [[eps,-eps*m*delta],[0,delta]]
                    C = matmul(matmul(Pinv,B),P)
                    bp = eps*t*m + eps*delta*b
                    assert C == [[t,bp],[0,0]]

print('TRACE_MAGNITUDES_WITH_ONLY_FINE_CLASSES=', special)
print('TRACE_5_ORBITS=', sign_orbits(5))
print('TRACE_8_ORBITS=', sign_orbits(8))
print('CONJUGATION_FORMULA_CHECK_OK')
print('CHECK_OK')
