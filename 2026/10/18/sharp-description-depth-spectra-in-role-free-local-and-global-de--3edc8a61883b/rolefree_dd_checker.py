"""Direct finite semantic checks for role-free definite-description concepts.

Language: k unary predicates, Booleans, local singleton nominal L(C),
and global predicate G(C,D), with G(C,D) true everywhere iff C
names one object belonging to D. No roles or individual constants.
Run: python3 rolefree_dd_checker.py
"""
from __future__ import annotations
from functools import lru_cache
from itertools import product
from collections import defaultdict
import random

TOP=('top',)
BOT=('bot',)
def atom(j): return ('a',j)
def neg(x): return ('not',x)
def disj(x,y): return ('or',x,y)
def conj(x,y): return ('and',x,y)
def loc(x): return ('L',x)
def glob(x,y=TOP): return ('G',x,y)

def color(t,k):
    return tuple(['and',] + []) if False else make_and([atom(i) if t&(1<<i) else neg(atom(i)) for i in range(k)])
def make_and(formulas):
    out=TOP
    for f in formulas:out=conj(out,f)
    return out

def model_eval(colors, formula):
    n=len(colors)
    full=(1<<n)-1
    @lru_cache(None)
    def ev(f):
        op=f[0]
        if op=='top': return full
        if op=='bot': return 0
        if op=='a': return sum(1<<i for i,t in enumerate(colors) if t&(1<<f[1]))
        if op=='not': return full ^ ev(f[1])
        if op=='or': return ev(f[1])|ev(f[2])
        if op=='and': return ev(f[1])&ev(f[2])
        if op=='L':
            a=ev(f[1]);return a if a.bit_count()==1 else 0
        if op=='G':
            a=ev(f[1]);b=ev(f[2]);return full if a.bit_count()==1 and a&b else 0
        raise ValueError(f)
    return ev(formula)

def truncated_signature(counts, tau, language, depth):
    t=len(counts)
    if depth==0: return ('atomic',tau)
    if language=='local':
        if counts[tau]!=1: return ('non-singleton',tau)
        if depth==1:
            return ('singleton',tau,tuple(0 if counts[j]==0 else 1 for j in range(t) if j!=tau))
        return ('singleton',tau,counts)
    if not any(v==1 for v in counts):return ('without-anchor',tau)
    return ('anchored',tau,counts)

def signatures_of_tests(k,language,depth):
    t=1<<k
    types=[color(i,k) for i in range(t)]
    tests=[atom(i) for i in range(k)]
    if depth>=1:
        if language=='local':
            tests += [loc(types[i]) for i in range(t)]
            tests += [loc(disj(types[i],types[j])) for i in range(t) for j in range(t) if i!=j]
            if depth>=2:
                tests += [loc(disj(types[i],conj(types[j],neg(loc(types[j])))))
                          for i in range(t) for j in range(t) if i!=j]
        else:
            tests += [glob(types[i]) for i in range(t)]
            tests += [glob(disj(types[i],types[j])) for i in range(t) for j in range(t) if i!=j]
    actual_to_pred={}; pred_to_actual={}; pointed=0
    for counts in product(range(3),repeat=t):
        if not any(counts):continue
        colors=tuple(i for i,c in enumerate(counts) for _ in range(c))
        observations=[model_eval(colors,f) for f in tests]
        for w,tau in enumerate(colors):
            observed=tuple(bool(m&(1<<w)) for m in observations)
            predicted=truncated_signature(counts,tau,language,depth)
            old=actual_to_pred.setdefault(observed,predicted)
            assert old==predicted,(k,language,depth,'nonconstant predicted',counts,tau,old,predicted)
            old2=pred_to_actual.setdefault(predicted,observed)
            assert old2==observed,(k,language,depth,'same predicted diff observations',counts,tau)
            pointed+=1
    N=len(pred_to_actual)
    expected=t if depth==0 else (
      t*(1+2**(t-1)) if language=='local' and depth==1 else
      t*(1+3**(t-1)) if language=='local' else
      t*(1+2*3**(t-1)-2**(t-1)))
    assert N==expected,(k,language,depth,N,expected)
    return {'k':k,'language':language,'depth':depth,'pointed':pointed,
            'test_formulas':len(tests),'theories':N}

def random_formula(rng,k,kind,level):
    if level==0 or rng.random()<.21:
        return rng.choice([TOP,BOT]+[atom(i) for i in range(k)])
    choice=rng.choice(['not','and','or',kind])
    if choice=='not':return neg(random_formula(rng,k,kind,level-1))
    if choice=='and':return conj(random_formula(rng,k,kind,level-1),random_formula(rng,k,kind,level-1))
    if choice=='or':return disj(random_formula(rng,k,kind,level-1),random_formula(rng,k,kind,level-1))
    if kind=='L':return loc(random_formula(rng,k,kind,level-1))
    return glob(random_formula(rng,k,kind,level-1),random_formula(rng,k,kind,level-1))

def random_invariance():
    rng=random.Random(19361)
    comparisons=0
    # independently change each non-singleton color multiplicity; keep same pointed type
    for k in (0,1,2,3):
      T=1<<k
      for kind in ('L','G'):
        forms=[random_formula(rng,k,kind,5) for _ in range(100)]
        for _ in range(60):
          c=[rng.randrange(3) for j in range(T)]
          if not any(c):c[rng.randrange(T)]=1
          tau=rng.choice([j for j,v in enumerate(c) if v>0])
          c2=[v if v<2 else rng.randint(2,6) for v in c]
          a=tuple(j for j,v in enumerate(c) for i in range(v))
          b=tuple(j for j,v in enumerate(c2) for i in range(v))
          wa=a.index(tau);wb=b.index(tau)
          for f in forms:
              z=model_eval(a,f)&(1<<wa)
              y=model_eval(b,f)&(1<<wb)
              assert bool(z)==bool(y),(k,kind,c,c2,tau,f)
              comparisons+=1
    print('ROLEFREE_DD_RANDOM_TRUNCATION_INVARIANCE_OK',comparisons)

if __name__=='__main__':
    total=0
    for k in range(3):
      for lang in ('local','global'):
        for depth in (0,1,2) if lang=='local' else (0,1):
          r=signatures_of_tests(k,lang,depth)
          print('DD_PARTITION_OK',r)
          total+=r['pointed']
    random_invariance()
    print('ROLEFREE_DD_CHECKS_OK', 'pointed_comparisons=',total)
