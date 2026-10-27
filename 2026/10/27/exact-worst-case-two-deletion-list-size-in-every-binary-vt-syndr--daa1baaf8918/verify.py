"""Independent finite checks of an exact binary VT two-deletion list theorem.

Run: python3 verify.py
No nonstandard Python dependencies.
"""
from itertools import product
from collections import defaultdict


def insert1(w):
    return {w[:i] + bit + w[i:] for i in range(len(w)+1) for bit in '01'}


def syndrome(w):
    return sum(i * int(ch) for i, ch in enumerate(w, 1)) % (len(w)+1)


def inside(y, x):
    it = iter(x)
    return all(any(ch == bit for ch in it) for bit in y)


def of_support(n, positions):
    s = set(positions)
    assert len(s) == len(positions)
    assert all(1 <= i <= n for i in s)
    return ''.join('1' if j in s else '0' for j in range(1,n+1))


def witness(n, a):
    assert n >= 3 and 0 <= a <= n
    k = n//2
    N = n+1
    if a == 0:
        y = '0'*(n-2)
        x = {'0'*n}
        x |= {of_support(n,(i,N-i)) for i in range(1,k+1) if i != N-i}
        return y,x
    if n % 2:
        if a % 2:
            y = '0'*(n-2)
            x = {of_support(n,(a,))}
            x |= {of_support(n,(i,(a-i)%N)) for i in range(1,n+1) if i < (a-i)%N <= n}
        elif a == 2:
            y = '1'+'0'*(n-3)
            x = {of_support(n,(2,))}
            x |= {of_support(n,(1,j,N+1-j)) for j in range(2,k+2)}
        elif a == 4:
            y = '01'+'0'*(n-4)
            x = {of_support(n,(4,)), of_support(n,(1,3))}
            x |= {of_support(n,(2,j,N+2-j)) for j in range(3,k+2)}
        else:
            y = '1'+'0'*(n-3)
            x = {of_support(n,(1,a-1)), of_support(n,(2,a-2))}
            x |= {of_support(n,(1,j,(a-1-j)%N)) for j in range(2,n+1) if j < (a-1-j)%N <= n}
        return y,x
    if a >= n-1:
        y,x = witness(n, N-a)
        return y[::-1], {s[::-1] for s in x}
    r = a
    y = '0'*(r-1)+'1'+'0'*(n-r-2)
    x = {of_support(n,(r,)), of_support(n,(r+1,n))}
    for i in range(1,k+1):
        u,v = i,N-i
        if r in (u,v):
            continue
        if r<u:
            positions=(r,u,v)
        elif u<r<v:
            positions = (u,r-1,r+2) if v==r+1 else ((u,r,r+2) if v==r+2 else (u,r+1,v-1))
        elif v<r:
            positions = (u-1,v-1,r+2)
        else:
            raise AssertionError((n,r,u,v))
        x.add(of_support(n,positions))
    return y,x


def exhaustive(n):
    maxes = [0]*(n+1)
    for bits in product('01',repeat=n-2):
        y=''.join(bits)
        loads=defaultdict(set)
        for z in insert1(y):
            for x in insert1(z):
                loads[syndrome(x)].add(x)
        for a,words in loads.items():
            maxes[a]=max(maxes[a],len(words))
        assert all(len(words) <= n//2+1 for words in loads.values()), (n,y)
    return maxes


def main():
    for n in range(3,14):
        values=exhaustive(n)
        assert values==[n//2+1]*(n+1),(n,values)
        print('EXHAUSTIVE',n, values)
    for n in range(3,81):
        for a in range(n+1):
            y,C=witness(n,a)
            assert len(C)==n//2+1, (n,a,len(C),n//2+1)
            assert len(y)==n-2
            for x in C:
                assert len(x)==n
                assert syndrome(x)==a,(n,a,x,syndrome(x))
                assert inside(y,x),(n,a,y,x)
        if n in (3,4,10,20,40,80):print('CONSTRUCTION',n,'OK')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
