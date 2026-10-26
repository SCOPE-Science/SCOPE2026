"""Standalone finite-field checks for commuting triples in truncated Witt Lie algebras.

Run: python3 verify.py ; uses Python standard library only.
"""
from itertools import product
from collections import Counter
import random


class Field:
    def __init__(self, p, ext=1, modulus_constant=None):
        self.p, self.ext, self.q = p, ext, p**ext
        self.modc = modulus_constant
        assert ext == 1 or (ext == 2 and modulus_constant is not None)
        self.add = [[0]*self.q for _ in range(self.q)]
        self.mul = [[0]*self.q for _ in range(self.q)]
        for a in range(self.q):
            for b in range(self.q):
                if ext == 1:
                    self.add[a][b] = (a+b) % p
                    self.mul[a][b] = (a*b) % p
                else:
                    a0,a1 = a%p,a//p
                    b0,b1 = b%p,b//p
                    self.add[a][b] = ((a0+b0)%p)+p*((a1+b1)%p)
                    self.mul[a][b] = ((a0*b0-modulus_constant*a1*b1)%p)+p*((a0*b1+a1*b0)%p)
        self.inv = [0]*self.q
        for a in range(1,self.q):
            self.inv[a] = next(b for b in range(1,self.q) if self.mul[a][b] == 1)
        self.scalar = [i%p for i in range(p)]

    def rank(self, rows):
        mat = [list(row) for row in rows]
        if not mat: return 0
        r = 0
        for c in range(len(mat[0])):
            k = next((i for i in range(r,len(mat)) if mat[i][c]), None)
            if k is None: continue
            mat[k],mat[r] = mat[r],mat[k]
            inv = self.inv[mat[r][c]]
            mat[r] = [self.mul[inv][v] for v in mat[r]]
            for i in range(r+1,len(mat)):
                z = mat[i][c]
                if z:
                    mat[i] = [self.add[x][self.neg(self.mul[z][y])] for x,y in zip(mat[i],mat[r])]
            r += 1
            if r == len(mat): break
        return r

    def neg(self,a):
        if self.ext==1: return (-a)%self.p
        a0,a1=a%self.p,a//self.p
        return (-a0)%self.p+self.p*((-a1)%self.p)

    def bracket(self,f,g):
        p=self.p
        out=[0]*p
        for i,x in enumerate(f):
            if not x: continue
            for j,y in enumerate(g):
                if not y:continue
                degree=i+j-1
                if 0<=degree<p:
                    term=self.mul[self.mul[x][y]][(j-i)%p]
                    out[degree]=self.add[out[degree]][term]
        return tuple(out)

    def adjoint_rank(self,f):
        p=self.p
        M=[[0]*p for _ in range(p)]
        for i,x in enumerate(f):
            if not x:continue
            for j in range(p):
                k=i+j-1
                if 0<=k<p:
                    M[k][j]=self.add[M[k][j]][self.mul[x][(j-i)%p]]
        return self.rank(M)


def rank_prediction(p,v):
    if v==p:return 0
    if v<=1:return p-1
    return p-v+1-int(2*v<=p)


def pair_formula(p,q):
    return q**(p+1) + ((p-1)//2)*(q*q-1)*q**(p-2)


def triple_formula(p,q):
    t=(p-1)//2
    return (q+1)**2*q**(3*t-1)+(q*q-1)*q**p-(2*q+1)*q**(p-2)


def verify(p,ext=1,modc=None,exhaustive=True):
    F=Field(p,ext,modc)
    q=F.q
    vec=lambda: product(range(q),repeat=p)
    ranks=Counter()
    tested=0
    if exhaustive:
        iterator=vec()
    else:
        r=random.Random(237*100+p*17+q)
        iterator=([0]*v+[r.randrange(1,q)]+[r.randrange(q) for _ in range(p-v-1)] if v<p else [0]*p
                  for v in list(range(p+1))*20)
    for f in iterator:
        v=next((i for i,x in enumerate(f) if x),p)
        rank=F.adjoint_rank(f)
        expected=rank_prediction(p,v)
        assert rank==expected,(p,q,f,rank,expected)
        ranks[rank]+=1;tested+=1
    if exhaustive:
        assert tested==q**p
        k2=sum(n*q**(p-r) for r,n in ranks.items())
        assert k2==pair_formula(p,q),('K2',p,q,k2,pair_formula(p,q))
    # Literal centralizer tests on configurations of all valuation types.
    if q**p <= 3200:
        vectors=list(vec())
        for v in range(p+1):
            f=tuple(([0]*v+[1]+[(i*i+v)%q for i in range(p-v-1)]) if v<p else [0]*p)
            central=sum(F.bracket(f,g)==(0,)*p for g in vectors)
            assert central==q**(p-rank_prediction(p,v)),('cent',p,q,v,central)
    if p==3 and q==3:
        vs=list(vec())
        comm={(f,g):F.bracket(f,g)==(0,)*p for f in vs for g in vs}
        triples=sum(comm[f,g] and comm[f,h] and comm[g,h]
                    for f in vs for g in vs for h in vs)
        assert triples==triple_formula(p,q),(triples,triple_formula(p,q))
    if p==5 and q==5:
        # Directly count commuting pairs in the nonabelian 3-space of vector
        # fields with coefficients divisible by x^2, without invoking ranks.
        B=[(0,0,*tail) for tail in product(range(q),repeat=3)]
        KB=sum(F.bracket(f,g)==(0,)*p for f in B for g in B)
        assert KB==q**4+(q*q-1)*q**3,(KB,q**4+(q*q-1)*q**3)
        assert ranks==Counter({4:3000,3:120,2:4,0:1})
        # The centralizers for valuations 0,1,2,3 are abelian;
        # those for valuation 4 are B. Enumerating the entire f population
        # yields the triple statistic using the independently counted KB.
        total=pair_formula(p,q)
        for v in range(p):
            multiplicity=(q-1)*q**(p-v-1)
            if v<=1: total+=multiplicity*q*q
            elif v==4: total+=multiplicity*KB
            else:total+=multiplicity*q**(2*(p-rank_prediction(p,v)))
        assert total==triple_formula(p,q),(total,triple_formula(p,q))
    print('FIELD_PASS',p,q,'tested',tested,'ranks',dict(sorted(ranks.items())))


if __name__=='__main__':
    verify(3,1)
    verify(3,2,1)  # F_9 = F_3[u]/(u^2+1)
    verify(5,1)
    verify(7,1,exhaustive=False)
    verify(5,2,2,exhaustive=False) # F_25 = F_5[u]/(u^2+2)
    print('VERIFY_OK_WITT_COMMUTING_TRIPLES')
