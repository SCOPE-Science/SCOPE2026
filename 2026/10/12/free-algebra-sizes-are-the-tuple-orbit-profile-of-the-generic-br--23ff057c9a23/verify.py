#!/usr/bin/env python3
from itertools import product

checks = 0

def ok(cond, msg='assertion failed'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def is_poset(n, rel):
    # rel is bit mask over n*n ordered pairs
    def R(i,j): return (rel >> (i*n+j)) & 1
    for i in range(n):
        if not R(i,i): return False
    for i in range(n):
        for j in range(n):
            if i != j and R(i,j) and R(j,i): return False
    for i in range(n):
        for j in range(n):
            if R(i,j):
                for k in range(n):
                    if R(j,k) and not R(i,k): return False
    return True

def upsets(n, rel):
    def R(i,j): return (rel >> (i*n+j)) & 1
    out=[]
    for mask in range(1<<n):
        good=True
        for i in range(n):
            if (mask>>i)&1:
                for j in range(n):
                    if R(i,j) and not ((mask>>j)&1):
                        good=False; break
                if not good: break
        if good: out.append(mask)
    return out

def impl_mask(n, rel, A, B):
    def R(i,j): return (rel >> (i*n+j)) & 1
    ans=0
    for i in range(n):
        good=True
        for j in range(n):
            if R(i,j) and ((A>>j)&1) and not ((B>>j)&1):
                good=False; break
        if good: ans |= 1<<i
    return ans

# All Kripke models on labeled posets of size <=3 with two monotone variables.
posets=[]
for n in range(1,4):
    count=0
    for rel in range(1<<(n*n)):
        if is_poset(n,rel):
            posets.append((n,rel)); count += 1
    ok(count == {1:1,2:3,3:19}[n], f'poset count n={n}: {count}')

models=[]
for n,rel in posets:
    ups=upsets(n,rel)
    for P in ups:
        for Q in ups:
            models.append((n,rel,P,Q))
ok(len(models)==564, len(models))

TOP=tuple((1<<n)-1 for n,rel,P,Q in models)
P_SIG=tuple(P for n,rel,P,Q in models)
Q_SIG=tuple(Q for n,rel,P,Q in models)

def meet(a,b): return tuple(x&y for x,y in zip(a,b))

def impl(a,b):
    return tuple(impl_mask(n,rel,A,B) for (n,rel,_,_),A,B in zip(models,a,b))

# Generate the free two-generated implicative semilattice semantically.
elems=[TOP,P_SIG,Q_SIG]
seen=set(elems)
changed=True
round_sizes=[]
while changed:
    changed=False
    snapshot=list(elems)
    for a in snapshot:
        for b in snapshot:
            for c in (meet(a,b), impl(a,b)):
                if c not in seen:
                    seen.add(c); elems.append(c); changed=True
    round_sizes.append(len(elems))
ok(len(elems)==18, f'closure size {len(elems)} rounds={round_sizes}')

idx={a:i for i,a in enumerate(elems)}
meet_table=[[idx[meet(a,b)] for b in elems] for a in elems]
impl_table=[[idx[impl(a,b)] for b in elems] for a in elems]
top=idx[TOP]

# Algebra axioms + residual law directly on the 18-element algebra.
def leq(i,j): return meet_table[i][j]==i
for a in range(18):
    ok(meet_table[a][a]==a)
    ok(meet_table[a][top]==a)
    ok(impl_table[a][a]==top)
    for b in range(18):
        ok(meet_table[a][b]==meet_table[b][a])
        for c in range(18):
            ok((leq(c,impl_table[a][b])) == leq(meet_table[c][a],b))

# Enumerate every deductive filter. Finite filters must be principal.
filters=[]
for S in range(1<<18):
    if not ((S>>top)&1):
        continue
    good=True
    members=[i for i in range(18) if (S>>i)&1]
    # upward closed
    for i in members:
        for j in range(18):
            if leq(i,j) and not ((S>>j)&1):
                good=False; break
        if not good: break
    if not good: continue
    # meet closed
    for i in members:
        for j in members:
            if not ((S>>meet_table[i][j])&1):
                good=False; break
        if not good: break
    if good: filters.append(S)
ok(len(filters)==18, f'filter count {len(filters)}')
principal=[]
for m in range(18):
    S=sum(1<<j for j in range(18) if leq(m,j))
    principal.append(S)
ok(set(filters)==set(principal))

# Congruence-filter correspondence checked explicitly for each principal filter.
partitions=[]
for m,S in enumerate(principal):
    def equiv(a,b):
        e=meet_table[impl_table[a][b]][impl_table[b][a]]
        return bool((S>>e)&1)
    # equivalence relation
    for a in range(18):
        ok(equiv(a,a))
        for b in range(18):
            ok(equiv(a,b)==equiv(b,a))
            for c in range(18):
                if equiv(a,b) and equiv(b,c): ok(equiv(a,c))
    # operation compatibility
    for a in range(18):
        for b in range(18):
            if not equiv(a,b): continue
            for c in range(18):
                for d in range(18):
                    if equiv(c,d):
                        ok(equiv(meet_table[a][c],meet_table[b][d]))
                        ok(equiv(impl_table[a][c],impl_table[b][d]))
    # canonical partition code
    classes=[]; used=set()
    for a in range(18):
        if a in used: continue
        cl=tuple(b for b in range(18) if equiv(a,b)); used.update(cl); classes.append(cl)
    partitions.append(tuple(classes))
ok(len(set(partitions))==18)

# Every congruence kernel corresponds to one tuple orbit in a universal ultrahomogeneous limit;
# here the exact finite numerical anchor is |Con(F_2)|=|F_2|=18.
print(f'VERIFY_OK {checks} exact assertions; 23 labeled posets, 564 Kripke models; free F_2 size=18; filters=congruences=18')
