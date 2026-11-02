"""Exact finite checks for a one-shot temporal double-star epidemic theorem.

Run: python temporal_double_star_verify.py
Uses only Python standard library. Computational checks supplement the proof.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial
from collections import Counter

checks=0

def require(cond):
    global checks
    checks+=1
    if not cond:
        raise AssertionError('check '+str(checks))

def calendar_formula(a,b,seq):
    n=a+b+2
    i=seq.index(('B',0))
    x=sum(e[0]=='L' for e in seq[:i]); y=i-x
    m=x*(b-y)+(a-x)*y
    return m, (Fraction(1)+Fraction(2*(a+b+1),n)*Fraction(1,2)
               +Fraction(comb(a,2)+comb(b,2)+a+b,n)*Fraction(1,2)**2
               +Fraction(m,n)*Fraction(1,2)**3)

def graph_edges(a,b):
    # central vertices 0,1; L leaves 2..a+1, R leaves a+2..a+b+1
    return {('B',0):(0,1), **{('L',i):(0,2+i) for i in range(a)},
            **{('R',j):(1,2+a+j) for j in range(b)}}

def simulated_exact_mean(a,b,seq,p,d):
    edges=graph_edges(a,b); n=a+b+2; m=len(seq)
    numerator=0
    for mask in range(1<<m):
        k=mask.bit_count(); weight=p**k*(d-p)**(m-k)
        for seed in range(n):
            infected={seed}
            for pos,e in enumerate(seq):
                if not (mask>>pos)&1: continue
                u,v=edges[e]
                if u in infected and v not in infected: infected.add(v)
                elif v in infected and u not in infected: infected.add(u)
            numerator += len(infected)*weight
    return Fraction(numerator,n*d**m)

def theory_mean(a,b,m,p,d):
    n=a+b+2;q=Fraction(p,d)
    return (Fraction(1)+Fraction(2*(a+b+1),n)*q
            + Fraction(comb(a,2)+comb(b,2)+a+b,n)*q**2
            +Fraction(m,n)*q**3)

for a in range(1,5):
 for b in range(1,5):
    seq0=[('L',i) for i in range(a)]+[('R',i) for i in range(b)]+[('B',0)]
    if a+b<=6:
        calendars=list(permutations(seq0))
    else:
        calendars=[]
        # fixed samples, plus both optimal orderings
        from random import Random
        rng=Random(187*a+29*b)
        for _ in range(70):
            z=list(seq0);rng.shuffle(z);calendars.append(tuple(z))
        calendars.append(tuple(seq0))
        calendars.append((('B',0),)+tuple(seq0[:-1]))
        calendars.append(tuple(seq0[:a])+(('B',0),)+tuple(seq0[a:-1]))
        calendars.append(tuple(seq0[a:-1])+(('B',0),)+tuple(seq0[:a]))
    observed=Counter()
    for seq in calendars:
        M,_=calendar_formula(a,b,seq);observed[M]+=1
        x=seq.index(('B',0));L=sum(e[0]=='L' for e in seq[:x]);R=x-L
        require(M==L*(b-R)+(a-L)*R)
        require(0<=M<=a*b)
        require((M==0)==((L,R) in [(0,0),(a,b)]))
        require((M==a*b)==((L,R) in [(a,0),(0,b)]))
    if a+b<=6:
        assert len(calendars)==factorial(a+b+1)
        weighted=Counter()
        for x in range(a+1):
          for y in range(b+1):
            k=x+y;M=x*(b-y)+(a-x)*y
            weight=comb(a,x)*comb(b,y)*factorial(k)*factorial(a+b-k)
            weighted[M]+=weight
        require(observed==weighted)
        den=len(calendars)
        mean=Fraction(sum(k*v for k,v in observed.items()),den)
        var=Fraction(sum(k*k*v for k,v in observed.items()),den)-mean*mean
        require(mean==Fraction(a*b,3))
        require(var==Fraction(a*b*(a+b+2),18)
                   +Fraction(a*b*(a-1)*(b-1),45))
        require(observed[0]==2*factorial(a+b))
        require(observed[a*b]==2*factorial(a)*factorial(b))
        if a+b<=4:
            for seq in calendars:
                M,_=calendar_formula(a,b,seq)
                for p,d in [(1,2),(2,3)]:
                    require(simulated_exact_mean(a,b,seq,p,d)==theory_mean(a,b,M,p,d))
        else:
            for seq in calendars[:min(12,len(calendars))]:
                M,_=calendar_formula(a,b,seq)
                require(simulated_exact_mean(a,b,seq,2,3)==theory_mean(a,b,M,2,3))
print('VERIFY_OK checks='+str(checks))
