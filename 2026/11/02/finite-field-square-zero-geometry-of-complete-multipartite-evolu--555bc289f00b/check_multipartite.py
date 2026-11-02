"""Independent finite-field point and span checks for multipartite evolution algebras."""
from itertools import product
from math import prod

class Field:
    def __init__(self,q):
        assert q in (3,5,7,9,11)
        self.q=q
        self.p=3 if q==9 else q
    def add(self,x,y):
        if self.q!=9:return (x+y)%self.p
        return ((x%3+y%3)%3)+3*((x//3+y//3)%3)
    def neg(self,x):
        if self.q!=9:return (-x)%self.p
        return (-x%3)+3*(-(x//3)%3)
    def mul(self,x,y):
        if self.q!=9:return x*y%self.p
        a,b=x%3,x//3;c,d=y%3,y//3
        return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
    def inv(self,x):
        assert x!=0
        y=1
        for _ in range(self.q-2):y=self.mul(y,x)
        return y
    def sq(self,x):return self.mul(x,x)
    def sub(self,x,y):return self.add(x,self.neg(y))

def prediction(q,parts):
    p=3 if q==9 else q
    r=len(parts)
    e_neg=1 if q%4==1 else -1
    a=[];b=[];c=[]
    for n in parts:
        v=q**(n-1)
        if n%2==0:
            a.append(v);b.append(e_neg**(n//2)*q**(n//2-1));c.append(None)
        else:
            a.append(v);b.append(None);c.append(e_neg**((n-1)//2)*q**((n-1)//2))
    z=prod(a[i]+(q-1)*b[i] if b[i] is not None else a[i] for i in range(r))
    if (r-1)%p:
        span=sum(n if n>=3 or (n==2 and q%4==1) else 0 for n in parts)
        return z,span
    even=prod(a[i]-b[i] for i in range(r) if b[i] is not None)
    plus=prod(a[i]+c[i] for i in range(r) if c[i] is not None)
    minus=prod(a[i]-c[i] for i in range(r) if c[i] is not None)
    return z+(q-1)*(even*(plus+minus)//2),sum(parts)

def rank_of_vectors(f,vectors,n):
    pivots={}
    for vector in vectors:
        v=list(vector)
        for j in sorted(pivots):
            if v[j]:
                w=pivots[j];alpha=v[j]
                v=[f.sub(v[k],f.mul(alpha,w[k])) for k in range(n)]
        j=next((k for k,x in enumerate(v) if x),None)
        if j is not None:
            inv=f.inv(v[j]);pivots[j]=[f.mul(inv,x) for x in v]
    return len(pivots)

def brute(q,parts):
    f=Field(q)
    N=sum(parts);r=len(parts)
    square=[f.sq(i) for i in range(q)]
    pts=[]
    for x in product(range(q),repeat=N):
        s=[];pos=0
        for n in parts:
            val=0
            for xi in x[pos:pos+n]:val=f.add(val,square[xi])
            s.append(val);pos+=n
        total=0
        for val in s:total=f.add(total,val)
        if all(f.sub(total,val)==0 for val in s):pts.append(x)
    return len(pts),rank_of_vectors(f,pts,N)

def main():
    cases=[(3,(1,1)),(5,(1,1)),(3,(2,2)),(5,(2,2)),(7,(2,2)),(11,(2,2)),
           (3,(3,2)),(5,(3,2)),(3,(2,2,1)),(5,(2,2,1)),
           (3,(1,1,1,1)),(3,(2,1,1,1)),(3,(2,2,1,1)),(3,(2,2,2,2)),
           (9,(1,1,1,1)),(9,(2,1,1,1)),(5,(1,1,1,1,1,1)),(5,(2,1,1,1,1,1)),(7,(1,1,1,1,1,1)),(7,(1,2,1)),(3,(3,1,2))]
    for q,parts in cases:
        pred=prediction(q,parts);got=brute(q,parts)
        assert pred==got,(q,parts,pred,got)
        print('PASS',q,parts,'points',got[0],'span_dimension',got[1])
    print('MULTIPARTITE_EVOLUTION_ABSOLUTE_NILPOTENTS_OK',len(cases))
if __name__=='__main__':main()
