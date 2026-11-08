"""Independent small-case vertex/edge-coordinate Euclidean inball checks.
Only the public theorem's combinatorial H-description is used."""
import math
from itertools import combinations
import numpy as np
from scipy.optimize import linprog

def candidate(n):
    D=max(n+2+math.sqrt(1+2/n), n+1+math.sqrt(n+1))
    return 1/D

def facet_orbits(n):
    # Build all original-space inequalities, excluding duplicate representatives.
    N=n*n+2*n
    def vx(i): return i
    def vy(j): return n+j
    def ve(i,j): return 2*n+n*i+j
    F=[]
    for k in range(N):
        row=np.zeros(N);row[k]=-1;F.append((row,0.,'coord'))
    for i in range(n):
        row=np.zeros(N);row[vx(i)]=1
        for j in range(n):row[ve(i,j)]=1
        F.append((row,1.,'degree'))
    for j in range(n):
        row=np.zeros(N);row[vy(j)]=1
        for i in range(n):row[ve(i,j)]=1
        F.append((row,1.,'degree'))
    for i in range(n):
        for j in range(n):
            row=np.zeros(N);row[vx(i)]=row[vy(j)]=row[ve(i,j)]=1
            F.append((row,1.,'edge'))
    for t in range(2,n+1):
        for A in combinations(range(n),t):
            for B in combinations(range(n),t):
                row=np.zeros(N)
                for i in A:row[vx(i)]=1
                for j in B:row[vy(j)]=1
                for i in A:
                    for j in B:row[ve(i,j)]=1
                F.append((row,float(t),'balanced'))
    # All 2023 nonbalanced lifted facets, including transposed orientations.
    for u in range(2,n):
        for v in range(u+1,n+1):
            for swap in (False,True):
                for Ai in combinations(range(n),u):
                    for Bj in combinations(range(n),v):
                        for a in range(1,u):
                            for b in range(a):
                                if b==0 and a!=1:continue
                                beta=1+(v-u)/(a-b)
                                for AA in combinations(Ai,a):
                                    for BB in combinations(Bj,b):
                                        row=np.zeros(N)
                                        for i in Ai:row[vy(i) if swap else vx(i)]=1
                                        for j in Bj:row[vx(j) if swap else vy(j)]=1
                                        for i in Ai:
                                            for j in Bj:row[ve(j,i) if swap else ve(i,j)]=1
                                        for i in AA:row[vy(i) if swap else vx(i)]=beta
                                        for j in BB:row[vx(j) if swap else vy(j)]=beta
                                        for i in AA:
                                            for j in BB:row[ve(j,i) if swap else ve(i,j)]=beta
                                        F.append((row,u+a*(beta-1),'nonbalanced'))
    return F

def check(n):
    F=facet_orbits(n);N=2*n+n*n
    A=np.stack([np.r_[row,np.linalg.norm(row)] for row,b,t in F]); b=np.array([b for row,b,t in F]);
    obj=np.zeros(N+1);obj[-1]=-1
    sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(None,None)]*N+[(0,None)],method='highs')
    assert sol.success,sol.message
    R=candidate(n)
    assert abs(sol.x[-1]-R)<1e-7,(n,sol.x[-1],R)
    c=np.full(N,R); margins=b-np.array([row@c+np.linalg.norm(row)*R for row,b,t in F]);
    assert np.min(margins)>-1e-9, (n,np.min(margins))
    tight={}
    for (row,b,t),slack in zip(F,margins):
        if abs(slack)<1e-8:tight[t]=tight.get(t,0)+1
    if n in (2,3):expected={'coord':N,'balanced':1}
    else:expected={'coord':N,'degree':2*n}
    assert tight==expected,(n,tight,expected)
    # distinct centers? force every coordinate to min or max, fixed radius
    C=np.stack([row for row,b,t in F]); rhs=np.array([b-R*np.linalg.norm(row) for row,b,t in F]);
    for k in range(N):
        p=np.zeros(N);p[k]=1
        mi=linprog(p,A_ub=C,b_ub=rhs,bounds=[(None,None)]*N,method='highs')
        ma=linprog(-p,A_ub=C,b_ub=rhs,bounds=[(None,None)]*N,method='highs')
        assert mi.success and ma.success
        assert abs(mi.fun+ma.fun)<1e-7,(n,k,mi.fun,ma.fun)
        assert abs(mi.x[k]-R)<1e-7
    print('LP_IREM',n,'facets',len(F),'radius',R,'contacts',tight)

def check_inequality_orbits():
    for r in range(2,31):
        D=max(r+2+math.sqrt(1+2/r),r+1+math.sqrt(r+1))
        closest=(float('-inf'),None)
        for u in range(2,r):
            for v in range(u+1,r+1):
                for a in range(1,u):
                    for b in range(a):
                        if b==0 and a!=1: continue
                        t=(v-u)/(a-b);M=a+b+a*b;N=u+v+u*v; B=u+a*t
                        inv=(N+t*M+math.sqrt(N+(t*t+2*t)*M))/B
                        assert inv < D - 1e-8, (r,u,v,a,b,inv,D)
                        if inv>closest[0]:closest=(inv,(u,v,a,b))
        print('ORBIT',r,'max-nonbalanced-denominator',round(closest[0],7), 'optimal-denominator',round(D,7))
if __name__=='__main__':
    check_inequality_orbits()
    for n in (2,3,4):check(n)
    print('BALANCED_TOTAL_MATCHING_INBALL_VERIFIED')
