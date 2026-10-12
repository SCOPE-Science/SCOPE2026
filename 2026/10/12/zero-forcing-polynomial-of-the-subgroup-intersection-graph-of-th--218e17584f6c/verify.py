#!/usr/bin/env python3
from itertools import combinations, product
from collections import defaultdict

def abstract_graph(p):
    r=p+1
    names=[f"M{i}" for i in range(r)]+["Z"]
    blocks=[]
    for i in range(r):
        block=[f"L{i}_{j}" for j in range(p)]
        blocks.append(block); names.extend(block)
    N={v:set() for v in names}
    core=[f"M{i}" for i in range(r)]+["Z"]
    for a,b in combinations(core,2):
        N[a].add(b); N[b].add(a)
    for i,block in enumerate(blocks):
        for x in block:
            N[x].add(f"M{i}"); N[f"M{i}"].add(x)
    return names,N,blocks

def zero_forces(S,N):
    blue=set(S)
    while len(blue)<len(N):
        move=None
        for v in N:
            if v in blue:
                W=N[v]-blue
                if len(W)==1:
                    move=next(iter(W)); break
        if move is None: return False
        blue.add(move)
    return True

def mul(A,B):
    C=defaultdict(int)
    for i,a in A.items():
        for j,b in B.items(): C[i+j]+=a*b
    return dict(C)

def ppow(A,n):
    R={0:1}
    for _ in range(n): R=mul(R,A)
    return R

def predicted_poly(p):
    r=p+1
    A={p-1:p,p:1}
    core=ppow({0:1,1:1},r)
    P=defaultdict(int)
    for k,v in mul(core,{j+1:a for j,a in ppow(A,r).items()}).items(): P[k]+=v
    for k,v in mul(core,ppow(A,r)).items(): P[k]+=v
    for k,v in mul(core,{(p-1)*r:p**r}).items(): P[k]-=v
    return dict(sorted((k,v) for k,v in P.items() if v))

def brute_poly(p):
    names,N,_=abstract_graph(p)
    out=defaultdict(int)
    for mask in range(1<<len(names)):
        S=[names[i] for i in range(len(names)) if (mask>>i)&1]
        if zero_forces(S,N): out[len(S)]+=1
    return dict(sorted(out.items()))

def heis_mul(x,y,p):
    a,b,c=x; d,e,f=y
    return ((a+d)%p,(b+e)%p,(c+f+a*e)%p)

def heis_pow(x,n,p):
    y=(0,0,0)
    for _ in range(n): y=heis_mul(y,x,p)
    return y

def cyclic_subgroup(x,p):
    return frozenset(heis_pow(x,k,p) for k in range(p))

def direct_pattern(p):
    G=list(product(range(p),repeat=3)); e=(0,0,0)
    Z=frozenset((0,0,c) for c in range(p))
    order_p={cyclic_subgroup(x,p) for x in G if x!=e}
    assert len(order_p)==p*p+p+1
    lines=[{(t,s*t%p) for t in range(p)} for s in range(p)]
    lines.append({(0,t) for t in range(p)})
    maxs=[frozenset((a,b,c) for (a,b) in L for c in range(p)) for L in lines]
    assert len(set(maxs))==p+1 and all(len(M)==p*p for M in maxs)
    noncentral=[H for H in order_p if H!=Z]
    owners={}
    for H in noncentral:
        c=[i for i,M in enumerate(maxs) if H<=M]
        assert len(c)==1; owners[H]=c[0]
    assert all(sum(owners[H]==i for H in noncentral)==p for i in range(p+1))
    subs=list(order_p)+maxs
    for A,B in combinations(subs,2):
        adj=len(A&B)>1
        if A in maxs and B in maxs: pred=True
        elif (A==Z and B in maxs) or (B==Z and A in maxs): pred=True
        elif A in noncentral and B in maxs: pred=owners[A]==maxs.index(B)
        elif B in noncentral and A in maxs: pred=owners[B]==maxs.index(A)
        else: pred=False
        assert adj==pred
    return len(subs)

p=3
names,N,blocks=abstract_graph(p)
P=brute_poly(p); Q=predicted_poly(p)
assert P==Q and min(P)==9 and P[9]==189
for mask in range(1<<len(names)):
    blue={names[i] for i in range(len(names)) if mask>>i&1}
    white=set(names)-blue
    cond1=all(sum(x in white for x in block)<=1 for block in blocks)
    cond2=("Z" not in white) or any(all(x in blue for x in block) for block in blocks)
    assert zero_forces(blue,N)==(cond1 and cond2)
print("p=3 full polynomial:",P)
print("p=3 characterization checked on all 2^17 subsets")

for p in (3,5):
    n=direct_pattern(p)
    assert n==p*p+2*p+2
    print(f"Heisenberg p={p}: {n} proper nontrivial subgroups, graph pattern OK")

for p in (3,5,7,11):
    P=predicted_poly(p)
    z=min(P)
    assert z==p*p and P[z]==(2*p+1)*p**p
    print(f"p={p}: Z={z}, min_count={P[z]}, polynomial_at_1={sum(P.values())}")

print("VERIFY_OK")
