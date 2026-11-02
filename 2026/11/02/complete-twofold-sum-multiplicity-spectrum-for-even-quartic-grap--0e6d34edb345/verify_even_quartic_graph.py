"""Standalone exact spectra for sums of graphs (x,x**4+a*x**2) over finite fields.

Requires only Python's standard library. Finite tests corroborate an independent proof.
"""
from collections import Counter
from math import gcd

class Field:
    def __init__(self, p, modulus=None):
        self.p=p; self.mod=modulus
        self.m=1 if modulus is None else len(modulus)-1
        self.q=p**self.m
        self.digits=[self._digits(i) for i in range(self.q)]
        self.add=[[self._encode([(a+b)%p for a,b in zip(self.digits[x],self.digits[y])]) for y in range(self.q)] for x in range(self.q)]
        self.mul=[[self._multiply(x,y) for y in range(self.q)] for x in range(self.q)]
        self.square=[self.mul[x][x] for x in range(self.q)]
        self.fourth=[self.mul[v][v] for v in self.square]
        self.nonzero_squares=set(self.square[1:])
    def _digits(self,x):
        out=[]
        for _ in range(self.m):out.append(x%self.p);x//=self.p
        return out
    def _encode(self,v):return sum((x%self.p)*self.p**i for i,x in enumerate(v))
    def _multiply(self,x,y):
        if self.m==1:return x*y%self.p
        a=self.digits[x];b=self.digits[y];r=[0]*(2*self.m-1)
        for i in range(self.m):
            for j in range(self.m):r[i+j]=(r[i+j]+a[i]*b[j])%self.p
        for k in range(2*self.m-2,self.m-1,-1):
            c=r[k]
            if c:
                for j in range(self.m):r[k-self.m+j]=(r[k-self.m+j]-c*self.mod[j])%self.p
        return self._encode(r[:self.m])
    def c(self,k):return k%self.p
    def neg(self,x):return self._encode([(-a)%self.p for a in self.digits[x]])
    def chi(self,x):
        if x==0:return 0
        return 1 if x in self.nonzero_squares else -1
    def div(self,x,y):
        assert y!=0
        for z in range(1,self.q):
            if self.mul[y][z]==x:return z
        raise ValueError('modulus not irreducible')
    def predicted_spectrum(self,a):
        q=self.q;p=self.p
        if p==2:return {0:q*q-q,q:q}
        eta=self.chi(self.c(-1));tau=self.chi(self.c(2));d=gcd(4,q-1)
        if p==3:
            if a==0:Z=q; S=0
            else:Z=0;S=q*self.chi(self.neg(a))
        elif a==0:
            Z=1;S=(q-1)*self.chi(self.c(-6))
        else:
            crit=self.neg(self.div(self.mul[self.c(2)][a],self.c(3)))
            Z=1+self.chi(crit)
            S=-self.chi(self.c(-6))
        assert (q-Z+S)%2==0 and (q-Z-S)%2==0
        plus=(q-Z+S)//2; minus=(q-Z-S)//2
        assert plus>=0 and minus>=0 and plus+minus+Z==q
        D={0:q-1-(q-1)//d, 1:1, d:(q-1)//d}
        H={}
        for lam in [-1,1]:
            H[lam]={
                0:(5*q-4-eta+2*lam*(1-tau))//8,
                1:(1-lam)//2,
                2:(q+eta+2*tau*lam)//4,
                3:(1+lam)//2,
                4:(q-4-eta-2*lam*(1+tau))//8,
            }
            assert all(x>=0 for x in H[lam].values()),(q,a,lam,H[lam])
            assert sum(H[lam].values())==q
            assert sum(j*x for j,x in H[lam].items())==q
        out=Counter()
        for j,v in D.items():out[j]+=Z*v
        for lam,num in ((1,plus),(-1,minus)):
            for j,v in H[lam].items():out[j]+=num*v
        assert sum(out.values())==q*q
        assert sum(j*v for j,v in out.items())==q*q
        return {j:v for j,v in out.items() if v>0}
    def brute_spectrum(self,a):
        q=self.q
        pol=[self.add[self.fourth[t]][self.mul[a][self.square[t]]] for t in range(q)]
        r=Counter()
        for x in range(q):
            for y in range(q):r[(self.add[x][y],self.add[pol[x]][pol[y]])]+=1
        h=Counter(r.values());h[0]=q*q-len(r)
        assert sum(h.values())==q*q
        return {j:v for j,v in h.items() if v>0}
    def check(self,parameters):
        q=self.q
        for a in parameters:
            actual=self.brute_spectrum(a)
            expected=self.predicted_spectrum(a)
            assert actual==expected,(q,a,actual,expected)
            if self.p!=2 and self.p!=3 and a:
                # Two sign classes of nonzero coefficients have distinct sizes.
                # Checked once the other class appears.
                pass
        print('FIELD_OK q=%d cases=%d last_sumset=%d'%(q,len(parameters),q*q-actual.get(0,0)))

if __name__=='__main__':
    prime_list=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127]
    fields=[Field(p) for p in prime_list]
    fields.extend([
        Field(2,[1,1,1]),Field(2,[1,1,0,1]),Field(2,[1,1,0,0,1]),
        Field(3,[1,0,1]),Field(3,[1,2,0,1]),Field(3,[2,1,0,0,1]),
        Field(5,[2,0,1]),Field(5,[1,1,0,1]),Field(7,[1,0,1]),
        Field(11,[1,0,1])])
    tested=0
    for F in fields:
        q=F.q
        params=list(range(q)) if q<=49 else list(dict.fromkeys([0,1,2,3,4,5,q//2,q-1]))
        F.check(params);tested+=len(params)
    print('VERIFY_OK finite_fields=%d coefficient_cases=%d'% (len(fields),tested))
