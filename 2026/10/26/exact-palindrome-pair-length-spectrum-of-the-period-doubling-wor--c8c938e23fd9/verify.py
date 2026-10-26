"""Finite checks supporting a characterization of palindrome-pair lengths
in the binary period-doubling word. All unrestricted claims require the
symbolic proof and the published exact palindromic-periodicity count.
"""
from itertools import product


def morphism(w):
    return ''.join('01' if a == '0' else '00' for a in w)


def direct_symbol(i):
    j = i + 1
    count = 0
    while j % 2 == 0:
        j //= 2
        count += 1
    return str(count % 2)


def morphism_prefix(length):
    w = '0'
    while len(w) < length:
        w = morphism(w)
    return w[:length]


def is_pp_by_cuts(w):
    return any(w[:j] == w[:j][::-1] and w[j:] == w[j:][::-1]
               for j in range(len(w) + 1))


def is_pp_by_reflection(w):
    return w[::-1] in (w + w)[:-1] if w else True


def factor_count_known(n):
    if n == 1:
        return 2
    k = n.bit_length() - 1
    r = n - 2**k
    if r <= 2**(k-1):
        return 3 * 2**(k-1) + 2*r
    return 2**(k+1) + r


def periodicity_count_known(n):
    # Fici-Shallit-Simpson, CPM 2025, Theorem 13, for n >= 4.
    assert n >= 4
    k = n.bit_length() - 1
    r = n - (1 << k)
    if r < (1 << (k-2)):
        return 3 * (1 << (k-1))
    if r < (1 << (k-1)):
        return 1 << (k+1)
    if r < 3 * (1 << (k-2)):
        return 6 * (1 << (k-1)) - r
    return 7 * (1 << (k-1)) - r


def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n


def main():
    bound = 160
    data = morphism_prefix(32768)
    assert data == ''.join(direct_symbol(j) for j in range(len(data)))
    for n in range(1, 13):
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            assert is_pp_by_cuts(w) == is_pp_by_reflection(w)
            assert is_pp_by_reflection(w) == is_pp_by_reflection(morphism(w))
    good = []
    for n in range(1, bound+1):
        seen = {data[j:j+n] for j in range(0, 8192)}
        assert len(seen) == factor_count_known(n), (n, len(seen), factor_count_known(n))
        for w in seen:
            assert is_pp_by_cuts(w) == is_pp_by_reflection(w), (n,w)
        all_ok = all(is_pp_by_reflection(w) for w in seen)
        assert all_ok == (odd_part(n) in (1,3,5)), n
        if all_ok:
            good.append(n)
    assert {w for w in (data[i:i+7] for i in range(8192)) if not is_pp_by_reflection(w)} == {'1000101','1010001'}
    for k in range(0,12):
        w = '1000101'
        for _ in range(k):
            w = morphism(w)
        assert not is_pp_by_reflection(w)
        assert w in data if len(w) <= 32768 else True
    for n in range(8, 32769):
        eq = periodicity_count_known(n) == factor_count_known(n)
        assert periodicity_count_known(n) <= factor_count_known(n)
        assert eq == (odd_part(n) in (1,3,5,7)), n
    print('VERIFY_OK symbolic_count_comparison=8..32768 exact equality families=1,3,5,7')
    print('VERIFY_OK two_word_generators=32768; complete_factor_sets=1..160')
    print('VERIFY_OK palindrome_pair_tests=cuts_and_cyclic_reflection; morphism_reflection=all_binary_words_to_length_12')
    print('VERIFY_OK length_spectrum=1..160; length_7_non_pairs=1000101,1010001')
    print('VERIFY_OK counterexample_desubstitution_levels=0..11')
    print('VERIFY_OK sample_good_lengths=' + ','.join(map(str,good)))

if __name__ == '__main__':
    main()
