#!/usr/bin/env python3
from fractions import Fraction
import math

def N(m):
    return math.sqrt((4**(m+1)-1)/3.0)

checks=0
for n in range(1,21):
    # Vertices u,v_1,...,v_n as integer tuples.
    u=tuple([1]*n)
    V=[u]
    for k in range(1,n+1):
        v=[0]*n
        v[k-1]=-1
        for j in range(k,n):
            v[j]=1
        V.append(tuple(v))

    A=[]
    for k in range(1,n+1):
        a=[0]*n
        a[k-1]=2**(n-k)
        for j in range(k+1,n+1):
            a[j-1]=-2**(n-j)
        A.append(tuple(a))
        vals=[sum(a[i]*v[i] for i in range(n)) for v in V]
        assert vals[k] < 1
        assert all(vals[i]==1 for i in range(n+1) if i!=k)
        assert sum(x*x for x in a)==(4**(n-k+1)-1)//3
        checks += len(vals)

    b=tuple(-2**(n-j) for j in range(1,n+1))
    vals=[sum(b[i]*v[i] for i in range(n)) for v in V]
    assert vals[0] < 1
    assert all(vals[i]==1 for i in range(1,n+1))
    assert sum(x*x for x in b)==(4**n-1)//3

    # Exact positive normal dependence.
    dep=list(b)
    for k,a in enumerate(A,start=1):
        for i in range(n): dep[i]+=2**(k-1)*a[i]
    assert dep==[0]*n

    den=N(n-1)+sum(2**(k-1)*N(n-k) for k in range(1,n+1))
    r=2**n/den
    r_alt=math.sqrt(3)/(2*math.sqrt(1-4**(-n)) + sum(math.sqrt(1-4**(-j)) for j in range(1,n)))
    assert abs(r-r_alt) < 2e-13*max(1.0,r)

    c=[]
    for k in range(1,n+1):
        m=n-k
        inner=N(m)+sum(2**(m-1-t)*N(t) for t in range(m))
        c.append(1-r*inner/2**m)
    assert abs(c[0]) < 2e-12
    for k,a in enumerate(A,start=1):
        lhs=sum(a[i]*c[i] for i in range(n))
        rhs=1-r*N(n-k)
        assert abs(lhs-rhs)<2e-10*max(1.0,abs(rhs))
    lhs=sum(b[i]*c[i] for i in range(n)); rhs=1-r*N(n-1)
    assert abs(lhs-rhs)<2e-10*max(1.0,abs(rhs))

    # Circumcenter and squared radius are rational and checked exactly.
    q=[Fraction(1,2)-Fraction(1,2**j) for j in range(1,n+1)]
    R2=Fraction(n,4)+Fraction(4,3)-Fraction(1,2**n)-Fraction(1,3*4**n)
    for v in V:
        d2=sum((Fraction(v[i])-q[i])**2 for i in range(n))
        assert d2==R2
    assert q[0]>=0 and all(q[j]>=q[j-1] for j in range(1,n)) and q[-1]<=1

print(f"VERIFY_OK enriched-order-chain-radii n=1..20 incidence_checks={checks} exact_circumspheres=yes")
