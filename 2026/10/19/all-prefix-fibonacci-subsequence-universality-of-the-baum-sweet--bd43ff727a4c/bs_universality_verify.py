#!/usr/bin/env python3
"""Independent checks of finite scattered-subsequence universality assertions."""
from itertools import groupby


def digit_word(N):
    out=[]
    for n in range(N):
        if n==0: out.append(1); continue
        groups=[sum(1 for _ in g) for bit,g in groupby(bin(n)[2:]) if bit=='0']
        out.append(int(all(k%2==0 for k in groups)))
    return out


def automaton_word(N):
    out=[]
    for n in range(N):
        state=0  # 0 means zero-run parity even; 1 means odd; 2 dead
        if n==0: out.append(1); continue
        for bit in bin(n)[2:]:
            if state==2: continue
            if bit=='0': state^=1
            elif state==1: state=2
        out.append(int(state==0))
    return out


def greedy_arches(word):
    ans=seen=0
    for digit in word:
        seen |= 1<<digit
        if seen==3:
            seen=0;ans+=1
    return ans


def shortest_absent_length(word):
    n=len(word)
    dp=[0]*(n+1);dp[n]=1
    first=[n,n]
    for i in range(n-1,-1,-1):
        first[word[i]]=i
        cost=[]
        for digit in (0,1):
            j=first[digit]
            cost.append(1 if j==n else 1+dp[j+1])
        dp[i]=min(cost)
    return dp[0]


def one_count(word): return sum(word)


def exceptional(N):
    return N>=17 and (N-1)&(N-2)==0 and ((N-1).bit_length()-1)%2==0


def predicted(N,word):
    if N<8: return [0,0,0,1,1,1,2,2][N]
    return one_count(word)-2-int(exceptional(N))


def run():
    total=65536
    a=digit_word(total)
    b=automaton_word(total)
    assert a==b, 'independent definitions disagree'
    small=[0,0,0,1,1,1,2,2]
    for n in range(1,2049):
        g=greedy_arches(a[:n])
        assert g==predicted(n,a[:n]), ('arch',n,g,predicted(n,a[:n]))
        assert shortest_absent_length(a[:n])==g+1, ('shortest absent',n)
    test=set([4096,8192,16384,32768,65536])
    for j in range(2,8):
        p=4**j
        for n in (p-1,p,p+1,p+2):
            if 8<=n<=total:test.add(n)
    for n in sorted(test):
        g=greedy_arches(a[:n])
        assert g==predicted(n,a[:n]), ('arch-large',n,g)
        assert shortest_absent_length(a[:n])==g+1, ('shortest-large',n)
    fib=[0,1]
    for _ in range(25): fib.append(sum(fib[-2:]))
    for m in range(3,17):
        n=1<<m
        assert one_count(a[:n])==fib[m+2]
        assert greedy_arches(a[:n])==fib[m+2]-2
    firstpairs=[i for i in range(total-1) if a[i] and a[i+1]]
    assert firstpairs==[4**j-1 for j in range(9) if 4**j<total]
    print('VERIFY_OK: all prefixes 1..2048, large dyadic/power-of-four boundaries,')
    print('two independent Baum-Sweet generators, shortest-absent dynamic programming,')
    print('Fibonacci counts and all adjacent-one locations below 65536.')

if __name__=='__main__': run()
