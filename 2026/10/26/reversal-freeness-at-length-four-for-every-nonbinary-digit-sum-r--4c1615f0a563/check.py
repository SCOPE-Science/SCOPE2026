"""Independent finite checks for reversal-freeness of digit-sum residues."""
from itertools import product

def test(m, N=1 << 16, max_length=10):
    # Independently form the finite word by the dyadic recursion.
    a = [0] * N
    for i in range(1, N):
        a[i] = (a[i >> 1] + (i & 1)) % m
    direct = [(i.bit_count() % m) for i in range(N)]
    assert a == direct
    # Check all length-3 residue-difference possibilities and all initial symbols.
    three = {tuple(a[i:i+3]) for i in range(N-2)}
    expected = {(v, (v+p) % m, (v+p+q) % m)
                for v, p, q in product(range(m), repeat=3)
                if p == 1 or q == 1}
    assert three == expected, (m,len(three),len(expected))
    assert len(three) == 2*m*m-m
    pairs = {tuple(a[i:i+2]) for i in range(N-1)}
    assert len(pairs) == m*m
    for n in range(3, max_length+1):
        obs = {tuple(a[i:i+n]) for i in range(N-n+1)}
        both = {w for w in obs if w[::-1] in obs}
        if n == 3:
            assert len(both) == 2*m
            assert all(w == w[::-1] for w in both)
        else:
            assert not both, (m,n,sorted(both)[:2])
    return (m,len(three),len(pairs))

def main():
    for m in range(3,9):
        print('m, triples, pairs',*test(m))
    print('MODULAR_DIGIT_SUM_REFLECTION_PASS m=3..8 N=65536 length=3..10')
if __name__ == '__main__':
    main()
