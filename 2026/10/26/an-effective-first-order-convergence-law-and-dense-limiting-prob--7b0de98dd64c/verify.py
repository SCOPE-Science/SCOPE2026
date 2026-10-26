"""Standalone exact checks for two-involution component formulas.
Requires Python 3 standard library only. All exact tests use integers or Fractions.
"""
from fractions import Fraction
from collections import Counter
from math import factorial

def make_involutions(n):
    p=[-1]*n
    def rec(unused):
        if not unused:
            yield tuple(p)
            return
        a=unused[0]
        p[a]=a
        yield from rec(unused[1:])
        for b in unused[1:]:
            p[a],p[b]=b,a
            yield from rec(tuple(u for u in unused[1:] if u!=b))
        p[a]=-1
    return list(rec(tuple(range(n))))

def components(a,b):
    n=len(a)
    seen=set()
    out=Counter()
    for v in range(n):
        if v in seen: continue
        todo=[v]
        seen.add(v)
        comp=[]
        while todo:
            x=todo.pop(); comp.append(x)
            for y in (a[x],b[x]):
                if y not in seen:
                    seen.add(y);todo.append(y)
        size=len(comp)
        loops=[(x,a[x]==x,b[x]==x) for x in comp if a[x]==x or b[x]==x]
        if not loops:
            assert size%2==0
            out[('cycle',size//2)]+=1
        elif size%2:
            if size==1: assert len(loops)==1 and loops[0][1:]==(True,True)
            else: assert len(loops)==2 and {('a' if q else 'b') for _,q,_ in loops}=={'a','b'}
            out[('path',size)]+=1
        else:
            assert len(loops)==2
            assert all((x+y)==1 for _,x,y in loops)
            color='a' if loops[0][1] else 'b'
            assert all(('a' if q else 'b')==color for _,q,_ in loops)
            out[('path',size,color)]+=1
    return out

def exact_coefficients(nmax):
    coeff=[Fraction(1)]
    for n in range(1,nmax+1):
        c=sum(Fraction(j+1+(j%2))*coeff[n-1-j] for j in range(n))
        coeff.append(c/n)
    return coeff

def main():
    N=7
    coeff=exact_coefficients(N)
    reps=0
    moment_tests=0
    targets=[('path',1),('path',2,'a'),('path',2,'b'),('path',3),('cycle',1),('cycle',2)]
    weights={('path',1):Fraction(1),('path',2,'a'):Fraction(1,2),('path',2,'b'):Fraction(1,2),('path',3):Fraction(1),('cycle',1):Fraction(1,2),('cycle',2):Fraction(1,4)}
    sizes={('path',1):1,('path',2,'a'):2,('path',2,'b'):2,('path',3):3,('cycle',1):2,('cycle',2):4}
    for n in range(0,N+1):
        inv=make_involutions(n)
        assert Fraction(len(inv)**2,factorial(n))==coeff[n]
        counts=Counter()
        for a in inv:
            for b in inv:
                reps+=1
                co=components(a,b)
                for t in targets:
                    counts[(t,1)]+=co[t]
                    counts[(t,2)]+=co[t]*(co[t]-1)
                counts[('cross',0)]+=co[('path',1)]*co[('cycle',1)]
                counts[('cross',1)]+=co[('path',2,'a')]*co[('path',2,'b')]
        den=len(inv)**2
        for t in targets:
            for order in (1,2):
                if order*sizes[t]>n: continue
                expected=weights[t]**order*coeff[n-order*sizes[t]]/coeff[n]
                assert Fraction(counts[(t,order)],den)==expected,(n,t,order,counts[(t,order)],expected)
                moment_tests+=1
        if n>=3:
            expected=weights[('path',1)]*weights[('cycle',1)]*coeff[n-3]/coeff[n]
            assert Fraction(counts[('cross',0)],den)==expected
            moment_tests+=1
        if n>=4:
            expected=Fraction(1,4)*coeff[n-4]/coeff[n]
            assert Fraction(counts[('cross',1)],den)==expected
            moment_tests+=1
    print('TWO_INVOLUTION_COMPONENTS_EXACT_OK',reps,moment_tests, 'last_coefficient',coeff[-1])
if __name__=='__main__':main()
