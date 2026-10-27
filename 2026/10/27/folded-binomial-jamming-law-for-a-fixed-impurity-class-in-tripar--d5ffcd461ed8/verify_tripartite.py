"""Independent finite-state verification of the dimer jamming law.

Python >=3.9, standard library only.
"""
from functools import lru_cache
from fractions import Fraction
from math import comb, factorial, log

@lru_cache(None)
def size_law(a,b,c):
    """Exact law by aggregated empty-part counts."""
    W=a*b+a*c+b*c
    if not W:
        return {a+b+c: Fraction(1)}
    out={}
    for aa,bb,cc,w in ((a-1,b-1,c,a*b),(a-1,b,c-1,a*c),(a,b-1,c-1,b*c)):
        if not w: continue
        sub=size_law(*sorted((aa,bb,cc)))
        for k,v in sub.items():out[k]=out.get(k,Fraction(0))+Fraction(w,W)*v
    return out

@lru_cache(None)
def bitmask_law(mask,edges):
    """Exact separate vertex-level recursion on graph edges and free vertex mask."""
    present=[(u,v) for u,v in edges if (mask&(1<<u)) and (mask&(1<<v))]
    if not present:return {mask.bit_count():Fraction(1)}
    w=Fraction(1,len(present)); out={}
    for u,v in present:
        sub=bitmask_law(mask^(1<<u)^(1<<v),edges)
        for k,p in sub.items():out[k]=out.get(k,Fraction(0))+w*p
    return out

def independent_law(n,r):
    edges=tuple((i,j) for i in range(2*n+r) for j in range(i+1,2*n+r)
        if (i//n if i<2*n else 2)!=(j//n if j<2*n else 2))
    return bitmask_law((1<<(2*n+r))-1,edges)

def limit_law(r):
    d={}
    for k in range(r+1):
        u=abs(2*k-r)
        d[u]=d.get(u,Fraction(0))+Fraction(comb(r,k),2**r)
    return d

def tv(p,q):
    return sum((abs(p.get(x,0)-q.get(x,0)) for x in (set(p)|set(q))),Fraction(0))/2

def bound(n,r):
    # Upper bound derived from marked-particle survival and fair-coin coupling.
    H=sum(Fraction(1,j) for j in range(1,n+1))
    return (Fraction(r*r,2)*(Fraction(1,n)+
        (n+2*H)/((n+1)*(n+2)))+
        Fraction(r*(r+2)*(r+3),(n+1)*(n+2)))

def run():
    count=0
    # Independent exact graph-level vs exchangeability lumping, finite state.
    for n,r in ((2,2),(2,3),(3,2),(3,3),(4,2),(4,3)):
        x=size_law(*sorted((n,n,r)))
        y=independent_law(n,r)
        assert x==y,(n,r,x,y)
        assert sum(x.values())==1
        count+=2
    # General structural parity/support, exact arithmetic.
    for r in range(2,7):
        q=limit_law(r)
        assert sum(q.values())==1
        for n in (2*r+2,3*r+3,5*r+8,12*r+12):
            p=size_law(*sorted((n,n,r)))
            assert sum(p.values())==1
            assert set(p).issubset(set(q))
            assert tv(p,q)<=bound(n,r),(n,r,float(tv(p,q)),float(bound(n,r)))
            count+=4
    # Exact exponent for minority-group survival in the single-marked model.
    for n in range(1,15):
        ratio=Fraction(1)
        for j in range(n,0,-1):ratio*=Fraction(j,j+2)
        assert ratio==Fraction(2,(n+1)*(n+2))
        count+=1
    # Convergence values, plus nonvanishing limits for r=2 and r=3.
    for n in (30,100,300):
        for r in (2,3,4):
            p=size_law(*sorted((n,n,r)))
            e=float(tv(p,limit_law(r)))
            assert e<=float(bound(n,r))
            count+=1
    assert limit_law(2)=={0:Fraction(1,2),2:Fraction(1,2)}
    assert limit_law(3)=={1:Fraction(3,4),3:Fraction(1,4)}
    count+=2
    print('PASS',count,'independent finite-state, rational, limit-support, and bound checks')
    for r in (2,3,4):
        p=size_law(*sorted((100,100,r)))
        print('n=100,r=',r,'law:',{k:round(float(v),8) for k,v in sorted(p.items())},
             'limit:',{k:float(v) for k,v in sorted(limit_law(r).items())},
             'TV:',round(float(tv(p,limit_law(r))),8))
if __name__=='__main__':run()
