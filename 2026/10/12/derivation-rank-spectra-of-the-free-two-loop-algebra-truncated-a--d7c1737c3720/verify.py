#!/usr/bin/env python3
"""Direct finite-field checks for derivations of two-loop radical-cube-zero algebra.
All data and tests are mathematical; no external dependencies.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        self.q=q
        if q==4:
            self.add=[[i^j for j in range(4)] for i in range(4)]
            def mul(a,b):
                r=0
                for x in range(2):
                    for y in range(2):
                        if (a>>x)&1 and (b>>y)&1:r^=1<<(x+y)
                # t^2=t+1
                if r&4:r^=7
                return r
            self.mul=[[mul(i,j) for j in range(4)] for i in range(4)]
        else:
            self.add=[[(i+j)%q for j in range(q)] for i in range(q)]
            self.mul=[[(i*j)%q for j in range(q)] for i in range(q)]
        self.neg=[next(k for k in range(q) if self.add[i][k]==0) for i in range(q)]
        self.inv=[None]+[next(k for k in range(1,q) if self.mul[i][k]==1) for i in range(1,q)]
    def rank(self,mat):
        a=[r[:] for r in mat]; m=len(a); n=len(a[0]); k=0
        for col in range(n):
            ix=next((i for i in range(k,m) if a[i][col]),None)
            if ix is None:continue
            a[k],a[ix]=a[ix],a[k]
            z=self.inv[a[k][col]]
            a[k]=[self.mul[z][v] for v in a[k]]
            for i in range(k+1,m):
                v=a[i][col]
                if v:
                    a[i]=[self.add[a[i][j]][self.neg[self.mul[v][a[k][j]]]] for j in range(n)]
            k+=1
            if k==m:break
        return k
    def plus(self,x,y):return self.add[x][y]
    def times(self,x,y):return self.mul[x][y]

def derivation(A,B,F):
    # 6x6 matrix on radical basis x,y,xx,xy,yx,yy.
    # A: two columns each of 2 linear coefficients
    # B: two columns each of 4 quadratic coefficients
    M=[[0]*6 for i in range(6)]
    for j in range(2):
        for i in range(2):M[i][j]=A[2*j+i]
        for i in range(4):M[2+i][j]=B[4*j+i]
    # D(uv) = D(u)v + uD(v)
    for x in range(2):
        for y in range(2):
            c=2+2*x+y
            for i in range(2):
                M[2+2*i+y][c]=F.plus(M[2+2*i+y][c],A[2*x+i])
                M[2+2*x+i][c]=F.plus(M[2+2*x+i][c],A[2*y+i])
    return M

def predict(q):
    G=(q*q-1)*(q*q-q)
    nil=q*q-1
    rk1=(q+1)*(q*q-1)
    N0=1
    N1=(q**4-1)*(q*q-1)//(q-1)
    N2=(q**4-1)*(q**4-q)
    d=Counter({0:N0,1:N1,2:N2})
    if q%2:
        rank1diag=q*(q*q-1)
        traceless=q*q*(q-1)
        nontrace=G-traceless
        # nilpotent A rank1, L rank2, a1, quotient dimension2
        d[3]+=nil*q**6
        d[4]+=nil*q**6*(q*q-1)
        # semisimple rank1, L rank3, a1, quotient dim1
        d[4]+=rank1diag*q**7
        d[5]+=rank1diag*q**7*(q-1)
        # invertible traceless A, L rank2
        d[4]+=traceless*q**8
        # invertible nontrace A, L rank4
        d[6]+=nontrace*q**8
    else:
        scalar=q-1
        non_scalar_invert=G-scalar
        # nonzero scalars, L rank0
        d[2]+=scalar*q**8
        # rank1, L rank2
        d[3]+=rk1*q**6
        d[4]+=rk1*q**6*(q*q-1)
        # rank2 nonscalar, L rank2
        d[4]+=non_scalar_invert*q**8
    assert sum(d.values())==q**12,(q,d)
    return d

def sample_exhaust(q,all_B=False):
    F=Field(q); tgt=predict(q); d=Counter(); vals=range(q)
    for A in product(vals,repeat=4):
        if not all_B:
            # sample fixed B patterns; test matrix rank vs quotient method
            Biter=[(0,)*8]+[tuple((j*j+5*j+z)%q for j in range(8)) for z in range(20)]
        else:Biter=product(vals,repeat=8)
        a=F.rank([[A[0],A[2]],[A[1],A[3]]])
        for B in Biter:
            M=derivation(A,B,F)
            r=F.rank(M)
            d[r]+=1
            assert r>=a
            if r>6:raise AssertionError(r)
    if all_B:assert d==tgt,(q,d,tgt)
    print('EXHAUSTIVE' if all_B else 'SAMPLED','q=',q,'direct=',sorted(d.items()),'prediction=',sorted(tgt.items()))

def independent_leibniz_dimension(q):
    F=Field(q)
    # Basis: 1,x,y,xx,xy,yx,yy; multiplication by concatenation.
    words=[(),(0,),(1,),(0,0),(0,1),(1,0),(1,1)]
    index={w:i for i,w in enumerate(words)}
    def prod(i,j):
        w=words[i]+words[j]
        return index.get(w,-1) if len(w)<3 else -1
    eq=[]
    # Coordinate unknown D[row][col].
    for i in range(7):
        for j in range(7):
            k=prod(i,j)
            for row in range(7):
                e=[0]*49
                if k>=0:e[7*k+row]=F.plus(e[7*k+row],1)
                for t in range(7):
                    if prod(t,j)==row:
                        e[7*i+t]=F.plus(e[7*i+t],F.neg[1])
                    if prod(i,t)==row:
                        e[7*j+t]=F.plus(e[7*j+t],F.neg[1])
                eq.append(e)
    rr=F.rank(eq)
    assert 49-rr==12,(q,rr)
    print('LEIBNIZ_SYSTEM',q,'variables',49,'rank',rr,'derivations dimension',49-rr)

if __name__=='__main__':
    independent_leibniz_dimension(2)
    independent_leibniz_dimension(3)
    for q in (2,3,4,5,7,8,9,11):
        if q not in (2,3,4,5,7,11):continue
        print('FORMULA',q,sorted(predict(q).items()))
    sample_exhaust(2,True)
    sample_exhaust(3,True)
    sample_exhaust(4,False)
    print('VERIFY_OK_FREE_TRUNC_DERIV')
