"""Independent exhaustive finite checks for the local-period law of Cantor blocks.
Run: python3 checker.py. Uses Python's standard library only.
"""
from collections import Counter


def cantor_by_ternary(rank):
    n = 3 ** rank
    def is_one(i):
        while i:
            i, d = divmod(i, 3)
            if d == 1:
                return False
        return True
    return ''.join('1' if is_one(i) else '0' for i in range(n))


def cantor_by_substitution(rank):
    word = '1'
    for _ in range(rank):
        word = ''.join('101' if x == '1' else '000' for x in word)
    return word


def shortest_border_or_whole(word):
    n = len(word)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j and word[i] != word[j]:
            j = pi[j-1]
        if word[i] == word[j]:
            j += 1
        pi[i] = j
    j = pi[-1]
    if not j:
        return n
    while pi[j-1]:
        j = pi[j-1]
    return j


def triadic_valuation(i):
    v = 0
    while i % 3 == 0:
        v += 1
        i //= 3
    return v


def expected_local_period(word, i):
    m = len(word)
    if i == 0 or i == m:
        return 2*m
    if i > m or word[i-1] == word[i]:
        return 1
    return 2 * (3 ** triadic_valuation(i))


def check_rank(r):
    p = cantor_by_ternary(r)
    assert p == cantor_by_substitution(r)
    m = len(p)
    v = p + '0'*m
    actual = []
    for i in range(2*m):
        rotated = v[i:] + v[:i]
        found = shortest_border_or_whole(rotated)
        predicted = expected_local_period(p, i)
        assert found == predicted, (r, i, found, predicted)
        actual.append(found)
    freq = Counter(actual)
    assert freq[2*m] == 2
    assert freq[1] == 2*m - 2 ** (r+1)
    for j in range(r):
        assert freq[2*3**j] == 2**(r-j)
    assert set(freq) == {2*m, 1} | {2*3**j for j in range(r)} if r >= 1 else set(freq) == {2*m}
    # Independently verify that every factor of C_{r+1} longer than 2m is bordered.
    w = cantor_by_substitution(r+1)
    assert w == p + '0'*m + p
    for length in range(2*m+1,3*m+1):
        for start in range(3*m-length+1):
            f = w[start:start+length]
            border = length - 2*m
            assert f[:border] == f[-border:]
    return r,2*m,len(freq),dict(sorted(freq.items()))


def main():
    for r in range(7):
        result = check_rank(r)
        print('CHECKED rank={} size={} distinct_local_periods={} histogram={}'.format(*result))
    print('VERIFY_OK all rotation borders and maximal-length bound at ranks 0..6')

if __name__ == '__main__':
    main()
