"""Exact finite-field certificates for six-branch generalized Fermat curves.

No third-party modules. A field element's integer encoding records its base-3
coefficients in the monic basis 1,t,t^2. The defining polynomials are
    GF(9): t^2+1;  GF(27): t^3-t-1.
The computation verifies finite examples, not the proof for every field.
"""
from itertools import combinations
from collections import Counter

class Field:
    def __init__(self, degree):
        assert degree in (2, 3)
        self.degree, self.size = degree, 3**degree
        self.add = [[self.rawadd(a, b) for b in range(self.size)] for a in range(self.size)]
        self.mul = [[self.rawmul(a, b) for b in range(self.size)] for a in range(self.size)]
        self.neg = [self.rawadd(0, self.scale(a, 2)) for a in range(self.size)]
        self.cube = [self.mul[self.mul[a][a]][a] for a in range(self.size)]
        assert all(self.cube[self.cube[a]] == a for a in range(self.size)) if degree == 2 else all(self.cube[self.cube[self.cube[a]]] == a for a in range(self.size))
    def coeff(self, a):
        return [(a // 3**j) % 3 for j in range(self.degree)]
    def number(self, v):
        return sum(int(t % 3)*3**j for j, t in enumerate(v))
    def rawadd(self, a, b):
        return self.number([(x+y) % 3 for x,y in zip(self.coeff(a), self.coeff(b))])
    def scale(self, a, c):
        return self.number([c*x%3 for x in self.coeff(a)])
    def rawmul(self, a, b):
        ca, cb = self.coeff(a),self.coeff(b)
        c = [0]*(2*self.degree-1)
        for i,x in enumerate(ca):
            for j,y in enumerate(cb):
                c[i+j] = (c[i+j]+x*y)%3
        for j in range(len(c)-1,self.degree-1,-1):
            t=c[j];c[j]=0
            if self.degree==2:
                c[j-2]=(c[j-2]+2*t)%3    # t^2=-1
            else:
                c[j-2]=(c[j-2]+t)%3      # t^3=t+1
                c[j-3]=(c[j-3]+t)%3
        return self.number(c[:self.degree])
    def plus(self,a,b):return self.add[a][b]
    def times(self,a,b):return self.mul[a][b]
    def minus(self,a,b):return self.add[a][self.neg[b]]
    def determinant(self,m):
        return self.minus(self.times(m[0][0],m[1][1]),self.times(m[0][1],m[1][0]))
    def matrix_product_twist(self,m):
        return [[self.plus(self.times(m[i][0],self.cube[m[0][j]]),
                           self.times(m[i][1],self.cube[m[1][j]]))
                 for j in range(2)] for i in range(2)]
    def harmonic(self,subset):
        if -1 in subset:       # -1 integer means the distinguished infinite point
            triple=[x for x in subset if x!=-1]
            return self.plus(self.plus(triple[0],triple[1]),triple[2])==0
        a,b,c,d=subset
        return self.plus(self.times(self.minus(a,c),self.minus(b,d)),
                         self.times(self.minus(a,d),self.minus(b,c)))==0
    def genus2_matrices(self,roots):
        poly=[1]
        for r in [0,1]+list(roots):
            nxt=[0]*(len(poly)+1)
            for j,t in enumerate(poly):
                nxt[j]=self.minus(nxt[j],self.times(t,r))
                nxt[j+1]=self.plus(nxt[j+1],t)
            poly=nxt
        assert len(poly)==6 and poly[5]==1
        # Cartier-Manin/Hasse-Witt convention from coefficients of f^(p-1)/2=f
        M=[[poly[2],poly[1]],[poly[5],poly[4]]]
        if self.determinant(M)!=0:return 2, M, poly
        P=self.matrix_product_twist(M)
        return (1 if any(x for row in P for x in row) else 0), M, poly
    def profile(self,roots):
        assert len(set(roots))==3 and all(a not in (0,1) for a in roots)
        B=(-1,0,1)+tuple(roots)
        h=sum(self.harmonic(sub) for sub in combinations(B,4))
        r,m,poly=self.genus2_matrices(roots)
        return h,r,m,poly

f9=Field(2)
f27=Field(3)
examples27={
    (0,0):(3,19,25),
    (0,1):(3,7,14),
    (0,2):(3,4,9),
    (1,2):(2,3,4),
    (2,2):(2,3,6),
}
for target,abc in examples27.items():
    h,r,m,poly=f27.profile(abc)
    assert (h,r)==target, (target,abc,(h,r),m,poly)
    print('GF27 example',abc, 'h=',h,'genus2rank=',r,'genus17rank=',15-h+r,
          'CM=',m)
h,r,m,p=f9.profile((2,3,6))
assert (h,r)==(3,2)
print('GF9 example',(2,3,6), 'h=',h,'genus2rank=',r,'genus17rank=',15-h+r, 'CM=',m)

counts27=Counter(); counts9=Counter()
for abc in combinations(range(2,27),3):
    h,r,_,_=f27.profile(abc)
    assert 0<=h<=3 and (h==0 or r==2)
    counts27[(h,r)]+=1
for abc in combinations(range(2,9),3):
    h,r,_,_=f9.profile(abc)
    assert 0<=h<=3 and (h==0 or r==2)
    counts9[(h,r)]+=1
assert counts27=={(0,0):6,(0,1):54,(0,2):1040,(1,2):1020,(2,2):180}, counts27
assert counts9=={(2,2):30,(3,2):5}, counts9
assert sum(counts27.values())==2300 and sum(counts9.values())==35
assert {15-h+r for h,r in set(counts27)|set(counts9)}=={14,15,16,17}
print('VERIFY_OK: GF9 35 and GF27 2300 six-branch charts; six (h,r) profiles; all ranks 14..17')
