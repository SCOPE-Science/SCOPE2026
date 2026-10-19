"""Exact finite-field orbit tests and numerical Fourier-frame tests."""
from __future__ import annotations
import cmath, json, math

class Field:
    def __init__(self,p,polynomial):
        self.p,self.poly=p,polynomial
        self.k=len(polynomial)-1
        self.q=p**self.k
        assert polynomial[-1]==1
        if self.k>1:
            # Check there are no proper finite-field divisors for the specified small test polynomials.
            for d in range(1,self.k//2+1):
                for n in range(p**d):
                    x=[(n//(p**i))%p for i in range(d)]+[1]
                    rem=polynomial[:]
                    for j in range(self.k-d,-1,-1):
                        a=rem[j+d]
                        for z in range(d+1):rem[j+z]=(rem[j+z]-a*x[z])%p
                    assert any(rem[:d]), (p,polynomial,x)
    def coeff(self,x):return [(x//self.p**i)%self.p for i in range(self.k)]
    def pack(self,a):return sum((v%self.p)*self.p**i for i,v in enumerate(a))
    def add(self,a,b):return self.pack([(x+y)%self.p for x,y in zip(self.coeff(a),self.coeff(b))])
    def neg(self,a):return self.pack([(-x)%self.p for x in self.coeff(a)])
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        x,y=self.coeff(a),self.coeff(b)
        r=[0]*(2*self.k-1)
        for i in range(self.k):
            for j in range(self.k):r[i+j]=(r[i+j]+x[i]*y[j])%self.p
        for j in range(2*self.k-2,self.k-1,-1):
            h=r[j]
            for i in range(self.k):r[j-self.k+i]=(r[j-self.k+i]-h*self.poly[i])%self.p
        return self.pack(r[:self.k])
    def power(self,x,n):
        ans=1
        while n:
            if n&1:ans=self.mul(ans,x)
            x=self.mul(x,x);n//=2
        return ans
    def tr(self,x):
        z=x;s=x
        for _ in range(1,self.k):
            s=self.power(s,self.p);z=self.add(z,s)
        assert z<self.p,(self.p,self.poly,z)
        return z
    def chi(self,x):
        if x==0:return 0
        return 1 if self.power(x,(self.q-1)//2)==1 else -1

CASES=[(3,[0,1]),(5,[0,1]),(7,[0,1]),(9,[1,0,1]),(11,[0,1]),(13,[0,1]),(25,[2,0,1]),(27,[1,2,0,1])]
res=[]
for q,poly in CASES:
    p=next(r for r in range(2,q+1) if q%r==0)
    F=Field(p,poly); assert F.q==q
    delta=next(x for x in range(1,q) if F.chi(x)==-1)
    c_values=[c for c in range(q) if F.chi(F.sub(1,F.mul(delta,F.mul(c,c))))==-1]
    assert len(c_values)==(q-(1 if q%4==1 else -1))//2
    c=c_values[0]
    H=set();done=set()
    for t in range(1,q):
        if t in done:continue
        H.add(t);done|={t,F.neg(t)}
    assert len(H)==(q-1)//2 and len(done)==q-1
    fn={t:(0 if t in H or t==0 else F.mul(c,t)) for t in range(q)}
    E=[(t,fn[t]) for t in range(1,q)]
    N=lambda pair:F.sub(F.mul(pair[0],pair[0]),F.mul(delta,F.mul(pair[1],pair[1])))
    assert set(N(e) for e in E)==set(range(1,q))
    T=[(u,v) for u in range(q) for v in range(q) if N((u,v))==1]
    assert len(T)==q+1
    cover=[]
    for u,v in T:
        cover.extend((F.add(F.mul(u,x),F.mul(delta,F.mul(v,y))),F.add(F.mul(v,x),F.mul(u,y))) for x,y in E)
    assert len(cover)==len(set(cover))==q*q-1
    assert set(cover)==set((x,y) for x in range(q) for y in range(q) if (x,y)!=(0,0))
    # The q columns of the Fourier block form a regular simplex over E*.
    max_gram=0.
    for s in range(q):
        for t in range(q):
            g=sum(cmath.exp(2j*math.pi*F.tr(F.mul(F.sub(s,t),x))/p) for x in range(1,q))/q
            target=(1. if s==t else 0.)-1/q
            max_gram=max(max_gram,abs(g-target))
    assert max_gram<1e-10
    res.append(dict(q=q,characteristic=p,delta=delta,c=c,admissible_slopes=len(c_values),graph_size=q,unit_norm_group_size=q+1,orbit_partition_size=len(cover),max_gram_error=max_gram))
print(json.dumps(dict(status='PASS',case_count=len(CASES),cases=res),indent=2))
