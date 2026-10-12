from math import comb, factorial

def square_recurrence(n, known):
    out = n*n
    for r in range(1, n):
        out += ((n-r)*(n-r)-1) * comb(n,r)**2 * known[r]
    return out

sq = {1: 1}
square_checks = 0
for n in range(2, 31):
    sq[n] = square_recurrence(n, sq)
    assert sq[n] == factorial(n)**2
    square_checks += 1

general_checks = 0
for v in range(1, 15):
    for w in range(1, 15):
        for u in range(1, min(v,w)+1):
            inner = u*w
            for r in range(1, u):
                inner += ((u-r)*(w-r)-1) * comb(u,r) * comb(w,r) * factorial(r)**2
            got = comb(v,u) * inner
            expected = comb(v,u) * comb(w,u) * factorial(u)**2
            assert got == expected, (v,w,u,got,expected)
            general_checks += 1

# Exact cross-multiplied telescoping identities.
telescoping_checks = 0
for j in range(1, 40):
    # (j^2-1)/(j!)^2 = 1/((j-1)!)^2 - 1/(j!)^2
    lhs_num = j*j - 1
    den = factorial(j)**2
    rhs_num = factorial(j)**2 - factorial(j-1)**2
    rhs_den = factorial(j-1)**2 * factorial(j)**2
    assert lhs_num * rhs_den == rhs_num * den
    telescoping_checks += 1

for q in range(0, 20):
    for j in range(1, 30):
        # [j(q+j)-1]/[j!(q+j)!]
        # = 1/[(j-1)!(q+j-1)!] - 1/[j!(q+j)!].
        a = factorial(j-1)*factorial(q+j-1)
        b = factorial(j)*factorial(q+j)
        lhs_num = j*(q+j)-1
        assert lhs_num * a == b - a
        telescoping_checks += 1

print("VERIFY_OK", square_checks, general_checks, telescoping_checks)
