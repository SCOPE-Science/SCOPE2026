"""Exhaustive small-field check of finite-field permutation signatures.
Stdlib only; polynomial field arithmetic and permutation-cycle signs are direct.
"""
from itertools import product
from math import gcd

def div_rem(a, b, p):
    a = list(a)
    b = list(b)
    while a and a[-1] == 0: a.pop()
    while b and b[-1] == 0: b.pop()
    while len(a) >= len(b):
        h = a[-1] * pow(b[-1], -1, p) % p
        shift = len(a)-len(b)
        for j,v in enumerate(b):
            a[j+shift]=(a[j+shift]-h*v)%p
        while a and a[-1] == 0: a.pop()
    return tuple(a)

def irreducible(f,p):
    n=len(f)-1
    for d in range(1,n//2+1):
        for co in product(range(p),repeat=d):
            if div_rem(f,tuple(co)+(1,),p)==():return False
    return True

def find_field_poly(p,m):
    for cs in product(range(p),repeat=m):
        if cs[0]==0:continue
        f=cs+(1,)
        if irreducible(f,p):return f
    raise AssertionError

class Field:
    def __init__(self,p,m):
        self.p=p; self.m=m; self.Q=p**m
        self.f=find_field_poly(p,m)
        self.vectors=[tuple((i//(p**k))%p for k in range(m)) for i in range(self.Q)]
        self.one=1
    def add(self,a,b):
        p=self.p
        return sum(((x+y)%p)*p**k for k,(x,y) in enumerate(zip(self.vectors[a],self.vectors[b])))
    def neg(self,a):
        p=self.p
        return sum((-x%p)*p**k for k,x in enumerate(self.vectors[a]))
    def mul(self,a,b):
        if not (a and b):return 0
        p=self.p; m=self.m
        v=[0]*(2*m-1)
        for i,x in enumerate(self.vectors[a]):
            for j,y in enumerate(self.vectors[b]):v[i+j]=(v[i+j]+x*y)%p
        for k in range(2*m-2,m-1,-1):
            c=v[k]
            if c:
                for j in range(m):v[k-m+j]=(v[k-m+j]-c*self.f[j])%p
        return sum(v[k]*p**k for k in range(m))
    def pow(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out

def sign(permutation):
    n=len(permutation); seen=[False]*n; cycles=0
    for i in range(n):
        if seen[i]:continue
        cycles+=1;j=i
        while not seen[j]:
            seen[j]=True;j=permutation[j]
    return (-1)**(n-cycles)

def verify_case(p,s,e,rs):
    q=p**s; Q=q**e; K=Field(p,s*e);ell=(Q-1)//(q-1)
    summary=[]
    for r in rs:
        assert gcd(r,Q-1)==1
        assert any(gcd(h,e)==1 and (r*((q**h-1)//(q-1))-1)%ell==0 for h in range(1,e))
        delta=(-1)**((r-1)//2) if Q%4==1 else 1
        # chi_q((-1)^(e+1)) is a scalar in F_p, hence evaluate in the size-q field.
        c=K.neg(1) if (e+1)%2 else 1
        ec=K.pow(c,(q-1)//2)
        eps=1 if ec==1 else -1
        pos=neg=0
        for a in range(1,Q):
            b=K.pow(a,ell)
            d=K.add(b, K.neg(1) if e%2==0 else 1)
            if d==0:continue
            sigma_expected=delta*(1 if K.pow(d,(q-1)//2)==1 else -1)
            perm=[K.add(K.pow(x,r+q-1), K.mul(a,K.pow(x,r))) for x in range(Q)]
            assert len(set(perm))==Q, (p,s,e,r,a)
            sigma=sign(perm)
            assert sigma==sigma_expected,(p,s,e,r,a,sigma,sigma_expected)
            if sigma==1:pos+=1
            else:neg+=1
        ep=((q-2)-delta*eps)*ell//2
        op=((q-2)+delta*eps)*ell//2
        assert (pos,neg)==(ep,op),(p,s,e,r,pos,neg,ep,op)
        summary.append((p,s,e,r,Q,pos,neg))
    return summary

if __name__=='__main__':
    scenarios=[(3,1,2,[1,5]),(3,1,3,[1,23]),(3,1,4,[1]),
               (5,1,2,[1,7]),(5,1,3,[1,57,119]),(7,1,2,[1,17]),
               (3,2,2,[1,11])]
    results=[]
    for p,s,e,rs in scenarios: results+=verify_case(p,s,e,rs)
    print('VERIFY_OK cases=%d computed_parameter_maps=%d' %(len(results),sum(x[5]+x[6] for x in results)))
    for x in results: print('p=%d s=%d e=%d r=%d field=%d even=%d odd=%d'%x)
