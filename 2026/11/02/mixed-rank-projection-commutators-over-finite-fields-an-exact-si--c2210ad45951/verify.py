"""Finite-field checks for the mixed-rank projection commutator census.
Usage: python verify.py. No third-party dependencies.
"""
import itertools
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return (a^b) if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4: return (a*b)%self.q
        out=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1): out ^= 1<<(i+j)
        if out&4: out^=7  # X^2+X+1
        return out
    def dot(self,a,b):
        val=0
        for x,y in zip(a,b): val=self.add(val,self.mul(x,y))
        return val
    def inv(self,a):
        assert a!=0
        for x in range(1,self.q):
            if self.mul(a,x)==1: return x
        raise AssertionError
    def scale(self,a,b):return tuple(self.mul(a,v) for v in b)
    def sub(self,a,b):return self.add(a,self.neg(b))


def product(a,b,f):
    n=len(a)
    return tuple(tuple(f.dot(a[i],tuple(b[k][j] for k in range(n))) for j in range(n)) for i in range(n))

def rank(M,f):
    m=[list(row) for row in M]; n=len(m); rk=0
    for col in range(n):
        pivot=next((i for i in range(rk,n) if m[i][col]),None)
        if pivot is None:continue
        m[rk],m[pivot]=m[pivot],m[rk]
        inv=f.inv(m[rk][col]);m[rk]=[f.mul(inv,v) for v in m[rk]]
        for i in range(n):
            if i!=rk and m[i][col]:
                x=m[i][col];m[i]=[f.sub(y,f.mul(x,z)) for y,z in zip(m[i],m[rk])]
        rk+=1
    return rk

def theory(n,r,q):
    s=n-r
    U=lambda m:(q**m-1)*q**(m-1)
    W=lambda m:(q**m-1)*(q**(m-1)-1)
    d=q-1
    counts=Counter()
    counts[(0,0)]=U(s)//d
    counts[(0,1)]=2*(q**r-1)*U(s)//d
    counts[(0,2)]=W(r)*U(s)//d
    counts[(1,0)]=U(r)//d
    counts[(1,1)]=2*(q**s-1)*U(r)//d
    counts[(1,2)]=W(s)*U(r)//d
    for alpha in range(2,q):
        # q=4 element codes 2,3 are both !=0,1
        counts[(alpha,2)]=U(r)*U(s)//d
    return +counts

def run(n,r,q):
    f=Field(q); s=n-r
    zero=(0,)*n
    I=tuple(tuple(int(i==j and i<r) for j in range(n)) for i in range(n))
    vectors=itertools.product(range(q),repeat=n)
    obs=Counter()
    for raw in vectors:
        if raw==zero:continue
        pos=next(i for i,x in enumerate(raw) if x)
        if raw[pos]!=1:continue # normalized image vector
        for v in itertools.product(range(q),repeat=n):
            if f.dot(raw,v)!=1:continue
            alpha=f.dot(raw[:r],v[:r])
            Q=tuple(tuple(f.mul(raw[i],v[j]) for j in range(n)) for i in range(n))
            if n<=4:
                QQ=product(Q,Q,f);assert QQ==Q
                PQ=product(Q,I,f); QP=product(I,Q,f)
                C=tuple(tuple(f.sub(PQ[i][j],QP[i][j]) for j in range(n)) for i in range(n))
                cr=rank(C,f)
                C2=product(C,C,f); C3=product(C2,C,f)
                delta=f.mul(alpha,f.sub(alpha,1))
                assert C3==tuple(tuple(f.mul(delta,C[i][j]) for j in range(n)) for i in range(n))
                if alpha in (0,1):
                    if cr==2:assert C2!=tuple((0,)*n for _ in range(n))
                    if cr==1:assert C2==tuple((0,)*n for _ in range(n))
            else:
                a,b=raw[:r],raw[r:]
                c,d=v[:r],v[r:]
                cr=int(any(a) and any(d))+int(any(b) and any(c))
            obs[(alpha,cr)]+=1
    expected=theory(n,r,q)
    assert obs==expected,(n,r,q,obs,expected)
    total=q**(n-1)*(q**n-1)//(q-1)
    assert sum(obs.values())==total
    # Symmetry under Q -> I-Q on scalar distribution (relabel alpha to 1-alpha)
    if q!=4:
        dual=theory(n,n-r,q)
        assert obs==Counter({(f.sub(1,a),t):c for (a,t),c in dual.items()})
    print(f'CHECK_OK q={q} n={n} r={r} projections={total} zero={sum(v for (a,t),v in obs.items() if t==0)}')

if __name__=='__main__':
    for q,n,r in [(2,4,2),(3,4,2),(4,4,2),(5,4,2),(2,5,2),(2,5,3),(3,5,2),(3,5,3),(2,6,2),(2,6,3),(2,6,4)]:
        run(n,r,q)
    print('VERIFY_OK all mixed-rank projection counts and cubic laws')
