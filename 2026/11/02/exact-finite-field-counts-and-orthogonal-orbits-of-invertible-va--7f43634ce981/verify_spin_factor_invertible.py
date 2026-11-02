#!/usr/bin/env python3
"""Independent finite-field enumeration of invertible-value derivations of Jordan spin factors.

Usage: python verify_spin_factor_invertible.py
Only Python standard library is required. This is a finite corroboration, not the proof.
"""
import itertools

class Field:
    def __init__(self, q):
        self.q = q
        if q not in (3, 5, 7, 9):
            raise ValueError('field supported by this test')
        if q == 9:
            self.add = lambda x, y: ((x%3+y%3)%3) + 3*((x//3+y//3)%3)
            self.neg = lambda x: (-x%3)+3*(-(x//3)%3)
            self.mul = lambda x, y: ((x%3)*(y%3)+2*(x//3)*(y//3))%3 + 3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
            self.one = 1
        else:
            self.add=lambda x,y:(x+y)%q
            self.neg=lambda x:(-x)%q
            self.mul=lambda x,y:(x*y)%q
            self.one=1
        self.inv = {a: next(b for b in range(q) if self.mul(a,b)==1) for a in range(1,q)}
        self.squares={self.mul(x,x) for x in range(1,q)}
    def sub(self,x,y): return self.add(x,self.neg(y))
    def dot(self,x,y):
        out=0
        for a,b in zip(x,y): out=self.add(out,self.mul(a,b))
        return out

def rank(M,F):
    A=[row[:] for row in M]
    if not A: return 0
    h=len(A);w=len(A[0]);p=0
    for j in range(w):
        i=next((i for i in range(p,h) if A[i][j]),None)
        if i is None: continue
        A[p],A[i]=A[i],A[p]
        inv=F.inv[A[p][j]]
        A[p]=[F.mul(inv,z) for z in A[p]]
        for i in range(h):
            if i!=p and A[i][j]:
                a=A[i][j]
                A[i]=[F.sub(A[i][k],F.mul(a,A[p][k])) for k in range(w)]
        p+=1
        if p==h: break
    return p

def rank_image_basis(T,F):
    n=len(T)
    basis=[]
    for col in range(n):
        v=[T[i][col] for i in range(n)]
        if rank([[z[i] for z in basis+[v]] for i in range(n)],F)>len(basis):
            basis.append(v)
    return basis

def quad(v,diag,F):
    return F.dot([F.mul(diag[i],v[i]) for i in range(len(diag))],v)

def count_by_eta(q,diag):
    F=Field(q);n=len(diag);counts={};total=0
    positions=list(itertools.combinations(range(n),2))
    for coeff in itertools.product(range(q),repeat=len(positions)):
        K=[[0]*n for i in range(n)]
        for (i,j),x in zip(positions,coeff):
            K[i][j]=x;K[j][i]=F.neg(x)
        T=[[F.mul(F.inv[diag[i]],K[i][j]) for j in range(n)] for i in range(n)]
        basis=rank_image_basis(T,F)
        if len(basis)==0: continue
        anisotropic=True
        for coefficients in itertools.product(range(q),repeat=len(basis)):
            if not any(coefficients): continue
            v=[0]*n
            for b,c in zip(basis,coefficients):
                v=[F.add(v[i],F.mul(c,b[i])) for i in range(n)]
            if quad(v,diag,F)==0:
                anisotropic=False
                break
        if not anisotropic: continue
        assert len(basis)==2, ('unexpected anisotropic image dimension',q,diag,len(basis))
        T2=[[F.dot(T[i],[T[j][k] for j in range(n)]) for k in range(n)] for i in range(n)]
        tr=0
        for i in range(n): tr=F.add(tr,T2[i][i])
        eta=F.mul(tr,F.inv[2])
        assert eta not in F.squares and eta!=0, (q,diag,eta)
        total+=1;counts[eta]=counts.get(eta,0)+1
    return total,counts

def expected_planes(q,diag):
    F=Field(q);n=len(diag)
    if n<2:return 0
    if n%2:
        m=(n-1)//2
        return q**(2*m-1)*(q**(2*m)-1)//(2*(q+1))
    m=n//2
    discriminant=1
    for x in diag:discriminant=F.mul(discriminant,x)
    if m%2:discriminant=F.neg(discriminant)
    epsilon=1 if discriminant in F.squares else -1
    return q**(2*m-2)*(q**m-epsilon)*(q**(m-1)-epsilon)//(2*(q+1))

def run():
    cases=[(3,[1,1]),(3,[1,2]),(5,[1,1]),(5,[1,2]),
           (3,[1,1,1]),(5,[1,1,1]),(7,[1,1,1]),(9,[1,1,1]),
           (3,[1,1,1,1]),(3,[1,1,1,2]),(5,[1,1,1,1]),
           (3,[1,1,1,1,1])]
    for q,diag in cases:
        n=len(diag);N=expected_planes(q,diag)
        actual,by_eta=count_by_eta(q,diag)
        assert actual==(q-1)*N,(q,diag,actual,N)
        nonsquares=set(range(1,q))-Field(q).squares
        if N:
            assert set(by_eta)==nonsquares,(q,diag,by_eta)
            assert set(by_eta.values())=={2*N},(q,diag,by_eta,N)
        else: assert not by_eta
        print('OK q=%d dimension=%d diagonal=%s anisotropic_planes=%d derivations=%d orbit_sizes=%s'%(q,n,diag,N,actual,sorted(by_eta.values())))
    print('SPIN_FACTOR_IV_DERIVATIONS_OK',len(cases))
if __name__=='__main__':run()
