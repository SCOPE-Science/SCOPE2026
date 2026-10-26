"""Independent small-graph check of the chip-firing period-two orbit census."""
from itertools import product
from math import comb, prod, factorial
from fractions import Fraction

def closed_count(a,b):
    base=(a**b)*(b**a)
    s=sum((Fraction(prod(range(a-k+1,a+1)) if k else 1,a**k) * Fraction(prod(range(b-k+1,b+1)) if k else 1,b**k)) for k in range(min(a,b)+1))
    return base*s/2

def phase_sum(a,b):
    acc=0
    for p in range(a+1):
        for q in range(b+1):
            x=(b-q)**p * q**(a-p) * (a-p)**q *p**(b-q)
            acc+=comb(a,p)*comb(b,q)*x
    return acc//2

def direct_count(a,b):
    d=[b]*a+[a]*b
    edges=[tuple(range(a,a+b))]*a+[tuple(range(a))]*b
    periodic=0
    for state in product(*(range(2*x) for x in d)):
        fire=[int(state[i]>=d[i]) for i in range(a+b)]
        nxt=tuple(state[i]-d[i]*fire[i]+sum(fire[j] for j in edges[i]) for i in range(a+b))
        fire2=[int(nxt[i]>=d[i]) for i in range(a+b)]
        nxt2=tuple(nxt[i]-d[i]*fire2[i]+sum(fire2[j] for j in edges[i]) for i in range(a+b))
        if state==nxt2 and state!=nxt:
            periodic+=1
    return periodic//2

def main():
    nstates=0
    for a,b in [(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4)]:
        x=closed_count(a,b);y=phase_sum(a,b);z=direct_count(a,b)
        assert x.denominator==1 and x==y==z,(a,b,x,y,z)
        nstates+=(2*b)**a*(2*a)**b
        print(f'a={a}, b={b}, orbits={x}, phase={y}, exhaustive={z}')
    for a in range(1,12):
        for b in range(1,12):
            assert phase_sum(a,b)==closed_count(a,b),(a,b)
    print('Exhaustively simulated configurations:',nstates)
    print('Closed vs phase formula parameter pairs:',11*11)
    print('BICLIQUE_TWO_CYCLE_EXACT_VERIFY_OK')
if __name__=='__main__':main()
