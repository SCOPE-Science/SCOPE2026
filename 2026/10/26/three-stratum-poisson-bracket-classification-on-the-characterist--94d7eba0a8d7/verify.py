#!/usr/bin/env python3
"""Standalone finite-field tests for four-dimensional Poisson bracket classification.

All computations are built from explicit polynomial-basis arithmetic, independent of
normal-form elimination arguments. Run with Python 3; no dependencies.
"""
from itertools import product

class Field:
    def __init__(self, degree):
        self.degree=degree
        self.q=1<<degree
        self.poly={1:0b11,2:0b111}[degree]
        self.elems=range(self.q)
        self.table=[[self._mul(i,j) for j in self.elems] for i in self.elems]
        self.inverse={a:next(b for b in self.elems if self.table[a][b]==1)
                      for a in range(1,self.q)}
    def _mul(self,a,b):
        out=0
        while b:
            if b&1:out^=a
            b>>=1
            a<<=1
            if a&self.q:a^=self.poly
        return out
    def m(self,a,b):return self.table[a][b]
    def mul(self,A,B):
        m=self.m;a,b,c,d=A;e,f,g,h=B
        return (m(a,e), m(a,f)^m(b,e), m(a,g)^m(c,e),
                m(a,h)^m(d,e)^m(b,g)^m(c,f))
    def add(self,A,B):return tuple(x^y for x,y in zip(A,B))
    def scl(self,a,V):return tuple(self.m(a,v) for v in V)
    def dx(self,V):return (V[1],0,V[3],0)
    def dy(self,V):return (V[2],V[3],0,0)
    def jacobian(self,X,Y):
        return self.add(self.mul(self.dx(X),self.dy(Y)),
                        self.mul(self.dy(X),self.dx(Y)))
    def bracket(self,V,W,F):return self.mul(F,self.jacobian(V,W))
    def invunit(self,V):
        a,b,c,d=V;assert a
        ia=self.inverse[a]
        n=self.scl(ia,(0,b,c,d))
        assert self.mul(n,n)==(0,0,0,0)
        return self.scl(ia,self.add((1,0,0,0),n))
    def phi(self,F,X,Y):
        return self.add(self.add(self.scl(F[0],(1,0,0,0)),self.scl(F[1],X)),
                        self.add(self.scl(F[2],Y),self.scl(F[3],self.mul(X,Y))))
    def change(self,F,X,Y):
        J=self.jacobian(X,Y)
        assert J[0]
        return self.mul(self.phi(F,X,Y),self.invunit(J))

def check(degree):
    K=Field(degree);q=K.q
    one=(1,0,0,0);zero=(0,0,0,0)
    basis=[one,(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    brackets=list(product(K.elems,repeat=4))
    for F in brackets:
        for V in basis:
            assert K.bracket(V,V,F)==zero
        for V,W,T in product(basis,repeat=3):
            jac=K.add(K.add(K.bracket(V,K.bracket(W,T,F),F),
                            K.bracket(W,K.bracket(T,V,F),F)),
                      K.bracket(T,K.bracket(V,W,F),F))
            assert jac==zero,(degree,F,V,W,T)
    autos=[]
    for u,v,w,z in product(K.elems,repeat=4):
        delta=K.m(u,z)^K.m(v,w)
        if not delta:continue
        for s,t in product(K.elems,repeat=2):
            X=(0,u,v,s);Y=(0,w,z,t)
            assert K.mul(X,X)==zero and K.mul(Y,Y)==zero
            assert K.jacobian(X,Y)[0]==delta
            autos.append((X,Y))
    expected_aut=(q*q-1)*(q*q-q)*q*q
    assert len(autos)==expected_aut,(degree,len(autos),expected_aut)
    orbits=[]
    for d in K.elems:
        for rep,size in [((1,0,0,d),(q-1)*q*q),
                         ((0,1,0,d),q*q-1),
                         ((0,0,0,d),1)]:
            orbit=set(K.change(rep,X,Y) for X,Y in autos)
            assert len(orbit)==size,(degree,rep,len(orbit),size)
            assert all(F[3]==d for F in orbit)
            orbits.append(orbit)
    all_brackets=set().union(*orbits)
    assert len(all_brackets)==q**4
    assert sum(map(len,orbits))==q**4
    for i in range(len(orbits)):
        for j in range(i):
            assert orbits[i].isdisjoint(orbits[j])
    print(f"char2_GF_{q}: PASS, all {q**4} brackets satisfy Jacobi; "
          f"{len(autos)} automorphisms; {len(orbits)} disjoint exact isomorphism orbits")

if __name__=='__main__':
    for degree in (1,2):check(degree)
    print('VERIFY_OK')
