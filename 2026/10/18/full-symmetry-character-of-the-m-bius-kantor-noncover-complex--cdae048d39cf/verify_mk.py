#!/usr/bin/env python3
"""Exact, reproducible finite checks for the Möbius–Kantor line-noncover complex."""
from collections import Counter
from itertools import permutations

N=8
P=[('u',i) for i in range(0,8,2)]+[('v',i) for i in range(1,8,2)]
L=[('u',i) for i in range(1,8,2)]+[('v',i) for i in range(0,8,2)]
E=[]
for i in range(8):
    E.extend([frozenset((('u',i),('u',(i+1)%8))),frozenset((('u',i),('v',i))),frozenset((('v',i),('v',(i+3)%8)))])
lines=sorted(tuple(sorted(P.index(next(t for t in e if t!=v)) for e in E if v in e)) for v in L)
assert lines==[(0,1,4),(0,3,7),(0,5,6),(1,2,5),(1,6,7),(2,3,6),(2,4,7),(3,4,5)]
faces=sorted([f for f in range(1,256) if any(all(not(f>>i&1) for i in line) for line in lines)],key=lambda f:(f.bit_count(),f))
fs=set(faces)
fd=Counter(f.bit_count()-1 for f in faces)
assert [fd[i] for i in range(5)]==[8,28,56,40,8] and len(faces)==140
remaining=set(faces);mate={};pairs=[]
for v in range(8):
    for f in sorted(remaining):
        t=f|(1<<v)
        if not(f>>v&1) and t in remaining:
            pairs.append((f,t));mate[f]=t;mate[t]=f;remaining.remove(f);remaining.remove(t)
assert len(pairs)==67 and remaining=={1,14,22,82,164,204}
# Orientation upper->lower for all covers, reversed for matched covers.
indeg={f:0 for f in faces};out={f:[] for f in faces};cover=0
for top in faces:
    for j,v in enumerate(i for i in range(8) if top>>i&1):
        lo=top^(1<<v)
        if lo not in fs:continue
        a,b=(lo,top) if mate.get(lo)==top else (top,lo)
        out[a].append(b);indeg[b]+=1;cover+=1
queue=[f for f in faces if indeg[f]==0];seen=0
while queue:
    f=queue.pop();seen+=1
    for v in out[f]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert seen==140 and cover==424
# Exact integral Morse projection of critical 3-cell boundary.
def oriented_boundary(f):
    return [(f^(1<<i),(-1)**j) for j,i in enumerate(v for v in range(8) if f>>v&1)]
cache={}
def project(f):
    if f in cache:return cache[f]
    if f in remaining:val={f:1}
    elif f.bit_count()<mate[f].bit_count():
        top=mate[f];bd=oriented_boundary(top);eps=dict(bd)[f];val={}
        for b,sgn in bd:
            if b==f:continue
            for c,k in project(b).items():val[c]=val.get(c,0)-eps*sgn*k
        val={k:v for k,v in val.items() if v}
    else:val={}
    cache[f]=val;return val
b3={}
for f,s in oriented_boundary(204):
    for c,k in project(f).items():b3[c]=b3.get(c,0)+s*k
assert all(b3.get(c,0)==0 for c in [14,22,82,164])
# Full automorphism group: all point permutations preserving triples.
line_set=set(lines)
G=[p for p in permutations(range(8)) if {tuple(sorted(p[i] for i in ln)) for ln in lines}==line_set]
assert len(G)==48
center=[g for g in G if all(tuple(g[h[i]] for i in range(8))==tuple(h[g[i]] for i in range(8)) for h in G)]
assert len(center)==2
z=next(g for g in center if g!=tuple(range(8)))
blocks=sorted((i,z[i]) for i in range(8) if i<z[i]);assert len(blocks)==4

def sign_perm(seq):return (-1)**sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])
def fixed_signed_face(g,f):
    v=[i for i in range(8) if f>>i&1];a=[g[i] for i in v]
    return sign_perm(a) if sorted(a)==v else 0
