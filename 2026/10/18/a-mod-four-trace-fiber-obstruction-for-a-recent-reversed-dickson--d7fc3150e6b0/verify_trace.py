"""Exact small-field checks of the trace-zero fibers of G_q, no dependencies."""

IRREDUCIBLE = {8: 0x11B, 12: 0x1009, 16: 0x1002B}


def mul(a, b, poly, degree):
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= poly
    return ans


def power(a, exponent, poly, degree):
    ans = 1
    while exponent:
        if exponent & 1:
            ans = mul(ans, a, poly, degree)
        a = mul(a, a, poly, degree)
        exponent >>= 1
    return ans


def check(s):
    degree = 4 * s
    q = 1 << s
    poly = IRREDUCIBLE[degree]
    total = 1 << degree
    # Independently compute all four q-Frobenius transforms.
    frob = [power(x, q, poly, degree) for x in range(total)]
    trace = [x ^ frob[x] ^ frob[frob[x]] ^ frob[frob[frob[x]]]
             for x in range(total)]
    counts = {w: 0 for w in set(trace)}
    assert len(counts) == q
    for x in range(total):
        z = x ^ frob[x]
        w = trace[x]
        z_q2 = frob[frob[z]]
        g = x ^ z_q2 ^ mul(w, power(z, q-1, poly, degree), poly, degree)
        if trace[g] == 0:
            counts[w] += 1
    assert counts[0] == q ** 3, (s, counts[0])
    predicted_nonzero = 4 * q if s % 4 == 3 else 0
    assert all(counts[w] == predicted_nonzero for w in counts if w != 0), (s, counts)
    assert sum(counts.values()) == q ** 3 + (q-1) * predicted_nonzero
    print(f'q={q}: trace-zero inputs at w=0: {counts[0]}; '
          f'per nonzero w: {predicted_nonzero}; total: {sum(counts.values())}')


if __name__ == '__main__':
    for s in (2, 3, 4):
        check(s)
    print('VERIFY_OK')
