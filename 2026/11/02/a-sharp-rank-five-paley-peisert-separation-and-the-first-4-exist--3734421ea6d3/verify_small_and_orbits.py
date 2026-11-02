"""Reproducible exact Peisert and Paley extension checks (Python stdlib only).

A vertex of GF(p^k) is encoded by the base-p digits of its polynomial
representative, and all arithmetic is performed modulo the monic polynomial
listed below. Tested polynomials are certified irreducible by trial division
by all monic polynomials of degree <= floor(k/2).

Four-vertex checks with a fixed zero use translations. The orbit-reduced
positive checks also use multiplication by fourth powers for Peisert, and
multiplication by squares for Paley; see the accompanying mathematical proof.
"""
from itertools import product
from math import isqrt

# q, prime characteristic, monic modulus low-degree coefficients, primitive element.
PARAMETERS = ((9, 3, (1, 0), 4),
              (49, 7, (4, 0), 8),
              (81, 3, (2, 1, 0, 0), 3),
              (121, 11, (9, 0), 13),
              (361, 19, (17, 0), 21))

def rem(a, b, p):
    u = list(a)
    while u and u[-1] == 0: u.pop()
    while len(u) >= len(b):
        h = u[-1]  # b is monic
        off = len(u)-len(b)
        for i in range(len(b)): u[off+i] = (u[off+i]-h*b[i])%p
        while u and u[-1] == 0: u.pop()
    return u

def is_irreducible(coeff, p):
    k = len(coeff); polynomial = list(coeff)+[1]
    for j in range(1, k//2 + 1):
        for c in product(range(p), repeat=j):
            if not rem(polynomial, list(c)+[1], p): return False
    return True

class Field:
    def __init__(self, p, coeff, gen):
        self.p=p;self.coeff=coeff;self.k=len(coeff);self.q=p**self.k;self.gen=gen
        assert is_irreducible(coeff,p)
        self.digits=[]
        for x in range(self.q):
            ds=[];y=x
            for _ in range(self.k):ds.append(y%p);y//=p
            self.digits.append(ds)
        self.mul_table=[[self.multiply(i,j) for j in range(self.q)] for i in range(self.q)]
        assert self.power(gen,self.q-1)==1
        for l in range(2,self.q):
            if (self.q-1)%l==0 and all(l%v for v in range(2,isqrt(l)+1)):
                assert self.power(gen,(self.q-1)//l)!=1
        self.additive_negative=[self.encode([(-z)%p for z in self.digits[a]]) for a in range(self.q)]
    def encode(self, ds):return sum((z%self.p)*self.p**i for i,z in enumerate(ds))
    def add(self,a,b):return self.encode([(x+y)%self.p for x,y in zip(self.digits[a],self.digits[b])])
    def minus(self,a,b):return self.add(a,self.additive_negative[b])
    def multiply(self,a,b):
        p=self.p;k=self.k;coeff=self.coeff
        v=[0]*(2*k-1)
        for i,x in enumerate(self.digits[a]):
            for j,y in enumerate(self.digits[b]):v[i+j]=(v[i+j]+x*y)%p
        for h in range(2*k-2,k-1,-1):
            t=v[h]
            for j in range(k):v[h-k+j]=(v[h-k+j]-t*coeff[j])%p
        return self.encode(v[:k])
    def power(self,a,n):
        v=1
        while n:
            if n&1:v=self.mul_table[v][a]
            a=self.mul_table[a][a];n//=2
        return v
    def graph(self,peisert=True):
        d=set();v=1
        for j in range(self.q-1):
            if (j%4 in (0,1)) if peisert else (j%2==0):d.add(v)
            v=self.mul_table[v][self.gen]
        assert len(d)==(self.q-1)//2
        ms=[]
        for x in range(self.q):
            bit=0
            for y in range(self.q):
                if self.minus(x,y) in d:bit|=1<<y
            ms.append(bit)
        assert all((ms[x]>>y)&1 == (ms[y]>>x)&1 for x in range(self.q) for y in range(self.q))
        assert all(mask.bit_count()==(self.q-1)//2 for mask in ms)
        return ms

def count_patterns(mask, vertices):
    q=len(mask);cnt=[0]* (1<<len(vertices))
    forbidden=set(vertices)
    for x in range(q):
        if x in forbidden:continue
        pattern=sum(1<<j for j,y in enumerate(vertices) if (mask[x]>>y)&1)
        cnt[pattern]+=1
    return cnt

def orbit_minimum(fld,mask,peisert):
    q=fld.q;b=1;bs=[]
    for _ in range(4 if peisert else 2):
        bs.append(b);b=fld.mul_table[b][fld.gen]
    full=(1<<q)-1
    global_min=q;min_count=0;tuples=0;first=None
    for b in bs:
        for c in range(1,q):
            if c==b:continue
            for d in range(c+1,q):
                if d==b:continue
                vv=(0,b,c,d)
                hits=[full ^ sum(1<<u for u in vv)]
                for x in vv:
                    hits=[t&mask[x] for t in hits]+[t&(full^mask[x]) for t in hits]
                local=min(h.bit_count() for h in hits)
                tuples+=1
                if local<global_min:global_min=local;min_count=0;first=vv
                if local==global_min:min_count+=1
    return tuples,global_min,min_count,first


def main():
    witness={9:(0,1,2,3),49:(0,1,2,3),81:(0,1,2,42),121:(0,1,16,17)}
    for q,p,coeff,gen in PARAMETERS:
        f=Field(p,coeff,gen);peisert=f.graph()
        if q in witness:
            c=count_patterns(peisert,witness[q]);missing=[i for i,v in enumerate(c) if v==0]
            print(f'Peisert({q}) polynomial={tuple(coeff)} generator={gen} witness={witness[q]} missing_masks={missing}')
            assert missing
        if q in (121,361):
            m=orbit_minimum(f,peisert,True)
            print(f'Peisert({q}) orbit_check tuples/minimum/minimum_count/witness = {m}')
            if q==121:assert m[1]==0
            else:assert m[:3]==(257044,10,120)
        if q==121:
            paley=f.graph(False)
            mm=orbit_minimum(f,paley,False)
            print(f'Paley(121) orbit_check tuples/minimum/minimum_count/witness = {mm}')
            assert mm[:3]==(14042,2,120)
            for graph,label in [(paley,'Paley'),(peisert,'Peisert')]:
                n3=f.q;full=(1<<n3)-1;small=n3
                for b in range(1,n3):
                    for c in range(b+1,n3):
                        h=[full ^ (1|(1<<b)|(1<<c))]
                        for x in (0,b,c):h=[t&graph[x] for t in h]+[t&(full^graph[x]) for t in h]
                        small=min(small,min(t.bit_count() for t in h))
                print(label,'121 three-extension minimum',small)
                assert small==(12 if label=='Paley' else 11)
    print('ALL_EXACT_EXTENSION_TESTS_PASS')
if __name__=='__main__':main()
