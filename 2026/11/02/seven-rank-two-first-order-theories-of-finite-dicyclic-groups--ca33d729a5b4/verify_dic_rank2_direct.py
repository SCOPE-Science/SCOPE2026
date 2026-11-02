#!/usr/bin/env python3
"""Independent pair-atom rank-two type enumeration for finite dicyclic groups.
Only finite observations; the infinite theorem is proved separately."""
from itertools import product

def group(n):
    m=2*n
    return [(k,s) for s in (0,1) for k in range(m)]

def multiply(n,x,y):
    a,s=x; b,t=y
    return ((a + (b if s==0 else -b) + (n if s and t else 0))%(2*n),s^t)

def atoms(n,x,y):
    v=((0,0),x,y)
    bits=0
    for i,j in product(range(3),repeat=2):
        bits=(bits<<1)|int(v[i]==v[j])
    for i,j,k in product(range(3),repeat=3):
        bits=(bits<<1)|int(multiply(n,v[i],v[j])==v[k])
    return bits

def theory(n):
    els=group(n)
    ext=[]
    for x in els:
        ext.append(frozenset(atoms(n,x,y) for y in els))
    return frozenset(ext)

def anticipated(n):
    return (n==2,n==3,n==4,n>=5 and n%3==0,n>=5 and n%4==0,n>=5)

if __name__=='__main__':
    fingerprints={}
    for n in range(2,57):
        t=theory(n)
        fingerprints.setdefault(t,[]).append(n)
    assert len(fingerprints)==7, len(fingerprints)
    groups=sorted(fingerprints.values(),key=lambda v:v[0])
    expected=[]
    for cond in (lambda n:n==2,lambda n:n==3,lambda n:n==4,
                 lambda n:n>=5 and n%3!=0 and n%4!=0,
                 lambda n:n>=5 and n%3==0 and n%4!=0,
                 lambda n:n>=5 and n%3!=0 and n%4==0,
                 lambda n:n>=5 and n%3==0 and n%4==0):
       expected.append([n for n in range(2,57) if cond(n)])
    assert groups==expected,(groups,expected)
    print('direct exact two-round atomic-extension profiles: n=2..56')
    for v in groups: print('representative',v[0],'count',len(v),'members',','.join(map(str,v)))
    print('seven classes: PASS')
