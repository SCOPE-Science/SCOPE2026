"""Exhaustive small-field checks for permutation-type evolution algebras over F4.

Entries are logarithms of nonzero F4 elements in a fixed generator omega
of F4^*, so entries range in {0,1,2}; zero coordinates use -1.
Only elementary multiplication is needed for the cycle structure.
"""
from itertools import product
from math import gcd


def monomial_isomorphisms(a, b):
    """Pairs (shift, exponents) preserving weighted-cycle multiplication."""
    n = len(a)
    out = []
    for j in range(n):
        for x0 in range(3):
            x = [x0]
            for i in range(n-1):
                x.append((2*x[-1]+b[(i+j)%n]-a[i]) % 3)
            if (a[n-1]+x[0]-2*x[n-1]-b[(n-1+j)%n]) % 3 == 0:
                out.append((j,tuple(x)))
    return out


def field_idempotents(a):
    n=len(a); c=0
    for v in product((-1,0,1,2),repeat=n):
        yy = [None]*n
        for i in range(n):
            yy[(i+1)%n] = -1 if v[i]==-1 else (2*v[i]+a[i])%3
        if tuple(yy)==v: c+=1
    return c-1


def predicted(a):
    n=len(a); t=0
    for i in range(n-1):t=(2*t+a[i])%3
    c=(2*t+a[-1])%3
    if n%2:
        return n,1
    if c==0:
        return 3*n,3
    return 3*n//2,0


def order_map(n,pair):
    j,x=pair
    pos=0; v=0; k=0
    while True:
        v=(v+x[pos])%3; pos=(pos+j)%n;k+=1
        if pos==0 and v==0: return k
        assert k<=3*n


def verify():
    total=0
    for n in range(1,8):
        one=(0,)*n
        tw=(0,)*(n-1)+(1,)
        for a in product(range(3),repeat=n):
            aut=monomial_isomorphisms(a,a)
            want,ido=predicted(a)
            assert len(aut)==want,(n,a,len(aut),want)
            norms = [one] if n%2 else [one,tw]
            applicable=[b for b in norms if monomial_isomorphisms(a,b)]
            assert len(applicable)==1,(n,a,applicable)
            if n<=5:
                assert field_idempotents(a)==ido,(n,a)
            total+=1
        if n%2==0:
            G=monomial_isomorphisms(tw,tw)
            assert len(G)==3*n//2
            assert max(order_map(n,g) for g in G)==3*n//2
            # Restrict the shift to the quotient: precisely the even rotations.
            assert {j for j,_ in G}==set(range(0,n,2))
        else:
            assert len(monomial_isomorphisms(one,one))==n
        print('n=',n,'weight tuples=',3**n,'passed')
    assert total==sum(3**n for n in range(1,8))
    for n in [8,10,12,18,24]:
        tw=(0,)*(n-1)+(1,)
        G=monomial_isomorphisms(tw,tw)
        assert len(G)==3*n//2
        assert max(order_map(n,g) for g in G)==3*n//2
        print('n=',n,'twisted group order=',len(G),'split=',n%6!=0)
    print('VERIFY_OK')

if __name__=='__main__':verify()
