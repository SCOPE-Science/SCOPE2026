#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter

def outsets(n,bits):
    pairs=list(combinations(range(n),2))
    out=[set() for _ in range(n)]
    for k,(i,j) in enumerate(pairs):
        if (bits>>k)&1:
            out[i].add(j)
        else:
            out[j].add(i)
    return out

def banks_dp(n,bits):
    out=outsets(n,bits)
    lim=1<<n
    trans=[False]*lim
    top=[-1]*lim
    trans[0]=True
    for S in range(1,lim):
        for x in range(n):
            if not ((S>>x)&1):
                continue
            R=S^(1<<x)
            if trans[R] and all(y in out[x] for y in range(n) if (R>>y)&1):
                trans[S]=True
                top[S]=x
                break
    B=set()
    for S in range(1,lim):
        if not trans[S]:
            continue
        if any(trans[S|(1<<x)] for x in range(n) if not ((S>>x)&1)):
            continue
        B.add(top[S])
    return frozenset(B)

def transitive_no_triangle(n,bits,S):
    out=outsets(n,bits)
    els=[i for i in range(n) if (S>>i)&1]
    for a,b,c in combinations(els,3):
        deg=[]
        for x in (a,b,c):
            deg.append(sum(y in out[x] for y in (a,b,c) if y!=x))
        if sorted(deg)==[1,1,1]:
            return False
    return True

def banks_no_triangle(n,bits):
    out=outsets(n,bits)
    lim=1<<n
    trans=[False]*lim
    for S in range(1,lim):
        trans[S]=transitive_no_triangle(n,bits,S)
    B=set()
    for S in range(1,lim):
        if not trans[S]:
            continue
        if any(trans[S|(1<<x)] for x in range(n) if not ((S>>x)&1)):
            continue
        els=[i for i in range(n) if (S>>i)&1]
        tops=[x for x in els if all(y in out[x] for y in els if y!=x)]
        assert len(tops)==1
        B.add(tops[0])
    return frozenset(B)

def uncovered_on_subset(n,bits,S):
    out=outsets(n,bits)
    els=[i for i in range(n) if (S>>i)&1]
    U=set()
    for x in els:
        covered=False
        for y in els:
            if y==x or x not in out[y]:
                continue
            if all((z not in out[x]) or (z in out[y]) for z in els):
                covered=True
                break
        if not covered:
            U.add(x)
    return frozenset(U)

def minimal_cover_stability(n,bits):
    lim=1<<n
    stable=[]
    for B in range(1,lim):
        ok=True
        for x in range(n):
            if (B>>x)&1:
                continue
            if x in uncovered_on_subset(n,bits,B|(1<<x)):
                ok=False
                break
        if ok:
            stable.append(B)
    mins=[B for B in stable if not any(C!=B and (C&B)==C for C in stable)]
    assert len(mins)==1
    M=mins[0]
    return frozenset(i for i in range(n) if (M>>i)&1)

def minimal_cover_direct(n,bits):
    out=outsets(n,bits)
    lim=1<<n
    covering=[]
    for B in range(1,lim):
        ok=True
        for x in range(n):
            if (B>>x)&1:
                continue
            witness=False
            for y in range(n):
                if not ((B>>y)&1) or x not in out[y]:
                    continue
                # y covers x in the subtournament induced by B union {x}.
                if all((z not in out[x]) or (z in out[y])
                       for z in range(n) if (B>>z)&1):
                    witness=True
                    break
            if not witness:
                ok=False
                break
        if ok:
            covering.append(B)
    mins=[B for B in covering if not any(C!=B and (C&B)==C for C in covering)]
    assert len(mins)==1
    M=mins[0]
    return frozenset(i for i in range(n) if (M>>i)&1)

def permute_bits(n,bits,p):
    pairs=list(combinations(range(n),2))
    idx={e:k for k,e in enumerate(pairs)}
    out=outsets(n,bits)
    u=0
    for i,j in combinations(range(n),2):
        winner=i if j in out[i] else j
        loser=j if winner==i else i
        W,L=p[winner],p[loser]
        a,b=sorted((W,L))
        if W==a:
            u |= 1<<idx[(a,b)]
    return u

def canonical(n,bits):
    return min(permute_bits(n,bits,p) for p in permutations(range(n)))

hist={}
diffs={}
classes=Counter()

for n in range(1,6):
    H=Counter()
    D=[]
    total=1<<(n*(n-1)//2)
    for bits in range(total):
        B1=banks_dp(n,bits)
        B2=banks_no_triangle(n,bits)
        assert B1==B2

        M1=minimal_cover_stability(n,bits)
        M2=minimal_cover_direct(n,bits)
        assert M1==M2

        H[(len(B1),len(M1),B1==M1)] += 1

        if B1!=M1:
            assert M1 < B1
            D.append(bits)
            if n==5:
                classes[canonical(n,bits)] += 1

    hist[n]=H
    diffs[n]=len(D)

assert diffs == {1:0,2:0,3:0,4:0,5:120}
assert hist[4] == Counter({
    (1,1,True):32,
    (3,3,True):32,
})
assert hist[5] == Counter({
    (3,3,True):520,
    (1,1,True):320,
    (4,3,False):120,
    (5,5,True):64,
})
assert classes == Counter({41:120})

canon=41
BA=banks_dp(5,canon)
MC=minimal_cover_direct(5,canon)
O=outsets(5,canon)
deg=tuple(len(s) for s in O)

assert BA==frozenset({0,2,3,4})
assert MC==frozenset({0,3,4})
assert deg==(2,1,2,2,3)

# Full orbit and trivial automorphism group.
orbit={permute_bits(5,canon,p) for p in permutations(range(5))}
aut=sum(permute_bits(5,canon,p)==canon for p in permutations(range(5)))
assert len(orbit)==120
assert aut==1
assert set(orbit)=={b for b in range(1<<10) if banks_dp(5,b)!=minimal_cover_direct(5,b)}

print("VERIFY_OK")
for n in range(1,6):
    print("n",n,"total",1<<(n*(n-1)//2),"diff",diffs[n],"hist",dict(hist[n]))
print("n5_probability","120/1024 = 15/128")
print("n5_classes",dict(classes))
print("canonical_bits",canon)
print("canonical_outsets",[tuple(sorted(x)) for x in O])
print("canonical_degrees",deg)
print("canonical_BA",tuple(sorted(BA)))
print("canonical_MC",tuple(sorted(MC)))
print("orbit_size",len(orbit))
print("automorphism_order",aut)
