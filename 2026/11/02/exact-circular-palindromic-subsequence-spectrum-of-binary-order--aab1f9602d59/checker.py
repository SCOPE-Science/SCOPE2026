#!/usr/bin/env python3
"""Exhaustive order-five de Bruijn palindrome-deletion statistics.

Python 3 standard library only. Enumerators are mathematically different:
(1) complementary feedback permutations on five-bit states;
(2) Euler tours on the binary order-four de Bruijn graph.
Two dynamic programs independently compute each rooted LPS value.
"""
from collections import Counter
from hashlib import sha256

N = 32


def least_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def feedback_cycles():
    """Only complementary feedback tables yield bijective state evolution."""
    for table in range(1 << 16):
        s = 0
        out = []
        visited = 0
        for _ in range(N):
            if visited & (1 << s):
                break
            visited |= 1 << s
            out.append(str(s >> 4))
            fb = (s >> 4) ^ ((table >> (s & 15)) & 1)
            s = ((s << 1) & 31) | fb
        if s == 0 and len(out) == N:
            yield least_rotation(''.join(out))


def euler_cycles():
    """List every Euler tour, rooted at the unique edge 00000."""
    path = ['0']
    def dfs(vertex, used, count):
        if count == N:
            if vertex == 0:
                yield least_rotation(''.join(path))
            return
        for bit in (0, 1):
            edge = 2 * vertex + bit
            if used & (1 << edge):
                continue
            path.append(str(vertex >> 3))
            yield from dfs(edge & 15, used | (1 << edge), count + 1)
            path.pop()
    yield from dfs(0, 1, 1)


def lps_interval(s):
    """LPS via uncrossed matching on intervals."""
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for span in range(2, n+1):
        for i in range(n-span+1):
            j = i+span-1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i+1][j-1] if span > 2 else 0)
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][-1]


def lps_as_lcs_reversal(s):
    """Second implementation: LCS with the reverse word."""
    reverse = s[::-1]
    old = [0] * (len(s)+1)
    for x in s:
        new = [0] * (len(s)+1)
        for j, y in enumerate(reverse, 1):
            new[j] = old[j-1] + 1 if x == y else max(old[j], new[j-1])
        old = new
    return old[-1]


def elementary_small_word_controls():
    # A third, definition-level oracle confirms both dynamic programs on all
    # binary words through length nine.  It explicitly lists subsequences.
    for n in range(1, 10):
        for value in range(1 << n):
            word = format(value, f'0{n}b')
            brute = 0
            for mask in range(1 << n):
                subseq = ''.join(word[i] for i in range(n) if mask & (1 << i))
                if len(subseq) > brute and subseq == subseq[::-1]:
                    brute = len(subseq)
            assert brute == lps_interval(word) == lps_as_lcs_reversal(word)


def check():
    from time import monotonic
    start = monotonic()
    elementary_small_word_controls()
    a = list(feedback_cycles())
    assert len(a) == 2048, len(a)
    assert len(set(a)) == len(a)
    for w in a:
        assert len({(w+w)[i:i+5] for i in range(32)}) == 32
    b = list(euler_cycles())
    assert len(b) == 2048, len(b)
    assert set(a) == set(b)
    rooted = Counter()
    cycle_range = Counter()
    root_best = Counter()
    root_worst = Counter()
    opt_roots = Counter()
    examples = {}
    for w in a:
        values = []
        for i in range(32):
            r = w[i:]+w[:i]
            u = lps_interval(r)
            v = lps_as_lcs_reversal(r)
            assert u == v, (w, i, u, v)
            values.append(u)
            rooted[u] += 1
        lo, hi = min(values), max(values)
        cycle_range[lo, hi] += 1
        root_best[hi] += 1
        root_worst[lo] += 1
        opt_roots[values.count(hi)] += 1
        for tag, key in [('best',hi),('worst',lo)]:
            examples.setdefault((tag,key), w)
    assert sum(rooted.values()) == 65536
    assert sum(cycle_range.values()) == 2048
    assert rooted == Counter({19:40,20:224,21:2662,22:3656,23:16140,24:9804,25:18934,26:6808,27:6060,28:1008,29:200})
    assert root_best == Counter({25:76,26:114,27:1380,28:286,29:192})
    assert root_worst == Counter({19:40,20:212,21:1080,22:456,23:260})
    assert min(root_best) == 25 and max(root_best) == 29
    assert min(rooted) == 19 and max(rooted) == 29
    import json
    summary = {
        'n_cycles':len(a),'n_rooted':sum(rooted.values()),
        'rooted_lps':dict(sorted(rooted.items())),
        'cycle_minmax':{f'{lo},{hi}':cnt for (lo,hi),cnt in sorted(cycle_range.items())},
        'cycle_best_lps':dict(sorted(root_best.items())),
        'cycle_worst_lps':dict(sorted(root_worst.items())),
        'optimal_root_counts':dict(sorted(opt_roots.items())),
        'canonical_cycle_list_sha256':sha256(('\n'.join(sorted(a))+'\n').encode()).hexdigest(),
        'examples':{f'{k[0]}_{k[1]}':v for k,v in sorted(examples.items())},
    }
    with open('summary.json','w',encoding='utf-8') as f:
        json.dump(summary,f,sort_keys=True,indent=2);f.write('\n')
    print('VERIFY_OK',len(a),sum(rooted.values()),round(monotonic()-start,2),'s')
    print('ROOTED_LPS',sorted(rooted.items()))
    print('CYCLE_BEST',sorted(root_best.items()))
    print('CYCLE_WORST',sorted(root_worst.items()))
    print('CYCLE_MINMAX', sorted(cycle_range.items()))
    print('ROOT_OPT_COUNT', sorted(opt_roots.items()))
    print('CYCLES_SHA256',summary['canonical_cycle_list_sha256'])

if __name__ == '__main__':
    check()
