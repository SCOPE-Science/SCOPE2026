"""Reproducible finite-field tests for principal Fourier sampling on three lines.

Run: python three_line_rank_checker.py
Requires NumPy.  The analytic proof, not these finite tests, covers all fields.
"""
import math
import numpy as np


class Field:
    def __init__(self, p, polynomial=None):
        self.p = p
        self.poly = polynomial or (0, 1)
        self.d = len(self.poly) - 1
        self.q = p ** self.d
        self.zero = 0
        self.one = 1
        assert self.poly[-1] == 1
        self.digits = [self._digits(i) for i in range(self.q)]
        self.add_table = [[self._encode([(a+b)%p for a,b in zip(self.digits[i],self.digits[j])])
                           for j in range(self.q)] for i in range(self.q)]
        self.mul_table = [[self._multiply(i,j) for j in range(self.q)] for i in range(self.q)]
        self.generator = self._generator()
        self.powers = [self.power(self.generator,k) for k in range(self.q-1)]
        self.logs = {a:k for k,a in enumerate(self.powers)}
        assert len(self.logs) == self.q-1

    def _digits(self, v):
        out=[]
        for _ in range(self.d):
            out.append(v%self.p);v//=self.p
        return out

    def _encode(self,ds):
        return sum(x*self.p**j for j,x in enumerate(ds))

    def _multiply(self,x,y):
        p=self.p; d=self.d
        if d == 1:return x*y%p
        a=self.digits[x];b=self.digits[y]
        prod=[0]*(2*d-1)
        for i in range(d):
            for j in range(d):prod[i+j]=(prod[i+j]+a[i]*b[j])%p
        for k in range(2*d-2,d-1,-1):
            c=prod[k]
            for j in range(d):prod[k-d+j]=(prod[k-d+j]-c*self.poly[j])%p
        return self._encode(prod[:d])

    def add(self,x,y):return self.add_table[x][y]
    def mul(self,x,y):return self.mul_table[x][y]
    def power(self,x,k):
        out=1
        while k:
            if k&1:out=self.mul(out,x)
            x=self.mul(x,x);k>>=1
        return out
    def _generator(self):
        n=self.q-1
        factors=[j for j in range(2,n+1) if n%j == 0 and all(j%i for i in range(2,int(j**.5)+1))]
        for g in range(1,self.q):
            if all(self.power(g,n//r)!=1 for r in factors):return g
        raise ValueError('No primitive element; check irreducible polynomial')
    def trace(self,x):
        y=0
        for i in range(self.d):
            y=self.add(y,self.power(x,self.p**i))
        assert 0<=y<self.p
        return y


def predicted_nullity(F,t):
    z=F.mul(t,t); w=F.add(1,z); N=F.q-1
    if w==0:return N//2 if F.p!=2 else 0
    if N%6:return 0
    a=F.logs[z]; b=F.logs[w]
    congruences={(N//3,N//6),(2*N//3,5*N//6)}
    count=sum(((a*k)%N,(b*k)%N) in congruences for k in range(1,N))
    H=math.lcm(N//math.gcd(N,a),N//math.gcd(N,b))
    assert count in (0,2*N//H)
    return count


def numerical_nullity(F,t):
    q=F.q
    E=[(0,0)]+[(s,0) for s in range(1,q)]+[(0,s) for s in range(1,q)]+[(s,F.mul(s,t)) for s in range(1,q)]
    # Include origin only once, as specified in the theorem.
    roots=np.exp(2j*np.pi*np.arange(F.p)/F.p)
    A=np.empty((len(E),len(E)),dtype=complex)
    for i,(a,b) in enumerate(E):
        for j,(c,d) in enumerate(E):
            A[i,j]=roots[F.trace(F.add(F.mul(a,c),F.mul(b,d)))]
    s=np.linalg.svd(A,compute_uv=False)
    return int(np.count_nonzero(s<1e-8*s[0])), float(s[-1])


def run():
    fields=[Field(p) for p in [2,3,5,7,11,13,17,19,23,29,31]]
    fields += [Field(2,(1,1,1)),Field(2,(1,1,0,1)),
               Field(3,(1,0,1)),Field(2,(1,1,0,0,1)),
               Field(5,(2,0,1)),Field(3,(1,2,0,1))]
    count=0;singular=0
    for F in fields:
        for t in range(1,F.q):
            e=predicted_nullity(F,t)
            a,small=numerical_nullity(F,t)
            assert a==e, (F.q,t,'expected',e,'actual',a,'minimum singular value',small)
            count+=1;singular+=bool(e)
        print(f'GF({F.q}): {F.q-1} slopes verified')
    assert count>=200
    print(f'PASS: {count} independent numeric-rank comparisons; {singular} singular slope configurations.')

if __name__=='__main__':run()
