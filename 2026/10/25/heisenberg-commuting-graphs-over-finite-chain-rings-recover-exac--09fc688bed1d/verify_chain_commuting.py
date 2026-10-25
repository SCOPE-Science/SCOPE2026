"""Direct pair-by-pair verification of finite-chain-ring Heisenberg commuting-graph equivalence.
Public mathematics verifier: brute-force group commutators and an explicit digitwise projective-tree bijection.
Run: python verify_chain_commuting.py
"""
from itertools import product

class Chain:
    def __init__(self,p,m,kind):
        self.p,self.m,self.kind=p,m,kind
        self.N=p**m
    def digits(self,a,k=None):
        k=self.m if k is None else k
        return [(a//self.p**i)%self.p for i in range(k)]
    def mul(self,a,b,k=None):
        k=self.m if k is None else k
        mod=self.p**k
        if self.kind=='integer':
            return (a*b)%mod
        da,db=self.digits(a,k),self.digits(b,k)
        ans=[0]*k
        for i,ai in enumerate(da):
            for j in range(k-i):
                ans[i+j]=(ans[i+j]+ai*db[j])%self.p
        return sum(v*self.p**i for i,v in enumerate(ans))
    def neg(self,a,k=None):
        k=self.m if k is None else k
        if self.kind=='integer': return (-a)%(self.p**k)
        d=self.digits(a,k)
        return sum(((-v)%self.p)*self.p**i for i,v in enumerate(d))
    def add(self,a,b,k=None):
        k=self.m if k is None else k
        if self.kind=='integer':return (a+b)%(self.p**k)
        d,e=self.digits(a,k),self.digits(b,k)
        return sum(((u+v)%self.p)*self.p**i for i,(u,v) in enumerate(zip(d,e)))
    def sub(self,a,b,k=None): return self.add(a,self.neg(b,k),k)
    def inv(self,a,k=None):
        k=self.m if k is None else k
        if a%self.p==0:raise ZeroDivisionError
        if self.kind=='integer':return pow(a,-1,self.p**k)
        aa=self.digits(a,k); bb=[0]*k
        bb[0]=pow(aa[0],-1,self.p)
        for n in range(1,k):
            bb[n]=-bb[0]*sum(aa[i]*bb[n-i] for i in range(1,n+1))%self.p
        return sum(v*self.p**i for i,v in enumerate(bb))
    def valuation(self,a):
        if a==0:return self.m
        for i,z in enumerate(self.digits(a)):
            if z:return i
        raise AssertionError
    def divide_uniformizer(self,a,v):
        assert self.valuation(a)>=v
        return a//(self.p**v)
    def multiply_uniformizer(self,a,v):
        return (a*self.p**v)%(self.p**self.m)
    def det(self,a,b,u,v):
        return self.sub(self.mul(a,v),self.mul(b,u))

def projective_coordinates(r,a,b):
    v=min(r.valuation(a),r.valuation(b))
    if v==r.m:return (r.m,None,None,None)
    k=r.m-v
    aa,bb=r.divide_uniformizer(a,v),r.divide_uniformizer(b,v)
    if aa%r.p:
        return v,'A',aa,r.mul(bb,r.inv(aa,k),k)
    assert bb%r.p
    return v,'B',bb,r.mul(aa,r.inv(bb,k),k)

def target_vector(r,data):
    v,chart,alpha,param=data
    if v==r.m:return (0,0)
    k=r.m-v
    if chart=='A': a,b=alpha,r.mul(alpha,param,k)
    else: a,b=r.mul(alpha,param,k),alpha
    return r.multiply_uniformizer(a,v),r.multiply_uniformizer(b,v)

def verify(p,m):
    r1=Chain(p,m,'integer');r2=Chain(p,m,'polynomial')
    N=p**m
    image={}
    for a,b in product(range(N),repeat=2):
        image[(a,b)]=target_vector(r2,projective_coordinates(r1,a,b))
    assert len(set(image.values()))==N*N,('not bijective',p,m)
    # Direct determinants, not the proposed projective criterion.
    vals=list(image)
    pairs=0
    for i,(a,b) in enumerate(vals):
        aa,bb=image[(a,b)]
        for u,v in vals[:i+1]:
            uu,vv=image[(u,v)]
            assert (r1.det(a,b,u,v)==0)==(r2.det(aa,bb,uu,vv)==0), (p,m,(a,b),(u,v))
            pairs+=1
    # Every central coordinate is an independent clique fibre. The 2D test
    # therefore verifies the full graph of q^(3m) Heisenberg elements.
    hist={}
    for a,b in vals:
        val=min(r1.valuation(a),r1.valuation(b))
        hist[val]=hist.get(val,0)+1
        zeros=sum(r1.det(a,b,u,v)==0 for u,v in vals)
        want=N*N if val==m else p**(m+val)
        assert zeros==want,(p,m,(a,b),zeros,want)
    print(f'CASE_OK p={p} m={m} |R|={N} quotient_vertices={N*N} determinant_pairs={pairs} vector_valuation_hist={hist}')

def direct_group_check(p,m):
    """Independently compare products xy and yx at group-element level."""
    for kind in ('integer','polynomial'):
        ring=Chain(p,m,kind)
        Q=ring.N
        V=list(product(range(Q),repeat=3))
        def mul(x,y):
            a,b,c=x;u,v,w=y
            return (ring.add(a,u),ring.add(b,v),ring.add(ring.add(c,w),ring.mul(a,v)))
        for x in V:
            a,b,c=x
            assert mul(x,(0,0,0))==x
            assert mul((0,0,0),x)==x
            for y in V:
                u,v,w=y
                assert (mul(x,y)==mul(y,x)) == (ring.det(a,b,u,v)==0)
        print(f'GROUP_PRODUCTS_OK p={p} m={m} kind={kind} checked={Q**6}')

if __name__=='__main__':
    for case in [(2,2),(2,3),(3,2),(5,2)]: verify(*case)
    direct_group_check(2,2)
    print('VERIFY_OK all direct commuting-graph comparisons and group-product checks')
