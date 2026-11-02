#!/usr/bin/env python3
"""Direct palindrome census and canonical witness verification."""

def cantor(k):
    w = '1'
    for _ in range(k):
        w = w + ('0' * len(w)) + w
    return w

def central(w,n):
    assert len(w) % 2 == 1 and n % 2 == 1 and 1 <= n <= len(w)
    i = (len(w)-n)//2
    return w[i:i+n]

def predicted(k,n):
    size = 3**k
    L = size // 3
    if n == 1: return {'0','1'}
    if n % 2 == 0: return {'0'*n} if n<=L else set()
    if n > L: return {central(cantor(k),n)} if n<=size else set()
    j=1
    while 3**j < n: j+=1
    A = cantor(j)
    B = '0'*(3**(j-1)) + cantor(j-1) + '0'*(3**(j-1))
    return {'0'*n,central(A,n),central(B,n)}

def observed(w):
    n=len(w)
    pal_by_length = [set() for _ in range(n+1)]
    for center in range(n):
        # odd centers
        lo=hi=center
        while lo>=0 and hi<n and w[lo]==w[hi]:
            pal_by_length[hi-lo+1].add(w[lo:hi+1]);lo-=1;hi+=1
        # even centers
        lo=center;hi=center+1
        while lo>=0 and hi<n and w[lo]==w[hi]:
            pal_by_length[hi-lo+1].add(w[lo:hi+1]);lo-=1;hi+=1
    return pal_by_length

def main():
    for k in range(1,9):
        w=cantor(k); P=observed(w)
        for n in range(1,len(w)+1):
            expected = predicted(k,n)
            assert P[n]==expected, (k,n,len(P[n]),len(expected),P[n]^expected)
        assert sum(map(len,P))==len(w)
        print(f'k={k}, length={len(w)}, palindrome_total={sum(map(len,P))}, all lengths and exact representatives PASS')
    print('All level-by-level enumerations PASS')

if __name__=='__main__':main()
