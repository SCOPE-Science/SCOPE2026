"""Reproduce finite checks for the plane-branch fpt/Tjurina theorem.
Run: python verify.py (requires SymPy). These examples check finite primes, not the general proof.
"""
from collections import defaultdict
from math import comb
import sympy as sp

X, Y = sp.symbols('x y')


def multiply(a, b, q, p):
    z = defaultdict(int)
    for (i,j), ai in a.items():
        for (u,v), bj in b.items():
            if i+u<q and j+v<q:
                z[(i+u,j+v)] = (z[(i+u,j+v)] + ai*bj) % p
    return {ij:c for ij,c in z.items() if c}


def power(base, exponent, q, p):
    result={(0,0):1}
    while exponent:
        if exponent & 1:
            result=multiply(result,base,q,p)
        exponent//=2
        if exponent:
            base=multiply(base,base,q,p)
    return result


def length_from_groebner(polys,p):
    K=3*p+3
    G=sp.groebner(polys+[X**K,Y**K],X,Y,order='lex',modulus=p)
    leading=[h.LM().exponents for h in G.polys]
    return sum(not any(i>=u and j>=v for u,v in leading)
               for i in range(K) for j in range(K))


def verify_one(p):
    a,b=p+1,p+2
    assert p>=5 and (p-1)*(a+b)>a*b
    for lam in (0,1,2):
        f=X**a+Y**b+lam*X**(p-1)*Y**(p-1)
        m=length_from_groebner([sp.diff(f,X),sp.diff(f,Y)],p)
        t=length_from_groebner([sp.diff(f,X),sp.diff(f,Y),f],p)
        expected=(p*(p+1),p*(p+1)-(0 if lam==0 or p==5 else 2))
        assert (m,t)==expected,(p,lam,m,t,expected)
        for e in (1,2):
            q=p**e
            n=(q//p)-1 if lam==0 else (q-1)//(p-1)
            base={(a,0):1,(0,b):1}
            if lam:base[(p-1,p-1)]=lam
            pow_n=power(base,n,q,p)
            pow_n1=power(base,n+1,q,p)
            assert pow_n and not pow_n1,(p,lam,e,n,pow_n1)
            if lam:
                assert pow_n=={(q-1,q-1):pow(lam,n,p)},(p,lam,e,pow_n)
    return True


def main():
    for p in (5,7,11,13):
        verify_one(p)
        print('prime',p,'verified')
    print('VERIFY_OK')


if __name__=='__main__':main()
