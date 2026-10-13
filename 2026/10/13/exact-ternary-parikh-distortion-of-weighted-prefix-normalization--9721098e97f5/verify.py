#!/usr/bin/env python3
from itertools import product

W = {"a":1,"b":2,"c":3}

def signature(word):
    ps=[0]
    for ch in word:
        ps.append(ps[-1]+W[ch])
    n=len(word)
    return tuple(max(ps[i+k]-ps[i] for i in range(n-k+1))
                 for k in range(1,n+1))

def parikh(word):
    return tuple(word.count(ch) for ch in "abc")

def pnf_from_signature(sig):
    inv={1:"a",2:"b",3:"c"}
    prev=0
    out=[]
    for value in sig:
        d=value-prev
        assert d in inv
        out.append(inv[d])
        prev=value
    return "".join(out)

def l1(p,q):
    return sum(abs(x-y) for x,y in zip(p,q))

maxima=[]
pair_ranges=[]
total_words=0
for n in range(2,10):
    groups={}
    max_pnf=0
    for tup in product("abc", repeat=n):
        word="".join(tup)
        total_words += 1
        sig=signature(word)
        p=parikh(word)
        form=pnf_from_signature(sig)
        assert signature(form)==sig
        max_pnf=max(max_pnf,l1(p,parikh(form)))
        c=p[2]
        if sig not in groups:
            groups[sig]=[c,c]
        else:
            groups[sig][0]=min(groups[sig][0],c)
            groups[sig][1]=max(groups[sig][1],c)
    expected=4*((n-2)//2)
    assert max_pnf==expected
    maxima.append(max_pnf)
    max_t=max(hi-lo for lo,hi in groups.values())
    assert max_t==(n-2)//2
    pair_ranges.append(max_t)

for n in range(2,31):
    if n % 2 == 0:
        r=n//2
        word="bc"+"ac"*(r-1)
        form="c"+"b"*(n-1)
    else:
        r=(n-1)//2
        word="abc"+"ac"*(r-1)
        form="c"+"b"*(n-2)+"a"
    assert len(word)==len(form)==n
    assert signature(word)==signature(form)
    assert pnf_from_signature(signature(word))==form
    assert l1(parikh(word),parikh(form))==4*((n-2)//2)

print(
    "VERIFY_OK "
    f"exhaustive_words={total_words} "
    "n=2..9 "
    "max_l1="+",".join(map(str,maxima))+" "
    "max_abs_t="+",".join(map(str,pair_ranges))+" "
    "constructions_n=2..30"
)
