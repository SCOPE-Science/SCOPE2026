"""Direct finite factor enumeration for a separated reversal-language construction."""
from math import ceil


def de_bruijn_binary(k):
    """Standard binary Lyndon-cycle generation; result length 2**k."""
    a = [0] * (2 * k + 1)
    out = []
    def rec(t, p):
        if t > k:
            if k % p == 0:
                out.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            rec(t + 1, p)
            for j in range(a[t - p] + 1, 2):
                a[t] = j
                rec(t + 1, t)
    rec(1, 1)
    assert len(out) == 2**k
    assert len({tuple((out + out)[i:i + k]) for i in range(2**k)}) == 2**k
    return out


def component_block(k, component):
    cyc = de_bruijn_binary(k)
    if component < 3:
        bits = [0] * k + cyc + cyc[:k - 1] + [0] * k
        return ''.join(chr(ord('a') + 2 * component + b) for b in bits)
    pad = 3 * ceil(k / 3)
    core = cyc * 3 + cyc[:k - 1]
    suffix = pad + ((-len(core)) % 3)
    bits = [0] * pad + core + [0] * suffix
    block = ''.join(chr(ord('g') + 2 * (j % 3) + b) for j, b in enumerate(bits))
    assert len(block) % 3 == 0
    return block


def prefix(max_stage):
    return ''.join(component_block(k, i) + '#' * k for k in range(1, max_stage + 1) for i in range(4))


def profile(w, n):
    factors = {w[i:i+n] for i in range(len(w)-n+1)}
    pure = {s for s in factors if '#' not in s}
    marked = factors - pure
    classes = {min(s, s[::-1]) for s in factors}
    pure_classes = {min(s, s[::-1]) for s in pure}
    return len(factors), len(classes), len(pure), len(pure_classes), len(marked)


def main():
    print('n length factor_count reflection_count pure_count pure_reflection marked_count')
    for n in range(2, 10):
        w = prefix(n + 2)
        C, R, P, PR, marked = profile(w,n)
        expect_P = 6*2**n
        expect_PR = 3*((2**n + 2**ceil(n/2))//2) + 3*2**n
        assert P == expect_P, (n,P,expect_P)
        assert PR == expect_PR, (n,PR,expect_PR)
        assert 0 <= C-P == marked
        assert R-PR <= marked
        assert marked <= 8*n*n+1
        print(n,len(w),C,R,P,PR,marked)
    print('PASS: pure factor and reflection class formulas for n=2..9, with marked terms isolated.')

if __name__ == '__main__':
    main()
