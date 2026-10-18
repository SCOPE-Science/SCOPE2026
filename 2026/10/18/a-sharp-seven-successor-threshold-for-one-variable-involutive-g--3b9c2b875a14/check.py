"""Finite tests for a seven-leaf uniform bound in unary crisp Goedel modal stars.
Use: python3 check.py  (standard library only). Mathematical proof is in RESULT.md.
"""
import random
from functools import lru_cache
from itertools import combinations_with_replacement

ONE = 100
p = ('p',)
z = ('0',)
o = ('1',)

def neg(a): return ('~', a)
def conj(a,b): return ('&',a,b)
def imp(a,b): return ('->',a,b)
def diamond(a): return ('dia',a)
def box(a): return ('box',a)
def Delta(a): return imp(neg(a),z)
def gneg(a): return imp(a,z)

m0 = gneg(p)
m1 = Delta(p)
mh = Delta(conj(imp(p,neg(p)),imp(neg(p),p)))
ml = conj(neg(Delta(imp(neg(p),p))), neg(gneg(p)))
mr = conj(neg(Delta(imp(p,neg(p)))), neg(Delta(p)))

def spread(mask):
    hi=diamond(conj(mask,p))
    lo_complement=diamond(conj(mask,neg(p)))
    return neg(Delta(imp(hi,neg(lo_complement))))

stages=[diamond(m0),diamond(mh),diamond(m1),diamond(ml),spread(ml),diamond(mr),spread(mr)]

@lru_cache(None)
def value_leaf(term,x):
    k=term[0]
    if k=='p':return x
    if k=='0':return 0
    if k=='1':return ONE
    if k=='~':return ONE-value_leaf(term[1],x)
    if k=='&':return min(value_leaf(term[1],x),value_leaf(term[2],x))
    if k=='->':
        a=value_leaf(term[1],x);b=value_leaf(term[2],x)
        return ONE if a<=b else b
    if k=='dia':return 0
    if k=='box':return ONE
    raise AssertionError(k)

def value_root(term,r,leaves):
    k=term[0]
    if k=='p':return r
    if k=='0':return 0
    if k=='1':return ONE
    if k=='~':return ONE-value_root(term[1],r,leaves)
    if k=='&':return min(value_root(term[1],r,leaves),value_root(term[2],r,leaves))
    if k=='->':
        a=value_root(term[1],r,leaves);b=value_root(term[2],r,leaves)
        return ONE if a<=b else b
    if k=='dia':return max(value_leaf(term[1],x) for x in leaves)
    if k=='box':return min(value_leaf(term[1],x) for x in leaves)
    raise AssertionError(k)

def compressed(leaves):
    select=[]
    for t in (0,ONE//2,ONE):
        if t in leaves:select.append(t)
    for lower,upper in ((0,ONE//2),(ONE//2,ONE)):
        region=[x for x in leaves if lower<x<upper]
        if region:select.extend([min(region),max(region)])
    return tuple(sorted(set(select)))

def conjunction(terms):
    v=o
    for t in terms:v=conj(v,t)
    return v

# Verify all propositional stratum tests exhaustively on the discrete grid.
for x in range(101):
    target=(int(x==0),int(x==50),int(x==100),int(0<x<50),int(50<x<100))
    got=tuple(value_leaf(a,x)//100 for a in (m0,mh,m1,ml,mr))
    assert target==got,(x,target,got)
print('PASS: five crisp stratum tests, 101 degrees')

# Exhaustive multiset checks for each of the six strict validity separations.
exhaustive_cases=0
for m in range(1,7):
    phi=conjunction(stages[:m+1]);not_phi=neg(phi)
    for xs in combinations_with_replacement((0,20,40,50,60,80,100),m):
        assert value_root(phi,37,xs)==0,(m,xs)
        assert value_root(not_phi,37,xs)==100,(m,xs)
        exhaustive_cases+=1
    witnesses=[0,50,100,20,40,60,80][:m+1]
    assert value_root(phi,37,tuple(witnesses))==100,(m,witnesses)
    for x in witnesses:
        assert value_leaf(not_phi,x)==100
print('PASS: sharp six strict separation witnesses and',exhaustive_cases,'short-star multisets')

# Check the structural 7-representative rule for formula trees with modal nesting.
random.seed(7012026)
def random_term(d):
    if d<=0:return random.choice((p,z,o))
    t=random.choice(('p','0','1','~','&','->','dia','box'))
    if t in ('p','0','1'):return (t,)
    if t in ('~','dia','box'):return (t,random_term(d-1))
    return (t,random_term(d-1),random_term(d-1))
comparisons=0
for _ in range(250):
    size=random.randint(1,30)
    xs=tuple(random.randint(0,100) for __ in range(size))
    ys=compressed(xs)
    assert 1<=len(ys)<=7 and set(ys).issubset(set(xs))
    for j in range(90):
        term=random_term(random.randint(0,7))
        root=random.randint(0,100)
        assert value_root(term,root,xs)==value_root(term,root,ys),(xs,ys,term)
        comparisons+=1
print('PASS:',comparisons,'arbitrary nested-formula root comparisons')

# Seven unique extremal witnesses: remove any sample leaf and some diamond term changes.
whole=(0,20,40,50,60,80,100)
for x in whole:
    missing=tuple(y for y in whole if y!=x)
    if x==0: t=diamond(m0)
    elif x==50:t=diamond(mh)
    elif x==100:t=diamond(m1)
    elif x==20:t=diamond(conj(ml,neg(p)))
    elif x==40:t=diamond(conj(ml,p))
    elif x==60:t=diamond(conj(mr,neg(p)))
    else:t=diamond(conj(mr,p))
    assert value_root(t,37,whole)!=value_root(t,37,missing),x
print('PASS: each of seven leaves is indispensable for exact root-value preservation')
print('ALL TESTS PASSED')
