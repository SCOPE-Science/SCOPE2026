#!/usr/bin/env python3
"""Independent finite checks of an incomparability-sensitive one-type bound."""
from itertools import combinations, product
from collections import Counter


def all_posets(n):
    pairs=list(combinations(range(n),2))
    for choices in product((0,1,2),repeat=len(pairs)):
        relation=set()
        for (a,b),value in zip(pairs,choices):
            if value==1:relation.add((a,b))
            elif value==2:relation.add((b,a))
        if any((a,c) not in relation for a,b in relation for z,c in relation if b==z):
            continue
        yield relation


def ideals(n,R):
    return [s for s in range(1<<n) if all((not (s>>v&1)) or (s>>u&1) for u,v in R)]


def filters(n,R):
    return [s for s in range(1<<n) if all((not (s>>u&1)) or (s>>v&1) for u,v in R)]


def is_union_of_at_most_two_chains(n,R):
    components=[]
    remaining=set(range(n))
    while remaining:
        root=next(iter(remaining)); todo=[root]; cc={root}; remaining.remove(root)
        while todo:
            u=todo.pop()
            for a,b in R:
                if a==u and b in remaining: remaining.remove(b);cc.add(b);todo.append(b)
                if b==u and a in remaining: remaining.remove(a);cc.add(a);todo.append(a)
        components.append(cc)
    return len(components)<=2 and all(all((a,b) in R or (b,a) in R for a,b in combinations(sorted(cc),2)) for cc in components)


def inspect(n,R):
    I=ideals(n,R);F=filters(n,R)
    mixed=0
    for L in I:
        if not L:continue
        for U in F:
            if not U or L&U:continue
            if all((a,b) in R for a in range(n) if L>>a&1 for b in range(n) if U>>b&1):mixed+=1
    c=len(R);j=n*(n-1)//2-c;t=2*len(I)-1+mixed
    lower=(n+1)*(n+2)//2+j
    assert t>=lower,(n,R,t,lower)
    assert mixed>=c,(n,R,mixed,c)
    assert len(I)>=n+1+j,(n,R,len(I),n+1+j)
    assert t-lower==2*(len(I)-(n+1+j))+(mixed-c)
    assert (t==lower)==is_union_of_at_most_two_chains(n,R),(n,R,t,lower)
    return (n,t,lower,t==lower)


def main():
    examined=Counter();equality=Counter()
    for n in range(6):
        for relation in all_posets(n):
            _,_,_,sat=inspect(n,relation)
            examined[n]+=1;equality[n]+=bool(sat)
    print('EXHAUSTIVE_NATURALLY_LABELED_POSETS',dict(examined))
    print('EQUALITY_INSTANCES',dict(equality))
    print('NONNEGATIVE_TWO_TERM_DEFECT',sum(examined.values()))
    print('EXACT_EQUALITY_CLASSIFICATION',sum(examined.values()))
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
