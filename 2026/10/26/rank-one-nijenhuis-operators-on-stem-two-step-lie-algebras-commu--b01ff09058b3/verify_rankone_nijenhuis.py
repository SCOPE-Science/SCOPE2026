#!/usr/bin/env python3
"""Independently enumerate rank-one Nijenhuis operators on selected stem class-two Lie algebras."""
import itertools
from collections import Counter

def rank(M,q):
    A=[list(row) for row in M]; i=0
    if not A: return 0
    for j in range(len(A[0])):
        pivot=next((z for z in range(i,len(A)) if A[z][j]%q),None)
        if pivot is None: continue
        A[i],A[pivot]=A[pivot],A[i]
        inv=pow(A[i][j],-1,q); A[i]=[(x*inv)%q for x in A[i]]
        for z in range(len(A)):
            if z!=i:
                t=A[z][j]%q
                A[z]=[(x-t*y)%q for x,y in zip(A[z],A[i])]
        i+=1
        if i==len(A):break
    return i

def check(d,c,brackets,q):
    D=d+c
    vec=list(itertools.product(range(q),repeat=D))
    nv=[v for v in vec if any(v)]
    def comm(u,v):
        z=[0]*c
        for (i,j),a in brackets.items():
            for k,val in enumerate(a): z[k]=(z[k]+(u[i]*v[j]-u[j]*v[i])*val)%q
        return tuple(z)
    e=[tuple(int(i==j) for i in range(D)) for j in range(D)]
    comm_e={(i,j):comm(e[i],e[j]) for i in range(D) for j in range(i+1,D)}
    torsion=0; nonsquare=0
    for f in nv:
        a=f[:d]; b=f[d:]
        for w in nv:
            fw=sum(x*y for x,y in zip(f,w))%q
            gw=[sum(b[k]*v for k,v in enumerate(comm(w,e[i])))%q for i in range(D)]
            good=True
            for i in range(D):
                for j in range(i+1,D):
                    cij=comm_e[i,j]
                    hij=sum(b[k]*cij[k] for k in range(c))%q
                    if (f[i]*gw[j]-f[j]*gw[i]-fw*hij)%q:
                        good=False;break
                if not good:break
            if good:
                torsion+=1
                if fw: nonsquare+=1
    torsion//=q-1; nonsquare//=q-1
    rs=Counter()
    for b in itertools.product(range(q),repeat=c):
        if not any(b):continue
        B=[[sum(b[k]*comm_e[i,j][k] for k in range(c))%q if i<j else
            -sum(b[k]*comm_e[j,i][k] for k in range(c))%q if j<i else 0
             for j in range(d)] for i in range(d)]
        rs[rank(B,q)]+=1
    expected=((q**d-1)*(q**D-1)+q**d*sum(count*(q**(D-r-1)-1) for r,count in rs.items()))//(q-1)
    expect_nonzero=(q**d-1)*q**(D-1)
    assert torsion==expected and nonsquare==expect_nonzero,(d,c,q,torsion,expected,nonsquare,expect_nonzero)
    print('OK',f'd={d} c={c} q={q}', 'rank_spectrum='+str(sorted(rs.items())), 'total='+str(torsion), 'N_square_nonzero='+str(nonsquare))
    return torsion

if __name__=='__main__':
    check(2,1,{(0,1):(1,)},2)
    check(2,1,{(0,1):(1,)},3)
    check(3,3,{(0,1):(1,0,0),(0,2):(0,1,0),(1,2):(0,0,1)},2)
    check(3,2,{(0,1):(1,0),(0,2):(0,1)},2)
    check(3,2,{(0,1):(1,0),(0,2):(0,1)},3)
    check(4,1,{(0,1):(1,),(2,3):(1,)},2)
    check(2,1,{(0,1):(1,)},5)
    print('RANK_ONE_STEM_NIJENHUIS_OK')
