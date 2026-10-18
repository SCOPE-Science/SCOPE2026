"""Exhaustive small-parameter checks for rich double-occurrence words.

Uses two separate classifications: direct distinct-palindrome enumeration and
recursive block parsing. Run with Python 3 standard library.
"""
from collections import Counter
from math import factorial


def normalized_double_words(q):
    counts = [0]*q
    word = []
    def rec(next_letter):
        if len(word) == 2*q:
            yield tuple(word)
            return
        for a in range(next_letter):
            if counts[a] != 2:
                counts[a] += 1
                word.append(a)
                yield from rec(next_letter)
                word.pop()
                counts[a] -= 1
        if next_letter < q:
            a = next_letter
            counts[a] = 1
            word.append(a)
            yield from rec(next_letter + 1)
            word.pop()
            counts[a] = 0
    yield from rec(0)


def is_rich_by_palindromes(w):
    pals = {()}
    for center in range(len(w)):
        for left, right in ((center, center),(center,center+1)):
            while left >= 0 and right < len(w) and w[left] == w[right]:
                pals.add(w[left:right+1])
                left -= 1
                right += 1
    return len(pals) == len(w) + 1


def every_letter_return_is_palindrome(w):
    for x in set(w):
        left = w.index(x)
        right = len(w) - 1 - w[::-1].index(x)
        span = w[left:right+1]
        if span != span[::-1]:
            return False
    return True


def decomposes_into_blocks(w):
    p = 0
    while p < len(w):
        a = w[p]
        j = w.index(a, p+1)
        block = w[p:j+1]
        # A rainbow has a distinct-letter first half, mirrored in its second half.
        if len(block) % 2 == 0 and block == block[::-1] and len(set(block)) == len(block)//2:
            p = j+1
        elif p+3 < len(w) and w[p] == w[p+2] and w[p+1] == w[p+3] and w[p] != w[p+1]:
            p += 4
        else:
            return False
        if set(w[:p]).intersection(w[p:]):
            return False
    return True


def counts_from_compositions(q):
    c = [1]
    for k in range(1,q+1):
        c.append(sum((2 if j == 2 else 1)*c[k-j] for j in range(1,k+1)))
    return c


def crossing_pairs(w):
    endpoints = {a:(w.index(a), len(w)-1-w[::-1].index(a)) for a in set(w)}
    symbols = sorted(endpoints)
    total = 0
    for i,a in enumerate(symbols):
        x,y = endpoints[a]
        for b in symbols[i+1:]:
            u,v = endpoints[b]
            if (x < u < y < v) or (u < x < v < y):
                total += 1
    return total


def predicted_crossings(q):
    dp = [Counter({0:1})]
    for n in range(1,q+1):
        row=Counter()
        for length in range(1,n+1):
            for crossings,count in dp[n-length].items():
                row[crossings]+=count
                if length==2:
                    row[crossings+1]+=count
        dp.append(row)
    return dp[q]


def main():
    counts = counts_from_compositions(8)
    assert counts == [1,1,3,6,14,31,70,157,353]
    total = 0
    for q in range(1,8):
        actual = Counter()
        crossings = Counter()
        for w in normalized_double_words(q):
            a = is_rich_by_palindromes(w)
            b = every_letter_return_is_palindrome(w)
            c = decomposes_into_blocks(w)
            assert a == b == c, (q,w,a,b,c)
            actual[a] += 1
            if a:
                crossings[crossing_pairs(w)] += 1
        assert actual[True] == counts[q], (q,actual,counts[q])
        assert crossings == predicted_crossings(q), (q,crossings,predicted_crossings(q))
        assert sum(actual.values()) == factorial(2*q) // (2**q*factorial(q))
        print('q=',q,'total=',sum(actual.values()),'rich=',actual[True],'by_crossings=',sorted(crossings.items()), flush=True)
        total += sum(actual.values())
    print('RICH_DOUBLE_OCCURRENCE_PASS total_normalized_words=',total)


if __name__ == '__main__':
    main()
