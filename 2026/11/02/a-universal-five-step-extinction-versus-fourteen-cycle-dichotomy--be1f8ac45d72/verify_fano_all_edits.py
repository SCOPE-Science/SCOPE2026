#!/usr/bin/env python3
"""All 49 one-edge Fano incidence mutations, using an independent cyclic model."""
import numpy as np

def rank2(a):
    a = np.array(a, dtype=np.uint8, copy=True)
    h, w = a.shape
    k = 0
    for j in range(w):
        pivot = next((i for i in range(k, h) if a[i,j]), None)
        if pivot is None: continue
        if pivot != k: a[[pivot,k]]=a[[k,pivot]]
        for i in range(h):
            if i!=k and a[i,j]: a[i] ^= a[k]
        k += 1
        if k==h: break
    return k

def matmul(a,b): return (a.astype(np.int64) @ b.astype(np.int64) % 2).astype(np.uint8)

def mpower(a,t):
    r=np.eye(a.shape[0],dtype=np.uint8)
    while t:
        if t&1:r=matmul(r,a)
        a=matmul(a,a)
        t//=2
    return r

b=np.zeros((7,7),dtype=np.uint8)
for p in range(7):
    for ell in range(7):
        if (p-ell)%7 in (0,1,3):b[p,ell]=1
assert all(np.sum(b[i]&b[j])==1 for i in range(7) for j in range(i+1,7))
assert rank2(b)==4
counts={"delete":0,"add":0}
for p in range(7):
    for ell in range(7):
        tag='delete' if b[p,ell] else 'add'
        c=b.copy();c[p,ell]^=1
        a=np.block([[np.zeros((7,7),dtype=np.uint8),c],[c.T,np.zeros((7,7),dtype=np.uint8)]])
        assert rank2(c)==5
        ranks=[rank2(mpower(a,t)) for t in range(6)]
        if tag=='delete':
            assert ranks==[14,10,6,4,2,0]
        else:
            assert ranks==[14,10,6,6,6,6]
            assert np.array_equal(mpower(a,16),mpower(a,2))
            assert not np.array_equal(mpower(a,9),mpower(a,2))
            assert rank2((mpower(a,7)^np.eye(14,dtype=np.uint8)))==11
            assert rank2((a^np.eye(14,dtype=np.uint8)))==14
        counts[tag]+=1
print('Fano cyclic-incidence test: all 49 edge toggles pass: ',counts)
print('Power ranks, 7/14-order, fixed-space checks: ALL_CHECKS_PASS')
