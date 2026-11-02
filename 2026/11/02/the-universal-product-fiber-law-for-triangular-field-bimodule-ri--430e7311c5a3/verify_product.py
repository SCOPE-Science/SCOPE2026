"""Exact finite-field verification of triangular ring multiplication fibers."""
from itertools import product
from collections import Counter

def mul(a,b):
    z=0
    while b:
        if b&1: z^=a
        b>>=1
        a<<=1
        if a&4:a^=7
    return z

def square(a):return mul(a,a)

def prod(x,y,twisted):
    a,v1,v2,c=x
    b,w1,w2,d=y
    return (mul(a,b),mul(a,w1)^mul(v1,d),mul(a,w2)^mul(v2,square(d) if twisted else d),mul(c,d))

elts=list(product(range(4),repeat=4))
counts=[]
for twisted in (False,True):
    freq=Counter(prod(a,b,twisted) for a in elts for b in elts)
    assert len(freq)==256
    for a,v1,v2,c in elts:
        pred=16*(7 if a==0 else 3)*(7 if c==0 else 3)
        if a==c==0:pred+=16*(256 if v1==v2==0 else 0)-256
        assert freq[(a,v1,v2,c)]==pred, (twisted,a,v1,v2,c,freq[(a,v1,v2,c)],pred)
    center=[x for x in elts if all(prod(x,y,twisted)==prod(y,x,twisted) for y in elts)]
    assert len(center)==(2 if twisted else 4), (twisted,center)
    assert sum(freq.values())==65536
    counts.append(freq)
    print(('twisted' if twisted else 'untwisted')+' center='+str(len(center))+' target-count-by-fiber='+str(dict(sorted(Counter(freq.values()).items()))))
assert counts[0]==counts[1]
print('FIBERS_EQUAL_EXACTLY; VERIFY_OK')
