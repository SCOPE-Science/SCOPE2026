"""Exact finite certificate for greedy shortest superstrings of binary trigrams.

Run: python3 verify.py
Only the standard library is required. Words are nonempty binary strings.
"""
from functools import lru_cache
from itertools import product
from fractions import Fraction

K = 3
WORDS = tuple(''.join(t) for t in product('01', repeat=K))
assert WORDS == ('000','001','010','011','100','101','110','111')


def overlap(a, b):
    """Maximum suffix-prefix overlap, including a complete shorter word."""
    for t in range(min(len(a),len(b)), 0, -1):
        if a[-t:] == b[:t]:
            return t
    return 0


@lru_cache(maxsize=None)
def worst_greedy(state):
    """The largest terminal length under all maximum-overlap ordered merges."""
    if len(state) == 1:
        return len(state[0])
    choices = [(overlap(state[i], state[j]), i, j)
               for i in range(len(state)) for j in range(len(state)) if i != j]
    top = max(z for z, i, j in choices)
    ans = 0
    for z, i, j in choices:
        if z != top:
            continue
        merged = state[i] + state[j][z:]
        following = tuple(sorted([x for h, x in enumerate(state) if h not in (i, j)]
                                 + [merged]))
        ans = max(ans, worst_greedy(following))
    return ans


def brute_force_optima():
    """An unrelated certificate: list every binary superstring of length <=10."""
    infinity = 11
    ans = [infinity] * 256
    for length in range(K, 11):
        for digits in product('01', repeat=length):
            word = ''.join(digits)
            seen = 0
            for i in range(length-K+1):
                seen |= 1 << int(word[i:i+K], 2)
            sub = seen
            while sub:
                ans[sub] = min(ans[sub], length)
                sub = (sub-1) & seen
    assert max(ans[1:]) <= 10  # A linear binary order-three de Bruijn sequence.
    return ans


def optimal_overlap_dp(subset):
    """Independent Bellman certificate using Hamiltonian paths in the overlap graph."""
    n = len(subset)
    dp = {(1 << i, i): K for i in range(n)}
    for mask in range(1, 1 << n):
        for last in range(n):
            v = dp.get((mask, last))
            if v is None:
                continue
            for nxt in range(n):
                if not (mask & (1 << nxt)):
                    key = (mask | (1 << nxt), nxt)
                    val = v + K - overlap(subset[last],subset[nxt])
                    dp[key] = min(dp.get(key, 11), val)
    return min(dp[(2**n-1, i)] for i in range(n))


def main():
    opt = brute_force_optima()
    maxima_by_cardinality = {}
    extrema = []
    global_ratio = Fraction(0)
    # Independent Bellman check of every optimum, not needed for completeness.
    for mask in range(1,256):
        subset = tuple(w for i,w in enumerate(WORDS) if mask & (1 << i))
        assert opt[mask] == optimal_overlap_dp(subset), (mask, opt[mask])
        got = worst_greedy(subset)
        ratio = Fraction(got,opt[mask])
        n = len(subset)
        maxima_by_cardinality[n] = max(maxima_by_cardinality.get(n, Fraction(0)), ratio)
        if ratio > global_ratio:
            global_ratio = ratio
            extrema = [(mask,subset,got,opt[mask])]
        elif ratio == global_ratio:
            extrema.append((mask,subset,got,opt[mask]))
    expected = (
        ('000','001','010','011','100'),
        ('000','001','010','100','110'),
        ('001','011','101','110','111'),
        ('011','100','101','110','111'),
    )
    assert global_ratio == Fraction(10,7),global_ratio
    assert tuple(e[1] for e in extrema) == expected,extrema
    assert set(maxima_by_cardinality) == set(range(1,9))
    assert all(got==10 and op==7 for _,_,got,op in extrema)
    # Reversal and bit complement map the first extremal set onto all four.
    transformations = [lambda w: w,
                       lambda w: w[::-1],
                       lambda w: w.translate(str.maketrans('01','10')),
                       lambda w: w[::-1].translate(str.maketrans('01','10'))]
    orbit = {tuple(sorted(f(w) for w in expected[0])) for f in transformations}
    assert orbit == set(expected), orbit
    # Concrete optimal superstring (7 symbols) and greedy (10 symbols).
    witness = expected[0]
    optword='0100011'
    greedyword='0001001011'
    assert all(w in optword for w in witness) and len(optword)==7
    assert all(w in greedyword for w in witness) and len(greedyword)==10
    print('input_sets=255')
    print('possible_input_words=8')
    print('max_ratio=%s'%global_ratio)
    print('extremal_sets=%d'%len(extrema))
    for mask,subset,got,op in extrema:
        print('extremal_mask=%d input=%s greedy=%d optimal=%d'%(mask,','.join(subset),got,op))
    print('max_by_size='+','.join('%d:%s'%(k,maxima_by_cardinality[k]) for k in range(1,9)))
    print('distinct_greedy_states=%d'%worst_greedy.cache_info().currsize)
    print('optimal_witness='+optword)
    print('greedy_witness='+greedyword)
    print('verification=PASS')

if __name__ == '__main__':
    main()
