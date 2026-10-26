"""Independent arithmetic checks for a residue-imbalance theorem."""
from math import comb, isqrt


def digit_automaton(n):
    """Compute the residue 0, +1 or -1 by doubling base-five digits."""
    weights = [1, 0]
    while n:
        d = n % 5
        n //= 5
        nxt = [0, 0]
        for carry in (0, 1):
            if weights[carry] == 0:
                continue
            t = 2*d + carry
            e, carry_next = t % 5, t // 5
            if e <= 2:
                fac = 1j if e == 1 else 1
                nxt[carry_next] += weights[carry] * fac
        weights = nxt
    ans = weights[0] + 1j * weights[1]
    assert abs(ans.imag) < 1e-9
    assert ans.real in (-1, 0, 1)
    return int(ans.real)


def lucas_mod5(n):
    """Separate direct Lucas product on top 4n and bottom 2n."""
    top, bot, product = 4*n, 2*n, 1
    while top or bot:
        a, b = top % 5, bot % 5
        if b > a:
            return 0
        product = (product * comb(a, b)) % 5
        top //= 5
        bot //= 5
    return product


def gauss_mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def expected_imbalance(level):
    v = (1, 0)
    for _ in range(level):
        v = gauss_mul(v, (2, 1))
    return gauss_mul((1, 1), v)[0]


def main():
    for n in range(200):
        r = comb(4*n, 2*n) % 5
        assert digit_automaton(n) == {0: 0, 1: 1, 4: -1}[r]
    pos = neg = zero = 0
    seen = 0
    for level in range(1, 8):
        end = 5**level
        for n in range(seen, end):
            r = lucas_mod5(n)
            assert r in (0, 1, 4), (n, r)
            a = digit_automaton(n)
            assert a == {0:0, 1:1, 4:-1}[r], (n, a, r)
            if a == 1:
                pos += 1
            elif a == -1:
                neg += 1
            else:
                zero += 1
            assert abs(pos-neg) <= 20*(isqrt(n+1)+1)
        assert pos-neg == expected_imbalance(level), (level, pos-neg)
        assert pos+neg == 3**level, (level, pos+neg)
        seen = end
    print('VERIFY_OK: 200 exact binomials, 78125 independent Lucas tests, '
          'seven exact base-five block counts and a partial-sum bound')


if __name__ == '__main__':
    main()
