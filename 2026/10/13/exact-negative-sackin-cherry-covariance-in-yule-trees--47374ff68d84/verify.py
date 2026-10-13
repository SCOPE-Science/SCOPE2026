from collections import defaultdict
from fractions import Fraction
from math import factorial

LEAF = None

def canon(t):
    if t is None: return None
    a,b=(canon(t[0]),canon(t[1]))
    return tuple(sorted((a,b),key=repr))

def paths(t,p=()):
    if t is None:
        yield p
    else:
        yield from paths(t[0],p+(0,))
        yield from paths(t[1],p+(1,))

def split_at(t,p):
    if not p:
        assert t is None
        return (None,None)
    return canon((split_at(t[0],p[1:]),t[1]) if p[0]==0 else (t[0],split_at(t[1],p[1:])))

def shape_stats(t):
    s=c=q=0
    def walk(x,d):
        nonlocal s,c,q
        if x is None:
            s+=d
            return
        if x[0] is None and x[1] is None:
            c+=1; q+=2*(d+1)
        walk(x[0],d+1);walk(x[1],d+1)
    walk(t,0)
    return s,c,q

def harmonic(n):
    return sum((Fraction(1,i) for i in range(1,n+1)),Fraction(0))

def theorem(n):
    return -Fraction(n,9)+Fraction(2,3*(n-1)) if n>=3 else Fraction(0)

def main():
    dist={(None,None):Fraction(1)}
    for n in range(2,11):
        assert sum(dist.values())==1
        es=ec=eq=esc=Fraction(0)
        for t,p in dist.items():
            s,c,q=shape_stats(t)
            es+=p*s;ec+=p*c;eq+=p*q;esc+=p*s*c
        cov=esc-es*ec
        assert cov==theorem(n),(n,cov,theorem(n))
        if n>=3:
            assert es==2*n*(harmonic(n)-1)
            assert ec==Fraction(n,3)
            assert eq==Fraction(2*n,3)*(2*harmonic(n)-Fraction(5,3))
        else:assert(es,ec,eq)==(2,1,2)
        print(f'n={n}, shapes={len(dist)}, covariance={cov}, target={theorem(n)}, E[S]={es}, E[C]={ec}, E[Q]={eq}')
        nd=defaultdict(Fraction)
        for t,p in dist.items():
            for path in paths(t):
                nd[canon(split_at(t,path))]+=p/Fraction(n)
        dist=nd
    print('ALL EXACT ENUMERATION CHECKS PASS')
if __name__=='__main__':main()
