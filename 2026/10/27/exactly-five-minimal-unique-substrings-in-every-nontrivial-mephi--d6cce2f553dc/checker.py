"""Reproduce the finite tests for the Mephisto-Waltz MUS classification.
Python 3 standard library only. Zero-based substring positions throughout.
"""
from collections import Counter

IMAGES = {'0': '001', '1': '110'}

def iterate(m):
    word = '0'
    for _ in range(m):
        word = ''.join(IMAGES[c] for c in word)
    return word

def suffix_array(s):
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    step = 1
    while step < n:
        sa.sort(key=lambda i: (rank[i], rank[i + step] if i + step < n else -1))
        nxt = [0] * n
        for t in range(1, n):
            x, y = sa[t - 1], sa[t]
            nxt[y] = nxt[x] + int((rank[y], rank[y + step] if y + step < n else -1) !=
                                  (rank[x], rank[x + step] if x + step < n else -1))
        rank = nxt
        if rank[sa[-1]] == n - 1:
            break
        step *= 2
    return sa

def mus_suffix(s):
    n = len(s)
    sa = suffix_array(s)
    inverse = [0] * n
    for t, i in enumerate(sa):
        inverse[i] = t
    lcp = [0] * n
    h = 0
    for i in range(n):
        at = inverse[i]
        if at == 0:
            h = 0
            continue
        j = sa[at - 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[at] = h
        h = max(0, h - 1)
    min_unique = [0] * n
    for i in range(n):
        at = inverse[i]
        length = 1 + max(lcp[at], lcp[at+1] if at+1 < n else 0)
        min_unique[i] = length if i + length <= n else n + 1
    # Every MUS must be a shortest unique substring at its start.
    return [(i, min_unique[i]) for i in range(n)
            if min_unique[i] <= n-i
            and (i == n-1 or min_unique[i] <= min_unique[i+1])]

def mus_bruteforce(s):
    n = len(s)
    counter = Counter(s[i:j] for i in range(n) for j in range(i+1, n+1))
    return [(i, j-i) for i in range(n) for j in range(i+1, n+1)
            if counter[s[i:j]] == 1
            and (j == i+1 or
                 (counter[s[i+1:j]] > 1 and counter[s[i:j-1]] > 1))]

def expected(m):
    r = 3 ** (m-2)
    return [(a*r-1, r+2) for a in (2,3,5,6,7)]

def main():
    for x in '01':
        for y in '01':
            s = IMAGES[x] + IMAGES[y]
            for phase in (1,2):
                assert s[phase:phase+3] not in ('001','110')
    print('All eight nonaligned three-symbol windows exclude image blocks: PASS')
    assert iterate(2) == '001001110'
    assert Counter(iterate(2)[i:i+2] for i in range(8)) == Counter({'00':2,'01':2,'10':2,'11':2})
    for m in range(2,10):
        s = iterate(m)
        a = mus_suffix(s)
        e = expected(m)
        assert a == e, (m,a,e)
        if m <= 5:
            b = mus_bruteforce(s)
            assert b == e, (m,b,e)
        print('m=%d length=%d MUS_length=%d starts=%s%s' %
              (m,len(s),e[0][1],[i for i,L in a],
               ' exhaustive-factor-check=PASS' if m <= 5 else ''))
    print('Independent suffix-array and full-factor checks: PASS')

if __name__ == '__main__':
    main()
