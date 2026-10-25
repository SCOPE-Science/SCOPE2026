"""Exact arithmetic checks of two quartic bitangent configurations.
Only finite-field arithmetic and exhaustive projective-line enumeration; stdlib.
"""
from itertools import product

class Field:
    def __init__(self, poly):
        self.poly = tuple(t % 3 for t in poly) # monic irreducible
        self.n = len(poly)-1
        self.q = 3**self.n
        self.coords = [tuple((a // (3**i))%3 for i in range(self.n)) for a in range(self.q)]
        self.add = [[self.idx(tuple((x+y)%3 for x,y in zip(a,b))) for b in self.coords] for a in self.coords]
        self.mul = [[self.mul_tuples(a,b) for b in self.coords] for a in self.coords]
        self.neg = [self.idx(tuple(-x % 3 for x in a)) for a in self.coords]
        self.zero = 0
        self.one = 1
        self.inv = [None] + [next(j for j in range(1,self.q) if self.mul[i][j] == 1) for i in range(1,self.q)]
    def idx(self,c): return sum(v*3**i for i,v in enumerate(c))
    def mul_tuples(self,a,b):
        w=[0]*(2*self.n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): w[i+j] = (w[i+j]+x*y)%3
        for k in range(len(w)-1,self.n-1,-1):
            v=w[k]
            if v:
                for i,c in enumerate(self.poly[:-1]): w[k-self.n+i]=(w[k-self.n+i]-v*c)%3
        return self.idx(w[:self.n])
    def M(self,a,b): return self.mul[a][b]
    def A(self,a,b): return self.add[a][b]
    def N(self,a): return self.neg[a]
    def S(self,a,b): return self.A(a,self.N(b))
    def P(self,a,k):
        res=1
        while k:
            if k&1: res=self.M(res,a)
            a=self.M(a,a);k//=2
        return res

def coeffs_on_line(K,kind,s,t):
    # directly expand F(x,y,s*x+t*y) over char 3
    # F_1=(x*x+y*y)^2+y^3*z-y*z^3;
    # F_2=x^4+y^3*z-y*z^3.
    A=1
    B=K.N(K.P(s,3))
    C=2 if kind==1 else 0
    D=s
    E=K.S(K.A((1 if kind==1 else 0),t),K.P(t,3))
    return A,B,C,D,E

def is_square_form(K,coeff):
    A,B,C,D,E=coeff
    if A:
        # seek A*(x*x + v*x*y + w*y*y)^2
        v=K.M(B,K.inv[K.M(2,A)])
        w=K.M(K.S(C,K.M(A,K.P(v,2))),K.inv[K.M(2,A)])
        return K.M(2,K.M(v,w))==D and K.M(A,K.P(w,2))==E
    raise AssertionError('All considered forms have A=1')

def alternative_square_form(K,kind,s,t):
    # With A=1, brute force every quadratic u*x*x+v*x*y+w*y*y.
    # Quadratic must have u=+/-1. Coefficients y^4 etc compared in GF(q).
    A,B,C,D,E=coeffs_on_line(K,kind,s,t)
    for v in range(K.q):
        for w in range(K.q):
            if (K.M(2,v)==B and K.A(K.P(v,2),K.M(2,w))==C
                and K.M(2,K.M(v,w))==D and K.P(w,2)==E):
                return (v,w)
    return None

def run(kind,n,poly):
    K=Field(poly)
    bitangents=[]
    for s in range(K.q):
        for t in range(K.q):
            f=coeffs_on_line(K,kind,s,t)
            if is_square_form(K,f):
                bitangents.append((s,t))
    # Additional lines with projection (x,y) degenerate: y=0 only.
    assert K.q==3**n
    # Count hyperflex and ordinary bitangent lines via contact quadratic discriminant.
    ordinary=hyperflex=0
    for s,t in bitangents:
        A,B,C,D,E=coeffs_on_line(K,kind,s,t)
        v=K.M(B,K.inv[2]); w=K.M(K.S(C,K.P(v,2)),K.inv[2])
        discr=K.S(K.P(v,2),K.M(1,w)) # 4=1 modulo 3
        if discr==0: hyperflex+=1
        else: ordinary+=1
        assert alternative_square_form(K,kind,s,t)==(v,w)
    hyperflex+=1 # y=0
    print('F',kind,'GF(3^'+str(n)+')','bitangents=',len(bitangents)+1,'ordinary=',ordinary,'hyperflex=',hyperflex)
    # Frobenius permutation cycle lengths, including line y=0 fixed.
    points=set(bitangents)
    cycles=[1]
    while points:
        a=min(points); x=a; c=0
        while x in points:
            points.remove(x);c+=1;x=(K.P(x[0],3),K.P(x[1],3))
        assert x==a
        cycles.append(c)
    from collections import Counter
    print('orbit lengths:',dict(sorted(Counter(cycles).items())))
    if kind==1 and n==3:
        assert (len(bitangents),ordinary,hyperflex)==(27,27,1)
        assert Counter(cycles)==Counter({1:10,3:6})
    if kind==2 and n==4:
        assert (len(bitangents),ordinary,hyperflex)==(27,0,28)
        assert Counter(cycles)==Counter({1:4,4:6})

if __name__=='__main__':
    run(1,3,[1,2,0,1])
    run(2,4,[2,0,1,0,1])
    print('VERIFY_OK')
