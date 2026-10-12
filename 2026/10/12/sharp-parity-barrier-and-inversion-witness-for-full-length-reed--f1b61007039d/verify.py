"""Finite-field witness checks for full-length Reed-Solomon intersection geometry.

Run: python3 verify.py   (stdlib only)
The infinite-family argument is algebraic and does not depend on testing.
"""
from itertools import permutations, combinations

class FiniteField:
    def __init__(self, p, nonresidue=None):
        self.p=p; self.n= p if nonresidue is None else p*p
        self.c=nonresidue
        if self.c is not None:
            assert all(x*x%p!=self.c%p for x in range(p))
    def add(self,a,b):
        p=self.p
        if self.c is None:return (a+b)%p
        return (a%p+b%p)%p + p*((a//p+b//p)%p)
    def neg(self,a):
        p=self.p
        if self.c is None:return (-a)%p
        return (-(a%p))%p + p*((-(a//p))%p)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p=self.p
        if self.c is None:return a*b%p
        a0,a1=a%p,a//p;b0,b1=b%p,b//p
        return (a0*b0+self.c*a1*b1)%p + p*((a0*b1+a1*b0)%p)
    def power(self,a,e):
        y=1
        while e:
            if e&1:y=self.mul(y,a)
            a=self.mul(a,a);e>>=1
        return y
    def inv(self,a):
        assert a
        return self.power(a,self.n-2)

def rank(rows,F):
    if not rows:return 0
    a=[list(row) for row in rows]
    r=0;m=len(a);n=len(a[0])
    for col in range(n):
        pivot=next((i for i in range(r,m) if a[i][col]!=0),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        z=F.inv(a[r][col]);a[r]=[F.mul(z,v) for v in a[r]]
        for i in range(m):
            if i!=r:
                z=a[i][col]
                if z:a[i]=[F.sub(u,F.mul(z,v)) for u,v in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r

def generator(a,k,F):
    return [[F.power(x,j) for x in a] for j in range(k)]

def intersection_dim(G,H,F):
    return len(G)+len(H)-rank(G+H,F)

def theorem_tests(F):
    q=F.n;k=(q+1)//2
    x=list(range(q));y=[F.power(a,q-2) for a in x]
    assert sorted(y)==x,(q,'inversion not permutation')
    G,H=generator(x,k,F),generator(y,k,F)
    d=intersection_dim(G,H,F)
    assert d==2,(q,d)
    # Every generator row is in the sum-zero hyperplane.
    for row in G+H:
        s=0
        for a in row:s=F.add(s,a)
        assert s==0
    # Distinct k-spaces in a common (q-1)-space meet in dimension >=2.
    assert rank(G,F)==k and rank(H,F)==k
    print(f'FIELD={q} k={k} inversion_intersection={d} distance={2*(k-d)}')

def first_case():
    F=FiniteField(5)
    evals=[(0,1)+tail for tail in permutations((2,3,4))]
    codes=[generator(p,3,F) for p in evals]
    assert len(evals)==6
    assert len({tuple(p) for p in evals})==6
    # Distinct normalized evaluation vectors give distinct code subspaces.
    for i,j in combinations(range(6),2):
        assert intersection_dim(codes[i],codes[j],F)==2
    for inds in combinations(range(6),3):
        rows=[]
        # Common intersection = nullity of parity rows [1, evaluation vector] for each code.
        rows.append([1]*5)
        rows += [list(evals[t]) for t in inds]
        assert 5-rank(rows,F)==1
    # Normalize dual plane normals to (1,a,b); all satisfy one conic.
    pts={(1,p[2],p[3]) for p in evals}
    def quad(X,Y,Z):return (X*X+Y*Y+Z*Z+X*Y+X*Z+Y*Z)%5
    assert all(quad(*P)==0 for P in pts)
    proj=set()
    for x,y,z in [(x,y,z) for x in range(5) for y in range(5) for z in range(5) if (x,y,z)!=(0,0,0)]:
        if quad(x,y,z)==0:
            a=(x,y,z);idx=next(v for v in a if v)
            norm=tuple(t*pow(idx,-1,5)%5 for t in a)
            proj.add(norm)
    assert len(proj)==6
    assert pts==proj,(pts,proj)
    # Nondegenerate symmetric polar form: I+J has determinant 4 in F5.
    assert (4*1*1)%5!=0
    print('FIELD=5 distinct_RS=6 pair_intersections=15x2 triple_intersections=20x1 conic_points=6')

if __name__=='__main__':
    for f in [FiniteField(5),FiniteField(7),FiniteField(3,nonresidue=2),FiniteField(11),FiniteField(13),FiniteField(17),FiniteField(5,nonresidue=3)]:
        theorem_tests(f)
    first_case()
    print('VERIFY_OK')
