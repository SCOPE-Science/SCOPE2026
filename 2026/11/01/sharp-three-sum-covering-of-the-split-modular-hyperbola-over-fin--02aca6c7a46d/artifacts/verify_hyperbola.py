"""Independent finite-field enumeration of threefold reciprocal-graph sums.

Usage: python3 artifacts/verify_hyperbola.py
Only Python's standard library is required. Finite cases corroborate, but do
not prove, the theorem for arbitrary field orders.
"""

def test_field(p, degree, modulus):
    q = p**degree
    digits = [tuple((n // p**j) % p for j in range(degree)) for n in range(q)]
    idx = {vec: n for n, vec in enumerate(digits)}

    def add(a, b):
        return idx[tuple((digits[a][j] + digits[b][j]) % p for j in range(degree))]

    def mul(a, b):
        coeff = [0] * (2 * degree - 1)
        for i in range(degree):
            for j in range(degree):
                coeff[i+j] += digits[a][i] * digits[b][j]
        for j in range(2*degree-2, degree-1, -1):
            z = coeff[j]
            for i in range(degree):
                coeff[j-degree+i] -= z*modulus[i]
        return idx[tuple(coeff[i] % p for i in range(degree))]

    inverse = {}
    for a in range(1, q):
        matches = [b for b in range(1, q) if mul(a,b) == 1]
        assert len(matches) == 1, ('invalid field', p, degree, a)
        inverse[a] = matches[0]

    H = {(t, inverse[t]) for t in range(1, q)}
    two = {(add(a,c),add(b,d)) for a,b in H for c,d in H}
    three = {(add(a,c),add(b,d)) for a,b in two for c,d in H}
    zero = (0,0)
    if q >= 13:
        expect = {(a,b) for a in range(q) for b in range(q)}
        if p != 3 and q % 3 == 2:
            expect.remove(zero)
        assert three == expect, (q, len(three), len(expect), expect - three)
    if q == 11:
        assert (1, 6) not in three
    print('FIELD_OK', 'q='+str(q), 'two='+str(len(two)), 'three='+str(len(three)), 'origin='+str(zero in three))

for prime in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]:
    test_field(prime, 1, (0,1))
for prime, degree, modulus in [
    (2,2,(1,1,1)), (2,3,(1,1,0,1)), (2,4,(1,1,0,0,1)),
    (2,5,(1,0,1,0,0,1)), (3,2,(1,0,1)),
    (3,3,(1,2,0,1)), (5,2,(2,0,1)), (7,2,(1,0,1)),
]:
    test_field(prime, degree, modulus)
print('VERIFY_OK complete_prime_and_extension_field_sumsets')
