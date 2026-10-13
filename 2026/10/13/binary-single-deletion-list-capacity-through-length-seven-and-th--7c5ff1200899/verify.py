"""Recompute finite binary single-deletion list-capacity profile.

Requires Python 3, NumPy, SciPy/HiGHS. No external data access.
Usage: python verify.py
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.sparse import lil_matrix
from scipy.optimize import milp, Bounds, LinearConstraint

ROOT = Path(__file__).resolve().parent
PROFILE = (16,33,50,65,81,96,112,128)
EARLIER = ((1,2),(2,3),(2,4),(4,7),(6,12),(10,19))

def delete_once(s):
    return set(s[:j]+s[j+1:] for j in range(len(s)))

def matrices(n):
    # Forward matrix: enumerate all deletions independently for each codeword.
    c=1<<n; r=1<<(n-1)
    forward=lil_matrix((r,c),dtype=np.int8)
    for x in range(c):
        s=format(x, f'0{n}b')
        for y in delete_once(s):forward[int(y,2) if y else 0,x]=1
    # Reverse matrix: enumerate all insertions independently for each received word.
    backward=lil_matrix((r,c),dtype=np.int8)
    for y in range(r):
        s=format(y,f'0{n-1}b') if n>1 else ''
        superseq=set(s[:j]+ch+s[j:] for j in range(n) for ch in '01')
        assert len(superseq)==n+1
        for w in superseq:backward[y,int(w,2)]=1
    f=forward.tocsc();b=backward.tocsc()
    assert (f!=b).nnz==0
    return f,b

def solve(n,L,reverse=False):
    F,B=matrices(n)
    c=1<<n; r=1<<(n-1)
    if reverse:
        # Complement/minimum multiple-covering formulation: every received
        # word has exactly n+1 binary one-insertion supersequences.
        A=B; demand=n+1-L
        constraint=LinearConstraint(A,np.full(r,demand),np.full(r,np.inf))
        objective=np.ones(c)
    else:
        A=F; constraint=LinearConstraint(A,np.zeros(r),np.full(r,L))
        objective=-np.ones(c)
    sol=milp(objective,integrality=np.ones(c),bounds=Bounds(0,1),
             constraints=constraint,options={'mip_rel_gap':0.0,'time_limit':45.0})
    assert sol.status==0, (n,L,reverse,sol.message)
    assert sol.mip_gap < 1e-7
    assert np.max(np.abs(sol.x-np.round(sol.x))) < 1e-5
    k=int(round(sol.fun))
    assert abs(sol.fun-k)<1e-5
    if reverse:
        # MIP lower bound sufficient to force integer optimum >= k.
        assert sol.mip_dual_bound > k-1+1e-5
        return c-k
    assert sol.mip_dual_bound > k-1+1e-5
    return -k

def verify():
    data=json.loads((ROOT/'witnesses.json').read_text(encoding='utf-8'))
    assert data['length']==7 and data['alphabet']=='01'
    assert set(data['profiles'])==set(str(i) for i in range(1,9))
    for L,witness in sorted(data['profiles'].items(), key=lambda a:int(a[0])):
        L=int(L)
        C=set(witness)
        assert len(C)==PROFILE[L-1] and len(C)==len(witness)
        assert all(len(x)==7 and set(x)<={'0','1'} for x in C)
        loads={format(i,'06b'):0 for i in range(64)}
        for word in C:
            for y in delete_once(word): loads[y]+=1
        assert max(loads.values())<=L,(L,max(loads.values()))
        # Complete lower bound is a concrete admissible family.
        m1=solve(7,L,False)
        assert m1==len(C),(L,m1,len(C))
        print(f'L={L}: optimum={m1}, direct MIP and dual incidence PASS')
    # The codewords are partitioned into eight VT classes. Each class
    # contains sixteen words, with pairwise disjoint single-deletion shadows.
    classes=[set() for _ in range(8)]
    for i in range(128):
        s=format(i,'07b')
        syndrome=sum(j+1 for j,bit in enumerate(s) if bit=='1')%8
        classes[syndrome].add(s)
    assert all(len(v)==16 for v in classes)
    for cls in classes:
        union=set()
        for w in cls:
            shadow=delete_once(w)
            assert union.isdisjoint(shadow)
            union.update(shadow)
    for n,(M1,M2) in enumerate(EARLIER, start=1):
        assert solve(n,1)==M1 and solve(n,2)==M2,(n,M1,M2)
        assert M2 <= 2*M1
    assert PROFILE[1]>2*PROFILE[0]
    print('VT-classes and first strict two-class capacity gap PASS')
    print('VERIFY_OK')

if __name__=='__main__':verify()
