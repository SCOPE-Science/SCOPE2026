#!/usr/bin/env python3
"""Exact rational checks of a priced symmetric Markov-chain mixing frontier.

This is a finite cross-check. The all-size theorem is proved independently
by spectral splitting, symmetry averaging and an analytic linear program.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd

checks=0

def check(q,desc):
    global checks
    assert q, desc
    checks+=1

def eigen(n,a,b):
    s=(n-1)*a+b
    return [F(1),F(1)-2*s,F(1)-n*a,F(1)-(n-2)*a-2*b]

def mu(n,a,b):
    return max(abs(e) for e in eigen(n,a,b)[1:])

def make_P(n,a,b):
    d=F(1)-(n-1)*a-b
    return [[d if i==j else (b if (i<n and j==n+i) or (j<n and i==n+j) else (a if (i<n)!=(j<n) else F(0))) for j in range(2*n)] for i in range(2*n)]

def matvec(P,v):return [sum(u*x for u,x in zip(row,v)) for row in P]

def optimal(n,s,t):
    r=F(1)-s
    tc=F(2*(n-1),n-2)
    sc=F(n,3*n-4)
    if t<tc:
        a=b=r/n
    elif t>tc and s<sc:
        a=2*s/n
        b=(n-(3*n-4)*s)/(2*n)
    elif t>tc:
        a=r/(n-2);b=F(0)
    else:  # at threshold, choose one endpoint of the optimal segment
        a=r/n;b=r/n
    return a,b,n*((n-1)*a+t*b)

def halfplanes(n,s):
    return [(-1,0,F(0)),(0,-1,F(0)),(n-1,1,F(1)),
        (-2*(n-1),-2,s-1),(2*(n-1),2,F(1)+s),
        (-n,0,s-1),(n,0,F(1)+s),
        (-(n-2),-2,s-1),(n-2,2,F(1)+s)]

def vertices(n,s):
    hp=halfplanes(n,s)
    ans=set()
    for (u,v,w),(x,y,z) in combinations(hp,2):
        det=u*y-v*x
        if not det:continue
        a=(w*y-v*z)/det
        b=(u*z-w*x)/det
        if all(U*a+V*b<=W for U,V,W in hp):ans.add((a,b))
    return ans

mu_values=[F(1,3),F(17,50),F(2,5),F(9,20),F(1,2),F(3,5),F(4,5),F(19,20)]
for n in range(3,12):
    tc=F(2*(n-1),n-2)
    ts=[F(1,7),F(1),tc-F(1,10),tc,tc+F(1,10),F(5),F(30)]
    for s in mu_values:
        for t in ts:
            a,b,c=optimal(n,s,t)
            V=vertices(n,s)
            check(bool(V),(n,s,'LP feasible'))
            check((a,b) in V,(n,s,t,'selected LP vertex'))
            check(mu(n,a,b)<=s,(n,s,t,'spectral feasibility'))
            check(c==min(n*((n-1)*x+t*y) for x,y in V),(n,s,t,'LP optimum'))
            if t<tc: check(a==b==(1-s)/n,(n,s,t,'cheap branch'))
            if t>tc:
                check((b==0)==(s>=F(n,3*n-4)),(n,s,t,'matching-active cutoff'))
    for s in mu_values:
        aa,bb,_=optimal(n,s,tc)
        hi=min((F(1)-s)/(n-2),2*s/n)
        for q in [F(0),F(1,3),F(2,3),F(1)]:
            a=aa+(hi-aa)*q
            b=(F(1)-s-(n-2)*a)/2
            check(a>=0 and b>=0 and mu(n,a,b)<=s,(n,s,q,'critical face feasible'))
            check(n*((n-1)*a+tc*b)==n*((n-1)*aa+tc*bb),(n,s,q,'critical constant cost'))

# Independently reconstruct every spectral mode in the concrete 2n-by-2n matrix.
for n in range(3,9):
    for a,b in [(F(1,4*n),F(2,7*n)), (F(2,3*n),F(2,3*n)),(F(1,n),F(0))]:
        P=make_P(n,a,b)
        check(all(all(z>=0 for z in row) and sum(row)==1 for row in P),(n,a,b,'stochastic matrix'))
        basis=[([F(1)]*n+[F(1)]*n,F(1)),
               ([F(1)]*n+[F(-1)]*n,eigen(n,a,b)[1])]
        for i in range(n-1):
            v=[F(0)]*n;v[i]=F(1);v[-1]=F(-1)
            basis += [(v+v,eigen(n,a,b)[2]),(v+[-x for x in v],eigen(n,a,b)[3])]
        for v,e in basis:
            check(matvec(P,v)==[e*x for x in v],(n,a,b,e,'mode'))

# Independently invert the cost-vs-SLEM frontier in the resource-budget form.
for n in range(3,12):
    tc=F(2*(n-1),n-2)
    for t in [F(1), tc, tc+F(1),tc+F(5)]:
        BC=F(2*n*(n-1),3*n-4)
        B0=F(2*(n-1+t),3)
        for k in range(101):
            B=(B0+F(3))*F(k,100)
            if t<=tc:
                s=max(F(1,3), F(1)-B/F(n-1+t))
            elif B<=BC:
                s=F(1)-F(n-2)*B/F(n*(n-1))
            elif B<=B0:
                s=(t*n/F(2)-B)/(t*(3*n-4)/F(2)-2*(n-1))
            else:
                s=F(1,3)
            check(F(1,3)<=s<=F(1),(n,t,B,'budget frontier range'))
            if s<F(1):
                a,b,c=optimal(n,s,t)
                check(c<=B,(n,t,B,'budget frontier attainability'))
                if s>F(1,3):
                    check(c==B,(n,t,B,'budget frontier tightness'))
            else: check(B==0,(n,t,B,'identity case'))

print('VERIFY_OK',checks,'exact rational assertions; n=3..11; full LP vertices, eigenspaces, budget inversion')
