#!/usr/bin/env python3
"""Direct finite-state validation for majority dynamics on bouquets of squares.

This code checks sample finite sizes and the local identities used by the
all-size mathematical proof. It does not replace that proof.
"""
from math import comb, factorial
from itertools import product

def majority3(a,b,c):
    return int(a+b+c >= 2)

def local(h,x):
    a,b,c=x
    return (majority3(a,h,b),majority3(b,a,c),majority3(c,b,h))

def formula(k):
    fixed=4**k+comb(2*k,k)
    q=0
    for b in range(k+1):
        for c in range(k-b+1):
            a=k-b-c
            if 2*c < k < 2*(b+c):
                q+=factorial(k)//(factorial(a)*factorial(b)*factorial(c))
    alternate=sum(comb(k,j)*sum(comb(j,c) for c in range(min(j,(k-1)//2)+1))
                  for j in range(k//2+1,k+1))
    assert q==alternate
    return fixed,q

def adjacency(k):
    n=3*k+1
    v=[0]*n
    def edge(u,w):
        v[u]|=1<<w
        v[w]|=1<<u
    for i in range(k):
        a,b,c=3*i+1,3*i+2,3*i+3
        edge(0,a);edge(a,b);edge(b,c);edge(c,0)
    return v

def step(x, v):
    y=0
    for j, mask in enumerate(v):
        neighbors=(x&mask).bit_count()
        deg=mask.bit_count()
        if neighbors*2>deg or (neighbors*2==deg and ((x>>j)&1)):
            y |= 1<<j
    return y

def main():
    states=list(product((0,1),repeat=3))
    local_fixed={h:[x for x in states if local(h,x)==x] for h in (0,1)}
    local_period2=[(x,local(0,x)) for x in states if local(1,local(0,x))==x]
    assert local_fixed[0]==[(0,0,0),(0,1,1),(1,1,0),(1,1,1)]
    assert local_fixed[1]==[(0,0,0),(0,0,1),(1,0,0),(1,1,1)]
    assert local_period2==[
        ((0,0,0),(0,0,0)),
        ((1,0,1),(0,1,0)),
        ((1,1,1),(1,1,1))]
    print('LOCAL_IDENTITIES_OK: four fixed local words per hub phase; three alternating-cycle words')
    total=0
    for k in range(1,7):
        v=adjacency(k)
        fixed=two=0
        non12=0
        for x in range(1<<(3*k+1)):
            y=step(x,v)
            z=step(y,v)
            if y==x:
                fixed+=1
            elif z==x and x<y:
                two+=1
            elif z==x:
                pass
            total+=1
        f,q=formula(k)
        assert (fixed,two)==(f,q),(k,(fixed,two),(f,q))
        print(f'k={k}: states={1<<(3*k+1)}, fixed={fixed}, primitive_two_orbits={two}, formulas_agree')
    print(f'EXHAUSTIVE_OK: {total} directly evaluated configurations')
    # Independent symbolic sum identity and asymptotic elementary bound.
    for k in range(1,151):
        f,q=formula(k)
        assert f==4**k+comb(2*k,k) and 0<q<=3**k
    print('BINOMIAL_IDENTITY_OK: 150 parameter values')
if __name__=='__main__':
    main()
