"""Independent finite verification of the palindromic-duplication inverse list theorem.

Only the explicitly indicated bounded ranges are enumerated.  The infinite
assertion rests on the separate mathematical proof, not on this script.
"""
from itertools import product
from random import Random


def minimum_spacing(k):
    assert k >= 1
    return next(s for s in range(2, k + 3) if k % (2 * s))


def parents(y, k):
    return {
        y[:i + k] + y[i + 2*k:]
        for i in range(len(y) - 2*k + 1)
        if y[i:i + 2*k] == y[i:i + 2*k][::-1]
    }


def active_parents(y, k):
    return {
        i: y[:i + k] + y[i + 2*k:]
        for i in range(len(y) - 2*k + 1)
        if y[i:i + 2*k] == y[i:i + 2*k][::-1]
    }


def witness(k, m):
    d = minimum_spacing(k)
    residues = {(k - 1) % (2*d), k % (2*d)}
    return ''.join('1' if t % (2*d) in residues else '0' for t in range(m))


def theorem(k, m):
    return 1 + (m - 2*k) // minimum_spacing(k)


def verify():
    count_words = 0
    param_cases = 0
    sampled = 0
    rng = Random(161206)
    # Exhaustive on binary inputs, including even k with 4|k.
    for k, end in [(1, 11), (2, 12), (3, 14), (4, 15), (5, 16), (6, 16), (7, 16), (8, 17)]:
        for m in range(2*k, end + 1):
            target = theorem(k, m)
            maximum = 0
            for t in product('01', repeat=m):
                y = ''.join(t)
                p = active_parents(y, k)
                maximum = max(maximum, len(set(p.values())))
                for i, v in p.items():
                    for j, w in p.items():
                        if i < j and j-i < minimum_spacing(k):
                            assert v == w, (k, m, y, i, j)
                count_words += 1
            assert maximum == target, (k, m, maximum, target)
            assert len(parents(witness(k,m), k)) == target
            param_cases += 1

    # Ternary checks: alphabet independence, not merely binary evidence.
    for k, end in [(1, 8), (2, 9), (3, 10), (4, 9)]:
        for m in range(2*k, end + 1):
            maximum = 0
            for t in product('012', repeat=m):
                maximum = max(maximum, len(parents(''.join(t), k)))
                count_words += 1
            assert maximum == theorem(k, m), (k, m, maximum)
            param_cases += 1

    # Many k and m, including k divisible by 4, 6, 8, etc.
    for k in range(1, 701):
        d = minimum_spacing(k)
        for steps in (0, 1, 2, 3, 9, 16):
            m = 2*k + steps*d + (steps % 2)
            y = witness(k, m)
            p = active_parents(y, k)
            expected = 1 + (m - 2*k) // d
            assert len(set(p.values())) == expected, (k, m, d, len(set(p.values())), expected)
            assert all(i in p for i in range(0, m-2*k+1, d))
            sampled += 1

    # Random q-ary inputs, including ternary and quaternary alphabets.
    for _ in range(7000):
        k = rng.randint(1, 30)
        m = 2*k + rng.randint(0, 40)
        q = rng.randint(2, 5)
        y = ''.join(str(rng.randrange(q)) for _ in range(m))
        p = active_parents(y, k)
        assert len(set(p.values())) <= theorem(k, m)
        for i,v in p.items():
            for j,w in p.items():
                if i < j and j-i < minimum_spacing(k):
                    assert v == w, (k,m,y,i,j)
        sampled += 1
    assert minimum_spacing(4) == 3
    assert minimum_spacing(12) == 4
    assert minimum_spacing(24) == 5
    print(f'VERIFY_OK exhaustive_cases={param_cases} exhaustive_received_words={count_words} sampled_or_witness_cases={sampled} k_witness_range=1..700 max_alphabet_tested=5')

if __name__ == '__main__':
    verify()
