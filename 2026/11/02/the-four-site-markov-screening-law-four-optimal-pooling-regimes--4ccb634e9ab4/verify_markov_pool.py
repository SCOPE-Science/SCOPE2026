#!/usr/bin/env python3
"""Exact four-site Dorfman expected-test partition verifier (science only)."""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache

N=4

def partitions(items):
    if not items:
        yield ()
        return
    x=items[0]
    for blocks in partitions(items[1:]):
        yield (frozenset([x]),)+blocks
        for j in range(len(blocks)):
            bs=list(blocks)
            bs[j]=bs[j]|{x}
            yield tuple(bs)

PARTS=list(partitions(tuple(range(N))))
assert len(PARTS)==15, len(PARTS)


def zero_subset_formula(h,p,r):
    if not h:return F(1)
    u=1-p
    ii=sorted(h)
    z=u
    for x,y in zip(ii,ii[1:]): z*=u+p*r**(y-x)
    return z


def cost_group(h,p,r):
    if len(h)==1:return F(1)
    return 1+len(h)*(1-zero_subset_formula(h,p,r))


def expected_cost(part,p,r):
    return sum((cost_group(h,p,r) for h in part),F(0))


def candidates(p,r):
    u=1-p;a=u+p*r;b=u+p*r*r
    return {'4':5-4*u*a**3,
            '31':5-3*u*(a*a if r>=0 else a*b),
            '22':6-4*u*(a if r>=0 else b),
            '1111':F(4)}


def exact_distribution(p,r):
    u=1-p
    trans=((u+p*r,p*(1-r)),(u*(1-r),p+u*r))
    out={}
    for w in product((0,1), repeat=4):
        prob=u if w[0]==0 else p
        for i in range(1,4):prob*=trans[w[i-1]][w[i]]
        out[w]=prob
    assert sum(out.values())==1
    return out


def exact_cost_distribution(part,probs):
    s=F(0)
    for seq,w in probs.items():
        tests=0
        for h in part:
            tests+=1 if len(h)==1 else 1+len(h)*int(any(seq[i] for i in h))
        s+=w*tests
    return s

checks=0

def assert_eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1

# Symbolic equality for every subset, 2^4 complete chain configurations.
import sympy as S
p,r=S.symbols('p r')
u=1-p
T=S.Matrix([[u+p*r,p*(1-r)],[u*(1-r),p+u*r]])
for mask in range(1,16):
    h=[i for i in range(4) if mask>>i&1]
    prob=S.Integer(0)
    for bits in product((0,1),repeat=4):
        if any(bits[i] for i in h):continue
        a=(u if bits[0]==0 else p)
        for j in range(1,4):a*=T[bits[j-1],bits[j]]
        prob+=a
    formula=u
    for x,y in zip(h,h[1:]):formula*=u+p*r**(y-x)
    assert_eq(S.factor(prob-formula),0)

# All 15 partitions are checked independently by full 16-state enumeration.
params=[]
for pn in range(1,10):
    pp=F(pn,10)
    for rn in range(-10,11):
        rr=F(rn,10)
        if rr < -min(pp/(1-pp),(1-pp)/pp) or rr>=1:continue
        params.append((pp,rr))
# nonround neighborhoods including four mode witnesses
params += [(F(1,10),F(-1,10)),(F(2,7),F(-1,10)),(F(1,4),F(-1,4)),(F(1,2),F(-1,2)),(F(1,4),F(0)),(F(1,3),F(1,4))]
for pp,rr in params:
    dist=exact_distribution(pp,rr)
    formulas=candidates(pp,rr)
    allvals=[]
    for part in PARTS:
        cost=expected_cost(part,pp,rr)
        assert_eq(cost,exact_cost_distribution(part,dist))
        allvals.append(cost)
    assert_eq(min(allvals),min(formulas.values()))
    if rr>=0:
        assert min(formulas.values()) < formulas['22']
        checks+=1

witness={'4':(F(1,10),F(-1,10)),'31':(F(2,7),F(-1,10)),
         '22':(F(1,4),F(-1,4)),'1111':(F(1,2),F(-1,2))}
for shape,(pp,rr) in witness.items():
    fs=candidates(pp,rr)
    assert min(fs,key=fs.get)==shape
    assert all(fs[shape]<v for key,v in fs.items() if key!=shape)
    checks+=1
    print('WITNESS',shape,'p=',pp,'rho=',rr,'expected tests=',fs[shape], 'margin=',min(v-fs[shape] for key,v in fs.items() if key!=shape))

print('PASS',checks,'exact assertions;',len(params),'parameter points;',len(PARTS),'complete set partitions')
