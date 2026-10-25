"""Exact checks for shortest-path distance tomography on positive-length metric stars."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
from random import Random


def density(x, arms):
    arms = [F(a) for a in arms]
    L=sum(arms)
    plus=lambda a: max(F(0),a)
    u=2*sum(plus(a-x) for a in arms)
    for a,b in combinations(arms,2):
        u+=2*(plus(x)-plus(x-a)-plus(x-b)+plus(x-a-b))
    return u/(L*L)


def singularities(arms):
    k=len(arms); v=defaultdict(int)
    for a in arms: v[a]+=4-2*k
    for a,b in combinations(arms,2):v[a+b]+=2
    return {p:c for p,c in v.items() if c}


def reconstruct(jumps,k):
    if k<3:raise ValueError('at least three arms needed')
    coef=4-2*k
    rem=defaultdict(int,jumps)
    found=[]
    while len(found)<k:
        candidates=[x for x,v in rem.items() if v]
        if not candidates: raise AssertionError('missing arm')
        a=min(candidates); c=rem[a]
        if c>=0 or c%coef !=0: raise AssertionError(('bad next jump',a,c))
        multiplicity=c//coef
        if multiplicity<1 or multiplicity+len(found)>k:
            raise AssertionError(('bad multiplicity',a,multiplicity))
        rem[a]-=coef*multiplicity
        for z in found:rem[a+z]-=2*multiplicity
        rem[2*a]-= multiplicity*(multiplicity-1)
        found += [a]*multiplicity
    if any(rem.values()):raise AssertionError(('nonzero remaining',dict(rem)))
    return found


def positive_pdf_integral(arms):
    p=sorted({F(0)}|set(arms)|{a+b for a,b in combinations(arms,2)})
    integral=F(0)
    for a,b in zip(p,p[1:]):integral+=(density(a,arms)+density(b,arms))*(b-a)/2
    return integral


def exact_tests():
    samples=[(F(1),F(2),F(3)),(F(1),)*3,(F(1),F(1),F(2),F(3)),
      (F(1),F(1),F(2),F(2),F(3),F(4),F(5),F(6)),
      (F(1),)*9+(F(2),), (F(1),F(2),F(3),F(4),F(5),F(6),F(7),F(8)),
      (F(1,2),F(2,3),F(5,6),F(7,6),F(2)),
      (F(1),F(2),F(2),F(3),F(3),F(4),F(4),F(5),F(5)),]
    rng=Random(18471)
    for k in range(3,15):
        for _ in range(30): samples.append(tuple(F(rng.randint(1,11),rng.randint(1,7)) for j in range(k)))
    for arms in samples:
        r=reconstruct(singularities(arms),len(arms))
        assert r==sorted(arms),(arms,r)
        assert positive_pdf_integral(arms)==1,(arms,positive_pdf_integral(arms))
        L=sum(arms); k=len(arms)
        assert density(F(0),arms)==2/L
        mm=min(arms)
        assert (density(mm/2,arms)-density(F(0),arms))/(mm/2)==F(k*(k-3),L*L)
    print('exact distributions/inversion/integrals/small-distance slopes: PASS on',len(samples),'stars')
    # Check coincident jumps can be positive at an unknown arm after adding pair sums.
    special = [F(1)]*9 + [F(2)]
    print('coincidence example: signed atom at length 2:',singularities(special)[F(2)],'reconstruction:',reconstruct(singularities(special),10))


def stochastic_checks():
    rng=Random(29611)
    for arms in ([1.,2.,3.], [1.,1.,1.], [1.,1.,2.,4.,5.], [.3,.75,1.9,3.9]):
        k=len(arms); L=sum(arms)
        grid=[L*j/30 for j in range(31)]
        # exact cdf from formula, integrated piecewise
        breaks=sorted(set([0]+arms+[a+b for a,b in combinations(arms,2)]))
        def cdf(x):
            xs=[0]+[u for u in breaks if 0<u<x]+[x]
            return sum((float(density(F(str(v)), arms))+float(density(F(str(w)),arms)))*(w-v)/2 for v,w in zip(xs,xs[1:]))
        counts=[0]*len(grid)
        for _ in range(100000):
            a=rng.choices(range(k),weights=arms)[0]; b=rng.choices(range(k),weights=arms)[0]
            u=rng.random()*arms[a]; v=rng.random()*arms[b]
            dist=abs(u-v) if a==b else u+v
            for j,t in enumerate(grid):
                if dist<=t:counts[j]+=1
        err=max(abs(c/100000-cdf(x)) for c,x in zip(counts,grid))
        print('Monte Carlo',arms,'max CDF error',round(err,5))
        assert err<.015

if __name__=='__main__':
    exact_tests()
    stochastic_checks()
