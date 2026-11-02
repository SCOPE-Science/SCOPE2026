"""Exhaustive test of least-period-two counts for norm-lift binomial permutations.
Run: python verify_zieve_cycle.py
No external dependencies.
"""
from itertools import product

class Field:
    def __init__(self, p, modulus):
        self.p = p
        self.poly = tuple(z % p for z in modulus)
        self.d = len(modulus)-1
        assert self.poly[-1] == 1
        self.zero = (0,)*self.d
        self.one = (1,) + (0,)*(self.d-1)
        self.all = list(product(range(p), repeat=self.d))
        self.q = p**self.d
    def co(self, a):
        if isinstance(a, tuple):return a
        return (a%self.p,) + (0,)*(self.d-1)
    def add(self,a,b):return tuple((u+v)%self.p for u,v in zip(a,b))
    def neg(self,a):return tuple((-u)%self.p for u in a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        d,p=self.d,self.p
        t=[0]*(2*d-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b):t[i+j]=(t[i+j]+u*v)%p
        for j in range(2*d-2,d-1,-1):
            coeff=t[j]
            if coeff:
                for i in range(d):t[j-d+i]=(t[j-d+i]-coeff*self.poly[i])%p
        return tuple(t[:d])
    def pow(self,a,n):
        z=self.one
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n//=2
        return z
    def char(self,a):
        if a==self.zero:return 0
        return 1 if self.pow(a,(self.q-1)//2)==self.one else -1

class Quadratic:
    # E=K[alpha]/(alpha^2 - M alpha + N)
    def __init__(self,base,M,N):
        self.k=base;self.M=M;self.N=N
        self.zero=(base.zero,base.zero)
        self.one=(base.one,base.zero)
        self.alpha=(base.zero,base.one)
        self.all=list(product(base.all, repeat=2))
    def add(self,x,y):
        k=self.k
        return (k.add(x[0],y[0]),k.add(x[1],y[1]))
    def mul(self,x,y):
        k=self.k;a,b=x;c,d=y
        bd=k.mul(b,d)
        return (k.sub(k.mul(a,c),k.mul(self.N,bd)),
                k.add(k.add(k.mul(a,d),k.mul(b,c)),k.mul(self.M,bd)))
    def pow(self,x,n):
        v=self.one
        while n:
            if n&1:v=self.mul(v,x)
            x=self.mul(x,x);n//=2
        return v
    def norm(self,x):
        k=self.k;a,b=x
        return k.add(k.add(k.mul(a,a),k.mul(self.M,k.mul(a,b))),k.mul(self.N,k.mul(b,b)))
    def F(self,x,alpha=None):
        if alpha is None:alpha=self.alpha
        return self.mul(x,self.add((self.norm(x),self.k.zero),alpha))
    def counts(self,alpha=None):
        if alpha is None:alpha=self.alpha
        fixed=two=0
        for x in self.all:
            y=self.F(x,alpha)
            if y==x:fixed+=1
            elif self.F(y,alpha)==x:two+=1
        return fixed,two

FIELDS=[(2,[0,1]),(2,[1,1,0,1]),(3,[0,1]),(3,[1,0,1]),(3,[2,2,0,1]),
        (5,[0,1]),(11,[0,1]),(17,[0,1]),(23,[0,1])]

def check():
    total=0
    for p,poly in FIELDS:
        K=Field(p,poly);q=K.q
        if q%3==1:continue
        if p!=3:
            for mu in K.all:
                if mu==K.zero:continue
                M=K.mul(K.co(3),mu)
                N=K.mul(K.co(3),K.mul(mu,mu))
                E=Quadratic(K,M,N)
                choices=[E.alpha,(M,K.neg(K.one))]
                # conjugate alpha' = M-alpha
                for alpha in choices:
                    got=E.counts(alpha)
                    assert got==(1,0),(q,mu,got)
                    total+=1
        else:
            for beta in K.all:
                if K.char(beta)!=-1:continue
                E=Quadratic(K,K.zero,K.neg(beta))
                expected=2*(q+1) if K.char(K.sub(beta,K.one))==1 else 0
                for alpha in [E.alpha,(K.zero,K.neg(K.one))]:
                    got=E.counts(alpha)
                    assert got==(1,expected),(q,beta,got,expected)
                    total+=1
        print('verified q=',q,'parameter cases=',2*(q-1) if p!=3 else q-1)
    all_coeffs=0
    direct_power=0
    for p,poly in FIELDS:
        K=Field(p,poly);q=K.q
        if q%3==1:continue
        if p==3:
            beta=next(b for b in K.all if K.char(b)==-1)
            E=Quadratic(K,K.zero,K.neg(beta))
        else:E=Quadratic(K,K.co(3),K.co(3))
        candidates=[x for x in E.all if x[1]!=K.zero]
        if q>11:candidates=candidates[:40]
        for ai,alpha in enumerate(candidates):
            tr=K.add(K.mul(K.co(2),alpha[0]),K.mul(E.M,alpha[1]))
            if tr!=K.zero:expect=0
            else:
                assert p!=2
                aa=E.mul(alpha,alpha)
                assert aa[1]==K.zero
                expect=2*(q+1) if K.char(K.sub(aa[0],K.one))==1 else 0
            got=E.counts(alpha)
            assert got==(1,expect),(q,alpha,got,expect)
            all_coeffs+=1
            if ai<3:
                for x in E.all:
                    fp=E.add(E.pow(x,q+2),E.mul(alpha,x))
                    assert E.F(x,alpha)==fp
                    direct_power+=1
    print('VERIFY_OK permutation_parameters=',total,'general_parameters=',all_coeffs,'direct_power_checks=',direct_power)

if __name__=='__main__':check()
