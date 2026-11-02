#!/usr/bin/env python3
"""Direct finite-field checks for the Poisson-bracket classification and centre bounds."""
from itertools import product
from random import Random

class Field:
    def __init__(self,q):
        self.q=q
        self.p=2 if q in (2,4) else q
    def add(self,a,b):return a^b if self.p==2 else (a+b)%self.p
    def neg(self,a):return a if self.p==2 else (-a)%self.p
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.p
        r=0
        for _ in range(2):
            if b&1:r^=a
            b >>=1; a<<=1
            if a&4:a^=7
        return r
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)

class Algebra:
    def __init__(self,m,n,q):
        self.m=m;self.n=n;self.F=Field(q)
        self.bs=list(product(range(m),range(n)))
        self.ids={x:i for i,x in enumerate(self.bs)}
        self.N=m*n
        self.a=int(m%self.F.p!=0);self.b=int(n%self.F.p!=0)
        self.admissible=[i for i,(u,v) in enumerate(self.bs) if u>=self.a and v>=self.b]
    def mulpoly(self,v,w):
        F=self.F;r=[0]*self.N
        for i,(a,b) in enumerate(self.bs):
            if not v[i]:continue
            for j,(c,d) in enumerate(self.bs):
                if not w[j] or a+c>=self.m or b+d>=self.n:continue
                k=self.ids[(a+c,b+d)]
                r[k]=F.add(r[k],F.mul(v[i],w[j]))
        return r
    def monom(self,i):
        a=[0]*self.N;a[i]=1;return a
    def bracket(self,v,w,f):
        F=self.F;r=[0]*self.N
        for i,(a,b) in enumerate(self.bs):
            if not v[i]:continue
            for j,(c,d) in enumerate(self.bs):
                if not w[j]:continue
                coeff=(a*d-b*c)%F.p
                if coeff==0:continue
                z=self.mulpoly(f,self.monom_shift(a+c-1,b+d-1))
                vcoeff=F.mul(F.mul(v[i],w[j]),coeff)
                for k in range(self.N):
                    if z[k]:r[k]=F.add(r[k],F.mul(z[k],vcoeff))
        return r
    def monom_shift(self,i,j):
        a=[0]*self.N
        if 0<=i<self.m and 0<=j<self.n:a[self.ids[(i,j)]]=1
        return a
    def centre_dim(self,f):
        F=self.F;cols=[]
        x=self.monom(self.ids[(1,0)]);y=self.monom(self.ids[(0,1)])
        for i in range(self.N):
            mon=self.monom(i)
            cols.append(self.bracket(mon,x,f)+self.bracket(mon,y,f))
        rows=[list(row) for row in zip(*cols)]
        rank=0
        for j in range(self.N):
            pivot=next((t for t in range(rank,2*self.N) if rows[t][j]),None)
            if pivot is None:continue
            rows[rank],rows[pivot]=rows[pivot],rows[rank]
            z=F.inv(rows[rank][j]);rows[rank]=[F.mul(z,v) for v in rows[rank]]
            for t in range(rank+1,2*self.N):
                if not rows[t][j]:continue
                w=rows[t][j]
                rows[t]=[F.add(a,F.neg(F.mul(w,b))) for a,b in zip(rows[t],rows[rank])]
            rank+=1
        return self.N-rank
    def predicted_generic_centre(self):
        p=self.F.p;m=self.m;n=self.n;a=self.a;b=self.b
        return sum(int(((j%p==0) or (a and i==m-1)) and ((i%p==0) or (b and j==n-1))) for i,j in self.bs)
    def jacobi_basis(self,f):
        for a in range(self.N):
            va=self.monom(a)
            for b in range(self.N):
                vb=self.monom(b)
                for c in range(self.N):
                    vc=self.monom(c)
                    t1=self.bracket(va,self.bracket(vb,vc,f),f)
                    t2=self.bracket(vb,self.bracket(vc,va,f),f)
                    t3=self.bracket(vc,self.bracket(va,vb,f),f)
                    if any(self.F.add(self.F.add(x,y),z)!=0 for x,y,z in zip(t1,t2,t3)):
                        raise AssertionError(('Jacobi',a,b,c))
    def run(self,full=True):
        rng=Random(self.m*1000+self.n*100+self.F.q)
        d=len(self.admissible)
        assert d==(self.m-self.a)*(self.n-self.b)
        if full:
            it=product(range(self.F.q),repeat=d)
        else:
            it=(tuple(rng.randrange(self.F.q) for _ in range(d)) for _ in range(120))
        genericdim=self.predicted_generic_centre()
        soc=[0]*self.N;soc[self.ids[(self.m-1,self.n-1)]]=1
        assert self.centre_dim(soc)==self.N-2
        checked=0;generic=0;positive=0;jac=0
        for arr in it:
            f=[0]*self.N
            for k,v in zip(self.admissible,arr):f[k]=v
            cd=self.centre_dim(f)
            is_generic=f[self.ids[(self.a,self.b)]]!=0
            if is_generic:
                assert cd==genericdim,(self.m,self.n,self.F.q,f,cd,genericdim)
                generic+=1
            if any(f):
                assert genericdim<=cd<=self.N-2,(self.m,self.n,self.F.q,f,cd)
                positive+=1
            else:assert cd==self.N
            if jac<3:
                self.jacobi_basis(f);jac+=1
            checked+=1
        if full:
            assert checked==self.F.q**d
            assert generic==(self.F.q-1)*self.F.q**(d-1)
        print('PASS', (self.m,self.n,self.F.q),'complete' if full else 'sample',checked,'generic',generic,'centre_min',genericdim,'centre_max_nonzero',self.N-2,'jacobi_cases',jac)

if __name__=='__main__':
    for m,n,q,full in [(2,2,2,True),(2,2,3,True),(2,3,2,True),(2,3,3,True),(3,3,2,True),(3,4,2,True),(3,3,4,True),(3,3,3,False),(4,4,3,False),(3,5,5,False)]:
        Algebra(m,n,q).run(full)
    print('TRUNCATED_POISSON_CENTRE_OK')
