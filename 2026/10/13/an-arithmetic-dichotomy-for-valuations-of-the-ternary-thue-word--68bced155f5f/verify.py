"""Finite reproducible checks for the weighted-complexity classification of vtm.

This program checks selected finite factor sets; it is not a proof of the
all-length theorem, which follows from the Parikh-spectrum lemma and arithmetic.
"""

from itertools import product

MORPHISM = {"0": "012", "1": "02", "2": "1"}


def prefix(min_length=262144):
    word = "0"
    while len(word) < min_length:
        word = "".join(MORPHISM[x] for x in word)
    assert word.startswith("012021012")
    return word


def parikh_vectors(word, n):
    """All Parikh vectors in this *finite* string's length-n windows."""
    assert 0 < n <= len(word)
    counts = [word[:n].count(c) for c in "012"]
    answer = {tuple(counts)}
    for i in range(n, len(word)):
        counts[ord(word[i-n]) - 48] -= 1
        counts[ord(word[i]) - 48] += 1
        answer.add(tuple(counts))
    return answer


def predicted_injective(weights):
    a0, a1, a2 = weights
    A, E = a0 + a2 - 2 * a1, a0 - a2
    return A != 0 and E % A != 0


def statistics(vectors, weights):
    return len(vectors), len({sum(x*y for x,y in zip(p, weights)) for p in vectors})


def main():
    word = prefix()
    cases = [(0,1,2), (0,1,3), (0,1,4), (0,1,5), (0,2,7),
             (0,2,8), (0,2,9), (1,3,11), (5,5,5), (3,-2,7),
             (0,5,9), (-1,-2,-5)]
    lengths = [1, 2, 3, 4, 5, 7, 11, 12, 19, 31, 43, 71, 99, 171]
    cache = {}
    for n in lengths:
        vectors = parikh_vectors(word, n)
        cache[n] = vectors
        ones = sorted({p[1] for p in vectors})
        assert ones == list(range(min(ones),max(ones)+1))
        reconstructed = set()
        for j in ones:
            rem = n-j
            cs = (0,) if rem % 2 == 0 else (-1,1)
            for c in cs:
                reconstructed.add(((rem+c)//2, j, (rem-c)//2))
        assert vectors == reconstructed, (n, vectors.symmetric_difference(reconstructed))
    for weights in cases:
        injective = predicted_injective(weights)
        counts = {n: statistics(cache[n], weights) for n in lengths}
        if injective:
            assert all(a==b for a,b in counts.values()), (weights, counts)
        else:
            # For large |E/A| the first collision can occur far beyond
            # these selected lengths. Absence here proves nothing infinite.
            A = weights[0] + weights[2] - 2*weights[1]
            E = weights[0] - weights[2]
            if A == 0 or abs(E // A) <= 2:
                assert any(a>b for a,b in counts.values()), (weights, counts)
    # Initial published exceptional positions for two valuation rays.
    for val, expected in [(3,11),(4,43)]:
        first = next(n for n in range(1,expected+1)
                     if (lambda v: len(v) > len({p[1]+val*p[2] for p in v}))
                     (parikh_vectors(word, n)))
        assert first == expected, (val, first, expected)
    # Exactly the first five n_k and corresponding Parikh widths.
    nk = 1
    for k in range(5):
        vec = parikh_vectors(word, nk)
        ones = [p[1] for p in vec]
        assert max(ones)-min(ones) == k+1, (k,nk)
        nk = 4*nk-1
    # Independent arithmetic test on the complete *synthetic* spectrum of
    # all allowed Parikh vectors for odd length 61 and 1-counts 0..20.
    # This does NOT assert that those are the factors of any fixed word.
    synthetic = set()
    n = 61
    for j in range(21):
        r = n-j
        for c in ((0,) if r % 2 == 0 else (-1,1)):
            synthetic.add(((r+c)//2, j, (r-c)//2))
    checked = 0
    for weights in product(range(-3,4), repeat=3):
        p, q = statistics(synthetic, weights)
        assert (p == q) == predicted_injective(weights), (weights,p,q)
        checked += 1
    assert checked == 343
    print("VERIFY_OK sampled_lengths=%d valuations=%d prefix=%d widths=1..5 published_first_failures=11,43 arithmetic_triples=%d" %
          (len(lengths), len(cases), len(word), checked))

if __name__ == "__main__":
    main()
