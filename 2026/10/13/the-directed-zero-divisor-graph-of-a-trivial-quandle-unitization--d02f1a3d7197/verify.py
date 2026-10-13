"""Finite-field checks for the exact directed zero-divisor graph theorem.
Run: python verify.py. No third-party packages required.
"""
from itertools import product
from collections import Counter
from math import factorial

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.q
    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q
    def mul(self, a, b):
        if self.q != 4:
            return a*b % self.q
        a0,a1 = a & 1, a >> 1
        b0,b1 = b & 1, b >> 1
        return ((a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1))
    def inv(self, a):
        assert a
        return next(b for b in range(self.q) if self.mul(a,b)==1)
    def summation(self, arr):
        s=0
        for a in arr:s=self.add(s,a)
        return s

def mul_tri(x,y,F):
    la,mu,w=x; t,nu,z=y
    return (F.mul(la,t),F.mul(mu,nu),tuple(F.add(F.mul(la,zz),F.mul(nu,ww)) for ww,zz in zip(w,z)))

def mul_original(x,y,F):
    c,a=x[0],x[1:];d,b=y[0],y[1:]
    sb=F.summation(b)
    return (F.mul(c,d),)+tuple(F.add(F.add(F.mul(c,bj),F.mul(d,aj)),F.mul(sb,aj)) for aj,bj in zip(a,b))

def to_tri(x,F):
    c,a=x[0],x[1:]
    return (c,F.add(c,F.summation(a)),tuple(a[1:]))

def desc(x):
    la,mu,w=x
    return ('A' if la and not mu else 'B' if mu and not la else 'C' if not (la or mu) and any(w) else 'unit_or_zero')

def check(q,n):
    F=Field(q); W=list(product(range(q),repeat=n-1))
    ALL=[(a,b,w) for a,b in product(range(q),repeat=2) for w in W]
    D=[x for x in ALL if desc(x) in 'ABC']
    assert len(D)==(2*q-1)*q**(n-1)-1
    # Symbolically predicted all graph edges, including square-zero loops.
    adj={(x,y) for x in D for y in D if mul_tri(x,y,F)==(0,0,(0,)*(n-1))}
    assert all(((x,y) in adj)==(mul_tri(x,y,F)==(0,0,(0,)*(n-1))) for x,y in product(D,D))
    out=Counter(x for x,y in adj); inc=Counter(y for x,y in adj)
    type_counts=Counter(desc(x) for x in D)
    expected={'A':(q-1)*q**(n-1),'B':(q-1)*q**(n-1),'C':q**(n-1)-1}
    assert type_counts==expected,(q,n,type_counts,expected)
    for x in D:
        typ=desc(x)
        od,ind = {'A':(q-1,q**n-1),'B':(q**n-1,q-1),'C':(q**n-1,q**n-1)}[typ]
        assert (out[x],inc[x])==(od,ind),(q,n,x,out[x],inc[x],typ)
        if typ=='C':
            assert (x,x) in adj
        else:assert (x,x) not in adj
    # The zero product graph is exactly the three-stratum blow-up.
    for x,y in product(D,D):
        tx,ty=desc(x),desc(y)
        bx=tx=='B' and ty in ('A','C')
        cx=tx=='C' and ty in ('A','C')
        ax=tx=='A' and ty=='B' and all(F.add(F.mul(x[0],zz),F.mul(y[1],ww))==0 for ww,zz in zip(x[2],y[2]))
        assert ((x,y) in adj)==(bx or cx or ax),(q,n,x,y)
    # Distinct-vertex graph has exactly three observable bidegree strata.
    loops={x for x in D if (x,x) in adj}
    assert len(loops)==q**(n-1)-1
    arcs=len(adj)-len(loops)
    assert len(adj)==(q-1)**2*q**(n-1)+(q**n-1)**2
    # Check the ring isomorphism using the actual unital quandle multiplication.
    for u,v in product(ALL,repeat=2):
        # convert diagonal and radical coordinates back to original basis
        def inverse_tri(x):
            l,m,w=x
            a=F.add(F.add(m,F.neg(l)),F.neg(F.summation(w)))
            return (l,a)+w
        xu,yu=inverse_tri(u),inverse_tri(v)
        assert to_tri(mul_original(xu,yu,F),F)==mul_tri(u,v,F)
    print('FINITE_FIELD_OK',q,n,'vertices',len(D),'arcs',arcs,'with_loops',len(adj),'strata',dict(type_counts))

if __name__=='__main__':
    for q,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2),(5,3)]:
        check(q,n)
    print('VERIFY_OK')
