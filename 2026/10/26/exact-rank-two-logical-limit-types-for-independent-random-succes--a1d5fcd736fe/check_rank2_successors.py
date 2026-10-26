#!/usr/bin/env python3
"""Finite checks for rank-two successor profiles (small exhaustive cases)."""
import itertools, math, random, collections

def inspect(paths):
    n=len(paths[0]); r=len(paths)
    sig={x:[] for x in range(n)}
    arc=[]
    for p in paths:
        arc.append({(p[i],p[i+1]) for i in range(n-1)})
    counts={}
    used=[]
    for i in range(r):
        for j in range(i+1,r):
            co=arc[i]&arc[j]
            anti={(u,v) for (u,v) in arc[i] if (v,u) in arc[j]}
            counts[(i,j,'co')]=len(co)
            counts[(i,j,'anti')]=len(anti)
            used += [set(x) for x in co] + [set(x) for x in anti]
    endpoints=[z for p in paths for z in (p[0],p[-1])]
    good=(len(set(endpoints))==len(endpoints)
          and all(not s.intersection(endpoints) for s in used)
          and all(not used[i].intersection(used[j]) for i in range(len(used)) for j in range(i+1,len(used))))
    for a in range(n):
        masks=[]
        for b in range(n):
            if a==b:continue
            mask=0
            for i in range(r):
                if (a,b) in arc[i]:mask|=1<<(2*i)
                if (b,a) in arc[i]:mask|=1<<(2*i+1)
            masks.append(mask)
        sig[a]=tuple(sorted(set(masks)))
    supports=frozenset(sig.values())
    bits=tuple(int(counts[(i,j,orientation)]>0) for i in range(r) for j in range(i+1,r) for orientation in ('co','anti'))
    return counts,good,supports,bits

def expected(r,bits):
    full=set(1<<j for j in range(2*r))
    base={tuple(sorted([0,*full]))}
    for j in range(2*r):
        base.add(tuple(sorted([0,*(full-{1<<j})])))
    k=0
    for i in range(r):
        for j in range(i+1,r):
            if bits[k]:
                for a,b in ((2*i,2*j),(2*i+1,2*j+1)):
                    base.add(tuple(sorted([0,*(full-{1<<a,1<<b}), (1<<a)|(1<<b)])))
            k+=1
            if bits[k]:
                for a,b in ((2*i,2*j+1),(2*i+1,2*j)):
                    base.add(tuple(sorted([0,*(full-{1<<a,1<<b}), (1<<a)|(1<<b)])))
            k+=1
    return frozenset(base)

def main():
    for n in (5,6,7,8,9):
        ref=tuple(range(n)); c=collections.Counter(); patterns=set(); good_count=0
        for p in itertools.permutations(ref):
            counts,good,supports,bits=inspect([ref,p]);co=counts[(0,1,'co')];anti=counts[(0,1,'anti')]
            c[(co,anti)]+=1
            if good and (n>=6+2*sum(counts.values())):
                assert supports==expected(2,bits), (n,p,supports,expected(2,bits))
                good_count+=1; patterns.add(bits)
        total=math.factorial(n)
        mean_co=sum(a*v for (a,b),v in c.items())/total
        mean_anti=sum(b*v for (a,b),v in c.items())/total
        cross=sum(a*b*v for (a,b),v in c.items())/total
        assert abs(mean_co-(n-1)/n)<1e-10
        assert abs(mean_anti-(n-1)/n)<1e-10
        print('EXHAUSTIVE',n,total,'co_mean',round(mean_co,6),'anti_mean',round(mean_anti,6),'cross',round(cross,6),'good',good_count,'bits',sorted(patterns))
    random.seed(712)
    for r in (2,3,4):
        n=150
        for _ in range(500):
            paths=[random.sample(range(n),n) for _ in range(r)]
            counts,good,supports,bits=inspect(paths)
            if good:assert supports==expected(r,bits)
        print('SAMPLED',r,'OK')
    print('RANK2_SUCCESSOR_PROFILES_OK')
if __name__=='__main__':main()
