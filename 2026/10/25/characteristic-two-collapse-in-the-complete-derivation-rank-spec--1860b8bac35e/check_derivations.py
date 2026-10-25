#!/usr/bin/env python3
"""Independent finite-field linear-algebra checks for derivations of a radical-cube-zero free algebra."""
from itertools import product
from collections import Counter
import sys

def make_field(q):
    if q==4:
        def add(a,b): return a^b
        def mul(a,b):
            c=0
            for i in range(2):
                if b>>i&1: c^=a<<i
            if c&8: c^=0b1100
            if c&4: c^=0b111
            return c
        return add,mul
    return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q

def RREF_rank(A,q):
    add,mul=make_field(q);ch=2 if q==4 else q
    v=[x[:] for x in A];R=len(v);C=len(v[0]) if R else 0;j=0
    for c in range(C):
        k=next((i for i in range(j,R) if v[i][c]),None)
        if k is None:continue
        v[k],v[j]=v[j],v[k]
        for i in range(j+1,R):
            if not v[i][c]:continue
            u=v[i][c];pivot=v[j][c]
            for z in range(c,C):
                v[i][z]=add(mul(pivot,v[i][z]),mul(u,(-v[j][z])%q if q!=4 else v[j][z]))
        j+=1
        if j==R:break
    return j

def dr(M,B,q):
    add,mul=make_field(q)
    a,b,c,d=M
    T=[ [add(a,a),b,b,0],
        [c,add(a,d),0,b],
        [c,0,add(a,d),b],
        [0,c,c,add(d,d)] ]
    return [[a,b,0,0,0,0], [c,d,0,0,0,0]] + [[B[2*i],B[2*i+1]]+T[i] for i in range(4)]

def predicted(q):
    # number full rank for 2x2 finite matrices
    gl=q*(q-1)*(q*q-1)
    rank0=1
    rank1=(q**4-1)*(q+1)
    rank2=(q**4-1)*(q**4-q)
    if q%2:
        s=(q*q-1);sem=q*s; invtrace=q*q*(q-1)
        counts={0:rank0,1:rank1,2:rank2,
            3:s*q**6,
            4:s*(q**8-q**6)+sem*q**7+invtrace*q**8,
            5:sem*(q**8-q**7),
            6:(gl-invtrace)*q**8}
    else:
        s=(q+1)*(q*q-1)
        counts={0:rank0,1:rank1,2:rank2+(q-1)*q**8,
            3:s*q**6,
            4:s*(q**8-q**6)+(gl-(q-1))*q**8}
    assert sum(counts.values())==q**12,(q,counts,sum(counts.values()),q**12)
    return counts

def verify(q,all_B=False):
    add,mul=make_field(q)
    cnt=Counter();strata=Counter();import random;random.seed(q)
    Ms=list(product(range(q),repeat=4))
    Bset=list(product(range(q),repeat=8)) if all_B else [tuple(random.randrange(q) for _ in range(8)) for _ in range(250)]
    for M in Ms:
        Mmat=[[M[0],M[1]],[M[2],M[3]]]
        rM=RREF_rank(Mmat,q)
        z=dr(M,(0,)*8,q)
        t=RREF_rank([r[2:] for r in z[2:]],q)
        strata[(rM,t)]+=1
        for B in Bset:
            rr=RREF_rank(dr(M,B,q),q)
            cnt[rr]+=1
    exp=predicted(q)
    print('q=',q,'full_B',all_B,'strata',dict(sorted(strata.items())),'observed',dict(sorted(cnt.items())),'predicted',exp,'total',sum(exp.values()))
    if all_B:
        assert dict(cnt)==exp,(cnt,exp)
    else:
        assert set(cnt).issubset(set(exp))
        assert all(exp[k]>0 for k in cnt)

if __name__=='__main__':
    verify(2,True)
    verify(3,True)
    verify(4,False)
    verify(5,False)
    # Independently check Leibniz for all basic word products in sampled cases.
    import random
    rng=random.Random(314159)
    basis=['','x','y','xx','xy','yx','yy']
    def prod(i,j):
        s=basis[i]+basis[j]
        return basis.index(s) if len(s)<3 else -1
    for q in (2,3,4,5):
        add,mul=make_field(q)
        for _ in range(160):
            M=[rng.randrange(q) for z in range(4)]
            B=[rng.randrange(q) for z in range(8)]
            block=dr(M,B,q)
            D=[[0]*7 for _ in range(7)]
            for row in range(6):
                for col in range(6):D[row+1][col+1]=block[row][col]
            for i in range(7):
                for j in range(7):
                    ij=prod(i,j)
                    for out in range(7):
                        rhs=0
                        for u in range(7):
                            if prod(u,j)==out:rhs=add(rhs,mul(D[u][i],1))
                            if prod(i,u)==out:rhs=add(rhs,mul(D[u][j],1))
                        lhs=D[out][ij] if ij!=-1 else 0
                        assert lhs==rhs,(q,M,B,i,j,out,lhs,rhs)
    print('LEIBNIZ_BASIS_OK')
    print('DERIVATION_SPECTRUM_OK')
