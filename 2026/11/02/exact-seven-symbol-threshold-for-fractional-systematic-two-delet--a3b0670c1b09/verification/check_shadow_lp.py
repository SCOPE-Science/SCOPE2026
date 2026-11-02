"""Exact-arithmetic certificate for a systematic two-deletion shadow LP."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import factorial

def pattern(seq):
    labels = {}
    return tuple(labels.setdefault(x, len(labels)) for x in seq)

def shadow(word):
    return {tuple(word[i] for i in triple) for triple in combinations(range(5), 3)}

PATTERNS3 = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2)]
WEIGHTS = dict(zip(PATTERNS3, (14,3,2,5,2)))

def all_patterns(length):
    if length==0:
        yield ()
        return
    for prefix in all_patterns(length-1):
        for v in range(1+max(prefix,default=-1)+1):
            yield prefix+(v,)

# Exhaust every equality pattern of length five; valid over sufficiently large q,
# and subsets of these patterns cover each smaller q.
seen=set(all_patterns(5))
assert len(seen)==52, len(seen)
hist=Counter()
minimum={}
for p in seen:
    ct = Counter(pattern(s) for s in shadow(p))
    cost = sum(WEIGHTS[t]*k for t,k in ct.items())
    kind='same' if p[0]==p[1] else 'different'
    assert cost >= (14 if kind=='same' else 19), (p, cost)
    hist[kind, max(p)+1] += 1
    minimum[kind,max(p)+1]=min(cost, minimum.get((kind,max(p)+1),cost))
assert hist == {
    ('same',1):1,('same',2):7,('same',3):6,('same',4):1,
    ('different',2):8,('different',3):19,('different',4):9,('different',5):1
}, hist
assert minimum == {
    ("same",1):14,("same",2):17,("same",3):16,("same",4):17,
    ("different",2):19,("different",3):19,("different",4):19,("different",5):20
}, minimum

# The three chosen distinct-prefix orbits, all with an explicit five-letter
# representative. Rows are distinct-output profiles by equality pattern.
families=[(0,1,1,2,0),(0,1,1,2,2),(0,1,2,3,4)]
expect=[(0,2,2,1,2),(0,1,0,3,1),(0,0,0,0,10)]
for word,row in zip(families,expect):
    counts=Counter(pattern(y) for y in shadow(word))
    assert tuple(counts[t] for t in PATTERNS3)==row,(word,counts)
probs=[Fraction(2,5),Fraction(1,5),Fraction(2,5)]
profile=[sum(probs[j]*expect[j][i] for j in range(3)) for i in range(5)]
assert profile==list(map(Fraction,(0,1,)))+[Fraction(4,5),Fraction(1),Fraction(5)], profile

def add(w,coef,group,loads):
    assert coef>0
    group[w[:2]]+=coef
    for subword in shadow(w):loads[subword]+=coef

def check(q):
    group=Counter();loads=Counter()
    symbols=range(q)
    for a in symbols:
        add((a,)*5,Fraction(1),group,loads)
    for a in symbols:
        for b in symbols:
            if a==b:continue
            other=[v for v in symbols if v not in (a,b)]
            for c in other:
                add((a,b,b,c,a),Fraction(2,5*(q-2)),group,loads)
                add((a,b,b,c,c),Fraction(1,5*(q-2)),group,loads)
            for c,d,e in product(other,repeat=3):
                if len({c,d,e})<3:continue
                add((a,b,c,d,e),Fraction(2,5*(q-2)*(q-3)*(q-4)),group,loads)
    assert len(group)==q*q
    assert all(group[(a,b)]==1 for a,b in product(symbols,repeat=2))
    assert len(loads)==q**3, (q,len(loads),q**3)
    target={PATTERNS3[0]:Fraction(1),PATTERNS3[1]:Fraction(1),PATTERNS3[2]:Fraction(4,5),PATTERNS3[3]:Fraction(1),PATTERNS3[4]:Fraction(5,q-2)}
    assert all(loads[y]==target[pattern(y)] for y in product(symbols, repeat=3))
    assert all(v<=1 for v in loads.values())
    return [str(target[p]) for p in PATTERNS3],sum(loads.values())

for q in [7,8,9]:
    print('q=',q,'loads by AAA,AAB,ABA,ABB,ABC=',check(q)[0])
print('52 restricted-growth patterns proved weighted converse for q<=6')
print('VERIFY_OK')
