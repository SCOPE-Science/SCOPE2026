#!/usr/bin/env python3
"""Independent cycle-space and dynamical checks for 3-CCA on prisms."""
from itertools import product

def diff(a,b):
    d=(b-a)%3
    return 0 if d==0 else (1 if d==1 else -1)

def basis_zero(s,n):
    top=s[:n];bottom=s[n:]
    if sum(diff(top[i],top[(i+1)%n]) for i in range(n)):
        return False
    for i in range(n):
        j=(i+1)%n
        w=diff(top[i],top[j])+diff(top[j],bottom[j])+diff(bottom[j],bottom[i])+diff(bottom[i],top[i])
        if w: return False
    return True

def verify(n):
    cnt=0
    for s in product(range(3),repeat=2*n):
        if basis_zero(s,n):cnt+=1
    return cnt

if __name__=='__main__':
    expect={3:261,4:1485,5:8409,6:49215}
    for n,e in expect.items():
        val=verify(n)
        print(n,val,e,val==e,flush=True)
        assert val==e
    print('PASS')
