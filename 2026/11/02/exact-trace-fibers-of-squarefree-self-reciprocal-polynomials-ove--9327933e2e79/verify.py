"""Exhaustive checks for the odd-characteristic self-reciprocal trace law.
Runs with Python 3 and standard library only.
"""
from itertools import product
from math import comb

class F:
    def __init__(self,p,d=None):
        self.p=p; self.d=d; self.q=p if d is None else p*p
        if d is not None: assert all((a*a)%p!=d%p for a in range(p))
    def coords(self,a): return (a%self.p,a//self.p) if self.d is not None else (a,0)
    def add(self,a,b):
        x,y=self.coords(a);u,v=self.coords(b)
        return (x+u)%self.p + (self.p*((y+v)%self.p) if self.d is not None else 0)
    def neg(self,a):
        x,y=self.coords(a)
        return (-x)%self.p + (self.p*((-y)%self.p) if self.d is not None else 0)
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        x,y=self.coords(a);u,v=self.coords(b)
        return (x*u+self.d*y*v)%self.p + self.p*((x*v+y*u)%self.p) if self.d is not None else (a*b)%self.p
    def pow(self,a,n):
        b=1
        while n:
            if n&1:b=self.mul(b,a)
            a=self.mul(a,a);n//=2
        return b
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)
    def ev(self,pol,x):
        a=0
        for c in pol[::-1]: a=self.add(self.mul(a,x),c)
        return a
    def trim(self,pol):
        pol=list(pol)
        while pol and pol[-1]==0:pol.pop()
        return pol
    def remainder(self,a,b):
        a=self.trim(a);b=self.trim(b)
        assert b
        lead_inv=self.inv(b[-1])
        while len(a)>=len(b):
            factor=self.mul(a[-1],lead_inv)
            shift=len(a)-len(b)
            for i,x in enumerate(b):a[i+shift]=self.sub(a[i+shift],self.mul(factor,x))
            a=self.trim(a)
        return a
    def gcd_deg(self,a,b):
        a=self.trim(a);b=self.trim(b)
        while b:a,b=b,self.remainder(a,b)
        return len(a)-1
    def squarefree(self,g):
        deriv=[self.mul(i%self.p,g[i]) for i in range(1,len(g))]
        return self.gcd_deg(g,deriv)==0

def total(q,n):
    def c(k):
        return sum(q**a * (-1)**(k-a)*(k-a+1) for a in range(k+1))
    return c(n)-(q*c(n-2) if n>=2 else 0)

def predicted(field,n,c):
    p,q=field.p,field.q
    s=total(q,n)
    assert (s-(-1)**n*(n+1))%q==0
    main=(s-(-1)**n*(n+1))//q
    m=sum(c==(-2*n+4*j)%p for j in range(n+1))
    return main+(-1)**n*m

def reciprocal_transform(ff,g):
    n=len(g)-1
    f=[0]*(2*n+1)
    for j,a in enumerate(g):
        for t in range(j+1):
            idx=n-j+2*t
            f[idx]=ff.add(f[idx],ff.mul(a,comb(j,t)%ff.p))
    assert f[-1]==1 and f[0]==1
    assert f[2*n-1]==g[n-1] if n>=1 else True
    assert f==f[::-1]
    return f

if __name__=='__main__':
    cases=[(3,None,6),(5,None,5),(7,None,4),(11,None,3),(3,2,4),(5,2,3)]
    polynomials=0;fibers=0;tested=0;direct_transform_checks=0
    for p,d,maxn in cases:
        ff=F(p,d)
        for n in range(1,maxn+1):
            actual=[0]*ff.q
            for coeffs in product(range(ff.q),repeat=n):
                g=list(coeffs)+[1]
                ok=bool(ff.ev(g,2%p) and ff.ev(g,(-2)%p) and ff.squarefree(g))
                if n<=3:
                    f=reciprocal_transform(ff,g)
                    assert ff.squarefree(f)==ok,(p,d,n,g,f)
                    direct_transform_checks+=1
                if ok:
                    actual[coeffs[-1]]+=1
                polynomials+=1
            expect=[predicted(ff,n,c) for c in range(ff.q)]
            assert actual==expect,(p,d,n,actual,expect)
            assert (len(set(actual))==1)==(ff.q==p and (n+1)%p==0)
            assert sum(actual)==total(ff.q,n)
            tested+=1;fibers+=ff.q
    print('VERIFY_OK cases=%d fibers=%d polynomials=%d direct_transform_checks=%d'%(tested,fibers,polynomials,direct_transform_checks))