# Independent mod-p H3 quotient cocycle. Cycle coefficients are integral and all critical calculations independent.
by={d:[f for f in faces if f.bit_count()-1==d] for d in range(5)}
index={d:{f:i for i,f in enumerate(by[d])} for d in range(5)}
zs={0:-1,1:1,3:1,4:1,5:-1,6:1,9:-1,13:1,14:1,15:-1,17:1,20:1,21:-1,22:-1,24:1,25:-1,32:1,34:-1,35:1}
zy={by[3][i]:coef for i,coef in zs.items()}
cz={f:0 for f in by[2]}
for top,coef in zy.items():
    for lo,s in oriented_boundary(top):cz[lo]+=coef*s
assert all(v==0 for v in cz.values())

def solve_mod(A, rhs,p):
    m=[[(x%p) for x in row]+[v%p] for row,v in zip(A,rhs)]
    n=len(m[0])-1;piv=[];r=0
    for j in range(n):
        k=next((k for k in range(r,len(m)) if m[k][j]),None)
        if k is None:continue
        m[r],m[k]=m[k],m[r];iv=pow(m[r][j],-1,p);m[r]=[v*iv%p for v in m[r]]
        for k in range(len(m)):
            if k!=r and m[k][j]:
                q=m[k][j];m[k]=[(a-q*b)%p for a,b in zip(m[k],m[r])]
        piv.append(j);r+=1
        if r==len(m):break
    assert all(any(row[:-1]) or row[-1]==0 for row in m)
    x=[0]*n
    for k,j in enumerate(piv):x[j]=m[k][-1]
    return x
# cochain kills boundaries of all eight 4-simplices, pairs to 1 with z.
rows=[]
for t in by[4]:
    row=[0]*len(by[3])
    for b,sgn in oriented_boundary(t):row[index[3][b]]+=sgn
    rows.append(row)
rows.append([zy.get(t,0) for t in by[3]])
chars={}
for prime in [3,5]:
    lam=solve_mod(rows,[0]*8+[1],prime)
    assert all(sum(a*b for a,b in zip(row,lam))%prime==rhs%prime for row,rhs in zip(rows,[0]*8+[1]))
    ct=[]
    for g in G:
        mapped={}
        for t,coef in zy.items():
            vs=[i for i in range(8) if t>>i&1];dest=sum(1<<g[i] for i in vs)
            mapped[dest]=mapped.get(dest,0)+coef*sign_perm([g[i] for i in vs])
        a=sum(lam[index[3][t]]*v for t,v in mapped.items())%prime
        assert a in {1,prime-1}
        ct.append(1 if a==1 else -1)
    chars[prime]=ct
assert chars[3]==chars[5] and set(chars[3])=={1}
char2=[];char3=chars[3];L=[]
for j,g in enumerate(G):
    red=-1+sum((-1)**(f.bit_count()-1)*fixed_signed_face(g,f) for f in faces)
    L.append(red)
    chi2=red+char3[j]
    char2.append(chi2)
    p4=tuple(blocks.index(tuple(sorted((g[a],g[b])))) for a,b in blocks)
    assert chi2==sign_perm(p4)*sum(i==p4[i] for i in range(4))
assert len(set(tuple(blocks.index(tuple(sorted((g[a],g[b])))) for a,b in blocks) for g in G))==24
assert Counter(char2)==Counter({0:18,1:16,-2:12,4:2})
assert sum(char2)==0 and sum(x*x for x in char2)==96 and sum(char3)==48
print('MK_VERIFY_OK: 8 lines, 140 faces, 424 covers, 67 acyclic pairs')
print('Morse critical dimensions (0:1,2:4,3:1); exact Morse boundary zero')
print('Automorphisms 48; central involution pairs',blocks,'and S4 quotient 24')
print('H3 trace: 1 for all 48 elements (independent F3/F5 quotient calculations)')
print('H2 trace counts: -2:12, 0:18, 1:16, 4:2; sign*four-pair permutation verified')
print('Fixed H2 dimension 0, fixed H3 dimension 1, H2 character inner product 2')
