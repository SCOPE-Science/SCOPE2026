from itertools import product, combinations
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4); self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q in (2,4) else (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4: return (a*b)%self.q
        a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
        return ((a0*b0)^(a1*b1)) | ((((a0*b1)^(a1*b0)^(a1*b1)))<<1)
    def inv(self,a):
        assert a
        for b in range(1,self.q):
            if self.mul(a,b)==1: return b
        raise AssertionError

def data(n,q):
    F=Field(q); vn=list(product(range(q),repeat=n)); z=(0,)*n
    def va(a,b): return tuple(F.add(x,y) for x,y in zip(a,b))
    def ng(a): return tuple(F.neg(x) for x in a)
    def dot(a,b):
        s=0
        for x,y in zip(a,b): s=F.add(s,F.mul(x,y))
        return s
    E=[(x,y,c) for x in vn for y in vn for c in range(q)]; e=(z,z,0)
    def mul(g,h):
        x,y,c=g; X,Y,d=h
        return (va(x,X),va(y,Y),F.add(F.add(c,d),dot(x,Y)))
    def inv(g):
        x,y,c=g
        return (ng(x),ng(y),F.add(F.neg(c),dot(x,y)))
    def conj(g,h): return mul(mul(g,h),inv(g))
    def B(v,w):
        x,y=v[:n],v[n:]; X,Y=w[:n],w[n:]
        return F.sub(dot(x,Y),dot(X,y))
    return F,vn,E,e,mul,inv,conj,B

def canon(F,v):
    for a in v:
        if a:
            ai=F.inv(a)
            return tuple(F.mul(ai,x) for x in v)
    raise AssertionError

def spectrum(n,q):
    N=(q**(2*n)-1)//(q-1)
    f=((q+q**n)*(q**n-1))//(2*(q-1))
    g=((q**n-q)*(q**n+1))//(2*(q-1))
    C=Counter()
    C[q**(2*n-1)-2]+=1
    C[(q-1)*q**(n-1)-1]+=f
    C[-(q-1)*q**(n-1)-1]+=g
    C[-1]+=N*(q-2)
    return {k:v for k,v in C.items() if v}

def check(n,q):
    F,vn,E,e,mul,inv,conj,B=data(n,q); zero=(0,)*(2*n)
    for g in E:
        assert mul(g,inv(g))==e==mul(inv(g),g)
    center=[g for g in E if all(mul(g,h)==mul(h,g) for h in E)]
    assert set(center)=={((0,)*n,(0,)*n,c) for c in range(q)}
    nz=[v for v in product(range(q),repeat=2*n) if v!=zero]
    cls={}
    for v in nz:
        x,y=v[:n],v[n:]; rep=(x,y,0)
        orbit={conj(g,rep) for g in E}
        pred={(x,y,c) for c in range(q)}
        assert orbit==pred; cls[v]=pred
    adj={v:set() for v in nz}
    for i,v in enumerate(nz):
        for w in nz[i+1:]:
            expected=B(v,w)==0
            assert all((mul(a,b)==mul(b,a))==expected for a in cls[v] for b in cls[w])
            if expected: adj[v].add(w); adj[w].add(v)
    deg=q**(2*n-1)-2
    assert all(len(adj[v])==deg for v in nz)
    lines={}
    for v in nz: lines.setdefault(canon(F,v),[]).append(v)
    assert len(lines)==(q**(2*n)-1)//(q-1)
    assert all(len(L)==q-1 for L in lines.values())
    for L in lines.values(): assert all(w in adj[v] for v,w in combinations(L,2))
    ks=list(lines)
    for i,L in enumerate(ks):
        for M in ks[i+1:]:
            ex=B(L,M)==0
            assert all((w in adj[v])==ex for v in lines[L] for w in lines[M])
    if n>=2:
        for i,v in enumerate(nz):
            for w in nz[i+1:]:
                if w not in adj[v]: assert adj[v]&adj[w]
    lag=[tuple(x)+(0,)*n for x in vn if x!=(0,)*n]
    assert len(lag)==q**n-1
    assert all(w in adj[v] for v,w in combinations(lag,2))
    if n>=2:
        ac=set(); nc=set()
        for i,v in enumerate(nz):
            for w in nz[i+1:]:
                (ac if w in adj[v] else nc).add(len(adj[v]&adj[w]))
        assert nc=={q**(2*n-2)-1}
        assert ac==({q**(2*n-2)-3} if q==2 else {q**(2*n-1)-3,q**(2*n-2)-3})
    sp=spectrum(n,q); N=len(nz)
    assert sum(sp.values())==N
    assert sum(x*m for x,m in sp.items())==0
    assert sum(x*x*m for x,m in sp.items())==N*deg
    print({"n":n,"q":q,"vertices":N,"degree":deg,"spectrum":sp})

for c in [(1,4),(2,2),(2,3),(2,4),(3,2)]: check(*c)
print("VERIFY_OK")
