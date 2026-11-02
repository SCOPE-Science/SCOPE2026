#!/usr/bin/env python3
"""Independent finite-field checks for a nilpotent-rank-one commutator census."""
from itertools import product

def add(x,y,q): return (x^y if q==4 else (x+y)%q)
def neg(x,q): return (x if q==4 else (-x)%q)
def mul(x,y,q):
    if q!=4: return x*y%q
    z=0
    for i in range(2):
        for j in range(2):
            if (x>>i)&1 and (y>>j)&1: z^=1<<(i+j)
    if z&8: z^=0b1110 # x^3=x^2+x in GF(4), though degree-two inputs never trigger this
    if z&4: z^=0b111 # x^2=x+1
    return z

def dot(a,b,q):
    s=0
    for x,y in zip(a,b): s=add(s,mul(x,y,q),q)
    return s

def mv(A,u,q):return [dot(row,u,q) for row in A]
def outer(u,v,q):return [[mul(x,y,q) for y in v] for x in u]
def matmul(A,B,q):return [[dot(row,col,q) for col in zip(*B)] for row in A]
def rank(A,q):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]);r=0
    for c in range(n):
        k=next((i for i in range(r,m) if A[i][c]!=0),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        inv=next(x for x in range(1,q) if mul(A[r][c],x,q)==1)
        A[r]=[mul(x,inv,q) for x in A[r]]
        for i in range(m):
            if i==r or A[i][c]==0: continue
            factor=A[i][c]
            A[i]=[add(x,neg(mul(factor,y,q),q),q) for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def jordan(parts):
    n=sum(parts); J=[[0]*n for _ in range(n)];o=0
    for length in parts:
        for j in range(length-1):J[o+j][o+j+1]=1
        o+=length
    return J

def L(d,q):return (q**d-1)//(q-1)
def formula(n,parts,q):
    b=len(parts);c=parts.count(1); k2=sum(min(2,z) for z in parts)
    A=(q**n-q**k2)*q**(n-3)//(q-1)
    B=(q**k2-q**b)*q**(n-2)//(q-1)
    C=((q**b-1)*q**(n-1)-(q**n-1))//(q-1)
    P=L(b-c,q)*L(b,q)+(L(b,q)-L(b-c,q))*L(b-1,q)
    N0=(q-1)*P
    N1=2*(L(b,q)*(q**(n-1)-1)-N0)
    return A,B,C,N0,N1

def test_case(n,parts,q):
    J=jordan(parts);JJ=matmul(J,J,q)
    count={};types={};zero_ranks={0:0,1:0,2:0}
    for u in product(range(q),repeat=n):
        if not any(u) or next(x for x in u if x)!=1:continue
        a=mv(J,u,q); aa=mv(JJ,u,q)
        for v in product(range(q),repeat=n):
            if not any(v) or dot(u,v,q):continue
            t=dot(a,v,q);s=dot(aa,v,q)
            # More independent construction, rather than use same rank-one commutator formula.
            X=outer(u,v,q)
            JX=matmul(J,X,q); XJ=matmul(X,J,q)
            C=[[add(JX[i][j],neg(XJ[i][j],q),q) for j in range(n)]for i in range(n)]
            rr=rank(C,q)
            count[t,s]=count.get((t,s),0)+1
            if (t,s)==(0,0):zero_ranks[rr]+=1
            if t:
                assert rr==2,(parts,q,u,v,'nonzero t rank')
                C2=matmul(C,C,q)
                if q==4 or q%2==0:
                    # In characteristic two C^2-t C = -s X, so the nonzero eigenspace
                    # has two one-dimensional blocks for s=0 and a size-two block otherwise.
                    residual=[[add(C2[i][j],mul(t,C[i][j],q),q) for j in range(n)] for i in range(n)]
                    assert rank(residual,q)==(1 if s else 0)
                else:
                    C3=matmul(C2,C,q)
                    residual=[[add(C3[i][j],neg(mul(mul(t,t,q),C[i][j],q),q),q) for j in range(n)] for i in range(n)]
                    assert rank(residual,q)==0
            elif s:
                assert rr==2 and rank(matmul(C,C,q),q)==1 and rank(matmul(matmul(C,C,q),C,q),q)==0,(parts,q,u,v,'index3')
            else:
                assert rr in (0,1,2)
                assert rank(matmul(C,C,q),q)==0,(parts,q,u,v,'square zero')
    A,B,C,N0,N1=formula(n,parts,q)
    for t in range(q):
        for s in range(q):
            expected=A+(B if s==0 else 0)+(C if (t,s)==(0,0) else 0)
            assert count.get((t,s),0)==expected,(n,parts,q,(t,s),count.get((t,s),0),expected)
    assert zero_ranks[0]==N0 and zero_ranks[1]==N1,(n,parts,q,zero_ranks,N0,N1)
    assert sum(count.values())==(q**n-1)*(q**(n-1)-1)//(q-1)
    return len(count),sum(count.values())

def partitions(n,hi=None):
    if n==0:yield ();return
    hi=n if hi is None else min(hi,n)
    for z in range(hi,0,-1):
        for rest in partitions(n-z,z):yield (z,)+rest

def main():
    cases=0; matrices=0
    for q,limit in ((2,6),(3,4),(4,3),(5,3)):
        for n in range(3,limit+1):
            for parts in partitions(n):
                _,num=test_case(n,parts,q)
                cases+=1;matrices+=num
    print('NILPOTENT_RANK_ONE_COMMUTATOR_MOMENT_SPECTRUM_OK',cases,matrices)
if __name__=='__main__':main()
