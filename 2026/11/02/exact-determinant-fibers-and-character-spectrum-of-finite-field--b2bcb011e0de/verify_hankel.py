#!/usr/bin/env python3
"""Independent finite-field enumeration checks for Hankel determinant fibers.
Only uses the Python standard library. This is a finite check, not an infinite proof.
"""
from collections import Counter
from itertools import product
from math import gcd

class Field:
    def __init__(self, q):
        self.q = q
        assert q in (2, 3, 4, 5, 7, 8, 9, 11)
    def add(self, a, b):
        q = self.q
        if q in (2, 3, 5, 7, 11): return (a+b) % q
        if q in (4, 8): return a ^ b
        return ((a+b)%3) + 3*((a//3+b//3)%3)
    def neg(self, a):
        return self.add(0, a) if self.q in (4, 8) else self.mul(self.q-1 if self.q != 9 else 2, a)
    def mul(self, a, b):
        q = self.q
        if q in (2, 3, 5, 7, 11): return (a*b)%q
        if q == 9:
            a0, a1 = a%3, a//3
            b0, b1 = b%3, b//3
            return ((a0*b0-a1*b1)%3)+3*((a0*b1+a1*b0)%3)
        polynomial, bits = (0b111, 2) if q == 4 else (0b1011, 3)
        out = 0
        while b:
            if b & 1: out ^= a
            b >>= 1
            a <<= 1
            if a & (1 << bits): a ^= polynomial
        return out
    def power(self, a, n):
        ans=1
        while n:
            if n&1: ans=self.mul(ans,a)
            a=self.mul(a,a)
            n >>= 1
        return ans
    def inv(self, a):
        assert a
        return self.power(a, self.q-2)
    def sub(self, a, b):
        if self.q in (4, 8): return a ^ b
        if self.q == 9: return ((a-b)%3)+3*((a//3-b//3)%3)
        return (a-b)%self.q

def determinant(f, values, n):
    a = [[values[i+j] for j in range(n)] for i in range(n)]
    out = 1
    for i in range(n):
        pivot = next((j for j in range(i,n) if a[j][i]),None)
        if pivot is None: return 0
        if pivot != i:
            a[i],a[pivot] = a[pivot],a[i]
            out = f.sub(0,out)
        lead=a[i][i]
        out=f.mul(out,lead)
        inv=f.inv(lead)
        for j in range(i+1,n):
            mul=f.mul(a[j][i],inv)
            if mul:
                for k in range(i+1,n): a[j][k]=f.sub(a[j][k],f.mul(mul,a[i][k]))
                a[j][i]=0
    return out

def mu(n):
    signs=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; signs=-signs
            if n%p==0: return 0
        p+=1
    return -signs if n>1 else signs

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def cyclic_log(f):
    q=f.q
    for base in range(1,q):
        power=1; logs={}
        for k in range(q-1):
            logs[power]=k
            power=f.mul(power,base)
        if len(logs)==q-1 and power==1:return logs
    raise RuntimeError('No generator')

def ramanujan(r,k):
    return sum(d*mu(r//d) for d in divisors(gcd(r,k)))

def predict(f,n,t,logs):
    q=f.q
    if t==0:return q**(2*n-2)
    ans=q**(2*n-2)
    sign= 1 if n*(n-1)//2%2==0 else f.sub(0,1)
    factor=f.mul(sign,f.inv(t))
    j=logs[factor]
    for r in divisors(gcd(n,q-1)):
        if r>1:ans+=q**(n+n//r-2)*ramanujan(r,j)
    return ans

def main():
    groups=[(2,6),(3,5),(4,3),(5,4),(7,3),(8,2),(9,2),(11,2)]
    cases=0; matrices=0; fibers=0
    for q,nmax in groups:
        f=Field(q); logs=cyclic_log(f)
        for n in range(1,nmax+1):
            values=Counter(determinant(f,a,n) for a in product(range(q),repeat=2*n-1))
            expected={t:predict(f,n,t,logs) for t in range(q)}
            assert all(values[t]==expected[t] for t in range(q)),(q,n,values,expected)
            cases+=1; matrices+=q**(2*n-1); fibers+=q
            print('OK', 'q=',q,'n=',n,'counts=',','.join(str(values[t]) for t in range(q)))
    print('VERIFY_OK fields=8 cases=%d enumerated_matrices=%d predicted_fibers=%d' %(cases,matrices,fibers))

if __name__=='__main__':main()
