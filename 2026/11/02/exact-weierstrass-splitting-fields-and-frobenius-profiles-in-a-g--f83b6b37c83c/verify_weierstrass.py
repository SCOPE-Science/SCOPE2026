#!/usr/bin/env python3
"""Exact independent checks for Weierstrass splitting in a genus-two family.

Uses SymPy for rational polynomial identities; finite-field enumerations are
implemented independently in this file. Run: python verify_weierstrass.py.
"""
import sympy as S

t, x, z = S.symbols('t x z')
A=t*t-t+1
B=t-1
P=2*t**4-4*t**3+5*t**2-4*t+2
Q=16*t**4*x**4+8*P*x*x+1
U=t*(t*t+1)*(2*t*t+1)*(t*t+2)*(t*t-1)*(t**4+t*t+1)
assert S.expand(Q-((4*t*t*x*x+1)**2+16*(t*t+1)*(t-1)**2*x*x)) == 0
assert S.factor(S.resultant(4*x*x+t,Q,x)) == 256*(t-1)**4*(t*t-t+1)**4
assert S.factor(Q.subs(x,S.sqrt(-t)/2)) == (t-1)**2*(t*t-t+1)**2
assert S.expand(A*A-((t*t+1)*(t-1)**2+t*t)) == 0
I,T=S.symbols('I T')
red=S.groebner([I**2+1,T**2-(t*t+1)],I,T,t,order='lex')
for eps in (-1,1):
    for delta in (-1,1):
        root=I*(eps*A+delta*B*T)/(2*t*t)
        numerator=S.cancel(Q.subs(x,root))*(t**4)
        assert red.reduce(S.expand(S.cancel(numerator)))[1] == 0
print('EXACT_POLYNOMIAL_IDENTITIES_AND_FOUR_ROOTS_OK')

class Field:
    def __init__(self,p,degree):
        self.p=p;self.degree=degree;self.q=p**degree
        if degree==2:
            self.d=next(k for k in range(2,p) if pow(k,(p-1)//2,p)==p-1)
    def c(self,n):return n%self.p
    def add(self,a,b):
        p=self.p
        if self.degree==1:return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def neg(self,a):return self.sub(0,a)
    def sub(self,a,b):
        p=self.p
        if self.degree==1:return (a-b)%p
        return ((a%p-b%p)%p)+p*((a//p-b//p)%p)
    def mul(self,a,b):
        p=self.p
        if self.degree==1:return (a*b)%p
        a0,a1=a%p,a//p; b0,b1=b%p,b//p
        return ((a0*b0+self.d*a1*b1)%p)+p*((a0*b1+a1*b0)%p)
    def pow(self,a,n):
        assert n>=0
        r=self.c(1)
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a); n>>=1
        return r
    def chi(self,a):
        if a==0:return 0
        w=self.pow(a,(self.q-1)//2)
        assert w in (self.c(1),self.c(-1)),(self.q,a,w)
        return 1 if w==self.c(1) else -1
    def polynomial(self,tval,xval):
        # (4x^2+t)(16t^4x^4+8(2t^4-4t^3+5t^2-4t+2)x^2+1)
        mul=self.mul;add=self.add;sub=self.sub;pw=self.pow;c=self.c
        t2=pw(tval,2);t3=pw(tval,3);t4=pw(tval,4);x2=pw(xval,2)
        P=add(sub(add(sub(mul(c(2),t4),mul(c(4),t3)),mul(c(5),t2)),mul(c(4),tval)),c(2))
        qval=add(add(mul(mul(c(16),t4),pw(x2,2)),mul(mul(c(8),P),x2)),c(1))
        return mul(add(mul(c(4),x2),tval),qval)
    def admissible(self,tval):
        mul=self.mul;add=self.add;sub=self.sub;pw=self.pow;c=self.c
        t2=pw(tval,2); t4=pw(tval,4)
        return mul(mul(mul(mul(mul(tval,add(t2,c(1))),add(mul(c(2),t2),c(1))),add(t2,c(2))),sub(t2,c(1))),add(add(t4,t2),c(1))) !=0
    def wformula(self,tval):
        chi=self.chi;add=self.add;mul=self.mul;neg=self.neg;c=self.c
        return (2 if chi(neg(tval))==1 else 0)+(4 if chi(c(-1))==1 and chi(add(mul(tval,tval),c(1)))==1 else 0)
    def count_points(self,tval):
        mul=self.mul;add=self.add;sub=self.sub;c=self.c;pw=self.pow;chi=self.chi
        t2=pw(tval,2)
        L=mul(mul(add(t2,c(1)),add(sub(t2,tval),c(1))),sub(tval,c(1)))
        assert L!=0
        L_inv=pw(L,self.q-2)
        chi_sum=sum(chi(mul(self.polynomial(tval,xval),L_inv)) for xval in range(self.q))
        leading=mul(mul(c(64),pw(tval,4)),L_inv)
        return self.q+chi_sum+(2 if chi(leading)==1 else 0)

counts={}; total=0; ext_check=0; iso_check=0
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]:
    for d in (1,2) if p in (3,5,7,11) else (1,):
        F=Field(p,d); adm=0
        for tval in range(F.q):
            if not F.admissible(tval):continue
            adm+=1;total+=1
            roots=sum(F.polynomial(tval,xval)==0 for xval in range(F.q))
            assert roots==F.wformula(tval),(p,d,tval,roots,F.wformula(tval))
            minus=F.neg(tval)
            assert F.admissible(minus)
            other_roots=sum(F.polynomial(minus,xval)==0 for xval in range(F.q))
            assert other_roots==F.wformula(minus)
            if F.q%4==3:assert sorted([roots,other_roots])==[0,2]
            if F.q%4==1:assert roots==other_roots
            if d==1 or p<=11:
                pts=F.count_points(tval)
                ptsother=F.count_points(minus)
                assert pts==ptsother,('same-zeta',p,d,tval,pts,ptsother)
                iso_check+=1
        counts[(p,d)]=adm
        if d==2:
            E=F;Fbase=Field(p,1)
            for tval in range(p):
                if not Fbase.admissible(tval):continue
                roots=[r for r in range(E.q) if E.polynomial(tval,r)==0]
                assert len(roots)==6,('full quadratic splitting',p,tval,len(roots))
                assert all(E.pow(r,p*p)==r for r in roots)
                fixed=[r for r in roots if E.pow(r,p)==r]
                assert len(fixed)==Fbase.wformula(tval)
                ext_check+=1
        print(f'FIELD_OK p={p} degree={d} q={F.q} admissible={adm}')
print(f'WEIERSTRASS_AND_JACOBIAN_COMPATIBILITY_PASS parameter_cases={total} pair_point_counts={iso_check} quadratic_splitting_cases={ext_check}')
