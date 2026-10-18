"""Exact finite checks for terminal sibling pairs in a uniform recursive tree.

Python 3 standard library only. This is a corroborating finite computation,
not a substitute for the proof for unbounded tree size.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import factorial, comb

checks=0

def check(flag, msg):
    global checks
    assert flag, msg
    checks += 1


def stats(parents):
    n=len(parents)+1
    child_count=[0]*(n+1)
    for i,parent in enumerate(parents,2):
        child_count[parent]+=1
    leaf=[False]*(n+1)
    for i in range(2,n+1):
        leaf[i]=(child_count[i]==0)
    L=sum(leaf)
    leaf_children=[0]*(n+1)
    for i,parent in enumerate(parents,2):
        if leaf[i]:
            leaf_children[parent]+=1
    C=sum(comb(a,2) for a in leaf_children)
    pairs={(i,j) for i in range(2,n+1) for j in range(i+1,n+1)
           if leaf[i] and leaf[j] and parents[i-2]==parents[j-2]}
    check(C==len(pairs), ('pair definition',n,parents))
    return L,C,pairs

for n in range(2,9):
    denom=factorial(n-1)
    sL=sL2=sC=sLC=0
    pair_freq=defaultdict(int)
    for parents in product(*(range(1,j) for j in range(2,n+1))):
        L,C,pairs=stats(parents)
        sL+=L;sL2+=L*L;sC+=C;sLC+=L*C
        for pair in pairs:pair_freq[pair]+=1
    EL=Q(sL,denom);EL2=Q(sL2,denom)
    EC=Q(sC,denom);ELC=Q(sLC,denom)
    check(EL==Q(n,2),('mean leaves',n,EL))
    if n>=3:
        check(EL2-EL**2==Q(n,12),('var leaves',n))
        check(EC==Q(n,6),('mean pairs',n,EC))
        for i in range(2,n):
            for j in range(i+1,n+1):
                check(Q(pair_freq[(i,j)],denom)==Q(i-1,(n-1)*(n-2)),('pair age',n,i,j))
    else:check(EC==0,('initial C',n))
    if n>=4:
        check(ELC==Q(n*n,12)+Q(n,8),('mixed moment',n,ELC))
        check(ELC-EL*EC==Q(n,8),('covariance',n))
        check((ELC-EL*EC)/(EL2-EL**2)==Q(3,2),('regression',n))
    if n==3:
        check(ELC-EL*EC==Q(1,4),('small boundary',n))

# Check the exact one-step moment recurrences and claimed closed forms
# for a large consecutive range of indices, independent of enumeration.
mL=Q(1);mL2=Q(1);mC=Q(0);mLC=Q(0)
for n in range(2,150):
    lnext=mL+1-mL/Q(n)
    l2next=(1-Q(2,n))*mL2+(2-Q(1,n))*mL+1
    cnext=(1-Q(2,n))*mC+mL/Q(n)
    lcnext=(1-Q(3,n))*mLC+mC+(mL2+mL)/Q(n)
    mL,mL2,mC,mLC=lnext,l2next,cnext,lcnext
    k=n+1
    check(mL==Q(k,2),('mean recurrence',k))
    check(mL2-mL*mL==Q(k,12),('variance recurrence',k))
    check(mC==Q(k,6),('pair recurrence',k))
    if k>=4:check(mLC-mL*mC==Q(k,8),('mixed recurrence',k))

print(f'PASS: {checks} independently recomputed exact rational assertions')
