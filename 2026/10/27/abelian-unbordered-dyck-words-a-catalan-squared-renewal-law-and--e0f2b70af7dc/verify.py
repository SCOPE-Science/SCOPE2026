#!/usr/bin/env python3
"""Independent finite checks for abelian borders of Dyck words.

Uses literal Parikh vectors and height-return sets, then tests the
Catalan-squared renewal identities. Standard-library only.
"""
from functools import lru_cache
from math import comb

@lru_cache(None)
def dyck(n):
    if n == 0:
        return ('',)
    return tuple('0' + a + '1' + b
                 for j in range(n) for a in dyck(j) for b in dyck(n - 1 - j))

def direct_shortest(w):
    length = len(w)
    for k in range(1, length // 2 + 1):
        if w[:k].count('0') == w[length-k:].count('0'):
            return k
    return None

def paired_return_shortest(w):
    height = 0
    returns = {0}
    for j, c in enumerate(w, 1):
        height += 1 if c == '0' else -1
        assert height >= 0
        if height == 0:
            returns.add(j)
    assert height == 0
    return next((k for k in range(1, len(w)//2 + 1)
                 if k in returns and len(w)-k in returns), None)

def catalan(n):
    return comb(2*n, n)//(n+1)

def main():
    N = 30
    C = [catalan(i) for i in range(N+1)]
    S = [v*v for v in C]
    E = [0]*(N+1)
    for n in range(1, N+1):
        E[n] = S[n] - sum(E[j]*S[n-j] for j in range(1,n))
    U = [0]*(N+1)
    for n in range(N+1):
        U[n] = C[n] - sum(S[k]*U[n-2*k] for k in range(1,n//2+1))
        assert U[n] >= 0
        assert C[n] == U[n]+sum(E[k]*C[n-2*k]
                                  for k in range(1,n//2+1))
    verified = 0
    for n in range(1,13):
        obs = {}
        for w in dyck(n):
            a = direct_shortest(w)
            b = paired_return_shortest(w)
            assert a == b, (n,w,a,b)
            obs[a] = obs.get(a, 0) + 1
            verified += 1
        assert sum(obs.values()) == C[n]
        assert obs.get(None,0) == U[n],(n,obs.get(None,0),U[n])
        for k in range(1,n//2+1):
            assert obs.get(2*k,0)==E[k]*C[n-2*k]
        assert not any(isinstance(x,int) and x%2 for x in obs)
    paircases=0
    for k in range(1,7):
        count=0
        for a in dyck(k):
            prefix_zero_returns = {i//2 for i in range(2,2*k,2)
                                   if a[:i].count('0') == i//2}
            for b in dyck(k):
                suffix_zero_returns = {i//2 for i in range(2,2*k,2)
                                       if b[-i:].count('0') == i//2}
                count += not (prefix_zero_returns & suffix_zero_returns)
                paircases+=1
        assert count==E[k],(k,count,E[k])
    print('DYCK_ABELIAN_BORDERS_PASS',
          'dyck_words=',verified,
          'independent_pairs=',paircases,
          'recurrence_through=',N,
          'first_unbordered=',U[:13],
          'first_pair_counts=',E[:8])

if __name__=='__main__':main()
