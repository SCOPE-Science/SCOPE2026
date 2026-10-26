#!/usr/bin/env python3
"""Finite diagnostics for observation fibers of binary-modal ternary chain frames.

No external packages.  The general theorem is proved separately.
"""
from collections import defaultdict,Counter
from random import Random

def pairs(n): return [(a,b) for a in range(n) for b in range(n)]

def down(row,n):
    return frozenset((a,b) for a,b in pairs(n) if any(a<=v and b<=w for v,w in row))

def up(row,n):
    return frozenset((a,b) for a,b in pairs(n) if any(a>=v and b>=w for v,w in row))

def parse_mask(mask,n):
    pp=pairs(n)
    return tuple(frozenset(pp[j] for j in range(n*n) if mask>>(i*n*n+j)&1) for i in range(n))

def valid_original(rows,n):
    for u in range(n):
        for v,w in rows[u]:
            for u1 in range(u,n):
                if not any(a>=v and b>=w for a,b in rows[u1]): return False
            for a in range(v,n):
                for b in range(w,n):
                    if not any((a,b) in rows[u1] for u1 in range(u,n)): return False
    return True

def data(rows,n):
    D=tuple(down(r,n) for r in rows)
    S=tuple(frozenset().union(*rows[u:]) for u in range(n))
    return D,S

def valid_shadow(rows,n):
    D,S=data(rows,n)
    return all(D[u]<=D[u+1] for u in range(n-1)) and all(S[u]==up(S[u],n) for u in range(n))

def modal_signature(rows,n):
    # Truth-at-world arrays for every ordered pair of upward-closed truth sets.
    out=[]
    for a in range(n+1):
      for b in range(n+1):
        for u in range(n):
          c=any(v>=a and w>=b for v,w in rows[u])
          bullet=all(v>=a or w>=b for t in range(u,n) for v,w in rows[t])
          out.append((c,bullet))
    return tuple(out)

def fiber_from_shadow(D,S,n):
    exponent=0
    for u in range(n-1):
       maximal={p for p in D[u] if not any(p!=q and p[0]<=q[0] and p[1]<=q[1] for q in D[u])}
       exponent+=len((D[u]&S[u+1])-maximal)
    return 2**exponent

def canonical(rows,n):
    D,S=data(rows,n)
    lo=[];hi=[]
    for u in range(n):
      maximal={p for p in D[u] if not any(p!=q and p[0]<=q[0] and p[1]<=q[1] for q in D[u])}
      nextS=S[u+1] if u+1<n else frozenset()
      lo.append(frozenset(maximal|(S[u]-nextS)))
      hi.append(frozenset(D[u]&S[u]))
    return tuple(lo),tuple(hi)

def exhaustive(n):
    groups=defaultdict(list); semantic={}
    checked=0
    for mask in range(1<<(n**3)):
       rows=parse_mask(mask,n)
       a=valid_original(rows,n); b=valid_shadow(rows,n)
       assert a==b,(n,mask,'frame discrepancy')
       checked+=1
       if not a:continue
       k=data(rows,n)
       sig=modal_signature(rows,n)
       if k in semantic:assert semantic[k]==sig
       else:semantic[k]=sig
       groups[k].append(mask)
       lo,hi=canonical(rows,n)
       assert valid_original(lo,n) and valid_original(hi,n)
       assert data(lo,n)==k==data(hi,n)
       assert all(lo[u]<=rows[u]<=hi[u] for u in range(n))
    assert len(set(semantic.values()))==len(groups),'semantic quotient differs from shadow quotient'
    for k,lst in groups.items():
       assert len(lst)==fiber_from_shadow(*k,n),(n,k,len(lst))
    assert max(map(len,groups.values()))==2**((n-1)*(n*n-1))
    return checked,sum(map(len,groups.values())),len(groups),max(map(len,groups.values())),Counter(len(v) for v in groups.values())

for n in (1,2):
    print('exhaustive',n,exhaustive(n))

n=3;pp=pairs(n);rng=Random(137179)
# Realistically reachable, nontrivial valid relations: rows are nonempty upsets,
# which satisfy both original frame conditions. Also full-suffix fiber.
for trial in range(5000):
    rows=[]
    start=rng.randrange(n)
    for u in range(n):
        if u<start:rows.append(frozenset());continue
        chosen={p for p in pp if rng.random()<0.22}
        rows.append(up(chosen,n) if chosen else frozenset({(n-1,n-1)}))
    rows=tuple(rows)
    assert valid_original(rows,n)
    lo,hi=canonical(rows,n)
    assert data(lo,n)==data(rows,n)==data(hi,n)
    assert valid_original(lo,n) and valid_original(hi,n)
    assert modal_signature(lo,n)==modal_signature(rows,n)==modal_signature(hi,n)
    assert fiber_from_shadow(*data(rows,n),n)>=1
full=frozenset(pp)
top=(n-1,n-1)
seen=set()
for trial in range(2500):
    rows=(frozenset({top}|{p for p in pp if rng.getrandbits(1)}),
          frozenset({top}|{p for p in pp if rng.getrandbits(1)}), full)
    assert valid_original(rows,n)
    assert data(rows,n)==data((full,full,full),n)
    seen.add(tuple(tuple(sorted(r)) for r in rows))
assert fiber_from_shadow(*data((full,full,full),n),n)==65536
print('random_three_world',5000,'max_fiber_three_world',65536,'sampled_members',len(seen))
print('ALL_CHECKS_OK')

# Independent nested-formula evaluator on sampled equivalence classes.
# Formula nodes are tuples: atom(name), bottom, and/or/imp/circle/bullet(left,right).
def eval_formula(f,rows,n,valuation):
    op=f[0]
    if op=='atom':return valuation[f[1]]
    if op=='bottom':return frozenset()
    a=eval_formula(f[1],rows,n,valuation)
    b=eval_formula(f[2],rows,n,valuation)
    if op=='and':return a&b
    if op=='or':return a|b
    if op=='imp':return frozenset(i for i in range(n) if all(j not in a or j in b for j in range(i,n)))
    if op=='circle':return frozenset(i for i in range(n) if any(v in a and w in b for v,w in rows[i]))
    if op=='bullet':return frozenset(i for i in range(n) if all(v in a or w in b for t in range(i,n) for v,w in rows[t]))
    raise ValueError(op)

def random_formula(depth):
    if depth<=0:return ('atom',rng.choice(['p','q','r']))
    op=rng.choice(['and','or','imp','circle','bullet'])
    return (op,random_formula(depth-1),random_formula(depth-1))

for trial in range(600):
    n=3
    rows=(frozenset({(2,2)}|{p for p in pairs(n) if rng.getrandbits(1)}),
          frozenset({(2,2)}|{p for p in pairs(n) if rng.getrandbits(1)}),
          frozenset(pairs(n)))
    lo,hi=canonical(rows,n)
    val={p:frozenset(range(rng.randrange(n+1),n)) for p in ['p','q','r']}
    form=random_formula(4)
    assert eval_formula(form,lo,n,val)==eval_formula(form,rows,n,val)==eval_formula(form,hi,n,val)
print('nested_formulas',600,'ALL_NESTED_OK')
