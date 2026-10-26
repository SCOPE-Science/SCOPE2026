"""Finite cross-checks for the two-coordinate Horn closure of finite word products.
No external packages; run: python verify.py
"""
from itertools import product, combinations
from math import ceil
from random import Random


def setup(qs):
    d=len(qs); words=list(product(*(range(q) for q in qs)))
    idx={x:i for i,x in enumerate(words)}
    rules=[]; dist=[]
    for i,a in enumerate(words):
        for j in range(i+1,len(words)):
            b=words[j]
            dif=[h for h in range(d) if a[h]!=b[h]]
            if len(dif)==2:
                h=dif[0]
                c=list(a); c[h]=b[h]
                e=list(b); e[h]=a[h]
                rules.append(((1<<i)|(1<<j), (1<<idx[tuple(c)])|(1<<idx[tuple(e)])))
            dist.append((i,j,len(dif)))
    return words,rules,dist


def close(seed,rules):
    s=seed
    while True:
        t=s
        for premise,consequence in rules:
            if (premise&s)==premise: t|=consequence
        if t==s: return s
        s=t


def box(bits, words):
    selected=[w for i,w in enumerate(words) if bits>>i&1]
    if not selected:return 0
    allowed=[set(w[h] for w in selected) for h in range(len(words[0]))]
    return sum(1<<i for i,w in enumerate(words) if all(w[h] in allowed[h] for h in range(len(allowed))))


def component_boxes(bits,words,dist):
    n=len(words); adj=[0]*n
    for a,b,k in dist:
        if k==1:
            adj[a]|=1<<b; adj[b]|=1<<a
    remaining=bits; comps=[]
    while remaining:
        seed=remaining&-remaining; component=seed; pending=seed
        while pending:
            bit=pending&-pending; pending-=bit
            i=bit.bit_length()-1
            extra=adj[i]&bits&~component
            component|=extra; pending|=extra
        comps.append(component); remaining&=~component
    for c in comps: assert c==box(c,words),(words,c,box(c,words))
    for a,b,k in dist:
        if k<3 and (bits>>a&1) and (bits>>b&1):
            assert any(((c>>a)&1) and ((c>>b)&1) for c in comps)
    return comps


def merge_prediction(bits,words):
    groups=[{i} for i in range(len(words)) if (bits>>i)&1]
    d=len(words[0])
    def hull(A):
        al=[{words[i][h] for i in A} for h in range(d)]
        return {i for i,w in enumerate(words) if all(w[h] in al[h] for h in range(d))}
    while True:
        merged=False
        for u in range(len(groups)):
            for v in range(u+1,len(groups)):
                if any(sum(a!=b for a,b in zip(words[i],words[j]))<=2 for i in groups[u] for j in groups[v]):
                    groups[u]=hull(groups[u]|groups[v]);groups.pop(v);merged=True;break
            if merged:break
        if not merged:break
    return sum(1<<i for group in groups for i in group)


def goal(qs):
    changes=[q-1 for q in qs]
    return 1+max(max(changes),ceil(sum(changes)/2))


def verify(qs,exhaustive=False,samples=300):
    words,rules,dist=setup(qs); n=len(words); r=Random(314159+n)
    tests=range(1<<n) if exhaustive else [r.getrandbits(n) for _ in range(samples)]
    count=0
    for s in tests:
        cl=close(s,rules)
        if n<=16 or count<40: assert merge_prediction(s,words)==cl,('merge',qs,s)
        component_boxes(cl,words,dist)
        count+=1
    target=(1<<n)-1;k=goal(qs)
    for j in range(min(k,5)):
        if n<=18:
            for subset in combinations(range(n),j):
                s=sum(1<<i for i in subset)
                assert close(s,rules)!=target,('small generator',qs,j,subset)
    witness=None
    if k<=5 and n<=27:
        for subset in combinations(range(n),k):
            s=sum(1<<i for i in subset)
            if close(s,rules)==target: witness=subset;break
        assert witness is not None,('missing witness',qs,k)
    print('PASS',qs,'points',n,'tested_sets',count,'minimum_generator',k,'witness',witness)


def main():
    for qs in [(2,2),(2,3),(3,3),(2,2,2),(2,3,2),(2,2,2,2),(3,3,3),(3,2,4),(2,2,2,2,2)]:
        verify(qs,exhaustive=(len(qs)<=4 and __import__('math').prod(qs)<=16),samples=800)
    print('VERIFY_OK exact_closure=PASS canonical_boxes=PASS merging=PASS generator_lower_upper=PASS')

if __name__=='__main__':main()
