#!/usr/bin/env python3
"""Finite-prime-field, independent enumeration of star evolution algebra automorphisms.

Run: python verify_star.py
Only small cases are exhaustively enumerated; general theorem uses symbolic proof.
"""
from itertools import product
from math import gcd, prod


def chi(x, p):
    x %= p
    if x == 0: return 0
    return 1 if pow(x, (p-1)//2, p) == 1 else -1


def orth_order(d, p, det):
    if d % 2:
        r = (d-1)//2
        return 2 * p**(r*r) * prod(p**(2*i)-1 for i in range(1,r+1))
    r=d//2
    eps=chi((-1)**r * det,p)
    return 2*p**(r*(r-1))*(p**r-eps)*prod(p**(2*i)-1 for i in range(1,r))


def expected(p,m):
    if m%p:
        return gcd(3,p-1)*orth_order(m-1,p,m)
    d=m-2
    multipliers = (p-1) if m%2==0 else (p-1)//2
    return p**d * multipliers * orth_order(d,p,-1)


def dot(u,v,p):
    return sum(x*y for x,y in zip(u,v))%p


def brute(p,m):
    vectors=list(product(range(p), repeat=m))
    z=(0,)*m
    target=tuple([1]*m)
    count=0
    for a in range(1,p):
        cols=[v for v in vectors if dot(v,v,p)==a]
        t=tuple([a*a%p]*m)
        def visit(chosen, total):
            nonlocal count
            j=len(chosen)
            if j==m-1:
                v=tuple((t[k]-total[k])%p for k in range(m))
                if dot(v,v,p)!=a: return
                if any(dot(v,w,p) for w in chosen): return
                # Gram=a I implies W invertible, and W1=a^2 1.
                count+=1
                return
            for v in cols:
                if any(dot(v,w,p) for w in chosen): continue
                new=tuple((total[k]+v[k])%p for k in range(m))
                visit(chosen+[v],new)
        visit([],z)
    return count


def check_formula():
    for p,m in [(3,2),(5,2),(7,2),(3,3),(5,3),(7,3),(3,4)]:
        a=brute(p,m)
        b=expected(p,m)
        print('q=%d m=%d observed=%d predicted=%d'%(p,m,a,b))
        assert a==b,(p,m,a,b)

    # Check on a sample ordinary permutation automorphism over a prime field.
    for p,m in [(3,3),(5,3),(3,4),(5,5)]:
        s=tuple([1]*m)
        a=1
        W=list(zip(*[tuple(1 if i==j else 0 for i in range(m)) for j in range(m)]))
        assert all(dot(W[i],W[j],p)==(a if i==j else 0) for i in range(m) for j in range(m))
        assert all(sum(W[i])%p==a*a%p for i in range(m))
    # Modular case: q=5, m=5.  A multiplier a=4 is not a cube root,
    # yet the isotropic-s parabolic construction gives an automorphism.
    p,m,a=5,5,4
    s=(1,)*m
    t=tuple((int(i==0)-3)%p for i in range(m))  # t=e_1-(1/2)s
    assert dot(s,s,p)==0 and dot(s,t,p)==1 and dot(t,t,p)==0
    W=[]
    for j in range(m):
        e=tuple(int(i==j) for i in range(m))
        alpha=dot(t,e,p)
        beta=dot(s,e,p)
        W.append(tuple((2*e[i]-alpha*s[i]+2*beta*t[i])%p for i in range(m)))
    assert all(dot(W[i],W[j],p)==(a if i==j else 0) for i in range(m) for j in range(m))
    assert all(sum(W[j][i] for j in range(m))%p==a*a%p for i in range(m))
    assert a**3%p!=1
    print('isotropic modular non-cubic multiplier PASSED')
    print('small-field counts and generator checks PASSED')

if __name__=='__main__':
    check_formula()
