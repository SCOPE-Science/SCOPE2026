"""Exact-arithmetic checks for the three-shift cubic binomid classification.

Only finite diagnostics are computed; the unrestricted argument is in RESULT.md.
"""
from fractions import Fraction
from math import comb


def u(t):
    return Fraction(t+2, t+1)


def f(n, a, b, c):
    return (n+a)*(n+b)*(n+c)


def candidates():
    # The proof bounds a<=2, then b<=3,5,3 for a=0,1,2.
    bmax = {0: 3, 1: 5, 2: 3}
    found = []
    for a in range(3):
        for b in range(a, bmax[a]+1):
            K = u(a)*u(b)
            upper = K*u(b)
            for m in range(K.numerator//K.denominator+1,
                           upper.numerator//upper.denominator+1):
                den = Fraction(m)-K
                if den <= 0:
                    continue
                cp1 = K/den
                if cp1.denominator != 1:
                    continue
                c = int(cp1)-1
                if c >= b:
                    assert u(a)*u(b)*u(c) == m
                    found.append((a,b,c))
    return sorted(set(found))


def det_bareiss(a):
    a = [list(r) for r in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n-1):
        if a[k][k] == 0:
            q = next((i for i in range(k+1,n) if a[i][k]),None)
            if q is None:
                return 0
            a[k],a[q] = a[q],a[k]
            sign = -sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=a[i][j]*v-a[i][k]*a[k][j]
                assert numer%prev==0
                a[i][j]=numer//prev
        for i in range(k+1,n):
            a[i][k]=0
        prev=v
    return sign*a[-1][-1]


def main():
    cand = candidates()
    expected=[(0,0,0),(0,0,1),(0,0,3),(0,1,2),
              (0,2,7),(0,3,4),(1,1,2),(1,3,14),
              (1,4,8),(1,5,6),(2,2,7),(2,3,4)]
    assert cand==expected
    good = []
    print('Candidates after the first nontrivial coefficient:',len(cand))
    for abc in cand:
        a,b,c=abc
        r2=Fraction(f(2,*abc),f(1,*abc))
        r3=Fraction(f(3,*abc),f(1,*abc))
        assert r2.denominator==1
        if r3.denominator==1:
            good.append(abc)
        print(abc,'f2/f1=',r2,'f3/f1=',r3)
    assert good==[(0,0,0),(0,0,1),(0,1,2)]
    print('Surviving triples:',good)

    tested=0
    for abc in good:
        product=1
        facts=[1]
        for n in range(1,101):
            product*=f(n,*abc)
            facts.append(product)
        for n in range(1,101):
            for k in range(n+1):
                assert facts[n]%(facts[k]*facts[n-k])==0
                tested+=1
    print('Exact f-nomial coefficients tested:',tested)

    det_checks=0
    for m in (2,3):
        for N in range(1,29):
            for k in range(1,min(7,N)+1):
                A=[[comb(N-k+m+i,m+j) for j in range(k)] for i in range(k)]
                determinant=det_bareiss(A)
                fact=[1]
                for r in range(1,N+1):
                    fact.append(fact[-1]*comb(r+m-1,m))
                numerator=fact[N]
                denominator=fact[k]*fact[N-k]
                assert numerator%denominator==0
                assert determinant==numerator//denominator
                det_checks+=1
    print('Exact Pascal-column determinant identities checked:',det_checks)

    scan=0
    additional=0
    for a in range(40):
        for b in range(a,40):
            for c in range(b,81):
                scan+=1
                abc=(a,b,c)
                r2=Fraction(f(2,*abc),f(1,*abc))
                r3=Fraction(f(3,*abc),f(1,*abc))
                if r2.denominator==r3.denominator==1:
                    assert abc in good
                    additional+=1
    print('Additional finite parameter triples scanned:',scan)
    print('Finite parameter triples passing the two tests:',additional)
    print('All exact-arithmetic checks passed.')

if __name__=='__main__':
    main()
