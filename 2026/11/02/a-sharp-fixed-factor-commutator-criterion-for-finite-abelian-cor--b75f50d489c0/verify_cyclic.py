#!/usr/bin/env python3
"""Standalone exact checks of commutator spans and fixed-factor maps.

For R_n, use e_i * e_j=e_(2j-i), and [x,y]=x*y-y*x.
All arithmetic is integer; modular checks reduce the integer identities.
"""
from math import gcd, lcm
from collections import defaultdict
from random import Random

class DSU:
    def __init__(self,n):self.parent=list(range(n))
    def root(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]];x=self.parent[x]
        return x
    def join(self,x,y):self.parent[self.root(x)]=self.root(y)
    def components(self):
        parts=defaultdict(list)
        for x in range(len(self.parent)):parts[self.root(x)].append(x)
        return sorted([tuple(v) for v in parts.values()], key=lambda x:x[0])

def divisors(m):return [d for d in range(1,m+1) if m%d==0]
def phi(m):return sum(gcd(j,m)==1 for j in range(1,m+1))
def order(a,m):
    if m==1:return 1
    assert gcd(a,m)==1
    x=a % m;count=1
    while x!=1:x=x*a%m;count+=1
    return count

def mul(n,a,b):
    out=[0]*n
    for i,ci in enumerate(a):
        if ci:
            for j,dj in enumerate(b):
                if dj:out[(2*j-i)%n]+=ci*dj
    return out

def comm(n,a,b):
    x=mul(n,a,b);y=mul(n,b,a)
    return [v-w for v,w in zip(x,y)]

def e(n,i):
    x=[0]*n;x[i%n]=1;return x

def add(n,a,b):return [x+y for x,y in zip(a,b)]

def scalar(c,a):return [c*x for x in a]

def decomp(n):
    a=0;m=n
    while m%2==0:a+=1;m//=2
    return a,m

def sigma(n,j):return (-2*j)%n

def verify(n,rng):
    g=gcd(n,3);a,m=decomp(n)
    expected_c=sum(phi(d)//order(-2,d) for d in divisors(m))
    # All basis commutators generate the within-coset augmentation ideal.
    C=DSU(n)
    for i in range(n):
        for j in range(n):
            aa=(2*j-i)%n;bb=(2*i-j)%n
            assert (aa-bb)%g==0
            C.join(aa,bb)
    C_parts=C.components()
    assert len(C_parts)==g
    assert all(len(set(v%g for v in part))==1 for part in C_parts)
    # Incidence components of the map x -> -2x.
    D=DSU(n)
    for j in range(n):D.join(j,sigma(n,j))
    D_parts=D.components();c=len(D_parts)
    assert c==expected_c,(n,c,expected_c)
    assert c>=g
    predicted=(m in (1,3))
    assert (c==g)==predicted,(n,c,g)
    # A basis commutator with second factor e0 is the predicted edge.
    for j in range(n):
        want=add(n,e(n,j),scalar(-1,e(n,sigma(n,j))))
        assert comm(n,e(n,-j),e(n,0))==want
    if predicted:
        # Construct primitive for each root difference e_j-e_root.
        for j in range(n):
            pos=j
            primitive=[0]*n
            for t in range(a):
                primitive[(-pos)%n]+=1
                pos=sigma(n,pos)
            assert sigma(n,pos)==pos
            assert (pos-j)%g==0
            expected=add(n,e(n,j),scalar(-1,e(n,pos)))
            assert comm(n,primitive,e(n,0))==expected,(n,j)
        # Sample arbitrary integer members of W, solve by telescoping.
        for _ in range(3):
            weights=[rng.randint(-7,7) for i in range(n)]
            u=[0]*n;primitive=[0]*n
            for j,co in enumerate(weights):
                pos=j
                for t in range(a):
                    primitive[(-pos)%n]+=co
                    pos=sigma(n,pos)
            u=[0]*n
            for j,co in enumerate(weights):
                root=j
                for _ in range(a):root=sigma(n,root)
                u[j]+=co;u[root]-=co
            assert comm(n,primitive,e(n,0))==u
            for mod in (2,3,5,7):
                assert [x%mod for x in comm(n,primitive,e(n,0))]==[x%mod for x in u]
    else:
        # Construct an element of W that cannot be [a,e0].
        # Find two separate sigma-components within one residue mod g.
        comp_id={x:ii for ii,part in enumerate(D_parts) for x in part}
        pair=next((i,j) for i in range(n) for j in range(i+1,n)
                  if (i-j)%g==0 and comp_id[i]!=comp_id[j])
        i,j=pair
        u=add(n,e(n,i),scalar(-1,e(n,j)))
        assert sum(u[k] for k in D_parts[comp_id[i]])==1
        assert sum(u[k] for k in D_parts[comp_id[j]])==-1
    return (n,g,c,predicted)

if __name__=='__main__':
    rng=Random(20261029)
    results=[verify(n,rng) for n in range(1,145)]
    selected=[r for r in results if r[0] in (1,2,3,4,5,6,7,8,9,10,12,15,16,18,24,27,32,48,64,72,96,128,144)]
    print('n gcd(n,3) fixed_factor_components universal_fixed_factor')
    for row in selected:print(*row)
    yes=[n for n,g,c,ok in results if ok]
    print('Universal fixed-factor n up to 144:',yes)
    print('Verified all n=1..144: exact commutator span, orbit count, sharp classification,')
    print('basis telescoping over Z and samples over Z/2,Z/3,Z/5,Z/7.')
    print('VERIFY_OK')
