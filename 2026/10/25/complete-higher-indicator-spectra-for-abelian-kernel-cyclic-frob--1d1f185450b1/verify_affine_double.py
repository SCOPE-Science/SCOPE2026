#!/usr/bin/env python3
"""Independent brute-force checks for the indicators of scalar affine-group doubles."""
import cmath
import math

class FiniteField:
    def __init__(self,p,e,poly):
        self.p,self.e,self.q,self.poly=p,e,p**e,poly
        assert len(poly)==e+1 and poly[e]==1
        self.digits=[[n//(p**i)%p for i in range(e)] for n in range(self.q)]
        self.pow_p=[p**i for i in range(e)]
        self.plus=[[self._enc([(self.digits[a][i]+self.digits[b][i])%p for i in range(e)]) for b in range(self.q)] for a in range(self.q)]
        self.mult=[[self._mul_raw(a,b) for b in range(self.q)] for a in range(self.q)]
        self.neg=[self._enc([(-u)%p for u in self.digits[a]]) for a in range(self.q)]
        self.nonzero=[a for a in range(1,self.q)]
    def _enc(self,u): return sum(u[i]*self.pow_p[i] for i in range(self.e))
    def _mul_raw(self,a,b):
        t=[0]*(2*self.e-1)
        for i,x in enumerate(self.digits[a]):
            for j,y in enumerate(self.digits[b]): t[i+j]=(t[i+j]+x*y)%self.p
        for i in range(2*self.e-2,self.e-1,-1):
            c=t[i]
            for j in range(self.e): t[i-self.e+j]=(t[i-self.e+j]-c*self.poly[j])%self.p
        return self._enc(t[:self.e])
    def power(self,a,k):
        u=1
        for _ in range(k):u=self.mult[u][a]
        return u
    def trace(self,a):
        t=0
        for j in range(self.e):t=self.plus[t][self.power(a,self.p**j)]
        assert self.digits[t][1:]==[0]*(self.e-1)
        return self.digits[t][0]
    def subgroup(self,m):
        assert (self.q-1)%m==0
        for g in self.nonzero:
            if self.power(g,m)==1 and all(self.power(g,k)!=1 for k in range(1,m)):
                return [self.power(g,k) for k in range(m)]
        raise AssertionError('no generator')

def chk(q,p,e,poly,m,kmax):
    F=FiniteField(p,e,poly); hlist=F.subgroup(m); hindex={h:i for i,h in enumerate(hlist)}
    elems=[(a,h) for a in range(q) for h in hlist]
    def mul(x,y):return(F.plus[x[0]][F.mult[x[1]][y[0]]],F.mult[x[1]][y[1]])
    def power(x,k):
        r=(0,1)
        for _ in range(k):r=mul(r,x)
        return r
    def z(m,k):return cmath.exp(2j*math.pi*k/m)
    def compare(g,k,expected,character):
        total=0j
        for x in elems:
            if power(mul(g,x),k)==power(x,k):
                total+=character(power(x,k))
        denom=q if g[1]==1 and g[0]!=0 else m if g[1]!=1 else q*m
        val=total/denom
        assert abs(val-expected)<1e-6,(q,m,g,k,expected,val)
    for k in range(1,kmax+1):
        d=math.gcd(m,k); delta=int(k%p==0)
        # identity simples: complement characters and induced nontrivial additive characters.
        for j in range(m):
            compare((0,1),k,int((j*k)%m==0),lambda y,j=j:z(m,(j*hindex[y[1]])%m))
        seen=set()
        for a in range(1,q):
            if a in seen:continue
            orb={F.mult[a][h] for h in hlist};seen|=orb
            def chi(y,a=a):
                return 0 if y[1]!=1 else sum(cmath.exp(2j*math.pi*F.trace(F.mult[a][F.mult[h][y[0]]])/p) for h in hlist)
            compare((0,1),k,d-1+delta,chi)
        # all nonidentity kernel classes, including all linear centralizer characters.
        for a in range(1,q):
            for u in range(q):
                compare((a,1),k,d-1+delta,lambda y,u=u:cmath.exp(2j*math.pi*F.trace(F.mult[u][y[0]])/p))
        # all nontrivial complement conjugacy classes, all centralizer characters.
        for h0 in hlist[1:]:
            for j in range(m):
                expected=0 if F.power(h0,k)!=1 else int((j*k)%m==0)+(q-1)//m*(d-2+2*delta)
                compare((0,h0),k,expected,lambda y,j=j:z(m,j*hindex[y[1]]))
    print('PASS',q,m,'indicators up to',kmax,flush=True)

if __name__=='__main__':
    cases=[(3,3,1,[0,1],2,15),(4,2,2,[1,1,1],3,15),(5,5,1,[0,1],2,16),(5,5,1,[0,1],4,16),
           (7,7,1,[0,1],2,16),(7,7,1,[0,1],3,16),(7,7,1,[0,1],6,16),(8,2,3,[1,1,0,1],7,16),
           (9,3,2,[1,0,1],2,16),(9,3,2,[1,0,1],4,16),(9,3,2,[1,0,1],8,16)]
    for c in cases:chk(*c)
    print('VERIFY_OK_AFFINE_DOUBLE_INDICATORS')


def chk_abelian(n,r,a,m,kmax,selected_only=False):
    """Independently evaluate double-character indicators in (Z/nZ)^r semidirect C_m."""
    from itertools import product
    assert math.gcd(a,n)==1 and pow(a,m,n)==1
    assert all(math.gcd(pow(a,j,n)-1,n)==1 for j in range(1,m))
    V=list(product(range(n),repeat=r))
    zero=(0,)*r
    elems=[(v,j) for v in V for j in range(m)]
    N=len(V)
    def mul(x,y):
        v,h=x;w,t=y
        return (tuple((v[i]+pow(a,h,n)*w[i])%n for i in range(r)),(h+t)%m)
    def power(x,k):
        res=(zero,0)
        for _ in range(k):res=mul(res,x)
        return res
    def char(u,v):return cmath.exp(2j*math.pi*sum(u[i]*v[i] for i in range(r))/n)
    def charH(j,h):return cmath.exp(2j*math.pi*j*h/m)
    def indicator(g,k,fun):
        total=0j
        for x in elems:
            z=power(x,k)
            if power(mul(g,x),k)==z:total+=fun(z)
        return total/(N if g[0]!=zero and g[1]==0 else m if g[1]!=0 else N*m)
    kvectors=V[:]
    if selected_only:
        kvectors=[zero]+[v for v in V if any(x!=0 for x in v)][:4]
    for k in range(1,kmax+1):
        d=math.gcd(m,k)
        T=sum(all((k*x)%n==0 for x in v) for v in V)
        # identity complementary characters
        for j in range(m):
            actual=indicator((zero,0),k,lambda x,j=j:charH(j,x[1]))
            expected=int(j*k%m==0)
            assert abs(actual-expected)<1e-7,('identityH',n,r,a,m,k,j,actual,expected)
        # identity induced characters, using orbit representatives in dual V
        seen=set()
        for u in V:
            if u==zero or u in seen:continue
            orb={tuple(pow(a,h,n)*x%n for x in u) for h in range(m)}
            seen|=orb
            actual=indicator((zero,0),k,lambda x,u=u: sum(char(tuple(pow(a,h,n)*t%n for t in u),x[0]) for h in range(m)) if x[1]==0 else 0)
            expected=d-1+int(all((k*t)%n==0 for t in u))
            assert abs(actual-expected)<1e-7,('identityInd',n,r,a,m,k,u,actual,expected)
        # kernel-centralizer characters
        for v in kvectors:
            if v==zero:continue
            U=V if not selected_only else V[:6]
            for u in U:
                actual=indicator((v,0),k,lambda x,u=u:char(u,x[0]))
                expected=d-1+int(all((k*t)%n==0 for t in v) and all((k*t)%n==0 for t in u))
                assert abs(actual-expected)<1e-7,('kernel',n,r,a,m,k,v,u,actual,expected)
        # complement-centralizer characters
        for h0 in range(1,m):
            for j in range(m):
                actual=indicator((zero,h0),k,lambda x,j=j:charH(j,x[1]))
                expected=0 if (h0*k)%m else int(j*k%m==0)+((N-1)*(d-2)+2*(T-1))//m
                assert abs(actual-expected)<1e-7,('complement',n,r,a,m,k,h0,j,actual,expected)
    print('PASS_AB',n,r,a,m,kmax,flush=True)

if __name__=='__main__':
    for c in [(9,1,8,2,18,False),(25,1,7,4,16,False),(9,2,8,2,10,True)]:
        chk_abelian(*c)
    print('VERIFY_OK_ALL_FINITE_ABELIAN_KERNELS')
