"""Independent finite corroboration for exact net occurrences of period-doubling words."""
from collections import defaultdict


def morph(word):
    return ''.join('01' if c == '0' else '00' for c in word)


def repeated_prefix_profile(word):
    n = len(word)
    ranks = [int(c) for c in word]
    sa = list(range(n))
    jump = 1
    while True:
        sa.sort(key=lambda p: (ranks[p], ranks[p + jump] if p + jump < n else -1))
        nxt = [0] * n
        for j in range(1, n):
            x, y = sa[j - 1], sa[j]
            nxt[y] = nxt[x] + ((ranks[x], ranks[x + jump] if x + jump < n else -1) != (ranks[y], ranks[y + jump] if y + jump < n else -1))
        ranks = nxt
        if ranks[sa[-1]] == n - 1:
            break
        jump *= 2
    lcp = [0] * n
    inv = [0] * n
    for order, pos in enumerate(sa):
        inv[pos] = order
    match = 0
    for i in range(n):
        order = inv[i]
        if order == 0:
            match = 0
            continue
        j = sa[order - 1]
        while i + match < n and j + match < n and word[i + match] == word[j + match]:
            match += 1
        lcp[order] = match
        match = max(match - 1, 0)
    ans = [0] * n
    for j, p in enumerate(sa):
        ans[p] = max(lcp[j], lcp[j + 1] if j + 1 < n else 0)
    return ans


def claimed_profile(n):
    h = 2 ** (n - 3)
    return ([4*h - 1 - i for i in range(2*h)]
            + [5*h - 1 - i for i in range(2*h, 3*h)]
            + [6*h - 1 - i for i in range(3*h, 4*h)]
            + [8*h - 1 - i for i in range(4*h, 6*h)]
            + [8*h - i for i in range(6*h, 8*h)])


def naive_profile(word):
    n = len(word)
    out = [0] * n
    for i in range(n):
        best = 0
        for j in range(n):
            if i == j:
                continue
            t = 0
            while i + t < n and j + t < n and word[i + t] == word[j + t]:
                t += 1
            best = max(best, t)
        out[i] = best
    return out


def naive_net_occurrences(word):
    groups = defaultdict(list)
    n = len(word)
    for i in range(n):
        for length in range(1, n - i + 1):
            groups[word[i:i + length]].append(i)
    found = set()
    for substring, starts in groups.items():
        if len(starts) <= 1:
            continue
        for i in starts:
            k = len(substring)
            if i + k < n and len(groups[word[i:i+k+1]]) > 1:
                continue
            if i > 0 and len(groups[word[i-1:i+k]]) > 1:
                continue
            found.add((i, k))
    return found


def check():
    w = '0'
    for n in range(1, 15):
        w = morph(w)
        if n < 3:
            continue
        h = 2 ** (n - 3)
        profile = repeated_prefix_profile(w)
        assert profile == claimed_profile(n), (n, 'prefix profile')
        net = {(i, k) for i, k in enumerate(profile) if k > 0 and (i == 0 or k >= profile[i - 1])}
        expected = {(0, 4*h-1), (2*h, 3*h-1), (3*h, 3*h-1), (4*h, 4*h-1), (6*h, 2*h)}
        assert net == expected, (n, 'net list')
        if n <= 7:
            assert naive_profile(w) == profile, (n, 'naive pairwise')
            assert naive_net_occurrences(w) == expected, (n, 'naive net definition')
        print(f'n={n:2d} length={len(w):5d} net=5 exact_profile=PASS' + (' naive=PASS' if n<=7 else ''))
    print('ALL CHECKS PASSED: finite independent corroboration n=3..14')

if __name__ == '__main__':
    check()
