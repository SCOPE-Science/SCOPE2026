"""Exact arithmetic checks for the two-run digit-sum density theorem.

Runs with Python 3 using standard-library fractions only.
The infinite proof is mathematical; these checks validate identities and finite cases.
"""
from fractions import Fraction


def shift(r, s, gap):
    assert min(r, s, gap) >= 1
    return (1 << r) - 1 + ((1 << s) - 1 << (r + gap))


def tail(w, carries, state):
    if carries > w:
        return Fraction(0)
    return Fraction(1) if state == 0 else 1 - Fraction(1, 2 ** (w - carries + 1))


def density_dp(r, s, gap):
    t = shift(r, s, gap)
    w = r + s
    probs = {(0, 0): Fraction(1)}
    for bitno in range(t.bit_length()):
        tb = (t >> bitno) & 1
        next_probs = {}
        for (carry, count), probability in probs.items():
            for nb in (0, 1):
                newcarry = int(nb + tb + carry >= 2)
                key = (newcarry, count + newcarry)
                next_probs[key] = next_probs.get(key, Fraction(0)) + probability / 2
        probs = next_probs
    return sum(probability * tail(w, count, carry)
               for (carry, count), probability in probs.items())


def density_enum(r, s, gap):
    t = shift(r, s, gap)
    width = t.bit_length()
    w = r + s
    answer = Fraction(0)
    for n in range(1 << width):
        state = count = 0
        for j in range(width):
            state = int(((n >> j) & 1) + ((t >> j) & 1) + state >= 2)
            count += state
        answer += tail(w, count, state)
    return answer / (1 << width)


def N(r, s, h):
    if h < 0:
        return 0
    return sum(i + (h-i) == h and 0 <= h-i < s for i in range(r))


def increment(r, s, gap):
    w = r + s
    if gap >= w:
        return Fraction(0)
    h = w - gap - 1
    a = Fraction(N(r, s, h))
    for k in range(1, h+1):
        a -= Fraction(N(r, s, h-k), 4**k)
    assert a > 0, (r, s, gap, a)
    return a / 4**(gap+1)


def main():
    checks = 0
    for r in range(1, 10):
        for s in range(1, 10):
            last = density_dp(r, s, 1)
            for gap in range(1, r+s+3):
                nxt = density_dp(r, s, gap+1)
                predicted = increment(r, s, gap)
                assert nxt - last == predicted, (r, s, gap, nxt-last, predicted)
                checks += 1
                last = nxt
    enum_checks = 0
    for r in range(1, 4):
        for s in range(1, 4):
            for gap in range(1, r+s+2):
                assert density_dp(r, s, gap) == density_enum(r, s, gap)
                enum_checks += 1
    assert density_dp(1, 1, 1) == Fraction(5,8)
    assert density_dp(1, 1, 2) == Fraction(11,16)
    assert density_dp(2, 2, 1) == Fraction(73,128)
    assert density_dp(2, 2, 4) == Fraction(161,256)
    print('VERIFY_OK: exact increment identities',checks,'; independent residue-class enumerations',enum_checks)


if __name__ == '__main__':
    main()
