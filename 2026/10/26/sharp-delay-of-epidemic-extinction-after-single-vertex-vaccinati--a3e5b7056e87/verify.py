"""Exact checks for a five-node Reed-Frost vaccination-duration bound.
This script uses only the Python standard library.
"""
from collections import deque
from fractions import Fraction
from math import comb

# vertices s=0,v=1,a=2,b=3,t=4
ARCS = [(0,1),(0,2),(1,3),(1,4),(2,3),(3,4)]

def horizon(n, arcs, vaccinated=None):
    seen={0}; active={0}; time=0
    while active:
        next_active={b for a,b in arcs if a in active and b not in seen
                     and b != vaccinated and a != vaccinated}
        if not next_active: break
        seen.update(next_active); active=next_active; time+=1
    return time

def graph(n):
    assert n>=5
    arcs=[(0,1),(0,2)]
    arcs.extend((i,i+1) for i in range(2,n-1))
    arcs.extend((1,i) for i in range(3,n))
    return arcs

def poly_add(a,b):
    r=[0]*max(len(a),len(b))
    for i,x in enumerate(a):r[i]+=x
    for i,x in enumerate(b):r[i]+=x
    return r

def polynomial_from_full_enumeration():
    m=len(ARCS); answer=[0]*(m+1)
    for mask in range(1<<m):
        arcs=[e for i,e in enumerate(ARCS) if mask & (1<<i)]
        delta=horizon(5,arcs,1)-horizon(5,arcs)
        k=mask.bit_count()
        # p**k * (1-p)**(m-k)
        for j in range(m-k+1):
            answer[k+j]+=delta*comb(m-k,j)*(-1)**j
    return answer

if __name__=='__main__':
    assert polynomial_from_full_enumeration()==[0,-1,-1,0,3,1,-1]
    for n in range(5,61):
        a=graph(n)
        assert horizon(n,a)==2
        assert horizon(n,a,1)==n-2
    # Bound exact for all n<=4 and all directed graphs (including all possible nonloops).
    for n in range(2,5):
        pairs=[(a,b) for a in range(n) for b in range(n) if a!=b]
        for mask in range(1<<len(pairs)):
            arcs=[e for i,e in enumerate(pairs) if mask>>i&1]
            for v in range(1,n):
                assert horizon(n,arcs,v)<=horizon(n,arcs)
    Q=lambda x:x**5-x**4-3*x**3+x+1
    lo=Fraction(83659,100000); hi=Fraction(83660,100000)
    assert Q(lo)>0 and Q(hi)<0
    for k in range(1,1000):
        p=Fraction(k,1000)
        EV=p+p*p+p**3
        E0=2*p+2*p*p+p**3-3*p**4-p**5+p**6
        poly=sum(Fraction(c)*p**i for i,c in enumerate(polynomial_from_full_enumeration()))
        assert EV-E0==poly
    print('PASS: full 64-live-edge exact polynomial; every directed graph <=4 vertices;')
    print('       sharp n-vertex constructions n=5..60; 999 rational expectation checks;')
    print('       critical root strictly between',float(lo),'and',float(hi))
