"""Exact independent enumeration for affine commutator fibers over small chain rings."""
from collections import Counter
from math import gcd

class Ring:
    def __init__(self, q, n, kind):
        self.q, self.n, self.kind = q, n, kind
        self.N = q**n
        if kind == 'modular':
            self.add = lambda a,b: (a+b) % self.N
            self.neg = lambda a: (-a) % self.N
            self.mul = lambda a,b: (a*b) % self.N
            self.units = [a for a in range(self.N) if gcd(a, self.N)==1]
            self.valuation = lambda a: self.n if a == 0 else next(i for i in range(self.n) if a % (q**(i+1)) != 0)
        else:
            assert n == 2 and q in (2,3,4)
            def fadd(a,b):
                return (a^b) if q in (2,4) else (a+b)%q
            def fneg(a): return a if q in (2,4) else (-a)%q
            def fmul(a,b):
                if q != 4: return (a*b)%q
                raw = (a&1)*(b&1) ^ (((a>>1)&1)*((b>>1)&1)<<2) ^ (((a&1)*((b>>1)&1) ^ ((a>>1)&1)*(b&1))<<1)
                if raw&4: raw ^= 7
                return raw
            def add(a,b): return fadd(a%q,b%q) + q*fadd(a//q,b//q)
            def neg(a): return fneg(a%q)+q*fneg(a//q)
            def mul(a,b): return fmul(a%q,b%q)+q*fadd(fmul(a%q,b//q),fmul(a//q,b%q))
            self.add,self.neg,self.mul=add,neg,mul
            self.units=[a for a in range(self.N) if a%q]
            self.valuation=lambda a: 2 if a==0 else (0 if a%q else 1)
    def inv(self,a):
        for b in self.units:
            if self.mul(a,b)==1: return b
        raise AssertionError('missing inverse')

def theory(q,n):
    U=q**n-q**(n-1)
    layers=[U]+[q**(n-s) for s in range(1,n+1)]
    M=[layers[s]**2-layers[s+1]**2 for s in range(n)]+[1]
    assert sum(M)==U**2
    vals=[q**n*sum(q**s*M[s] for s in range(r+1)) for r in range(n)]
    vals += [q**n*sum(q**s*M[s] for s in range(n+1))]
    return vals

def check(q,n,kind):
    R=Ring(q,n,kind); mul=R.mul; add=R.add; neg=R.neg
    group=[(a,x) for a in R.units for x in range(R.N)]
    def compose(g,h):
        a,x=g;b,y=h
        return (mul(a,b),add(x,mul(a,y)))
    def inv(g):
        a,x=g; ia=R.inv(a)
        return (ia, neg(mul(ia,x)))
    inverse={g:inv(g) for g in group}
    dist=Counter()
    for g in group:
        for h in group:
            gh=compose(g,h)
            comm=compose(compose(gh,inverse[g]),inverse[h])
            assert comm[0]==1
            dist[comm[1]]+=1
    prediction=theory(q,n)
    for t in range(R.N):
        assert dist[t] == prediction[R.valuation(t)], (q,n,kind,t,dist[t],prediction)
    assert sum(dist.values())==len(group)**2
    # Independent centralizer/conjugacy-class count.
    U=len(R.units)
    expected_classes=U+(q**n-1)//(q-1)
    assert dist[0]==len(group)*expected_classes, ('class count',q,n,kind)
    # Verify derived subgroup support via additive closure and primitive image.
    support={t for t,z in dist.items() if z}
    if q==2:
        assert support=={t for t in range(R.N) if R.valuation(t)>=1}
    else:
        assert support==set(range(R.N))
    return (kind,q,n,len(group),dist[0],[(r,prediction[r]) for r in range(n+1)])

if __name__=='__main__':
    cases=[(2,1,'modular'),(2,2,'modular'),(2,3,'modular'),(2,4,'modular'),
           (3,1,'modular'),(3,2,'modular'),(3,3,'modular'),
           (5,1,'modular'),(5,2,'modular'),
           (2,2,'dual'),(3,2,'dual'),(4,2,'dual')]
    for q,n,k in cases:print(check(q,n,k))
    print('VERIFY_OK')
