"""Finite exhaustive checks for restricted-nilpotent outer derivation classes."""
from itertools import product
from math import prod

class Field:
    def __init__(self, q):
        self.q=q
        self.p=2 if q in (2,4) else 3
        assert q in (2,3,4)
    def add(self,a,b):
        return a^b if self.p==2 else (a+b)%3
    def neg(self,a): return a if self.p==2 else (-a)%3
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4: return a*b%self.p
        z=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: z^=1<<(i+j)
        if z&8: z^=0b1100  # x^3 = x^2+x modulo x^2+x+1
        if z&4: z^=0b0111
        return z
    def pow(self,a,n):
        z=1
        for _ in range(n):z=self.mul(z,a)
        return z

def mm(A,B,m,F):
    return tuple(F.add_many(F.mul(A[i*m+k],B[k*m+j]) for k in range(m)) for i in range(m) for j in range(m))

def add_many(self,xs):
    y=0
    for x in xs:y=self.add(y,x)
    return y
Field.add_many=add_many

def matpow(A,m,h,F):
    ans=tuple(int(i==j) for i in range(m) for j in range(m))
    for _ in range(h): ans=mm(ans,A,m,F)
    return ans

def sq_zero_mat(A,m,F,h): return not any(matpow(A,m,h,F))

def test(edges, sizes,q,h):
    F=Field(q)
    v=1+max(max(u,w) for u,w in edges)
    assert len(edges)==len(sizes)
    all_matrix=[list(product(range(q),repeat=m*m)) for m in sizes]
    blocks=list(product(*all_matrix))
    offsets=set()
    for potential in product(range(q),repeat=v-1):
        t=(0,)+potential
        offsets.add(tuple(F.sub(t[w],t[u]) for u,w in edges))
    def gauge(mats,alpha):
        return tuple(tuple(F.add(x,alpha[i]) if j//sizes[i]==j%sizes[i] else x for j,x in enumerate(mats[i])) for i in range(len(sizes)))
    seen=set(); actual=0; rank=[0]*len(sizes)
    for B in blocks:
        if B in seen: continue
        orbit={gauge(B,t) for t in offsets}
        seen.update(orbit)
        admissible=any(all(sq_zero_mat(C[i],sizes[i],F,h) for i in range(len(sizes))) for C in orbit)
        if admissible: actual+=1
    individual=[sum(sq_zero_mat(M,m,F,h) for M in matrices) for m,matrices in zip(sizes,all_matrix)]
    expected=prod(individual)
    assert len(seen)==len(blocks)
    assert actual==expected, (edges,sizes,q,h,actual,expected)
    print('PASS',edges,sizes,'q',q,'h',h,'classes',len(blocks)//len(offsets),'nilpotent',actual,'individual',individual)

if __name__=='__main__':
    tests=[
        ([(0,1)],[2],2,2),
        ([(0,1)],[2],3,3),
        ([(0,1)],[3],2,2),
        ([(0,1)],[3],2,4),
        ([(0,1),(1,2),(2,0)],[2,1,1],2,2),
        ([(0,1),(1,2),(2,3)],[2,1,1],2,2),
        ([(0,1),(1,2),(2,0)],[2,1,1],3,3),
        ([(0,1)],[2],4,2),
        ([(0,1),(1,2),(2,0)],[2,1,1],4,2),
    ]
    for E,M,q,h in tests:test(E,M,q,h)
    print('RESTRICTED_HH1_QUOTIENT_OK',len(tests),'complete quotient enumerations')

def direct_leibniz_binary_kronecker():
    # Basis e0,e1,a,b; both arrows oriented 0 -> 1.
    def multiply(x,y):
        z=0
        if x&1:
            if y&1: z^=1
            if y&4: z^=4
            if y&8: z^=8
        if x&2 and y&2: z^=2
        if x&4 and y&2: z^=4
        if x&8 and y&2: z^=8
        return z
    def lin(D,x):
        z=0
        for i in range(4):
            if (x>>i)&1:z^=D[i]
        return z
    inner={tuple(multiply(z,1<<i)^multiply(1<<i,z) for i in range(4)) for z in range(16)}
    valid=[]
    table=[[multiply(1<<i,1<<j) for j in range(4)] for i in range(4)]
    for D in product(range(16),repeat=4):
        if all(lin(D,table[i][j])==(multiply(D[i],1<<j)^multiply(1<<i,D[j])) for i in range(4) for j in range(4)):
            valid.append(D)
    orbits=set(); pnil=set()
    for D in valid:
        key=min(tuple(D[i]^I[i] for i in range(4)) for I in inner)
        orbits.add(key)
        Dsq=tuple(lin(D,D[i]) for i in range(4))
        if Dsq in inner:pnil.add(key)
    assert len(valid)==64 and len(inner)==8 and len(orbits)==8 and len(pnil)==4,(len(valid),len(inner),len(orbits),len(pnil))
    print('PASS direct full Leibniz GF2 Kronecker: derivations',len(valid),'inners',len(inner),'HH1',len(orbits),'p-square-zero',len(pnil))

if __name__=='__main__':
    direct_leibniz_binary_kronecker()

def partitions(n, ceiling=None):
    if ceiling is None:ceiling=n
    if n==0:
        yield ()
    else:
        for x in range(min(n,ceiling),0,-1):
            for tail in partitions(n-x,x): yield (x,)+tail

def jordan_count(m,h,q):
    from fractions import Fraction
    if m==0:return 1
    GL=prod(q**m-q**i for i in range(m))
    total=Fraction(0)
    for lam in partitions(m):
        if lam[0]>h:continue
        cols=[sum(x>=j for x in lam) for j in range(1,lam[0]+1)]
        centralizer=Fraction(q**sum(c*c for c in cols))
        for size in set(lam):
            for j in range(1,lam.count(size)+1):
                centralizer*=Fraction(q**j-1,q**j)
        total+=Fraction(GL,1)/centralizer
    assert total.denominator==1
    return int(total)

def check_jordan_numbers():
    tests=[(2,2,2),(2,3,3),(2,2,4),(3,2,2),(3,4,2),(3,3,3),(4,2,2)]
    for m,h,q in tests:
        F=Field(q)
        enumeration=sum(sq_zero_mat(M,m,F,h) for M in product(range(q),repeat=m*m))
        expected=jordan_count(m,h,q)
        assert enumeration==expected,(m,h,q,enumeration,expected)
        print('PASS Jordan-orbit count',m,h,q,enumeration)
    print('JORDAN_CENTRALIZER_SUM_OK',len(tests))

if __name__=='__main__':
    check_jordan_numbers()
