#!/usr/bin/env python3
"""Independent finite-field Cartier calculation, rebuilding f^2 and f^4 in x."""
class FiniteField:
    def __init__(self, n):
        self.n=n; self.size=7**n
        # theta^2=-1 or theta^3=-2: both are irreducible over F_7.
        self.mod={1:[0,1],2:[1,0,1],3:[2,0,0,1]}[n]
        self.digits=[tuple((i//(7**j))%7 for j in range(n)) for i in range(self.size)]
        self.add=[[sum(((self.digits[i][j]+self.digits[k][j])%7)*(7**j)
                         for j in range(n)) for k in range(self.size)]
                         for i in range(self.size)]
        self.mul=[[self._multiply(i,k) for k in range(self.size)]
                         for i in range(self.size)]
        self.neg=[self.minus(i) for i in range(self.size)]
        self.one=1
    def _multiply(self,i,j):
        c=[0]*(2*self.n-1)
        for a,x in enumerate(self.digits[i]):
            for b,y in enumerate(self.digits[j]): c[a+b]=(c[a+b]+x*y)%7
        for k in range(len(c)-1,self.n-1,-1):
            z=c[k]
            for j in range(self.n): c[k-self.n+j]=(c[k-self.n+j]-z*self.mod[j])%7
        return sum(c[k]*7**k for k in range(self.n))
    def plus(self,a,b):return self.add[a][b]
    def minus(self,a):return sum((-x%7)*7**k for k,x in enumerate(self.digits[a]))
    def times(self,a,b):return self.mul[a][b]
    def power(self,a,e):
        out=1
        while e:
            if e&1:out=self.times(out,a)
            a=self.times(a,a);e>>=1
        return out
    def inverse(self,a):
        assert a!=0
        return self.power(a,self.size-2)
    def eval(self, coeff, z):
        v=0
        for a in reversed(coeff):v=self.plus(self.times(v,z),a)
        return v
    def polynomial_multiply(self,p,q):
        out=[0]*(len(p)+len(q)-1)
        for i,a in enumerate(p):
            if not a:continue
            for j,b in enumerate(q):
                if b:out[i+j]=self.plus(out[i+j],self.times(a,b))
        return out
    def direct_cartier(self,a,b):
        f=[1,0,b,0,a,0,1]
        f2=self.polynomial_multiply(f,f)
        f4=self.polynomial_multiply(f2,f2)
        # Ordered basis dx/y, dx/y^2, x dx/y^2, x^2 dx/y^2
        scalar=f2[6]
        odd=f4[12]
        B=[[f4[6],f4[4]],[f4[20],f4[18]]]
        return scalar,odd,B
    def discriminant(self,a,b):
        T=self.times;A=self.plus
        a2=T(a,a);a3=T(a2,a);b2=T(b,b);b3=T(b2,b)
        return A(A(A(A(T(a2,b2),T(3,a3)),T(3,b3)),self.minus(T(3,T(a,b)))),1)

def verify(n):
    K=FiniteField(n);T=K.times;A=K.plus
    counts={(0,4):0,(2,2):0,(2,1):0,'singular':0}
    matches=0;marked=[]
    for a in range(K.size):
      for b in range(K.size):
        Delta=K.discriminant(a,b)
        if Delta==0:counts['singular']+=1;continue
        v=K.plus(T(a,b),1)
        c,odd,B=K.direct_cartier(a,b)
        assert c==T(2,v)
        assert odd==K.minus(Delta)
        det=K.plus(T(B[0][0],B[1][1]),K.minus(T(B[0][1],B[1][0])))
        assert det==T(T(2,v),Delta)
        full_det=T(T(c,odd),det)
        assert full_det==T(T(3,T(v,v)),T(Delta,Delta))
        if v:
            assert full_det
            counts[(0,4)]+=1
        else:
            assert b and c==0 and odd and det==0
            assert any(z for row in B for z in row)
            P=[[K.power(z,7) for z in row] for row in B]
            BB=[[A(T(P[i][0],B[0][j]),T(P[i][1],B[1][j]))
                   for j in range(2)] for i in range(2)]
            rk=1 if any(z for row in BB for z in row) else 0
            # Evaluate the derived elimination equation independently.
            z=K.power(b,3)
            Q=K.eval([1,4,3,4,5,3,3,3,1],z)
            assert (rk==0)==(Q==0)
            counts[(2,1+rk)]+=1
            if rk==0:marked.append((a,b))
    print('GF7^%d'%n,counts,'exceptional',len(marked))
    if n==1:assert counts=={(0,4):37,(2,2):6,(2,1):0,'singular':6}
    if n==2:assert counts=={(0,4):2311,(2,2):42,(2,1):0,'singular':48}
    if n==3:assert counts=={(0,4):116965,(2,2):318,(2,1):24,'singular':342}
    assert sum(counts.values())==K.size*K.size

for degree in [1,2,3]:verify(degree)
print('DIRECT_F7_F49_F343_FOUR_DIFFERENTIAL_CARTIER_CLASSIFICATION_OK')
