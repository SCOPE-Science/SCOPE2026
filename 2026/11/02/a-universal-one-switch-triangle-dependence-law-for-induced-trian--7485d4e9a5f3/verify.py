#!/usr/bin/env python3
"""Standalone exact checks for conditional triangle-count ratio monotonicity.
Requires Python >=3.9 and sympy. No network or external data.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import sympy as sp

checks=0

def check(ok, what=''):
    global checks
    checks+=1
    assert ok, what

def fall(x,k):
    z=1
    for j in range(k):z*=x-j
    return z

def ratio(x,N,k):
    if N<k or x<k:return Fraction(0)
    return Fraction(fall(x,k),fall(N,k))

def conditional(n,h,e,m):
    N=comb(n,2); a=comb(h,2);B=N-a;d=n-h
    A=comb(d,3)+h*comb(d,2)
    return A*ratio(m-e,B,3)+e*d*ratio(m-e,B,2)

def baseline(n,m):
    return comb(n,3)*ratio(m,comb(n,2),3)

def analytic_checks():
    h,d,e,x,c=sp.symbols('h d e x c',real=True)
    n=h+d; N=n*(n-1)/2; B=N-h*(h-1)/2
    A=d*(d-1)*(d+3*h-2)/6
    check(sp.simplify(3*A-d*(B-2)-d*(d-3)*(h-2)/2)==0,'bound c<=3e')
    num=x*(x-1)*(x-2+c)
    den=(x+e)*(x+e-1)*(x+e-2)
    derivative_numerator=sp.diff(num,x)*den-num*sp.diff(den,x)
    P=6*e**2*x-3*e**2+12*e*x**2-18*e*x+8*e+6*x**3-15*x**2+12*x-4
    check(sp.factor(derivative_numerator.subs(c,3*e)-e*(e-1)*P)==0,'endpoint derivative factorization')
    y=sp.symbols('y')
    pos=6*y**3+(12*e+21)*y**2+(6*e**2+30*e+24)*y+9*e**2+20*e+8
    check(sp.expand(P.subs(x,y+2)-pos)==0,'positive polynomial certificate')
    check(sp.Poly(derivative_numerator,c).degree()==1,'affine c derivative')
    # c=0 is a product of three increasing factors (x-j)/(x+e-j).
    for ee in range(2,10):
        for xx in range(2,20):
            for cc in (0,3*ee):
                val=derivative_numerator.subs({e:ee,x:xx,c:cc})
                check(val>0,'endpoint derivative sign')

def graph_enumeration(n,h,H_edges):
    E=list(combinations(range(n),2));N=len(E)
    p={ab:i for i,ab in enumerate(E)}
    h_edges={tuple(sorted(x)) for x in H_edges}
    S=set(range(h))
    all_h=list(combinations(range(h),2))
    target=sum((1<<p[q]) for q in h_edges)
    maskh=sum((1<<p[q]) for q in all_h)
    tri=[sum(1<<p[q] for q in combinations(t,2)) for t in combinations(range(n),3)]
    acc={m:[0,0] for m in range(N+1)}
    for mask in range(1<<N):
        if (mask&maskh)!=target: continue
        m=mask.bit_count()
        a=acc[m];a[0]+=1;a[1]+=sum((mask&t)==t for t in tri)
    e=len(h_edges)
    for m,(num,total) in acc.items():
        if not num:continue
        check(Fraction(total,num)==conditional(n,h,e,m),f'graph exact n={n} h={h} e={e} m={m}')
    return sum(v[0] for v in acc.values())

if __name__=='__main__':
    analytic_checks()
    path3=[(0,1),(1,2)]
    path4=[(0,1),(1,2),(2,3)]
    star4=[(0,1),(0,2),(0,3)]
    cycle4=[(0,1),(1,2),(2,3),(0,3)]
    for n in (5,6):
        for h,es in [(3,path3),(4,path4),(4,star4),(4,cycle4)]:
            if n>h:graph_enumeration(n,h,es)
    for h in range(3,10):
        for n in range(h+3,h+11):
            B=comb(n,2)-comb(h,2)
            for e in range(h-1,h*h//4+1):
                prev=None
                for m in range(e+2,B+e+1):
                    base=baseline(n,m)
                    check(base>0,'positive baseline')
                    curr=conditional(n,h,e,m)/base
                    if prev is not None:check(curr>prev,(n,h,e,m,prev,curr))
                    prev=curr
    print(f'PASS {checks} exact checks: symbolic derivative certificate, explicit graphs, and finite-parameter checks')
