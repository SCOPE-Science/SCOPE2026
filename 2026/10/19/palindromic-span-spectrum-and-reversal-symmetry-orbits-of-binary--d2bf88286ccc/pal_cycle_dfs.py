"""Exact longest-palindrome census for binary de Bruijn cycles, orders 2..5.
No third-party dependencies. Every cycle is anchored to the unique 0^n factor.
"""
from collections import Counter


def census_dfs(n):
    N = 1 << n
    bitmask = N-1
    used = bytearray(N)
    used[0] = 1
    bits = [0]*n
    distribution = Counter()
    witnesses = {}
    count=0
    def palmax(w):
        # Check all centers and all lengths <=N against the cyclic word.
        z = w+w+w
        ans=0
        for length in range(1,N+1):
            for a in range(N):
                t=z[a:a+length]
                if t==t[::-1]:ans=max(ans,length)
        return ans
    def dfs(v):
        nonlocal count
        if len(bits)==N+n-1:
            w=''.join(map(str,bits[:N]))
            assert len({(w+w)[i:i+n] for i in range(N)}) == N
            k=palmax(w)
            distribution[k]+=1
            witnesses.setdefault(k,w)
            count+=1
            return
        for b in (0,1):
            v2=((v<<1)|b)&bitmask
            if not used[v2]:
                used[v2]=1
                bits.append(b)
                dfs(v2)
                bits.pop()
                used[v2]=0
    dfs(0)
    return count,dict(sorted(distribution.items())),witnesses

if __name__=='__main__':
    for n in range(2,6):
        count,hist,wits=census_dfs(n)
        print('DFS',n,count,hist)
        print('WITNESSES',n,wits)
