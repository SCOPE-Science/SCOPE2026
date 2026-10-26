#!/usr/bin/env python3
"""Independent exhaustive adjacency-based verification of dissociation claims for full subdivisions of complete graphs."""
from collections import Counter
from math import comb


def polynomial(n):
    out=Counter()
    for a in range(n+1):
        b=n-a
        for h in range(b*(b-1)//2+1):
            for k in range(a+1):
                out[a+h+k]+=comb(n,a)*comb(b*(b-1)//2,h)*comb(a,k)*b**k
    return out


def maximal_polynomial(n):
    out=Counter({n:1,2*n-2:n})
    out[2*n-3]+=comb(n,2)*(2**(n-2)-2)
    for b in range(3,n+1):
        out[2*(n-b)+comb(b,2)]+=comb(n,b)*b**(n-b)
    return +out


def independent_bruteforce(n):
    edges=[(u,v) for u in range(n) for v in range(u+1,n)]
    N=n+len(edges)
    adj=[0]*N
    for e,(u,v) in enumerate(edges):
        j=n+e
        adj[u]|=1<<j
        adj[v]|=1<<j
        adj[j]|=(1<<u)|(1<<v)
    allmask=(1<<N)-1
    allsets,maxsets=Counter(),Counter()
    patterns=Counter()
    for mask in range(1<<N):
        cur=mask
        valid=True
        while cur:
            bit=cur&-cur
            u=bit.bit_length()-1
            if (mask&adj[u]).bit_count()>1:
                valid=False
                break
            cur-=bit
        if not valid:continue
        allsets[mask.bit_count()]+=1
        cur=allmask^mask
        maximal=True
        while cur:
            bit=cur&-cur
            trial=mask|bit
            probe=trial
            can=True
            while probe:
                pbit=probe&-probe
                u=pbit.bit_length()-1
                if (trial&adj[u]).bit_count()>1:
                    can=False
                    break
                probe-=pbit
            if can:
                maximal=False
                break
            cur-=bit
        if maximal:
            maxsets[mask.bit_count()]+=1
            b=n-(mask&((1<<n)-1)).bit_count()
            patterns[b]+=1
    return +allsets,+maxsets,patterns


def main():
    examined=0
    for n in range(3,7):
        p,m,pat=independent_bruteforce(n)
        assert p==+polynomial(n),(n,'all',p,polynomial(n))
        assert m==maximal_polynomial(n),(n,'maximal',m,maximal_polynomial(n))
        expected={0:1,1:n,2:comb(n,2)*(2**(n-2)-2)}
        for b in range(3,n+1):expected[b]=comb(n,b)*b**(n-b)
        assert dict(pat)=={b:t for b,t in expected.items() if t},(n,'patterns',pat,expected)
        examined+=(1<<(n+comb(n,2)))
        print(f'n={n} vertices={n+comb(n,2)} all_sets={sum(p.values())} maximal_sets={sum(m.values())} poly={sorted(p.items())} maximal_poly={sorted(m.items())} omitted_originals={dict(sorted(pat.items()))}')
    print(f'PASS: {examined:,} total vertex subsets exhaustively tested against original induced-degree/maximality definitions.')
if __name__=='__main__':main()
