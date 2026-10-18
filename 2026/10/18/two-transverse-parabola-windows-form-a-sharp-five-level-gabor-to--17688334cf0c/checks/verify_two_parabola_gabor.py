"""Standalone finite checks of exact Gabor projector-frame eigenvalue formulas.
Only the finite cases listed below are checked; the all-field theorem needs its proof.
Requires Python 3, and NumPy only for the optional full operator-matrix check.
"""
from collections import Counter
from itertools import product
from cmath import exp
from math import pi

class Field:
    def __init__(self, q):
        assert q in (3, 5, 7, 9)
        self.q=q
        self.p=3 if q==9 else q
        self.z=list(range(q))
    def unpack(self,x):
        return (x%3,x//3) if self.q==9 else (x,0)
    def add(self,x,y):
        if self.q==9:
            a,b=self.unpack(x); c,d=self.unpack(y)
            return (a+c)%3+3*((b+d)%3)
        return (x+y)%self.p
    def neg(self,x):
        if self.q==9:
            a,b=self.unpack(x)
            return (-a)%3+3*((-b)%3)
        return (-x)%self.p
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):
        if self.q==9:
            a,b=self.unpack(x); c,d=self.unpack(y)
            return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
        return (x*y)%self.p
    def tr(self,x):return ((2*(x%3))%3) if self.q==9 else x
    def psi(self,x):return exp(2j*pi*self.tr(x)/self.p)

def spectrum(q, full_matrix=False):
    F=Field(q); z=F.z; zero=0
    G=list(product(z,repeat=2))
    def subvec(u,v): return (F.sub(u[0],v[0]),F.sub(u[1],v[1]))
    def dot(u,v): return F.add(F.mul(u[0],v[0]), F.mul(u[1],v[1]))
    S0={(t,F.mul(t,t)) for t in z}
    S1={(F.mul(t,t),t) for t in z}
    spec=Counter(); errors=[]
    for shift in G:
        intersections=[tuple(u for u in S if subvec(u,shift) in S) for S in (S0,S1)]
        for freq in G:
            amps=[sum(F.psi(dot(freq,u)) for u in I)/q for I in intersections]
            lam=q*q*sum(abs(a)**2 for a in amps)
            val=round(lam)
            if abs(lam-val)>1.e-8:
                errors.append((shift,freq,lam))
            spec[val]+=1
    predicted=Counter({1:2*q*q*(q-1),2:q*q*(q-1)**2,q:2*(q-1),2*q:(q-1)**2,2*q*q:1})
    assert not errors,errors[:3]
    assert spec==predicted,(q,spec,predicted)
    assert sum(v*c for v,c in spec.items())==2*q**4
    assert sum(spec.values())==q**4
    print('q=',q,'eigenvalue multiplicities:',dict(sorted(spec.items())))
    if full_matrix:
        import numpy as np
        N=q*q
        ix={u:i for i,u in enumerate(G)}
        rows=[]
        for S in (S0,S1):
            g=np.array([1/(q**0.5) if u in S else 0 for u in G],dtype=complex)
            for shift in G:
                for freq in G:
                    h=np.array([F.psi(dot(freq,u))*g[ix[subvec(u,shift)]] for u in G])
                    P=np.outer(h,h.conj())
                    rows.append(P.T.reshape(-1))
        L=np.stack(rows)
        eig=np.linalg.eigvalsh(L.conj().T@L)
        target=np.array(sorted([v for v,c in spec.items() for _ in range(c)]))
        assert len(eig)==len(target)==N*N
        assert max(abs(eig-target))<1.e-7,max(abs(eig-target))
        print('q=',q,'full lifted-matrix eigenvalues independently verified', 'min=',eig[0],'max=',eig[-1])

if __name__=='__main__':
    for q in (3,5,7,9):spectrum(q,full_matrix=(q==3 or q==5))
    print('All finite checks passed; universal statement follows from the field-theoretic proof, not enumeration.')
