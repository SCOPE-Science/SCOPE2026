#!/usr/bin/env python3
"""Independent suffix-array census for minimal unique factors of period-doubling prefixes."""
from collections import Counter

def period_word(m):
    w = '0'
    for _ in range(m):
        w = ''.join('01' if x == '0' else '00' for x in w)
    return w

def suffix_uniqueness_lengths(w):
    n=len(w)
    sa=list(range(n))
    rank=[int(c) for c in w]
    k=1
    while k<n:
        sa.sort(key=lambda i: (rank[i], rank[i+k] if i+k<n else -1))
        next_rank=[0]*n
        for t in range(1,n):
            i,j=sa[t-1],sa[t]
            next_rank[j]=next_rank[i]+((rank[i],rank[i+k] if i+k<n else -1)!=(rank[j],rank[j+k] if j+k<n else -1))
        rank=next_rank
        if rank[sa[-1]]==n-1:break
        k*=2
    position=[0]*n
    for i,pos in enumerate(sa): position[pos]=i
    lcp=[0]*n
    k=0
    for i in range(n):
        r=position[i]
        if r==n-1:
            k=0; continue
        j=sa[r+1]
        while i+k<n and j+k<n and w[i+k]==w[j+k]:k+=1
        lcp[r+1]=k
        if k:k-=1
    return [max(lcp[position[i]],lcp[position[i]+1] if position[i]+1<n else 0) for i in range(n)]

def mus_census(w):
    n=len(w)
    forward=suffix_uniqueness_lengths(w)
    reverse=suffix_uniqueness_lengths(w[::-1])
    ans=[]
    for i in range(n):
        length=forward[i]+1
        if i+length>n: continue
        j=i+length
        if length==1 or reverse[n-j]>=length-1:
            ans.append((i,j))
    return sorted(ans)

def brute_mus(w):
    n=len(w)
    cnt=Counter(w[i:j] for i in range(n) for j in range(i+1,n+1))
    return sorted((i,j) for i in range(n) for j in range(i+1,n+1)
                  if cnt[w[i:j]]==1 and (j-i==1 or (cnt[w[i+1:j]]>1 and cnt[w[i:j-1]]>1)))

def main():
    n_checked=0
    for m in range(3,13):
        w=period_word(m)
        n=1<<m
        expected=sorted([(n//4-1,n//2),(3*n//8-1,5*n//8),(n//2-1,3*n//4),(3*n//4-1,n)])
        result=mus_census(w)
        assert result==expected,(m,result,expected)
        assert all(j-i==n//4+1 for i,j in result)
        if m<=7:
            assert brute_mus(w)==result
        if m>=4:
            counts=Counter(w[i:i+4] for i in range(n-3))
            assert all(v>=2 for v in counts.values()),(m,counts)
        # finite suffix parity property for all lengths, m<=8
        if m<=8:
            for ell in range(1,n+1):
                suffix=w[n-ell:]
                count=sum(w.startswith(suffix,i) for i in range(n-ell+1))
                assert count%2==1,(m,ell,count)
                n_checked+=1
        print(f'm={m:2d} n={n:4d} MUS={result} brute={m<=7}')
    print(f'PASS: 10 dyadic lengths through 4096; 5 brute-force censes; {n_checked} odd-terminal-suffix counts; 9 length-four-repeat checks.')
if __name__=='__main__':main()
