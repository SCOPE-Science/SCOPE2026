"""Finite reproducibility checks for the Brik-word subsequence entropy bound.
No finite check is used as proof of its asymptotic statement.
"""
from collections import Counter
from math import log2, ceil


def stage_words(max_stage):
    w = '101'
    out = {1: w}
    for j in range(1, max_stage):
        w = w + w[j:]
        out[j + 1] = w
    return out


def embedding(words, k, n):
    if n < k:
        raise ValueError('n must be at least k')
    positions = list(range(len(words[k])))
    for j in range(k, n):
        block_len = (1 << (j-k)) * len(words[k])
        positions = positions + [block_len + p for p in positions[j:]]
        assert len(positions) == len(words[j+1])
    return positions


def entropy(blocks):
    cnt = Counter(blocks)
    total = sum(cnt.values())
    return -sum((v/total)*log2(v/total) for v in cnt.values())


def run():
    words = stage_words(15)
    checks = 0
    for k in range(2,9):
        for n in range(k+1, 15):
            w = words[n]
            src = words[k] * (1 << (n-k))
            e = embedding(words, k, n)
            assert ''.join(src[p] for p in e) == w
            assert len(src)-len(w) == (1 << (n-k))*len(words[k])-len(w)
            checks += 1
            gap = [e[i+1]-e[i]-1 for i in range(len(e)-1)]
            for t in (2, 3, 7, 13, 31, 64):
                if t>len(w):
                    continue
                acc = sum(gap[:t-1])
                total = 0
                for s in range(len(w)-t+1):
                    total += acc
                    if s + t < len(w):
                        acc += gap[s+t-1]-gap[s]
                deleted = len(src)-len(w)
                assert total <= (t-1)*deleted, (k,n,t,total,deleted)
                checks += 1
    for t in list(range(2, 1001)) + [10**4, 10**6, 10**9]:
        L = log2(t+2)
        k = ceil(L + 2*log2(L+2) + 3)
        period_length = 2**(k-1) + k+1
        m = (t-1)*(k+1)/2**(k-1)
        assert k+1 <= 4*(L+2)
        assert m <= 1/(L+2)
        assert period_length <= 9*(t+2)*(L+2)**2
        checks += 3
    # Numerical entropy for feasible finite stages (not the infinite measure).
    n=15
    samples=[]
    for t in (2,3,5,8,13,21,34,55,89,144):
        w = words[n]
        h = entropy(w[i:i+t] for i in range(len(w)-t+1))
        samples.append((t,round(h,6)))
    print('PASS exact recursion, periodic-source embeddings, and window-gap inequality:', checks,'checks')
    print('Finite-stage block Shannon entropies (stage 15, not infinite-limit entropies):')
    for t,h in samples:
        print(t,h)

if __name__=='__main__':
    run()
