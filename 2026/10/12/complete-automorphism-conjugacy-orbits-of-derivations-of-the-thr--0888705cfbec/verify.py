#!/usr/bin/env python3
"""Direct finite-field orbit census for derivations of the 3D Heisenberg Lie algebra.
Run: python verify.py ; Python 3 standard library only."""
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):return (a^b) if self.q==4 else (a+b)%self.q
    def neg(self,a):return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        z=0
        for j in range(2):
            if b&(1<<j):z ^= a<<j
        if z&8:z ^= 0b1100  # reduce t^3=(t^2+t)=(t+1)+t=1? use polynomial t^2+t+1
        if z&4:z ^= 0b111
        return z
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)


def mx(F,B,A):
    a,b,c,d=B; e,f,g,h=A
    return (F.add(F.mul(a,e),F.mul(b,g)),F.add(F.mul(a,f),F.mul(b,h)),F.add(F.mul(c,e),F.mul(d,g)),F.add(F.mul(c,f),F.mul(d,h)))

def det(F,B):return F.sub(F.mul(B[0],B[3]),F.mul(B[1],B[2]))
def invert(F,B):
    a,b,c,d=B
    t=F.inv(det(F,B))
    return (F.mul(t,d),F.mul(t,F.neg(b)),F.mul(t,F.neg(c)),F.mul(t,a))

def conjugate(F,D,T):
    A=D[:4];u=D[4:]
    B,Bi,delta,v=T
    Ap=mx(F,mx(F,B,A),Bi)
    trace=F.add(A[0],A[3])
    # transformed row = (v (A-tr(A)I)+det(B)u) Bi
    t0=F.add(F.add(F.mul(v[0],F.sub(A[0],trace)),F.mul(v[1],A[2])),F.mul(delta,u[0]))
    t1=F.add(F.add(F.mul(v[0],A[1]),F.mul(v[1],F.sub(A[3],trace))),F.mul(delta,u[1]))
    up=(F.add(F.mul(t0,Bi[0]),F.mul(t1,Bi[2])), F.add(F.mul(t0,Bi[1]),F.mul(t1,Bi[3])))
    return Ap+up

def rank2(F,M):
    if det(F,M): return 2
    return 0 if M==(0,0,0,0) else 1

def independent_structure_check(q):
    # Exhaustively recover the automorphism and derivation matrix descriptions
    # from their defining bracket identities, independently of conjugation.
    F=Field(q); rng=range(q)
    def apply(M,w):
        return tuple(F.add(F.add(F.mul(M[i*3],w[0]),F.mul(M[i*3+1],w[1])),F.mul(M[i*3+2],w[2])) for i in range(3))
    def bracket(a,b): return (0,0,F.sub(F.mul(a[0],b[1]),F.mul(a[1],b[0])))
    e=((1,0,0),(0,1,0),(0,0,1))
    np_der=np_aut=0
    for M in product(rng,repeat=9):
        cols=[apply(M,x) for x in e]
        derivation= all(apply(M,bracket(e[i],e[j]))==tuple(F.add(a,b) for a,b in zip(bracket(cols[i],e[j]),bracket(e[i],cols[j]))) for i in range(3) for j in range(3))
        if derivation:
            np_der+=1
            assert M[2]==M[5]==0 and M[8]==F.add(M[0],M[4])
        automorphism= all(apply(M,bracket(e[i],e[j]))==bracket(cols[i],cols[j]) for i in range(3) for j in range(3))
        if automorphism and det(F,(M[0],M[1],M[3],M[4])):
            np_aut+=1
            assert M[2]==M[5]==0 and M[8]==det(F,(M[0],M[1],M[3],M[4]))
    assert np_der==q**6 and np_aut==q*q*(q*q-1)*(q*q-q),(q,np_der,np_aut)
    print('independent structural enumeration q=',q, 'derivations=',np_der,'automorphisms=',np_aut)

def verify(q):
    F=Field(q); field=range(q)
    units=[B for B in product(field,repeat=4) if det(F,B)]
    trans=[(B,invert(F,B),det(F,B),v) for B in units for v in product(field,repeat=2)]
    points=set(product(field,repeat=6))
    classes=[]
    while points:
        x=min(points)
        orbit={conjugate(F,x,T) for T in trans}
        assert orbit <=points,(q,x,len(orbit),len(orbit-points))
        points.difference_update(orbit)
        classes.append((x,len(orbit)))
    assert len(classes)==(q+1)**2,(q,len(classes))
    assert sum(size for _,size in classes)==q**6
    # Independently compute the centralizer and translation-rank orbit-size formula.
    for rep,sz in classes:
        A=rep[:4]; u=rep[4:]
        C=sum(mx(F,B,A)==mx(F,A,B) for B in units)
        sim_size=len(units)//C
        tr=F.add(A[0],A[3]);M=(F.sub(A[0],tr),A[1],A[2],F.sub(A[3],tr))
        rank=rank2(F,M)
        row_im={(F.add(F.mul(v[0],M[0]),F.mul(v[1],M[2])),F.add(F.mul(v[0],M[1]),F.mul(v[1],M[3]))) for v in product(field,repeat=2)}
        expected=sim_size*(q**rank if u in row_im else q*q-q**rank)
        assert sz==expected,(q,rep,sz,expected)
    # Each nonzero determinant similarity stratum has one orbit; each singular has two.
    nonsing=sum(det(F,rep[:4])!=0 for rep,_ in classes)
    assert nonsing==q*q-1,(q,nonsing)
    singular=[(rep,size) for rep,size in classes if det(F,rep[:4])==0]
    assert len(singular)==2*(q+1)
    print('q=',q,'group=',len(trans),'derivations=',q**6,'orbits=',len(classes),'nonsingular=',nonsing,'singular=',len(singular),'sum=',sum(s for _,s in classes))

if __name__=='__main__':
    for q in (2,3):independent_structure_check(q)
    for q in (2,3,4,5):verify(q)
    print('VERIFY_OK')
