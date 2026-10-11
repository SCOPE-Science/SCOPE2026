#!/usr/bin/env python3
import json,itertools,collections,sys,os

HERE=os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE,"certificate.json"),encoding="utf-8") as f: C=json.load(f)

def bits(x): return ((x>>0)&1,(x>>1)&1,(x>>2)&1)
cubeE=[]
for u in range(8):
    for d in range(3):
        v=u^(1<<d)
        if u<v: cubeE.append((u,v))
cubeEi={e:i for i,e in enumerate(cubeE)}
V=list(range(12))
E=[]
for i,e in enumerate(cubeE):
    for j in range(i+1,12):
        if set(e)&set(cubeE[j]): E.append((i,j))
E=sorted(E); Ei={e:i for i,e in enumerate(E)}
assert len(E)==24 and all(sum(v in e for e in E)==4 for v in V)

C0=list(itertools.combinations(V,2)); I0={x:i for i,x in enumerate(C0)}
C1=[(ei,v) for ei,(a,b) in enumerate(E) for v in V if v not in (a,b)]; I1={x:i for i,x in enumerate(C1)}
C2=[(i,j) for i,(a,b) in enumerate(E) for j in range(i+1,len(E)) if len({a,b,*E[j]})==4]; I2={x:i for i,x in enumerate(C2)}
assert [len(C0),len(C1),len(C2)]==C["cell_counts"]

# sparse columns
d1=[]
for ei,v in C1:
    a,b=E[ei]
    d1.append({I0[tuple(sorted((b,v)))]:1,I0[tuple(sorted((a,v)))]:-1})
d2=[]
for ei,ej in C2:
    a,b=E[ei]; c,d=E[ej]
    col={}
    for key,val in [((ej,b),1),((ej,a),-1),((ei,d),-1),((ei,c),1)]:
        r=I1[key]; col[r]=col.get(r,0)+val
    d2.append({r:v for r,v in col.items() if v})

for col in d2:
    z={}
    for r,a in col.items():
        for q,b in d1[r].items(): z[q]=z.get(q,0)+a*b
    assert all(v==0 for v in z.values())

# spanning tree in the configuration 1-skeleton
adj=[[] for _ in C0]
for j,col in enumerate(d1):
    rr=list(col)
    assert len(rr)==2
    u,w=rr
    adj[u].append((w,j)); adj[w].append((u,j))
par=[-1]*len(C0); par[0]=0; tree=set(); q=collections.deque([0])
while q:
    u=q.popleft()
    for w,e in adj[u]:
        if par[w]<0:
            par[w]=u; tree.add(e); q.append(w)
assert all(x>=0 for x in par) and len(tree)==C["tree_edge_count"]
chords=[j for j in range(len(C1)) if j not in tree]
assert len(chords)==C["chord_count"]
chordpos={e:i for i,e in enumerate(chords)}
B=[[0]*len(C2) for _ in chords]
for j,col in enumerate(d2):
    for e,v in col.items():
        if e in chordpos: B[chordpos[e]][j]=v

def bareiss(A):
    A=[row[:] for row in A]; n=len(A)
    if n==0:return 1
    s=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next((i for i in range(k+1,n) if A[i][k]),None)
            if p is None:return 0
            A[k],A[p]=A[p],A[k]; s=-s
        piv=A[k][k]
        for i in range(k+1,n):
            aik=A[i][k]
            if aik==0:
                for j in range(k+1,n): A[i][j]=(A[i][j]*piv)//prev
            else:
                for j in range(k+1,n): A[i][j]=(A[i][j]*piv-aik*A[k][j])//prev
            A[i][k]=0
        prev=piv
    return s*A[-1][-1]

rows=C["unit_minor_rows"]; cols=C["unit_minor_cols"]
minor=[[B[r][c] for c in cols] for r in rows]
assert len(rows)==len(cols)==C["rank_d2"]
assert bareiss(minor) in (1,-1)

K=C["kernel_basis"]; kp=C["kernel_pivot_rows"]; Kinv=C["kernel_pivot_inverse"]
assert len(K)==len(C2) and all(len(r)==43 for r in K)
# d2*K=0
for r in range(len(C1)):
    acc=[0]*43
    for j,col in enumerate(d2):
        a=col.get(r,0)
        if a:
            kr=K[j]
            for t in range(43): acc[t]+=a*kr[t]
    assert not any(acc)
# Kinv*Ksub=I
for i in range(43):
    for j in range(43):
        s=sum(Kinv[i][t]*K[kp[t]][j] for t in range(43))
        assert s==(1 if i==j else 0)

# cube automorphisms and actions
def parity_perm(sig):
    return -1 if sum(sig[i]>sig[j] for i in range(3) for j in range(i+1,3))%2 else 1
def apply(v,sig,b):
    x=bits(v); y=[x[sig[i]]^((b>>i)&1) for i in range(3)]
    return y[0]|(y[1]<<1)|(y[2]<<2)
diags=sorted(tuple(sorted((v,v^7))) for v in range(8) if v<(v^7)); DI={d:i for i,d in enumerate(diags)}
def ctype(p):
    seen=set(); out=[]
    for i in range(len(p)):
        if i not in seen:
            j=i;n=0
            while j not in seen: seen.add(j);n+=1;j=p[j]
            out.append(n)
    return tuple(sorted(out,reverse=True))
