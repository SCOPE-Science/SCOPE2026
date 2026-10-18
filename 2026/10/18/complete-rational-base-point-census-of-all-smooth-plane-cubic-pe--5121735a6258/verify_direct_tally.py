#!/usr/bin/env python3
"""Independent full ordered-pair enumeration, without projective-orbit weights.

Input smooth_ids.txt is checked externally from exact geometric-smoothness
classifications. All partner and rational-base counts are recomputed here.
"""
import pathlib
import numpy as np
path=pathlib.Path(__file__).with_name('smooth_ids.txt')
S=np.loadtxt(path,dtype=np.int32,ndmin=1)
assert len(S)==16848 and len(np.unique(S))==len(S)
mon=[(i,j,3-i-j) for i in range(4) for j in range(4-i)]
pows=3**np.arange(10,dtype=np.int32)
D=((np.arange(59049,dtype=np.int32)[:,None]//pows[None,:])%3).astype(np.int16)
assert np.all(D[S, np.argmax(D[S]!=0,axis=1)]==1)
smooth=np.zeros(59049,dtype=np.bool_)
smooth[S]=True
smooth[np.sum((D[S]*2%3)*pows[None,:],axis=1)]=True
pts=[(x,y,1) for x in range(3) for y in range(3)]+[(x,1,0) for x in range(3)]+[(1,0,0)]
assert len(pts)==13
mask=np.zeros(len(S),dtype=np.uint16)
for k,p in enumerate(pts):
 evals=np.array([np.prod([p[j]**e[j] for j in range(3)])%3 for e in mon],dtype=np.int16)
 mask+=( ((D[S]@evals)%3)==0).astype(np.uint16)*(1<<k)
chunks=((np.arange(243,dtype=np.int16)[:,None]//(3**np.arange(5))[None,:])%3).astype(np.int16)
table={}
for b in (1,2):
 vals=(chunks[:,None,:]+b*chunks[None,:,:])%3
 table[b]=np.sum(vals*(3**np.arange(5))[None,None,:],axis=2).astype(np.int32)
A=S%243;B=S//243
hist=np.zeros(10,dtype=np.int64)
for fi,f in enumerate(S):
 u=table[1][f%243,A]+243*table[1][f//243,B]
 v=table[2][f%243,A]+243*table[2][f//243,B]
 valid=(smooth[u]&smooth[v]&(S!=f))
 common=np.bitwise_count(np.bitwise_and(mask[fi],mask[valid])).astype(np.int32)
 hist+=np.bincount(common,minlength=10)
assert np.all(hist%12==0)
print('smooth_cubic_forms',len(S))
print('ordered_generator_pairs',int(hist.sum()))
print('pencils',int(hist.sum()//12))
for i,v in enumerate(hist):print('base',i,'pencils',int(v//12))
