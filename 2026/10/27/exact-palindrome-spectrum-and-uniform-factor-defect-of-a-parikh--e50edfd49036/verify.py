"""Exact finite certificates for palindromes of a specified morphic word.

Run with Python 3 standard library. All assertions are exact.
"""

F = {'0': '010011', '1': '1001'}
G = {
    '0': '01023', '1': '14501', '2': '10102',
    '3': '31450', '4': '45010', '5': '10231',
}
TAU = {'0': '0', '1': '1', '2': '0', '3': '1', '4': '1', '5': '0'}
PAIR_SET = {'01', '02', '10', '14', '23', '31', '45', '50'}
COUNTS = (2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 3,
          0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0)
LONGEST = {'01100101001110010100110', '10100111001010011100101'}


def apply_morphism(word, morphism, repetitions):
    for _ in range(repetitions):
        word = ''.join(morphism[letter] for letter in word)
    return word


def project(word):
    return ''.join(TAU[x] for x in word)


def factor_set(word, n):
    return {word[i:i+n] for i in range(len(word)-n+1)}


def positional_lift():
    """Derive the six-state 5-uniform representation from the binary morphism."""
    states = [(a, i) for a in '01' for i in range(len(F[a]))]
    merger = {
        ('0', 0): '0', ('0', 1): '1', ('0', 2): '0',
        ('0', 3): '2', ('0', 4): '3', ('0', 5): '1',
        ('1', 0): '4', ('1', 1): '5', ('1', 2): '0', ('1', 3): '1',
    }
    for a in '01':
        lifted = [(b, j) for b in F[a] for j in range(len(F[b]))]
        assert len(lifted) == 5 * len(F[a])
        for i in range(len(F[a])):
            s = (a, i)
            theta = lifted[5*i:5*(i+1)]
            assert len(theta) == 5
            assert ''.join(merger[t] for t in theta) == G[merger[s]]
            assert TAU[merger[s]] == F[a][i]
    assert len(states) == 10


def get_pair_set():
    w = G['0']
    pairs = factor_set(w, 2)
    assert pairs == {'01', '10', '02', '23'}
    w = apply_morphism('0', G, 2)
    assert factor_set(w, 2) == PAIR_SET
    # All pairs in the image of any legal pair remain legal.
    for xy in PAIR_SET:
        assert factor_set(G[xy[0]] + G[xy[1]], 2) <= PAIR_SET
    return factor_set(w, 2)


def main():
    positional_lift()
    pairs = get_pair_set()
    # A length <=25 window in a 25-uniform block partition
    # lies within two consecutive blocks. Every legal pair is present.
    projected_pair_blocks = [project(apply_morphism(xy, G, 2))
                             for xy in sorted(pairs)]
    assert all(len(block) == 50 for block in projected_pair_blocks)
    factors = {
        n: set().union(*(factor_set(block, n)
                          for block in projected_pair_blocks))
        for n in range(1, 26)
    }
    palindromes = {n: {word for word in factors[n] if word == word[::-1]}
                   for n in range(1, 26)}
    assert len(factors[24]) == 78 and len(factors[25]) == 81
    assert palindromes[23] == LONGEST
    assert not palindromes[24] and not palindromes[25]
    all_palindromes = set().union(*(palindromes[n] for n in range(1, 26)))
    assert len(all_palindromes) == 37

    # Each second iterate contains every possible adjacent state pair.
    for a in sorted(G):
        assert pairs <= factor_set(apply_morphism(a, G, 2), 2)
        # Applying the second iterate again embeds every pair block.
        full_block = project(apply_morphism(a, G, 4))
        assert len(full_block) == 625
        assert all(p in full_block for p in all_palindromes)

    # Independent direct comparison of the two presentations on prefixes.
    from_f = apply_morphism('0', F, 6)
    from_g = project(apply_morphism('0', G, 6))
    L = min(len(from_f), len(from_g))
    assert L >= 10000 and from_f[:L] == from_g[:L]
    for n in range(1, 26):
        # This check is independent of the pair-block factor enumeration.
        assert factor_set(from_f, n) == factors[n]

    # Witnesses for the longest palindromes (pair, index inside pair-block).
    witness = {'01100101001110010100110': ('02', 24),
               '10100111001010011100101': ('10', 14)}
    for word, (pair, i) in witness.items():
        block = project(apply_morphism(pair, G, 2))
        assert block[i:i+23] == word

    print('PARIKH_PALINDROME_SPECTRUM_PASS',
          'pairs=8', 'factors25=81', 'palindromes=37',
          'longest=23', 'block=625', 'universal_factor_length=1249',
          'prefix_comparison='+str(L))


if __name__ == '__main__':
    main()
