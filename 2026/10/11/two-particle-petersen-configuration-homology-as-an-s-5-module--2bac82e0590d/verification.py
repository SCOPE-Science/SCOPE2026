#!/usr/bin/env python3
import itertools, json, sys
from fractions import Fraction
from pathlib import Path

CERT=json.loads(Path(__file__).with_name("verification_certificate.json").read_text())

def det_bareiss(A):
    A=[list(map(int,r)) for r in A]
    n=len(A)
    if n==0:return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            q=next((i for i in range(k+1,n) if A[i][k]),None)
            if q is None:return 0
            A[k],A[q]=A[q],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            aik=A[i][k]
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-aik*A[k][j])//prev
            A[i][k]=0
        prev=piv
    return sign*A[-1][-1]

def rank_mod(A,p):
    A=[[x%p for x in r] for r in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]),None)
        if q is None:continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(n)]
        r+=1
        if r==m:break
    return r

def inv_frac(A):
    n=len(A)
    M=[[Fraction(A[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        q=next(i for i in range(c,n) if M[i][c])
        M[c],M[q]=M[q],M[c]
        f=M[c][c]; M[c]=[x/f for x in M[c]]
        for i in range(n):
            if i!=c and M[i][c]:
                f=M[i][c]; M[i]=[M[i][j]-f*M[c][j] for j in range(2*n)]
    return [r[n:] for r in M]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

# Petersen graph as KG(5,2).
V=list(itertools.combinations(range(5),2)); vi={v:i for i,v in enumerate(V)}
E=[]
for i in range(10):
    for j in range(i+1,10):
        if set(V[i]).isdisjoint(V[j]): E.append((i,j))
ei={e:i for i,e in enumerate(E)}
assert (len(V),len(E))==(10,15)
# girth is exactly five, so the graph is sufficiently subdivided for two particles.
adj=[set() for _ in V]
for a,b in E: adj[a].add(b); adj[b].add(a)
assert all(len(x)==3 for x in adj)
assert not any((b in adj[a] and c in adj[a] and c in adj[b]) for a in range(10) for b in range(a+1,10) for c in range(b+1,10))
def has_cycle(k):
    for cyc in itertools.permutations(range(1,10),k-1):
        seq=(0,)+cyc
        if all(seq[(i+1)%k] in adj[seq[i]] for i in range(k)): return True
    return False
# vertex-transitivity lets us root the cycle search at vertex zero.
assert not has_cycle(4) and has_cycle(5)

# Full automorphism group: complement is L(K5); its five maximal K4s are the five stars.
comp=[[j for j in range(10) if j!=i and j not in adj[i]] for i in range(10)]
K4=[]
for S in itertools.combinations(range(10),4):
    if all(b in comp[a] for a,b in itertools.combinations(S,2)):
        # maximum clique size is four here, so these are maximal.
        K4.append(S)
assert len(K4)==5 and all(sum(v in S for S in K4)==2 for v in range(10))
# Natural S5 gives 120 distinct actions, and every graph automorphism permutes these five K4s faithfully.

C0=list(itertools.combinations(range(10),2)); c0i={x:i for i,x in enumerate(C0)}
C1=[]
for k,(a,b) in enumerate(E):
    for w in range(10):
        if w not in (a,b): C1.append((k,w))
c1i={x:i for i,x in enumerate(C1)}
C2=[]
for i,j in itertools.combinations(range(15),2):
    if set(E[i]).isdisjoint(E[j]): C2.append((i,j))
c2i={x:i for i,x in enumerate(C2)}
assert [len(C0),len(C1),len(C2)]==[45,120,75]

# Signed cellular boundaries, column dictionaries.
d1=[]
for k,w in C1:
    a,b=E[k]
    d={c0i[tuple(sorted((b,w)))]:1,c0i[tuple(sorted((a,w)))]:-1}
    d1.append(d)
d2=[]
for i,j in C2:
    a,b=E[i]; c,d=E[j]
    col={}
    for cell,s in [((j,b),1),((j,a),-1),((i,d),-1),((i,c),1)]:
        r=c1i[cell]; col[r]=col.get(r,0)+s
    d2.append({r:s for r,s in col.items() if s})
for col in d2:
    acc={}
    for r,s in col.items():
        for q,t in d1[r].items(): acc[q]=acc.get(q,0)+s*t
    assert all(x==0 for x in acc.values())

# Deterministic spanning tree of the C0 graph; chord coordinates identify ker(d1) with Z^76.
parent=list(range(45))
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]; x=parent[x]
    return x
def union(a,b):
    a=find(a); b=find(b)
    if a==b:return False
    parent[b]=a; return True
tree=[]; chords=[]
for idx,(k,w) in enumerate(C1):
    a,b=E[k]; x=c0i[tuple(sorted((a,w)))]; y=c0i[tuple(sorted((b,w)))]
    (tree if union(x,y) else chords).append(idx)
assert len(tree)==44 and len(chords)==76 and len({find(i) for i in range(45)})==1
M=[[0]*75 for _ in range(76)]
chord_pos={r:i for i,r in enumerate(chords)}
for j,col in enumerate(d2):
    for r,s in col.items():
        if r in chord_pos:M[chord_pos[r]][j]=s
assert rank_mod(M,2)==CERT["h1_snf"]["rank_mod_2"]==69
assert rank_mod(M,3)==70
R=CERT["minor_rows_in_chord_matrix"]; C=CERT["minor_columns"]
minor=[[M[i][j] for j in C] for i in R]
det=det_bareiss(minor)
assert abs(det)==CERT["minor_determinant_abs"]==2

# Integral H2 certificate and rank upper bound for d2.
N=CERT["h2_basis"]; piv=CERT["h2_pivot_rows"]
assert len(N)==75 and all(len(r)==5 for r in N)
for j,col in enumerate(d2):
    for b in range(5):
        assert sum(col.get(r,0)*N[j][b] for r in [])==0  # no-op shape guard
# Direct d2*N multiplication.
for r in range(120):
    for b in range(5):
        assert sum(d2[j].get(r,0)*N[j][b] for j in range(75))==0
Np=[[N[r][c] for c in range(5)] for r in piv]
assert det_bareiss(Np)==CERT["h2_pivot_determinant"]==-1
# A nonzero 70-minor gives rank(d2)>=70; five independent kernel vectors give rank(d2)<=70.
# Hence rank(d2)=70.  The top determinantal divisor of M is 2: rank mod 2 is 69,
# while an integral maximal minor is ±2. Thus SNF(M)=(1^69,2,0^5).

# S5 action and rational characters.
Npinv=inv_frac(Np)
class_order=CERT["class_order"]
expected_sizes=dict(zip(class_order,CERT["class_sizes"]))
expected_h1=dict(zip(class_order,CERT["h1_character"]))
expected_h2=dict(zip(class_order,CERT["h2_character"]))
vals={k:[] for k in class_order}

def ctype(p):
    seen=set(); ls=[]
    for i in range(5):
        if i in seen:continue
        j=i;n=0
        while j not in seen:
            seen.add(j); n+=1; j=p[j]
        ls.append(n)
    ls=tuple(sorted(ls,reverse=True))
    return {(1,1,1,1,1):"1",(2,1,1,1):"(2)",(2,2,1):"(2,2)",(3,1,1):"(3)",(4,1):"(4)",(5,):"(5)",(3,2):"(3,2)"}[ls]

def action_data(p):
    gv=[vi[tuple(sorted((p[a],p[b])))] for a,b in V]
    ge=[]; esign=[]
    for a,b in E:
        aa,bb=gv[a],gv[b]
        esign.append(1 if aa<bb else -1)
        ge.append(ei[tuple(sorted((aa,bb)))])
    tr0=0
    for x in C0:
        y=tuple(sorted((gv[x[0]],gv[x[1]])))
        if y==x:tr0+=1
    tr1=0
    for k,w in C1:
        if (ge[k],gv[w])==(k,w): tr1+=esign[k]
    tr2=0; map2=[]
    for i,j in C2:
        a,b=ge[i],ge[j]; s=esign[i]*esign[j]
        if a>b:a,b=b,a;s=-s
        q=c2i[(a,b)]; map2.append((q,s))
        if q==c2i[(i,j)]:tr2+=s
    return tr0,tr1,tr2,map2

for p in itertools.permutations(range(5)):
    cl=ctype(p); tr0,tr1,tr2,map2=action_data(p)
    AN=[[0]*5 for _ in range(75)]
    for src,(dst,s) in enumerate(map2):
        for b in range(5): AN[dst][b]+=s*N[src][b]
    ANp=[[AN[r][c] for c in range(5)] for r in piv]
    T=matmul(Npinv,ANp)
    # Verify the solved action matrix on all 75 rows, not only pivots.
    NT=matmul([[Fraction(x) for x in r] for r in N],T)
    assert all(NT[i][j]==AN[i][j] for i in range(75) for j in range(5))
    trh2=sum(T[i][i] for i in range(5)); assert trh2.denominator==1
    trh2=int(trh2)
    trh1=tr1-tr0+1-tr2+trh2
    vals[cl].append((trh1,trh2,(tr0,tr1,tr2)))
for cl in class_order:
    assert len(vals[cl])==expected_sizes[cl]
    assert {x[0] for x in vals[cl]}=={expected_h1[cl]}
    assert {x[1] for x in vals[cl]}=={expected_h2[cl]}
# Irreducibility sanity checks from character inner products.
assert sum(expected_sizes[c]*expected_h1[c]**2 for c in class_order)==120
assert sum(expected_sizes[c]*expected_h2[c]**2 for c in class_order)==120
assert sum(expected_sizes[c]*expected_h1[c]*expected_h2[c] for c in class_order)==0
print("VERIFY_OK cells=45,120,75 rank_d1=44 rank_d2=70 H1=Z^6+Z/2 H2=Z^5 chars=verified_over_all_120_S5_elements")