def classkey(ct,z):
    base={ (1,1,1,1):"1^4",(2,1,1):"2,1,1",(2,2):"2,2",(3,1):"3,1",(4,):"4"}[ct]
    return base+(","+("+" if z==1 else "-"))
chars={"H1":{},"H2":{}}
counts=collections.Counter()
for sig in itertools.permutations(range(3)):
  ps=parity_perm(sig)
  for b in range(8):
    pc=[apply(v,sig,b) for v in range(8)]
    pv=[]
    for a,c in cubeE: pv.append(cubeEi[tuple(sorted((pc[a],pc[c])) )])
    z=ps*((-1)**sum(bits(b)))
    pd=[DI[tuple(sorted((pc[a],pc[c])))] for a,c in diags]
    key=classkey(ctype(pd),z); counts[key]+=1
    em=[]; es=[]
    for a,c in E:
        ga,gc=pv[a],pv[c]; em.append(Ei[tuple(sorted((ga,gc)))]); es.append(1 if ga<gc else -1)
    p1=[];s1=[]
    for ei,v in C1: p1.append(I1[(em[ei],pv[v])]); s1.append(es[ei])
    p2=[];s2=[]
    for ei,ej in C2:
        a,c=em[ei],em[ej]; s=es[ei]*es[ej]
        if a>c:a,c=c,a;s=-s
        p2.append(I2[(a,c)]);s2.append(s)
    inv=[0]*len(p2)
    for j,r in enumerate(p2):inv[r]=j
    # trace on H2 in the K basis using selected coordinate rows
    tr2=0
    for i in range(43):
        for t in range(43):
            src=inv[kp[t]]
            tr2 += Kinv[i][t]*s2[src]*K[src][i]
    # cellular traces
    tr0=0
    for i,(a,c) in enumerate(C0):
        if I0[tuple(sorted((pv[a],pv[c])))]==i: tr0+=1
    tr1c=sum(s1[i] for i,r in enumerate(p1) if i==r)
    tr2c=sum(s2[i] for i,r in enumerate(p2) if i==r)
    tr1=1+tr2-(tr0-tr1c+tr2c)
    chars["H1"].setdefault(key,set()).add(tr1); chars["H2"].setdefault(key,set()).add(tr2)

for h in ("H1","H2"):
    got={k:next(iter(v)) for k,v in chars[h].items() if len(v)==1}
    assert len(got)==10 and got==C["expected_characters"][h]

# irreducible decomposition of S4 x C2
classes=["1^4","2,1,1","2,2","3,1","4"]; sizes=[1,6,3,8,6]
irr={"triv":[1,1,1,1,1],"sgn":[1,-1,1,1,-1],"V":[3,1,-1,0,-1],"Vsgn":[3,-1,-1,0,1],"W":[2,0,2,-1,0]}
for h in ("H1","H2"):
    cp=[];cm=[]
    for c in classes:
        a=C["expected_characters"][h][c+",+"]; b=C["expected_characters"][h][c+",-"]
        cp.append((a+b)//2); cm.append((a-b)//2)
    for label,ch in [("plus",cp),("minus",cm)]:
        got={}
        for nm,ir in irr.items():
            num=sum(sizes[i]*ch[i]*ir[i] for i in range(5))
            assert num%24==0; got[nm]=num//24
        assert got==C["expected_decomposition"][h][label]


# Independent planar-face check of the H2 character.
tri=[frozenset(i for i,e in enumerate(cubeE) if u in e) for u in range(8)]
sq=[]
for d in range(3):
    for bit in (0,1):
        sq.append(frozenset(i for i,(a,b) in enumerate(cubeE) if bits(a)[d]==bit and bits(b)[d]==bit))
faces=tri+sq; FI={f:i for i,f in enumerate(faces)}
assert len(faces)==14
assert sum(1 for i in range(14) for j in range(i+1,14) if faces[i].isdisjoint(faces[j]))==43
facechars={}
for sig in itertools.permutations(range(3)):
  ps=parity_perm(sig)
  for b in range(8):
    pc=[apply(v,sig,b) for v in range(8)]
    pv=[cubeEi[tuple(sorted((pc[a],pc[c])))] for a,c in cubeE]
    z=ps*((-1)**sum(bits(b)))
    pd=[DI[tuple(sorted((pc[a],pc[c])))] for a,c in diags]
    key=classkey(ctype(pd),z)
    pf=[FI[frozenset(pv[i] for i in f)] for f in faces]
    tr=0
    for i in range(14):
      for j in range(i+1,14):
        if faces[i].isdisjoint(faces[j]):
          a,c=pf[i],pf[j]
          if {a,c}=={i,j}: tr += (1 if (a==i and c==j) else -1)
    facechars.setdefault(key,set()).add(tr)
assert {k:next(iter(v)) for k,v in facechars.items()}==C["expected_characters"]["H2"]

print("VERIFY_OK cells=66,240,204 H=(1,14,43) Aut=48 characters_decomposition_facecheck=OK")
