#!/usr/bin/env python3
"""Reproducibility checks for the exact two-marker restricted-overlap capacity.
Only Python standard library is required. Checks are finite supporting tests;
the all-length upper/lower proofs are provided separately in RESULT.md.
"""
from itertools import combinations


def upper(n):
    assert n >= 4
    return ((n - 1) // 2) * (n // 3) + (n // 6 if n % 2 == 0 else 0)


def construct(n):
    words = []
    for d in range(1, n // 2 + 1):
        period = n // 2 if 2 * d == n else n
        for r in range(0, 3 * (period // 3), 3):
            x = ['0'] * n
            x[r] = '1'
            x[(r + d) % n] = '1'
            words.append(''.join(x))
    assert len(set(words)) == len(words)
    return words


def forbidden(x,y):
    n = len(x)
    return any(x[:t] == y[-t:] for t in (n - 2, n - 1))


def independent_with_self(code):
    return all(not forbidden(x,y) for x in code for y in code)


def independent_neighbor_check(n,code):
    codes = set(code)
    for word in code:
        for k in (1,2):
            cut = word[:k]
            retained = word[k:]
            for j in range(1 << k):
                suffix = ''.join(str((j >> t) & 1) for t in range(k))
                if suffix.count('1') == cut.count('1'):
                    assert retained + suffix not in codes, (n,word,k,suffix)


def exact_independence(n):
    # Exponential exact solver, used only for n<=8. All possible codewords
    # including self-overlapping ones are handled by direct prefix-suffix tests.
    V = [''.join('1' if k in pair else '0' for k in range(n))
         for pair in combinations(range(n),2)]
    V = [x for x in V if not forbidden(x,x)]
    N = len(V)
    adj = [0] * N
    for i in range(N):
        for j in range(i):
            if forbidden(V[i],V[j]) or forbidden(V[j],V[i]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    # Exact maximum clique on complement, bitset branch-and-bound.
    # Greedy graph coloring provides an upper bound at each node.
    best=0
    def extend(cands,depth):
        nonlocal best
        if not cands:
            best=max(best,depth);return
        order=[];bounds=[];uncolored=cands;col=0
        while uncolored:
            col+=1;can=uncolored
            while can:
                v=(can&-can).bit_length()-1
                bit=1<<v;can^=bit;uncolored^=bit
                order.append(v);bounds.append(col)
                can &= adj[v]
        for v,bound in reversed(list(zip(order,bounds))):
            if depth+bound<=best:return
            bit=1<<v
            extend(cands & ~adj[v] & ~bit,depth+1)
            cands ^= bit
    extend((1 << N)-1,0)
    return best


def main():
    exact=[]
    for n in range(4,21):
        code=construct(n)
        assert len(code)==upper(n),(n,len(code),upper(n))
        assert independent_with_self(code),('direct',n)
        independent_neighbor_check(n,code)
    for n in range(21,121):
        code=construct(n)
        assert len(code)==upper(n)
        independent_neighbor_check(n,code)
    for n in range(4,9):
        opt=exact_independence(n)
        assert opt==upper(n),(n,opt,upper(n))
        exact.append((n,opt))
    print('EXACT_OPTIMA',exact)
    print('DIRECT_FACTOR_CHECKS_4_TO_20_OK')
    print('NEIGHBOR_CHECKS_4_TO_120_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
