from itertools import product
from math import comb

def pairs_nat(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def posets_natural(n):
    ps=pairs_nat(n)
    for mask in range(1<<len(ps)):
        E={ps[k] for k in range(len(ps)) if (mask>>k)&1}
        ok=True
        # transitivity suffices because i<j ensures irreflexive/antisymmetric
        for i,j in tuple(E):
            for jj,k in tuple(E):
                if j==jj and (i,k) not in E:
                    ok=False; break
            if not ok: break
        if ok:
            yield E

def is_lt(E,a,b):
    return (a,b) in E

def admissible_type_count(n,E):
    total=0
    for s in product((-1,0,1), repeat=n):
        # -1: a<x, 0: incomparable, +1: x<a
        L=[i for i,t in enumerate(s) if t==-1]
        U=[i for i,t in enumerate(s) if t==1]
        if any((j in L and i not in L) for i,j in E):
            continue
        if any((i in U and j not in U) for i,j in E):
            continue
        if any((l,u) not in E for l in L for u in U):
            continue
        total+=1
    return total

def extension_type_count(n,E):
    # independent check: directly add x=n with one of three statuses to each old point,
    # then check the strict relation is transitive.
    total=0
    for s in product((-1,0,1), repeat=n):
        R=set(E)
        for a,t in enumerate(s):
            if t==-1: R.add((a,n))
            elif t==1: R.add((n,a))
        ok=True
        if any(a==b for a,b in R): ok=False
        if ok and any((b,a) in R for a,b in R): ok=False
        if ok:
            for a,b in tuple(R):
                for bb,c in tuple(R):
                    if b==bb and (a,c) not in R:
                        ok=False; break
                if not ok: break
        if ok: total+=1
    return total

def ideal_count(n,E):
    total=0
    for bits in product((0,1), repeat=n):
        I={i for i,b in enumerate(bits) if b}
        if all(not (j in I and i not in I) for i,j in E):
            total+=1
    return total

def add_top_chain(n,E,m):
    # old P on 0..n-1, new top chain n<...<n+m-1, all old below each chain point
    R=set(E)
    for p in range(n):
        for t in range(n,n+m):
            R.add((p,t))
    for i in range(m):
        for j in range(i+1,m):
            R.add((n+i,n+j))
    return R

checked_posets=0
for n in range(0,6):
    vals=[]
    for E in posets_natural(n):
        checked_posets+=1
        c1=admissible_type_count(n,E)
        c2=extension_type_count(n,E)
        assert c1==c2,(n,E,c1,c2)
        J=ideal_count(n,E)
        for m in (1,2,3):
            Q=add_top_chain(n,E,m)
            cq=admissible_type_count(n+m,Q)
            rhs=c1+m*J+comb(m+1,2)
            assert cq==rhs,(n,m,E,c1,J,cq,rhs)
        vals.append(c1)
    if vals:
        print(f'n={n} posets={len(vals)} type_count_range={min(vals)}..{max(vals)}')

# Explicit examples.
for n in range(1,8):
    chain={(i,j) for i in range(n) for j in range(i+1,n)}
    anti=set()
    assert admissible_type_count(n,chain)==comb(n+2,2)
    assert admissible_type_count(n,anti)==2**(n+1)-1

# Reduction identity can recover the number J(P) of ideals using two instances that both have a greatest element:
# c(P+top+top) - c(P+top) - 2 = J(P).
for n in range(0,6):
    for E in posets_natural(n):
        q1=add_top_chain(n,E,1)
        q2=add_top_chain(n,E,2)
        recovered=admissible_type_count(n+2,q2)-admissible_type_count(n+1,q1)-2
        assert recovered==ideal_count(n,E)

print('checked_posets=',checked_posets)
print('VERIFY_OK')
