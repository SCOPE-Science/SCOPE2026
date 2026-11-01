"""Standalone exact arithmetic checks for path three-point median BV sensitivity."""
from itertools import permutations,product
from fractions import Fraction
from math import sin,pi,cos

def selectors(base):
    n=len(base)
    out=[0]
    for i in range(1,n-1):
        out.append(sorted((i-1,i,i+1),key=lambda j:base[j])[1])
    out.append(n-1)
    return out

def column_var(sel,k,w):
    z=[int(j>k) for j in sel]
    return sum(w[i]*abs(z[i+1]-z[i]) for i in range(len(w)))

def bound(w):
    m=len(w)
    if m==1:return Fraction(1)
    cand=[Fraction(1),w[1]/w[0],w[-2]/w[-1]]
    cand.extend((w[k-1]+w[k]+w[k+1])/w[k] for k in range(1,m-1))
    return max(cand)

def filter_values(base):
    return [base[j] for j in selectors(base)]

def tv(z,w):
    return sum(w[i]*abs(z[i+1]-z[i]) for i in range(len(w)))

if __name__=='__main__':
    checked=0
    for n in range(2,8):
        profiles=[[Fraction(1)]*(n-1)]
        profiles += [[Fraction(i%3+1) for i in range(n-1)],
                     [Fraction((2*i+1)%5+1) for i in range(n-1)]]
        for w in profiles:
            observed=Fraction(0)
            for perm in permutations(range(n)):
                sel=selectors(perm)
                for k in range(n-1):
                    r=column_var(sel,k,w)/w[k]
                    observed=max(observed,r)
                    if r>bound(w):raise AssertionError((n,w,perm,k,r,bound(w)))
                    checked+=1
            if observed!=bound(w):raise AssertionError(('not sharp',n,w,observed,bound(w)))
            print('PASS',n,tuple(map(str,w)),'exact',observed)
    for n in range(3,31):
        m=n-1
        v=[sin((i+.5)*pi/m) for i in range(m)]
        lam=1+2*cos(pi/m)
        L=max(([v[1]/v[0],v[-2]/v[-1]] + [(v[i-1]+v[i]+v[i+1])/v[i] for i in range(1,m-1)]))
        if abs(L-lam)>1.e-11: raise AssertionError((n,L,lam))
    for eps in [Fraction(1,10),Fraction(1,2),Fraction(3,4)]:
        f=[Fraction(0),Fraction(2),Fraction(1),Fraction(3)]
        g=[Fraction(0),Fraction(2),Fraction(1)+eps,Fraction(3)+eps]
        for w in ([Fraction(1)]*3,[Fraction(1),Fraction(2),Fraction(1)]):
            ratio=tv([a-b for a,b in zip(filter_values(g),filter_values(f))],w)/tv([a-b for a,b in zip(g,f)],w)
            if ratio!=bound(w):raise AssertionError(('witness',eps,w,ratio,bound(w)))
    print('ALL TESTS PASS. Permutation-column checks',checked)
