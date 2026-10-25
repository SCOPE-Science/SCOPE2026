"""Exact exhaustive verification of three-symbol substring permutation volumes.
No external dependencies.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

PERMS = tuple(permutations(range(3)))

def direct_volume(x):
    n=len(x)
    out={x}
    for i in range(n-2):
        sub=x[i:i+3]
        for p in PERMS:
            out.add(x[:i]+tuple(sub[j] for j in p)+x[i+3:])
    return len(out)

def local_volume(x):
    n=len(x)
    return (1+sum(x[i]!=x[i+1] for i in range(n-1))
              +sum(x[i]!=x[i+2] for i in range(n-2))
              +2*sum(len(set(x[i:i+3]))==3 for i in range(n-2)))

def transfer(q,n):
    # Two states: last two letters equal (0) or unequal (1).
    assert q>=2 and n>=3
    states=[Counter({0:q}),Counter({0:q*(q-1)})]
    for _ in range(n-2):
        new=[Counter(),Counter()]
        for z,c in states[0].items():
            new[0][z]+=c
            new[1][z+1]+=c*(q-1)
        for z,c in states[1].items():
            new[0][z+2]+=c
            new[1][z+1]+=c
            if q>2:
                new[1][z+4]+=c*(q-2)
        states=new
    result=Counter()
    for z,c in states[0].items():result[z+1]+=c
    for z,c in states[1].items():result[z+2]+=c
    return +result

def mean(q,n):
    return Fraction(q-1,q)+1+Fraction(4*(q-1)**2*(n-2),q*q)

def variance(q,n):
    return Fraction((q-1)*(n*(34*q*q-88*q+48)-75*q*q+208*q-128),q**4)

def predicted_top(q,n):
    if q==2:return ((3*n-2)//2, 2 if n%2==0 else n+3)
    return (4*n-6, q*(q-1)*(q-2)**(n-2))

def check(q,n):
    counts=Counter()
    for x in product(range(q),repeat=n):
        v=direct_volume(x)
        if v!=local_volume(x):
            raise AssertionError(('local',q,n,x,v,local_volume(x)))
        counts[v]+=1
    expected=transfer(q,n)
    if counts!=expected:
        raise AssertionError(('spectrum',q,n,counts,expected))
    mean_actual=sum(k*v for k,v in counts.items())
    m=Fraction(mean_actual,q**n)
    v=Fraction(sum(k*k*c for k,c in counts.items()),q**n)-m*m
    if m!=mean(q,n) or v!=variance(q,n):
        raise AssertionError(('moments',q,n,m,v,mean(q,n),variance(q,n)))
    top=max(counts)
    if (top,counts[top])!=predicted_top(q,n):
        raise AssertionError(('max',q,n,top,counts[top],predicted_top(q,n)))
    if counts[1]!=q:
        raise AssertionError(('minimum',q,n,counts[1]))
    return q**n,len(counts),top,counts[top]

if __name__=='__main__':
    examined=0; cases=0
    for q,mx in [(2,12),(3,10),(4,8),(5,7),(6,6)]:
        for n in range(3,mx+1):
            words,bins,top,multiplicity=check(q,n)
            examined+=words;cases+=1
            print('q=%d n=%d words=%d bins=%d max=%d max_count=%d' % (q,n,words,bins,top,multiplicity))
    print('TOTAL cases=%d distinct_input_words=%d' % (cases,examined))
    print('VERIFY_OK')
