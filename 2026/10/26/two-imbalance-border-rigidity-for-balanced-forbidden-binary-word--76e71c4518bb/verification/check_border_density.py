#!/usr/bin/env python3
"""Independent finite checks for balanced forbidden binary factors."""
import itertools
import math
import numpy as np


def borders(w):
    return [j for j in range(1,len(w)+1) if w[:j]==w[-j:]]

def imbalance(w,j):
    return 2*w[:j].count('1')-j

def transition_matrices(w):
    k=len(w)
    M=np.zeros((k,k),dtype=float)
    M1=np.zeros_like(M)
    for i in range(k):
        for a in '01':
            s=w[:i]+a
            if s.endswith(w):
                continue
            j=max(j for j in range(k) if s.endswith(w[:j]))
            M[i,j]+=1
            if a=='1': M1[i,j]+=1
    return M,M1

def measure(w):
    M,M1=transition_matrices(w)
    eig,R=np.linalg.eig(M)
    idx=np.argmax(eig.real)
    lam=float(eig[idx].real)
    r=np.real(R[:,idx]);
    eigl,L=np.linalg.eig(M.T)
    l=np.real(L[:,np.argmin(np.abs(eigl-lam))])
    rho=float((l@M1@r)/(lam*(l@r)))
    return lam,rho


def run():
    tested=0
    near=0
    bad=[]
    grouped={}
    for k in (4,6,8,10):
      count=0
      for bits in itertools.product('01',repeat=k):
        w=''.join(bits)
        if w.count('1')*2!=k:continue
        B=borders(w)
        wrong=[j for j in B if imbalance(w,j)!=0]
        if len(wrong)>2:continue
        lam,rho=measure(w)
        p=sum(imbalance(w,j)*lam**j for j in B)
        sign_rho=0 if abs(rho-0.5)<1e-9 else (1 if rho>0.5 else -1)
        sign_p=0 if abs(p)<1e-8 else (-1 if p>0 else 1)
        if sign_rho!=sign_p:bad.append((w,lam,rho,p,B))
        if len(wrong)==2 and imbalance(w,wrong[0])*imbalance(w,wrong[1])<0:near+=1
        count+=1
      tested+=count;grouped[k]=count
    assert not bad, bad[:5]
    w='100011110001';B=borders(w)
    lam,rho=measure(w)
    assert B==[1,5,12],B
    assert [(j,imbalance(w,j)) for j in B]==[(1,1),(5,-1),(12,0)]
    assert rho>0.5
    print('Balanced test words checked:',tested,'by length:',grouped)
    print('Mixed-sign two-imbalanced-border cases:',near)
    print('Every test matched sign of border polynomial (or exact balance).')
    print('Motivating word:',w,'borders with imbalance:',[(j,imbalance(w,j)) for j in B])
    print('Perron root: %.12f; limiting one frequency: %.12f'%(lam,rho))
    print('P(lambda) = %.12f'%(sum(imbalance(w,j)*lam**j for j in B)))
    print('Theorem is a symbolic proof; finite tests are illustrative only.')
if __name__=='__main__':run()
