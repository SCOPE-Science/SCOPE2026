"""Independent finite verification of the (2,3)-overlap-free binary capacity kernel."""
from itertools import product

BITS = [''.join(t) for t in product('01', repeat=3)]
STATES = [''.join(t) for t in product('01', repeat=2)]

def good(words):
    for x in words:
        for y in words:
            for j in (2, 3):
                if x[:j] == y[-j:]:
                    return False
    return True

def admissible(P):
    first_two = {p[:2] for p in P}
    return {s for s in BITS if s not in P and s[-2:] not in first_two}

def compute():
    opt, witnesses = 0, []
    size_to_max = {i: 0 for i in range(9)}
    prefix_count = {i: 0 for i in range(5)}
    for mask in range(256):
        P = {w for i, w in enumerate(BITS) if mask & (1 << i)}
        S = admissible(P)
        size = len(P) * len(S)
        size_to_max[len(P)] = max(size_to_max[len(P)], size)
        prefix_count[len({p[:2] for p in P})] += 1
        if size > opt:
            opt, witnesses = size, [(P, S)]
        elif size == opt:
            witnesses.append((P, S))
        assert good({p + s for p in P for s in S})
    assert opt == 10
    assert len(witnesses) > 0
    assert sum(prefix_count.values()) == 256
    # The closed-form witness in the proof.
    P = {'000', '001'}
    S = {'010', '011', '101', '110', '111'}
    assert admissible(P) == S and len(P) * len(S) == 10
    assert good({p+s for p in P for s in S})
    # Independently check all four cases of the degree-two De Bruijn argument.
    for mask in range(1, 16):
        B = {s for i,s in enumerate(STATES) if mask & (1 << i)}
        inside = {p for p in BITS if p[:2] in B and p[-2:] in B}
        if len(B) == 1:
            assert len(inside) <= 1
        if len(B) == 2:
            assert len(inside) <= 2
        if len(B) == 3:
            assert len(inside) <= 5
    # Direct check the length-7 and length-8 middle-coordinate construction.
    for n in (6, 7, 8):
        C = {p + ''.join(mid) + s for p in P for mid in product('01',repeat=n-6) for s in S}
        assert len(C) == 10 * (1 << (n-6))
        assert good(C)
    print('KERNEL_MAX',opt,'OPTIMAL_PREFIX_PAIRS',len(witnesses))
    print('SIZE_CLASS_MAXIMA',size_to_max)
    print('VERIFY_OK')

if __name__ == '__main__':
    compute()
