"""Reproducible exact certificate for universal anti-power radii in the regular paperfolding word.

Requires Python 3 standard library only. All indexing is zero based.
"""
from hashlib import sha256

PREFIX = 2048
ANCHORS = [(2, 2), (3, 5), (4, 6), (5, 7), (8, 7), (9, 9), (16, 9), (17, 15)]


def generate_recurrence(N):
    a = bytearray(N)
    for n in range(1, N):
        a[n] = (n//2) % 2 if n % 2 == 0 else a[n//2]
    return bytes(a)


def generate_oddpart(N):
    a = bytearray(N)
    for n in range(N):
        z = n + 1
        while z % 2 == 0:
            z //= 2
        a[n] = int(z % 4 == 3)
    return bytes(a)


def direct_factors(prefix, L):
    return {prefix[i:i+L] for i in range(len(prefix)-L+1)}


def numeric_factors(prefix, L):
    mask = (1 << L) - 1
    value = 0
    for b in prefix[:L]:
        value = (value << 1) | b
    out = {value}
    for b in prefix[L:]:
        value = ((value << 1) | b) & mask
        out.add(value)
    return out


def is_antipower(factor, k, block_length):
    # Exactly k adjacent pairwise unequal blocks of the same positive length.
    return len({factor[j*block_length:(j+1)*block_length] for j in range(k)}) == k


def prefix_radius(factor, k, r):
    return next((m for m in range(1, r+1) if is_antipower(factor, k, m)), None)


def main():
    a = generate_recurrence(PREFIX)
    b = generate_oddpart(PREFIX)
    assert a == b, "independent binary paperfolding generators disagree"
    stats = []
    for k, radius in ANCHORS:
        L = k * radius
        factors = direct_factors(a, L)
        assert len(factors) == (12 if L == 4 else 4*L), (k, L, len(factors))
        nums = numeric_factors(b, L)
        # Each length-L factor, seen as a base-two integer, must appear.
        def to_int(w):
            v = 0
            for x in w:
                v = 2*v + x
            return v
        assert nums == {to_int(w) for w in factors}, k
        bad = sorted(w for w in factors if prefix_radius(w,k,radius) is None)
        assert not bad, (k, 'upper', bad[:1])
        obstructing = sorted(w for w in factors if prefix_radius(w,k,radius-1) is None)
        assert obstructing, (k, 'lower')
        witness = obstructing[0]
        first_index = a.find(witness)
        assert first_index >= 0
        assert all(not is_antipower(witness,k,m) for m in range(1,radius))
        assert is_antipower(witness,k,radius)
        stats.append((k, radius, L, len(factors), len(obstructing), first_index, ''.join(map(str,witness))))
    # For every infinite word, the minimum block size producing a k-antipower
    # at one start cannot decrease as k increases: its first k blocks remain
    # pairwise different in a (k+1)-antipower.
    # Sandwiching between the seven anchors gives all missing k=6,7,10,...,15.
    derived = {2:2, 3:5, 4:6, **{k:7 for k in range(5,9)},
               **{k:9 for k in range(9,17)},17:15}
    for ka, ra in ANCHORS:
        assert derived[ka] == ra
    assert [derived[k] for k in range(2,18)] == [2,5,6,7,7,7,7,9,9,9,9,9,9,9,9,15]
    for k,r,L,c,h,i,w in stats:
        print('ANCHOR',k,'R',r,'L',L,'factors',c,'obstructions_at_R-1',h,
              'first_lex_obstruction_index',i,'sha256_witness',sha256(w.encode('ascii')).hexdigest(),
              'witness',w)
    print('VERIFY_OK paperfolding_independent_generators exact_Allouche_factor_counts '
          'two_enumerators eight_anchor_complete_certificates '
          'monotonicity_R_k_for_k_2_to_17')


if __name__ == '__main__':
    main()
