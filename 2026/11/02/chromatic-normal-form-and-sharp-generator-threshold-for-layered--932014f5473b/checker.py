"""Independent finite modal partition-refinement and layered-generator census."""
from itertools import product
from math import prod

def falling(x,r):
    z=1
    for j in range(r):z*=x-j
    return z

def quotient_size(levels,colors):
    n=len(colors)
    starts=[0]
    for width in levels:starts.append(starts[-1]+width)
    assert n==starts[-1]
    lev=[next(i for i in range(len(levels)) if starts[i]<=j<starts[i+1]) for j in range(n)]
    succ=[tuple(w for w in range(n) if w==v or lev[w]>lev[v]) for v in range(n)]
    labels=tuple(colors)
    while True:
        # canonical label of each (atomic colour, set of current successor types)
        keys=[(colors[v],frozenset(labels[w] for w in succ[v])) for v in range(n)]
        table={x:i for i,x in enumerate(sorted(set(keys),key=repr))}
        nextlabels=tuple(table[key] for key in keys)
        if all((labels[i]==labels[j])==(nextlabels[i]==nextlabels[j]) for i in range(n) for j in range(n)):
            return len(set(nextlabels))
        labels=nextlabels

def predicts_all(levels, colors):
    starts=[0]
    for width in levels:starts.append(starts[-1]+width)
    for i,width in enumerate(levels):
        ss=colors[starts[i]:starts[i+1]]
        if len(set(ss))!=width:return False
        if i<len(levels)-1 and levels[i+1]==1:
            forbidden=colors[starts[i+1]]
            if forbidden in ss:return False
    return True

def predicted_count(levels,q):
    z=falling(q,levels[-1])
    for i in range(len(levels)-1):
        z*=falling(q-int(levels[i+1]==1),levels[i])
    return z

def compositions(n):
    if n==0:
        yield ()
    for first in range(1,n+1):
        for tail in compositions(n-first): yield (first,)+tail

def full_generated_direct(levels, colors, q):
    # Enumerate closure of the actual Boolean-modal operations, not types.
    n=len(colors)
    starts=[0]
    for width in levels:starts.append(starts[-1]+width)
    lv=[next(i for i in range(len(levels)) if starts[i]<=j<starts[i+1]) for j in range(n)]
    nxt=[tuple(j for j in range(n) if j==i or lv[j]>lv[i]) for i in range(n)]
    bits=max(1,(q-1).bit_length())
    universe=(1<<n)-1
    generated={0,universe}
    for bit in range(bits):
        v=sum((1<<i) for i in range(n) if colors[i]&(1<<bit))
        generated.add(v)
    while True:
        old=len(generated)
        for a in list(generated):
            generated.add(universe^a)
            generated.add(sum((1<<i) for i in range(n) if any((a>>j)&1 for j in nxt[i])))
        frozen=list(generated)
        for a in frozen:
            for b in frozen:generated.add(a|b)
        if len(generated)==old:break
    return len(generated)==(1<<n)

def main():
    tests=0; checked_profiles=0
    for n in range(1,7):
        for levels in compositions(n):
            for q in (1,2,3,4):
                if q**n>1500:continue
                actual=0
                for colors in product(range(q),repeat=n):
                    got=quotient_size(levels,colors)==n
                    expect=predicts_all(levels,colors)
                    assert got==expect, (levels,q,colors,got,expect)
                    actual+=got;tests+=1
                want=predicted_count(levels,q)
                assert actual==want, (levels,q,actual,want)
                checked_profiles+=1
    direct=0
    for n in range(1,5):
        for levels in compositions(n):
            for colors in product(range(4),repeat=n):
                got=full_generated_direct(levels,colors,4)
                assert got==predicts_all(levels,colors),('direct',levels,colors)
                direct+=1
    print('ALL_CHECKS_OK', 'bisim_valuations=',tests,'profiles=',checked_profiles,'direct_closure_valuations=',direct)
if __name__=='__main__':main()
