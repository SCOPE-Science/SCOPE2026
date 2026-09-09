"""Verify one Fano-type Dr(3,8) cell verdict: explicit matrix over F2(t),
t-adic Plucker valuations w, tropical Plucker check, initial matroid M0."""
import json, itertools

# polys over F2 as int bitmasks; add=XOR; mul=shift-xor
def padd(a,b): return a^b
def pmul(a,b):
    r=0
    while b:
        if b&1: r^=a
        a<<=1; b>>=1
    return r
def pdet(M):
    # 3x3 det over F2[t] (char 2: signs irrelevant)
    s=0
    for p in [(0,1,2),(1,2,0),(2,0,1)]: s^=pmul(M[0][p[0]],pmul(M[1][p[1]],M[2][p[2]]))
    for p in [(0,2,1),(2,1,0),(1,0,2)]: s^=pmul(M[0][p[0]],pmul(M[1][p[1]],M[2][p[2]]))
    return s
def pval(p):
    if p==0: return None
    v=0
    while not (p>>v)&1: v+=1
    return v

C=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]  # Fano pts PG(2,2)
V=(0b1,0b10,0b100)  # (1,t,t^2)
def col(j):
    if j<7: return (C[j][0],C[j][1],C[j][2])
    return V
def detpoly(T):
    M=[[col(T[k])[r] for k in range(3)] for r in range(3)]
    return pdet(M)

triples=list(itertools.combinations(range(8),3))
w={}; polys={}
for T in triples:
    p=detpoly(T); polys[T]=p; w[T]=pval(p)
nb=[T for T in triples if w[T] is None]
assert len(nb)==7, nb
assert sorted(nb)==sorted([(0,1,3),(0,2,4),(1,2,5),(0,5,6),(1,4,6),(2,3,6),(3,4,5)])
n0=sum(1 for T in triples if w[T]==0)
print("nonbases:",nb,"#val0:",n0,"min val: 0")

# every pair of Fano pts + v independent (free extension check)
for a,b in itertools.combinations(range(7),2):
    assert polys[tuple(sorted((a,b,7)))]!=0
print("free-point check: all 21 triples with col7 are bases")

# Dressian: 3-term tropical Plucker for k=3: A size2, B size4, j in B\A
INF=10**9
def W(T): return w[tuple(sorted(T))] if w[tuple(sorted(T))] is not None else INF
bad=0; tot=0
for A in itertools.combinations(range(8),2):
    for B in itertools.combinations(range(8),4):
        terms=[]
        for j in B:
            if j in A: continue
            Aj=tuple(sorted(set(A)|{j})); Bj=tuple(sorted(set(B)-{j}))
            terms.append(W(Aj)+W(Bj))
        tot+=1
        m=min(terms)
        # Speyer convention: all-INF (unsupported) relations pass vacuously (min attained >=2 at INF)
        if sum(1 for t in terms if t==m)<2: bad+=1; print("FAIL",A,B,terms)
print(f"Plucker: {tot} relations, {bad} failures")
assert bad==0

# initial matroid M0 = {bases with w==0}; symmetric exchange check
B0=[set(T) for T in triples if w[T]==0]
def isbasis(S): return frozenset(S) in {frozenset(b) for b in B0}
Bs={frozenset(b) for b in B0}
for X,Y in itertools.product(Bs,Bs):
    for x in X-set(Y):
        assert any(frozenset((set(X)-{x})|{y}) in Bs for y in set(Y)-set(X)), (X,Y,x)
print(f"M0: {len(Bs)} bases, exchange axiom holds, rank 3")
# deletion M0\7 == Fano
NB0=sorted([tuple(sorted(set(t)-{7})) for t in triples if 7 in t and w[t] is not None and w[t]>0])
delB={frozenset(b) for b in B0 if 7 not in b}
FanoB={frozenset(t) for t in itertools.combinations(range(7),3)}-{frozenset(t) for t in nb}
assert delB==FanoB
print("M0\\7 == F7 certified")
# M0 connected (matroid polytope full-dim): separator check
def connected():
    for S in itertools.chain.from_iterable(itertools.combinations(range(8),r) for r in (1,2,3)):
        S=set(S)
        if all(len(set(b)&S) in (0,len(b)) or True for b in []): pass
        # separator: exists S with 0<|S|<8, no basis meeting both... use rank test
    return True
# rank function from bases
def rank(S):
    return max(len(set(b)&set(S)) for b in Bs)
sep=[S for r in (1,2,3,4,5,6,7) for S in itertools.combinations(range(8),r)
     if rank(set(S))+rank(set(range(8))-set(S))==3]
assert sep==[], sep
print("M0 connected: maximal cell (dim 7)")
# w values with col7
from collections import Counter
print("val distribution on triples w/7:",Counter(w[t] for t in triples if 7 in t))
json.dump({"w":{str(k):v for k,v in w.items()},"M0_bases":sorted([sorted(b) for b in Bs])},
          open("output/artifacts/cell_data.json","w"),indent=1)
print("ALL CHECKS PASS")
