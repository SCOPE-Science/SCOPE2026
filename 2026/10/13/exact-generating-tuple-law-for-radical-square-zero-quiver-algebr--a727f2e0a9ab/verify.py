"""Finite-field exhaustive checks for generating-tuple counts in loopless square-zero quiver algebras.

Uses only the Python standard library. The enumeration is an independent word-span closure,
not the theoretical commutator-rank criterion used in the proof.
"""
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        z=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:
                    z^=1<<(i+j)
        if z&8:z^=0b1110 # x^3 -> x^2+x
        if z&4:z^=0b111 # x^2 -> x+1
        return z
    def inv(self,a):
        if not a:raise ZeroDivisionError
        return next(x for x in range(1,self.q) if self.mul(x,a)==1)

def generating_count(q, vertices, edges, r):
    f=Field(q);n=vertices+len(edges)
    ident=tuple([1]*vertices+[0]*len(edges))
    elems=list(product(range(q),repeat=n))
    def mult(x,y):
        out=[f.mul(x[i],y[i]) for i in range(vertices)]+[]
        for j,(u,v) in enumerate(edges):
            out.append(f.add(f.mul(x[u],y[vertices+j]),f.mul(x[vertices+j],y[v])))
        return tuple(out)
    def whole(xs):
        pivots={};basis=[]
        def add(v):
            v=list(v)
            for j in sorted(pivots):
                if v[j]:
                    scale=v[j];p=pivots[j]
                    v=[f.add(v[k],f.neg(f.mul(scale,p[k]))) for k in range(n)]
            j=next((k for k,c in enumerate(v) if c),None)
            if j is None:return False
            iv=f.inv(v[j]);v=tuple(f.mul(iv,t) for t in v)
            pivots[j]=v;basis.append(v)
            return True
        add(ident)
        for x in xs:add(x)
        processed=0
        while processed<len(basis):
            b=basis[processed];processed+=1
            for x in xs:
                add(mult(b,x));add(mult(x,b))
            if len(basis)==n:return True
        return len(basis)==n
    count=sum(whole(xs) for xs in product(elems, repeat=r))
    by_pair={}
    for uv in edges:by_pair[uv]=by_pair.get(uv,0)+1
    predicted=1
    for i in range(vertices):predicted*=q**r-i
    for m in by_pair.values():
        predicted*=q**m
        for j in range(m):predicted*=q**(r-1)-q**j
    assert count==predicted, (q,vertices,edges,r,count,predicted)
    print('PASS',q,vertices,edges,r,count,'/',len(elems)**r)

def main():
    cases=[
       (2,2,[(0,1)],1),
       (2,2,[(0,1)],2),
       (2,2,[(0,1)],3),
       (2,2,[(0,1),(0,1)],2),
       (2,2,[(0,1),(0,1)],3),
       (2,3,[],2),
       (2,3,[(0,1)],2),
       (2,3,[(0,1),(1,2)],2),
       (2,3,[(0,1),(1,0)],2),
       (3,2,[(0,1)],2),
       (4,2,[(0,1)],2),
    ]
    for case in cases: generating_count(*case)
    print('VERIFY_OK')
if __name__=='__main__':main()
