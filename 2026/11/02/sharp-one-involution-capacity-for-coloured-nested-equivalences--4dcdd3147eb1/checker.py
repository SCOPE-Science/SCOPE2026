"""Exact small-carrier verification of colour-preserving nested-partition symmetries."""
from collections import Counter
from itertools import product, permutations
from math import factorial


def parts(seq):
    seq=tuple(seq)
    if not seq:
        yield ()
        return
    x=seq[0]
    for rest in parts(seq[1:]):
        yield (frozenset((x,)),)+rest
        for i in range(len(rest)):
            new=list(rest)
            new[i]=rest[i]|frozenset((x,))
            yield tuple(new)


def refine_sequences(n, k):
    # Each entry is a partition into E_i classes, with E_i contained in E_(i+1).
    def ext(lower, remaining):
        if remaining==0:
            yield (lower,)
            return
        blocks=tuple(range(len(lower)))
        for p in parts(blocks):
            upper=tuple(frozenset().union(*(lower[j] for j in b)) for b in p)
            for tail in ext(upper,remaining-1):
                yield (lower,)+tail
    for p in parts(range(n)):
        yield from ext(p,k-1)


def signature(colors, layers):
    old={frozenset((i,)): (colors[i],) for i in range(len(colors))}
    for partition in layers:
        new={}
        for b in partition:
            children=[v for s,v in old.items() if s<=b]
            new[b]=tuple(sorted(children))
        old=new
    return tuple(sorted(old.values()))


def automorphisms(colors, layers):
    n=len(colors)
    same=[{(min(a,b),max(a,b)): any(a in block and b in block for block in layer)
           for a in range(n) for b in range(a,n)} for layer in layers]
    count=0
    for p in permutations(range(n)):
        if any(colors[i]!=colors[p[i]] for i in range(n)):continue
        if all(all(L[(a,b)]==L[(min(p[a],p[b]),max(p[a],p[b]))]
                   for a,b in L) for L in same):
            count+=1
    return count


def mul(a,b):
    r=Counter()
    for i,x in a.items():
        for j,y in b.items():r[i+j]+=x*y
    return +r


def R_T_step(R,T):
    f=Counter({0:1})
    for w,c in R.items():
        for _ in range(c): f=mul(f,Counter({0:1,w:1}))
    nr=+Counter({n:c for n,c in f.items() if n>0})
    nt=mul(f,T)
    for w,c in R.items():
        rem=Counter({0:1})
        for u,d in R.items():
            for _ in range(d-(u==w)):rem=mul(rem,Counter({0:1,u:1}))
        nt+=mul(rem,Counter({2*w:c}))
    return nr,+nt


def predicted(q,k):
    R,T=Counter({1:q}),Counter()
    for _ in range(k+1): R,T=R_T_step(R,T)
    return R,T


def finite_check(q,k,max_n):
    R,T=predicted(q,k)
    for n in range(1,max_n+1):
        groups={1:set(),2:set()}
        labelled=Counter()
        for layers in refine_sequences(n,k):
            for colors in product(range(q),repeat=n):
                order=automorphisms(colors,layers)
                if order in (1,2):
                    key=signature(colors,layers)
                    groups[order].add(key)
                    labelled[order]+=1
        for order,poly in [(1,R),(2,T)]:
            expected=poly.get(n,0)
            assert len(groups[order])==expected, (q,k,n,order,len(groups[order]),expected)
            assert labelled[order]==factorial(n)//order*expected,(q,k,n,order,labelled[order],factorial(n)//order*expected)
    return True


def main():
    for q,k,n in [(1,1,5),(1,2,5),(2,1,5),(2,2,4),(3,1,4)]:
        assert finite_check(q,k,n)
        print('VERIFIED',q,k,n)
    for q in range(1,4):
        for k in range(0,3):
            R,T=predicted(q,k)
            if q==3 and k==2:continue
            print('POLYNOMIAL',q,k,'rigid',sorted(R.items())[:15], 'order2',sorted(T.items())[:15],
                  'counts',sum(R.values()),sum(T.values()),'caps',max(R),max(T))
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()
