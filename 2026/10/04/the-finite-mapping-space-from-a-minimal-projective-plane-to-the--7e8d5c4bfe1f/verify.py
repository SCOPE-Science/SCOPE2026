#!/usr/bin/env python3
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
cert=json.loads((HERE/'beat_certificate.json').read_text('utf-8'))
source=cert['source_points']; N=len(source); idx={x:i for i,x in enumerate(source)}
le=[[False]*N for _ in range(N)]
for i in range(N): le[i][i]=True
for x,y in cert['covers']: le[idx[x]][idx[y]]=True
for k in range(N):
    for i in range(N):
        if le[i][k]:
            for j in range(N):
                if le[k][j]: le[i][j]=True
# Sanity: three ranks 4+6+3 and all covers respect them.
assert N==13 and source[:4]==['c1','c2','c3','c4'] and source[4:10]==['b1','b2','b3','b4','b5','b6']
T=range(4)
tle=[[False]*4 for _ in T]
for i in T: tle[i][i]=True
for lo in (0,1):
    for hi in (2,3): tle[lo][hi]=True
preds=[[j for j in range(i) if le[j][i] and j!=i] for i in range(N)]
maps=[]; cur=[None]*N
def rec(i):
    if i==N:
        maps.append(tuple(cur)); return
    for y in T:
        if all(tle[cur[j]][y] for j in preds[i]):
            cur[i]=y; rec(i+1)
    cur[i]=None
rec(0)
assert len(maps)==cert['map_count']==868
M=len(maps)
up=[0]*M; down=[0]*M
for i,f in enumerate(maps):
    bits=0
    for j,g in enumerate(maps):
        if all(tle[f[q]][g[q]] for q in range(N)):
            bits|=1<<j
    up[i]=bits
for i in range(M):
    for j in range(M):
        if (up[j]>>i)&1: down[i]|=1<<j
# Full comparability graph components.
allbits=(1<<M)-1; seen=0; comps=[]
while seen!=allbits:
    rem=allbits & ~seen; seed=(rem & -rem).bit_length()-1
    stack=[seed]; seen|=1<<seed; n=0
    while stack:
        u=stack.pop(); n+=1
        nb=(up[u]|down[u]) & allbits & ~seen
        while nb:
            l=nb&-nb; v=l.bit_length()-1; nb-=l; seen|=l; stack.append(v)
    comps.append(n)
assert comps==cert['component_sizes']==[868]

def beat_info(x, alive):
    su=(up[x]&alive)&~(1<<x)
    if su:
        zbits=su
        while zbits:
            l=zbits&-zbits; z=l.bit_length()-1; zbits-=l
            if (up[z]&su)==su: return ('up',z)
    sd=(down[x]&alive)&~(1<<x)
    if sd:
        zbits=sd
        while zbits:
            l=zbits&-zbits; z=l.bit_length()-1; zbits-=l
            if (down[z]&sd)==sd: return ('down',z)
    return None
alive=allbits; counts={'up':0,'down':0}
for step,e in enumerate(cert['deletions']):
    x=e['map_index']; kind=e['kind']; witness=e['witness_index']
    assert (alive>>x)&1, (step,'deleted')
    assert (alive>>witness)&1, (step,'witness absent')
    bi=beat_info(x,alive)
    assert bi==(kind,witness), (step,e,bi)
    counts[kind]+=1; alive&=~(1<<x)
remaining=[i for i in range(M) if (alive>>i)&1]
assert len(cert['deletions'])==864
assert counts==cert['deletion_counts']=={'up':196,'down':668}
assert remaining==cert['constant_map_indices']==[0,491,814,867]
# Remaining maps are exactly constants and have target order C.
for v,i in enumerate(remaining): assert maps[i]==(v,)*N
for u,iu in enumerate(remaining):
    for v,iv in enumerate(remaining):
        assert bool((up[iu]>>iv)&1)==tle[u][v]
for x in remaining: assert beat_info(x,alive) is None
print('VERIFY_OK maps=868 components=1 deletions=864 up=196 down=668 core=4')
