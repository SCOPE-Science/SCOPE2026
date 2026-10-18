"""Independent exact checks for the bidirectional product-rank formula.

Run: python3 verify_joint_squarezero.py
Only the Python standard library is required.
"""
from itertools import product
from collections import Counter
from math import prod


def gaussian(n, k, q):
    if not (0 <= k <= n):
        return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))


def gl(k, q):
    return prod(q**k-q**i for i in range(k))


def squarezero_count(n, q, k):
    return gaussian(n,k,q)*gaussian(n-k,k,q)*gl(k,q)


def joint(n,q,a,b,r,s):
    if not (0<=a<=n//2 and 0<=b<=n//2 and 0<=r<=min(a,b) and 0<=s<=min(a,b)):
        return 0
    fixed_a=squarezero_count(n,q,a)
    scale=fixed_a*gl(b,q)
    acc=0
    for c in range(min(a,b)+1):
        d=b-r-c
        e=n-2*b-a+s+c
        if d<0 or e<0:
            continue
        acc += (gaussian(a,c,q)*gaussian(n-2*a,d,q)*gaussian(a,r,q)
                * q**(d*(a-c)+r*(n-a-b+r))
                * gaussian(a-c,s,q)*gaussian(n-b-a+c,e,q)*q**(s*e))
    return scale*acc


class Field:
    def __init__(self,q):
        self.q=q
        assert q in (2,3,4)
        if q==4:
            self.add=lambda a,b:a^b
            def m(a,b):
                v=0
                for j in range(2):
                    if (b>>j)&1: v^=a<<j
                if v&8:v^=14  # remove t^3 using t^3=t+1 in GF(4)
                if v&4:v^=7   # t^2=t+1
                return v
            self.mul=m
            self.neg=lambda a:a
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
            self.neg=lambda a:(-a)%q
        self.inv={x:next(y for y in range(1,q) if self.mul(x,y)==1) for x in range(1,q)}

    def mult(self,A,B):
        n=len(A)
        o=[]
        for i in range(n):
            row=[]
            for j in range(n):
                v=0
                for k in range(n): v=self.add(v,self.mul(A[i][k],B[k][j]))
                row.append(v)
            o.append(tuple(row))
        return tuple(o)

    def rank(self,A):
        M=[list(x) for x in A]; n=len(M); k=0
        for j in range(n):
            p=next((i for i in range(k,n) if M[i][j]),None)
            if p is None:continue
            M[k],M[p]=M[p],M[k]
            v=self.inv[M[k][j]]
            M[k]=[self.mul(v,x) for x in M[k]]
            for i in range(k+1,n):
                v=M[i][j]
                if v:
                    M[i]=[self.add(x,self.neg(self.mul(v,y))) for x,y in zip(M[i],M[k])]
            k+=1
            if k==n: break
        return k


def exhaustive(n,q):
    f=Field(q)
    zeros=[]
    for v in product(range(q),repeat=n*n):
        A=tuple(tuple(v[i*n+j] for j in range(n)) for i in range(n))
        sq=f.mult(A,A)
        if all(w==0 for row in sq for w in row):
            zeros.append((A,f.rank(A)))
    observed=Counter()
    for A,a in zeros:
        for B,b in zeros:
            r=f.rank(f.mult(A,B))
            s=f.rank(f.mult(B,A))
            observed[(a,b,r,s)]+=1
    expected=Counter()
    for a in range(n//2+1):
        for b in range(n//2+1):
            for r in range(min(a,b)+1):
                for s in range(min(a,b)+1):
                    k=joint(n,q,a,b,r,s)
                    if k: expected[(a,b,r,s)]=k
    assert observed==expected,[(p,observed[p],expected[p]) for p in observed.keys()|expected.keys() if observed[p]!=expected[p]]
    assert len(zeros)==sum(squarezero_count(n,q,a) for a in range(n//2+1))
    print('EXHAUSTIVE_PASS',n,q,len(zeros),len(observed),'strata')


def identities():
    for q in (2,3,4,5,7):
        for n in range(1,12):
            for a in range(n//2+1):
                for b in range(n//2+1):
                    assert sum(joint(n,q,a,b,r,s) for r in range(min(a,b)+1) for s in range(min(a,b)+1))==squarezero_count(n,q,a)*squarezero_count(n,q,b)
                    for r in range(min(a,b)+1):
                        for s in range(min(a,b)+1):
                            z=joint(n,q,a,b,r,s)
                            assert z==joint(n,q,b,a,s,r)
                            assert (z>0)==(abs(r-s)<=n-a-b)
            if n%2==0:
                m=n//2
                for r in range(m+1):
                    x=joint(n,q,m,m,r,r)
                    target=gaussian(n,m,q)*gl(m,q)**2*gaussian(m,r,q)**2*q**(r*r)
                    assert x==target
                    assert all(joint(n,q,m,m,r,s)==0 for s in range(m+1) if s!=r)
    print('SYMBOLIC_IDENTITY_INSTANCES_PASS')

if __name__=='__main__':
    for n,q in ((2,2),(3,2),(4,2),(3,3),(3,4)):
        exhaustive(n,q)
    identities()
    print('VERIFY_OK_SQUAREZERO_BIDIRECTIONAL_PRODUCT_RANKS')
