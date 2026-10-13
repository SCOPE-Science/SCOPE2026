#!/usr/bin/env python3
"""Finite S4.3-chain modal generator census: standalone reproducibility checks.
No third-party dependencies. Run: python VERIFY.py
"""
from itertools import product
from math import comb, factorial, ceil, log2
from random import Random


def binom(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def prediction(sizes,colors):
    o=0; sets=[]
    for a in sizes:
        p=colors[o:o+a];o+=a
        if len(set(p)) != a:return False
        sets.append(set(p))
    return all(not sets[i].issubset(sets[i+1]) for i in range(len(sets)-1))


def modal_full(sizes,colors):
    """Compute the coarsest finite bisimulation partition by modal refinement."""
    n=sum(sizes)
    level=[j for j,a in enumerate(sizes) for _ in range(a)]
    sig=tuple(colors)
    for _ in range(n+2):
        rows=[]
        for x in range(n):
            reachable={sig[y] for y in range(n) if level[y] >= level[x]}
            rows.append((colors[x],tuple(sorted(reachable))))
        codes={x:j for j,x in enumerate(sorted(set(rows)))}
        nxt=tuple(codes[z] for z in rows)
        if len(set(nxt))==n:return True
        if all((sig[i]==sig[j])==(nxt[i]==nxt[j])
               for i in range(n) for j in range(n)):
            return False
        sig=nxt
    raise AssertionError('refinement did not stabilize')


def count_formula(sizes,q):
    a=list(sizes)
    return (factorial_product(a)*binom(q,a[-1]) *
            int_product(binom(q,a[i])-binom(a[i+1],a[i])
                        for i in range(len(a)-1)))


def factorial_product(vals):
    ans=1
    for a in vals:ans*=factorial(a)
    return ans


def int_product(vals):
    ans=1
    for a in vals:ans*=a
    return ans


def min_q(sizes):
    need=max(sizes)
    for a,b in zip(sizes,sizes[1:]):
        if a<=b:need=max(need,b+1)
    return need


def explicit_tail_check(sizes,colors):
    """Independently evaluate the displayed modal tail formulas as subsets."""
    if not prediction(sizes,colors):return
    n=sum(sizes)
    offsets=[0]
    for a in sizes:offsets.append(offsets[-1]+a)
    reach=[{j for j in range(n) if next(i for i in range(len(sizes)) if offsets[i]<=j<offsets[i+1])
                             >= next(i for i in range(len(sizes)) if offsets[i]<=x<offsets[i+1])}
           for x in range(n)]
    tails=[set() for _ in range(len(sizes)+2)]
    for i in range(len(sizes)-2,-1,-1):
        S_i=set(colors[offsets[i]:offsets[i+1]])
        S_next=set(colors[offsets[i+1]:offsets[i+2]])
        color=next(iter(S_i-S_next))
        guard={v for v in range(n) if colors[v]==color and v not in tails[i+2]}
        tails[i+1]={v for v in range(n) if not (reach[v]&guard)}
        want=set(range(offsets[i+1],n))
        assert tails[i+1]==want,(sizes,colors,i,tails[i+1],want)


def modal_closure(sizes,colors,q):
    """Explicitly generate the Boolean powerset algebra and modal images."""
    n=sum(sizes)
    block=[]
    for i,a in enumerate(sizes):block += [i]*a
    full=(1<<n)-1
    known={0,full}
    for a in range(q):
        known.add(sum((1<<i) for i,c in enumerate(colors) if c==a))
    while True:
        before=len(known)
        more=set(known)
        for x in known:
            more.add(x^full)
            # x is the characteristic set. Diamond(x) true at levels <= max occupied level.
            highest=max((block[i] for i in range(n) if (x>>i)&1),default=-1)
            more.add(sum(1<<i for i in range(n) if block[i]<=highest))
        if len(more) != len(known):known=more;continue
        # closure for unions and intersections on current finite family
        for x in known:
            for y in known:
                more.add(x|y)
        if len(more) == before:
            return len(known)==(1<<n)
        known=more


def main():
    checked=0; formulas=0; censuses=0; closures=0; ranks=0
    rng=Random(20261010)
    for h in range(1,5):
        for sizes in product(range(1,4),repeat=h):
            n=sum(sizes)
            for q in (1,2,3,4):
                if q**n>36000:continue
                actual=0
                for colors in product(range(q),repeat=n):
                    b=prediction(sizes,colors)
                    assert modal_full(sizes,colors)==b,(sizes,q,colors)
                    actual+=b;checked+=1
                    if b and (checked%17 ==0):
                        explicit_tail_check(sizes,colors)
                        formulas+=1
                    if (n<=6 and checked%19==0):
                        assert modal_closure(sizes,colors,q)==b,(sizes,q,colors)
                        closures+=1
                assert actual==count_formula(sizes,q),(sizes,q,actual,count_formula(sizes,q))
                censuses+=1
                assert (actual>0)==(q>=min_q(sizes))
                ranks+=1
    for _ in range(1500):
        h=rng.randrange(1,13)
        sizes=tuple(rng.randint(1,5) for _ in range(h))
        q=rng.randint(1,8)
        colors=tuple(rng.randrange(q) for _ in range(sum(sizes)))
        assert modal_full(sizes,colors)==prediction(sizes,colors),(sizes,colors)
        checked+=1
        if prediction(sizes,colors):explicit_tail_check(sizes,colors);formulas+=1
    print('VERIFY_OK exhaustive_bisimulation_labelings',checked,
          'independent_complete_censuses',censuses,
          'direct_modal_algebra_closures',closures,
          'constructive_tail_formula_checks',formulas,
          'rank_feasibility_checks',ranks)
    for sizes in [(1,),(1,1),(1,1,1),(2,2),(2,1,2),(3,2,1),(2,3,2),(3,3,3)]:
        print('EXAMPLE',sizes,'qmin',min_q(sizes),'N(q=4)',count_formula(sizes,4))

if __name__=='__main__':main()
