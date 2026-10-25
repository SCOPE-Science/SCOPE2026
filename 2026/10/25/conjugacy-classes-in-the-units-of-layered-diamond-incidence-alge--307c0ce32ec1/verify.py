#!/usr/bin/env python3
"""Independently verify a finite-field class-number formula by commuting-pair counting.
No external libraries. The full pair loop is used only for small prime fields.
"""
from itertools import product

def make_group(q,b):
    t=list(product(range(1,q),repeat=b+2))
    # D0, Dmiddle_0...middle_(b-1), Dend
    out=[]
    for a in t:
        for w in product(range(q),repeat=2*b+1):
            out.append((a,w))
    return out

def commute(g,h,q,b):
    a,x=g; d,y=h
    for i in range(b):
        if ((a[0]-a[i+1])*y[i]-(d[0]-d[i+1])*x[i])%q: return False
        if ((a[i+1]-a[-1])*y[b+i]-(d[i+1]-d[-1])*x[b+i])%q: return False
    z=(a[0]-a[-1])*y[-1]-(d[0]-d[-1])*x[-1]
    z+=sum(x[i]*y[b+i]-y[i]*x[b+i] for i in range(b))
    return z%q==0

def direct(q,b):
    G=make_group(q,b)
    n=sum(1 for g in G for h in G if commute(g,h,q,b))
    assert n%len(G)==0
    return n//len(G),len(G)

def predicted(q,b):
    return q*(q-2)*(q+1)**b + (2*q)**b+(q-1)**(b+1)

for q,b in [(2,1),(2,2),(2,3),(3,1)]:
    result,size=direct(q,b)
    expected=predicted(q,b)
    assert result==expected, (q,b,result,expected)
    print('DIRECT_OK',q,b,'order',size,'classes',result)

# Independently sum number of commuting additive pairs by linear/quadratic factorization.
def symbolic_commutation_sum(q,b):
    # t,s diagonal tuples; for each pair, the off-diagonal solution count
    # is evaluated using only whether each first superdiagonal equation has zero coefficients.
    all_t=product(range(1,q), repeat=b+2)
    count=0
    for a in all_t:
        for d in product(range(1,q),repeat=b+2):
            equal_outer=(a[0]==a[-1] and d[0]==d[-1])
            if equal_outer:
                k=sum(a[i+1]==a[0] and d[i+1]==d[0] for i in range(b))
                count+=q**(2*b+2*k+1)+(q-1)*q**(2*b+1)
            else:
                exp=sum(4-(int((a[0],d[0])!=(a[i+1],d[i+1])))
                         -(int((a[-1],d[-1])!=(a[i+1],d[i+1]))) for i in range(b))
                count+=q**(exp+1)
    size=(q-1)**(b+2)*q**(2*b+1)
    assert count%size==0
    return count//size

for q,b in [(2,4),(3,2),(3,3),(4,2),(5,1),(5,2)]:
    got=symbolic_commutation_sum(q,b)
    assert got==predicted(q,b),(q,b,got,predicted(q,b))
    print('SUM_OK',q,b,'classes',got)
print('ALL_CHECKS_OK')
