"""Enumerate Chein loop M(S3,2), verify Moufang, census Sylow 3-subloops, Inn orbits."""
from itertools import permutations, product

# Represent S3 as permutations of {0,1,2} in one-line tuple form.
elems = list(permutations([0,1,2]))
idx = {p:i for i,p in enumerate(elems)}
def comp(a,b):  # apply a then b? need consistent group op; use tuple composition
    # treat permutation as function: (a*b)(i) = a(b(i))? choose one; any gives S3
    return tuple(a[b[i]] for i in range(3))
def inv(a):
    ia = [0]*3
    for i,v in enumerate(a): ia[v]=i
    # inverse function
    inva = [0]*3
    for i in range(3): inva[a[i]]=i
    return tuple(inva)
one = (0,1,2)

# label group elements 0..5, coset 6..11
G = elems
n=12
def mul(a,b):
    # version A:
    # g*h=gh; g*(hu)=(hg)u; (gu)*h=(g h^{-1})u; (gu)*(hu)=h^{-1} g
    if a<6 and b<6:
        return idx[comp(G[a],G[b])]
    elif a<6 and b>=6:
        h = G[b-6]; g=G[a]
        return 6+idx[comp(G[b-6],G[a])]  # (h g)u
    elif a>=6 and b<6:
        g=G[a-6]; h=G[b]
        return 6+idx[comp(g,inv(h))]  # (g h^{-1})u
    else:
        g=G[a-6]; h=G[b-6]
        return idx[comp(inv(h),g)]  # h^{-1} g

# identity
e=idx[one]
print("identity index:",e)
# check identity laws
ok=True
for a in range(12):
    if mul(e,a)!=a or mul(a,e)!=a: ok=False; print("ident fail",a)
print("two-sided identity:",ok)

# Moufang identity: (xy)(zx) = x((yz)x)  (one of equivalent forms); check all
def moufang_hold():
    for x,y,z in product(range(12),repeat=3):
        if mul(mul(x,y),mul(z,x)) != mul(x,mul(mul(y,z),x)):
            return False,(x,y,z)
    return True,None
print(moufang_hold())

# also check left Bol? just the one form suffices given identity element? Check another form for safety
def moufang2():
    for x,y,z in product(range(12),repeat=3):
        if mul(mul(mul(x,y),z),y) != mul(x,mul(y,mul(z,y))):
            return False,(x,y,z)
    return True,None
print(moufang2())

# associativity failure
fails=[(x,y,z) for x,y,z in product(range(12),repeat=3) if mul(mul(x,y),z)!=mul(x,mul(y,z))]
print("num assoc failures:",len(fails),"example:",fails[0] if fails else None)

# element orders: powers x^1=x, x^{k+1}=x^k * x (right powers); verify power-assoc by comparing left powers
def powers(x):
    p=[None,x]  # 1-indexed
    cur=x
    for k in range(2,13):
        cur=mul(cur,x)
        p.append(cur)
        if cur==e: return k,p
    return None,p
for a in range(12):
    k,_=powers(a)
    print(a, "group?" , a<6, "perm:", G[a-6] if a>=6 else G[a], "order:",k)

# left powers check
def lpower(x,k):
    cur=x
    for _ in range(k-1): cur=mul(x,cur)
    return cur
def rpower(x,k):
    cur=x
    for _ in range(k-1): cur=mul(cur,x)
    return cur
print("power-assoc check:", all(lpower(x,k)==rpower(x,k) for x in range(12) for k in range(1,7)))

# enumerate order-3 subloops: 3-subsets containing e closed under mul
import itertools
subs=[]
for combo in itertools.combinations(range(12),3):
    if e not in combo: continue
    s=set(combo)
    if all(mul(a,b) in s for a in s for b in s):
        subs.append(s)
print("closed 3-sets containing 1:", [sorted(s) for s in subs])
print("n3 =",len(subs))

# verify each element order 3 lies in exactly one
ord3=[a for a in range(12) if powers(a)[0]==3]
print("order-3 elements:",ord3)

# translations
def perm_of(f):
    return tuple(f(a) for a in range(12))
L=[perm_of(lambda a,x=x: mul(x,a)) for x in range(12)]
R=[perm_of(lambda a,x=x: mul(a,x)) for x in range(12)]
def compose(p,q): return tuple(p[q[i]] for i in range(12))  # p after q
def invert(p):
    q=[0]*12
    for i,v in enumerate(p): q[v]=i
    return tuple(q)
# generators: T_x = R_x L_x^{-1}? conventions vary; include both orders
# L_{x,y} = L_{xy}^{-1} L_x L_y ; R_{x,y}=R_{xy}^{-1} R_y R_x ; T_x = L_x^{-1} R_x
gens=set()
for x in range(12):
    Tx=compose(R[x],invert(L[x]))
    Tx2=compose(invert(L[x]),R[x])
    gens.add(Tx); gens.add(Tx2)
for x in range(12):
    for y in range(12):
        Lxy=compose(invert(L[mul(x,y)]),compose(L[x],L[y]))
        Rxy=compose(invert(R[mul(x,y)]),compose(R[y],R[x]))
        gens.add(Lxy); gens.add(Rxy)
gens=[g for g in gens if g!=tuple(range(12))]
print("num nontrivial Inn generators (unique perms):",len(gens))
# group generated: BFS
seen={tuple(range(12))}
stack=[tuple(range(12))]
from collections import deque
dq=deque([tuple(range(12))])
genlist=list(gens)
ginv=[invert(g) for g in genlist]
allg=genlist+ginv
while dq:
    cur=dq.popleft()
    for g in allg:
        nxt=compose(g,cur)
        if nxt not in seen:
            seen.add(nxt); dq.append(nxt)
print("|Inn| =",len(seen))
# check each Inn element fixes e and preserves multiplication? check automorphisms
import random
sample=list(seen)[:50]
print("all fix identity:",all(g[e]==e for g in seen))
# check automorphism property for all Inn elements (12^2 checks each; |Inn| maybe small)
def is_auto(p):
    if p[e]!=e: return False
    for a in range(12):
        for b in range(12):
            if p[mul(a,b)]!=mul(p[a],p[b]): return False
    return True
print("all Inn are automorphisms:", all(is_auto(g) for g in seen))
# orbits on points
def orbits_on_points():
    vis=[False]*12; orbs=[]
    for i in range(12):
        if not vis[i]:
            orb=set()
            dq2=deque([i])
            orb.add(i); vis[i]=True
            # BFS via generators
            q=deque([i])
            s={i}
            for g in seen:
                if g[i] not in s: s.add(g[i])
            for j in s: vis[j]=True
            orbs.append(sorted(s))
    return orbs
print("point orbits:",orbits_on_points())
# orbits on Sylow set: since unique, trivial; but compute action
if subs:
    S=subs[0]
    print("Sylow fixed by all Inn:", all(set(g[a] for a in S)==S for g in seen))
# orbit sizes of order-3 elements
print("Inn orbit of order-3 element:", sorted(set(g[ord3[0]] for g in seen)) if ord3 else None)
