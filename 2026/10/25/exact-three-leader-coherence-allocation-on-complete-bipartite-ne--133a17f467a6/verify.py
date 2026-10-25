#!/usr/bin/env python3
"""Exact checks for the three-leader complete-bipartite coherence classification.

Requires Python 3 and SymPy >= 1.12. Run: python verify.py
The symbolic inequalities are also proved directly in RESULT.md;
finite enumerations below are independent consistency tests, not an infinite proof.
"""
from fractions import Fraction
from itertools import combinations
import sympy as sp

p,q=sp.symbols('p q',integer=True,positive=True)
def Jsym(a):
    b=3-a;u=p-a;v=q-b
    return (u-1)/q+(v-1)/p+(p+q)/(p*q-u*v)

def check_identities():
    expected={
       (1,2):(p-2)*(q-p)*(q-2)*(p+q-1)/(p*q*(p+2*q-2)*(2*p+q-2)),
       (0,3):(q-p)*(p+q-9)/(3*p*q),
       (3,2):((6-p)*q*q-(5*p+6)*q+p*(p-2)*(p-3))/(3*p*q*(p+2*q-2)),
       (0,1):(q-6)*(q-1)/(6*q),
    }
    for pair, formula in expected.items():
        got=Jsym(pair[0])-Jsym(pair[1]); d=got-formula
        if pair==(0,1): d=d.subs(p,2)
        assert sp.cancel(d)==0,pair
    k=sp.symbols('k',integer=True,nonnegative=True)
    P=(6-p)*q*q-(5*p+6)*q+p*(p-2)*(p-3)
    assert sp.expand(P.subs(q,p+k)-((6-p)*k*k+(-2*p*p+7*p-6)*k-4*p*p))==0
    return len(expected)+1

def cost(P,Q,a):
    b=3-a;u=P-a;v=Q-b
    assert 0<=a<=P and 0<=b<=Q and P+Q>=4
    return Fraction(u-1,Q)+Fraction(v-1,P)+Fraction(P+Q,P*Q-u*v)

def prediction(P,Q):
    assert 2<=P<=Q
    if P==2:
        if Q==2:return {1,2}
        if Q<6:return {0}
        if Q==6:return {0,1,2}
        return {1,2}
    if P==3:
        if Q==3:return {0,3}
        if Q<=5:return {0}
        if Q==6:return {0,3}
        if Q==7:return {2,3}
        return {2}
    if P==4:
        if Q<=5:return {0,3}
        if Q<=12:return {3}
        return {2}
    if P==5:
        if Q==5:return {0,3}
        if Q<=29:return {3}
        if Q==30:return {2,3}
        return {2}
    if Q==P:return {0,3}
    return {3}

def check_phase():
    count=0
    for P in range(2,62):
        for Q in range(P, max(P+200,300)+1):
            costs={a:cost(P,Q,a) for a in range(4) if a<=P and 3-a<=Q}
            mv=min(costs.values());best={a for a,z in costs.items() if z==mv}
            assert best==prediction(P,Q),(P,Q,best,prediction(P,Q))
            count+=1
    return count

def trace_inverse(a):
    # Exact Gauss-Jordan elimination over rationals.
    n=len(a); m=[[Fraction(v) for v in row]+[Fraction(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for i in range(n):
        j=next(j for j in range(i,n) if m[j][i]!=0)
        m[i],m[j]=m[j],m[i]
        z=m[i][i];m[i]=[x/z for x in m[i]]
        for j in range(n):
            if j!=i:
                z=m[j][i]
                if z:m[j]=[m[j][k]-z*m[i][k] for k in range(2*n)]
    return sum(m[i][n+i] for i in range(n))

def check_dense():
    tested=0
    for P in range(2,6):
        for Q in range(P, min(P+4,8)+1):
            n=P+Q
            L=[[0]*n for _ in range(n)]
            for i in range(P):
                for j in range(P,n):
                    L[i][i]+=1;L[j][j]+=1;L[i][j]=-1;L[j][i]=-1
            for leaders in combinations(range(n),3):
                followers=[v for v in range(n) if v not in leaders]
                B=[[L[i][j] for j in followers] for i in followers]
                val=trace_inverse(B)
                a=sum(i<P for i in leaders)
                assert val==cost(P,Q,a),(P,Q,leaders,val,cost(P,Q,a))
                tested+=1
    return tested

if __name__=='__main__':
    ids=check_identities();ph=check_phase();dense=check_dense()
    print('VERIFY_OK symbolic_identities=%d exact_phase_cases=%d dense_grounded_inverse_cases=%d'%(ids,ph,dense))
