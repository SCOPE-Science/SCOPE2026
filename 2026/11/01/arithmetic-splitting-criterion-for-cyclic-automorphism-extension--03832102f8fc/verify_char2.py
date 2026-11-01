"""Independent characteristic-two test of the cyclic extension theorem over F4."""
from itertools import product
from collections import Counter
from math import gcd,lcm

def mul(a,b):
    x=0
    while b:
        if b&1:x^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return x

def power(a,n):
    x=1
    while n:
        if n&1:x=mul(x,a)
        a=mul(a,a);n>>=1
    return x

def order(a):
    assert a
    x=a;n=1
    while x!=1:x=mul(x,a);n+=1
    return n

def main():
    m=3;h=2;M=3;xi=2;r=1
    c=[1,1,power(xi,r)];N=m*h
    ix=lambda i,j:(i%m)*h+j
    B=[[0]*N for _ in range(N)]
    for i in range(m):
        B[ix(i,0)][ix(i,1)]=1
        B[ix(i,0)][ix(i+1,1)]=c[i]
        B[ix(i,1)][ix(i,0)]=1
    roots=[1,2,3]
    good=[]
    for s in range(m):
        for base in product(roots,repeat=m):
            perm=[ix(i+s,j) for i in range(m) for j in range(h)]
            fac=[power(base[i],2**j) for i in range(m) for j in range(h)]
            if all(mul(B[v][u],fac[u])==mul(mul(fac[v],fac[v]),B[perm[v]][perm[u]])
                   for v in range(N) for u in range(N)):
                good.append((s,perm,fac))
    assert len(good)==9
    orders=[]
    for s,perm,fac in good:
        seen=set();o=1
        for v in range(N):
            if v in seen:continue
            x=v;length=0;prod=1
            while x not in seen:
                seen.add(x);prod=mul(prod,fac[x]);length+=1;x=perm[x]
            o=lcm(o,length*order(prod))
        orders.append(o)
    assert Counter(orders)==Counter({1:1,3:2,9:6})
    print('CHAR2_OK F4 m=3 h=2 r=1 automorphism_group=C9 nonsplit')
    print('VERIFY_OK')

if __name__=='__main__':main()
