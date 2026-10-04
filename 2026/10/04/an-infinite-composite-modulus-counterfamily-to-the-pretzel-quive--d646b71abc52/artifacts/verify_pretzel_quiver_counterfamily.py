#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import product

def colorings(p):
    n=2*p
    out=[]
    for a,b,c in product(range(n), repeat=3):
        e1=(p*(p-1)*(a-b)+p*(c-a))%n
        e2=(p*(p+1)*(a-b)+p*(c-b))%n
        if e1==0 and e2==0:
            out.append((a,b,c))
    return out

def proj_label(x,p):
    a,b,c=x
    u=((b-a)//2)%p
    v=((c-a)//2)%p
    if u==0 and v==0: return None
    if u:
        return (1,(v*pow(u,-1,p))%p)
    return (0,1)

def image(x,r,s,n):
    return tuple((r*t+s)%n for t in x)

def check_prime(p):
    n=2*p
    C=colorings(p)
    assert len(C)==2*p**3
    assert all((a-b)%2==0 and (a-c)%2==0 for a,b,c in C)
    blocks=defaultdict(list); constants=[]
    for x in C:
        lab=proj_label(x,p)
        (constants if lab is None else blocks[lab]).append(x)
    assert len(constants)==2*p
    assert len(blocks)==p+1
    assert {len(v) for v in blocks.values()}=={2*p*(p-1)}
    constant_set=set(constants)
    block_sets={lab:set(v) for lab,v in blocks.items()}
    maps=[(r,s) for r in range(n) for s in range(n)]
    for x in C:
        cnt=Counter(image(x,r,s,n) for r,s in maps)
        lab=proj_label(x,p)
        if lab is None:
            assert set(cnt)==constant_set
            assert set(cnt.values())=={2*p}
        else:
            assert set(cnt)==constant_set|block_sets[lab]
            assert set(cnt.values())=={2}
    actual=sorted([2*p]+[2*p*(p-1)]*(p+1))
    printed=sorted([2*p,2*p*(p-1),2*p*(p-1),2*p*(p-1),2*p*(p-1)*(p-2)])
    assert actual!=printed
    return actual,printed

summaries={p:check_prime(p) for p in (5,7,11)}
a5,t5=summaries[5]
fmt=lambda xs:"+".join(map(str,xs))
print("VERIFY_OK primes=5,7,11 p5_actual="+fmt(a5)+" p5_theorem29="+fmt(t5)+" projective_block_pattern=true")
