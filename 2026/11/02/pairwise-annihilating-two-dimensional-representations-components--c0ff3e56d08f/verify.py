#!/usr/bin/env python3
"""Direct finite-field matrix arithmetic for the pairwise-annihilating tuple census.

No symbolic formulas are used in constructing or testing matrix products.
"""
from itertools import product
from functools import lru_cache
from math import comb

class Field:
    def __init__(self, p, poly=(0,1)):
        self.p, self.poly = p, tuple(poly)
        self.deg = len(poly)-1
        self.q = p**self.deg
        assert self.poly[-1] == 1
        self.add = [[self._add(a,b) for b in range(self.q)] for a in range(self.q)]
        self.mul = [[self._mul(a,b) for b in range(self.q)] for a in range(self.q)]
    def digits(self, x):
        ds=[]
        for _ in range(self.deg):
            ds.append(x%self.p);x//=self.p
        return ds
    def value(self,ds):return sum(x*self.p**i for i,x in enumerate(ds))
    def _add(self,a,b):
        return self.value([(x+y)%self.p for x,y in zip(self.digits(a),self.digits(b))])
    def _mul(self,a,b):
        x,y=self.digits(a),self.digits(b)
        c=[0]*(2*self.deg-1)
        for i in range(self.deg):
            for j in range(self.deg): c[i+j]=(c[i+j]+x[i]*y[j])%self.p
        for i in range(len(c)-1,self.deg-1,-1):
            factor=c[i]
            for j in range(self.deg): c[i-self.deg+j]=(c[i-self.deg+j]-factor*self.poly[j])%self.p
        return self.value(c[:self.deg])

def mm(A,B,F):
    a,b,c,d=A;e,f,g,h=B
    z=F.add;w=F.mul
    return (z[w[a][e]][w[b][g]],z[w[a][f]][w[b][h]],
            z[w[c][e]][w[d][g]],z[w[c][f]][w[d][h]])

def census(F,ms):
    z=(0,0,0,0);q=F.q
    mats=list(product(range(q),repeat=4)); n=len(mats)
    adj=[]
    for A in mats:
        bits=0
        for j,B in enumerate(mats):
            if mm(A,B,F)==z and mm(B,A,F)==z:bits|=1<<j
        adj.append(bits)
    # Every recursion intersects all pairwise-annihilator neighborhoods.
    @lru_cache(maxsize=None)
    def count(allowed,depth):
        if depth==0:return 1
        total=0
        bits=allowed
        while bits:
            b=bits & -bits; i=b.bit_length()-1
            total+=count(allowed & adj[i],depth-1)
            bits-=b
        return total
    allowed_all=(1<<n)-1
    for m in ms:
        actual=count(allowed_all,m)
        predicted=1+m*(q**4-1)+(q+1)*(q**m-1-m*(q-1))+comb(m,2)*q*(q+1)*(q-1)**2
        assert actual==predicted,(q,m,actual,predicted)
        print('q=%d m=%d count=%d OK'%(q,m,actual))
    if q<=4:
        # Classify individual solutions using only products, traces and scalar multiples.
        m=4 if q==2 else 3
        idx0=mats.index(z)
        counts={0:0,1:0,2:0,3:0,4:0}
        def scalar_multiple(X,Y):
            return any(tuple(F.mul[a][x] for x in X)==Y for a in range(q))
        def det(X):
            a,b,c,d=X
            minus_one=F.p-1
            neg=F.mul[minus_one][F.mul[b][c]]
            return F.add[F.mul[a][d]][neg]
        def legal(prefix,allowed):
            if len(prefix)==m:
                active=[mats[i] for i in prefix if i!=idx0]
                r=len(active);counts[r]+=1
                if r>=2:
                    nil=[mm(X,X,F)==z for X in active]
                    if r>=3 or all(nil):
                        assert all(nil)
                        assert all(scalar_multiple(active[0],Y) for Y in active[1:])
                    else:
                        assert r==2 and not any(nil)
                        assert all(det(X)==0 for X in active)
                return
            x=allowed
            while x:
                bit=x & -x;i=bit.bit_length()-1
                legal(prefix+(i,),allowed & adj[i]);x-=bit
        legal(tuple(),allowed_all)
        assert sum(counts.values())==count(allowed_all,m)
        for r in range(2,m+1):
            expected=comb(m,r)*(q+1)*(q-1)**r
            if r==2:expected+=comb(m,2)*q*(q+1)*(q-1)**2
            assert counts[r]==expected,(q,m,r,counts[r],expected)
        print('q=%d m=%d STRATA=%s OK'%(q,m,counts))
    return len(ms)

def main():
    cases=[(Field(2),range(0,7)),(Field(3),range(0,6)),
           (Field(2,(1,1,1)),range(0,5)),(Field(5),range(0,5)),
           (Field(7),range(0,4))]
    total=0
    for F,ms in cases:total+=census(F,ms)
    # Independently verify all multiplication identities defining the nilpotent line family
    for F in (Field(2), Field(3), Field(2,(1,1,1)), Field(5)):
        mats=list(product(range(F.q),repeat=4)); z=(0,0,0,0)
        for X in mats:
            if mm(X,X,F)!=z:continue
            for a in range(F.q):
                ax=tuple(F.mul[a][x] for x in X)
                assert mm(X,ax,F)==z and mm(ax,X,F)==z
    print('M2_MUTUALLY_ANNIHILATING_ALL_ARITIES_OK %d CENSUS_CASES'%total)
if __name__=='__main__':main()
