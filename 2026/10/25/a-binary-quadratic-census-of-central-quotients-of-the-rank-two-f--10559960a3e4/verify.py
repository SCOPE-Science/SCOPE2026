"""Exact finite-field checks for central quotients of the rank-two, class-four free Lie algebra.

Run: python3 verify.py
Only Python's standard library is required.  All calculations use exact finite-field arithmetic.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self, q):
        if q not in (2, 3, 4, 5):
            raise ValueError('Only explicitly tested fields are implemented')
        self.q = q
        self.p = 2 if q == 4 else q

    def add(self, a, b):
        return a ^ b if self.q == 4 else (a+b) % self.q

    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q

    def mul(self, a, b):
        if self.q != 4:
            return a*b % self.q
        r = 0
        while b:
            if b & 1:
                r ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7  # monic irreducible t^2+t+1
        return r

    def inverse(self, a):
        assert a
        for b in range(1, self.q):
            if self.mul(a,b) == 1:
                return b
        raise AssertionError('Finite-field inversion failed')

    def subtract(self,a,b):
        return self.add(a,self.neg(b))

    def poly_Q(self,K,x,y):
        A,B,C=K
        return self.add(self.subtract(self.mul(A,self.mul(y,y)),self.mul(B,self.mul(x,y))),self.mul(C,self.mul(x,x)))

    def rank(self, rows):
        A=[row[:] for row in rows]
        m=len(A);n=len(A[0]);r=0
        for j in range(n):
            pivot=next((i for i in range(r,m) if A[i][j]),None)
            if pivot is None:
                continue
            A[r],A[pivot]=A[pivot],A[r]
            inverse=self.inverse(A[r][j])
            A[r]=[self.mul(x,inverse) for x in A[r]]
            for i in range(r+1,m):
                if A[i][j]:
                    t=A[i][j]
                    A[i]=[self.subtract(v,self.mul(t,w)) for v,w in zip(A[i],A[r])]
            r+=1
            if r==m:
                break
        return r

    def normalize(self,v):
        t=next(x for x in v if x)
        inv=self.inverse(t)
        return tuple(self.mul(x,inv) for x in v)

    def projective_roots(self,K):
        n=sum(self.poly_Q(K,x,y)==0 for x,y in product(range(self.q),repeat=2) if x or y)
        assert n % (self.q-1)==0
        return n//(self.q-1)

    def adjoint_augmented(self,alpha,beta,gamma,delta,epsilon,K):
        # Basis x,y,z,u,v,a,b,c for the eight-dimensional free algebra.
        # Brackets: [x,y]=z,[x,z]=u,[y,z]=v,
        # [x,u]=a,[y,u]=b,[x,v]=b,[y,v]=c.
        M=[[0]*9 for _ in range(8)]
        def put(i,j,val):
            M[i][j]=self.add(M[i][j],val)
        put(2,0,self.neg(beta));put(3,0,self.neg(gamma))
        put(5,0,self.neg(delta));put(6,0,self.neg(epsilon))
        put(2,1,alpha);put(4,1,self.neg(gamma))
        put(6,1,self.neg(delta));put(7,1,self.neg(epsilon))
        put(3,2,alpha);put(4,2,beta)
        put(5,3,alpha);put(6,3,beta)
        put(6,4,alpha);put(7,4,beta)
        for k in range(3):
            M[5+k][8]=K[k]
        return M

    def expected(self,K):
        q=self.q;nu=self.projective_roots(K)
        return {0:q*q,1:nu*(q-1)*q*q,
                2:(q-1)*q**4+(q*q-1-nu*(q-1))*q*q,
                3:nu*(q-1)*q**5,
                4:(q*q-1-nu*(q-1))*q**5}

    def spectrum(self,K):
        out=Counter()
        for alpha,beta,gamma,delta,epsilon in product(range(self.q),repeat=5):
            M=self.adjoint_augmented(alpha,beta,gamma,delta,epsilon,K)
            # Rank of the induced map on the central quotient is rank([ad_X|K])-1.
            r=self.rank(M)-1
            out[r]+=self.q**2  # both free central coordinates are arbitrary
        return dict(out)

    def orbit_partition(self):
        lines={self.normalize(v) for v in product(range(self.q),repeat=3) if any(v)}
        mats=[]
        for r,s,t,u in product(range(self.q),repeat=4):
            determinant=self.subtract(self.mul(r,u),self.mul(s,t))
            if determinant:
                mats.append((r,s,t,u))
        unseen=set(lines);orbits=[]
        while unseen:
            K=next(iter(unseen));A,B,C=K
            orb=set()
            for r,s,t,u in mats:
                two=self.add(1,1)
                kp=(self.add(self.add(self.mul(A,self.mul(r,r)),self.mul(B,self.mul(r,t))),self.mul(C,self.mul(t,t))),
                    self.add(self.add(self.mul(self.mul(two,A),self.mul(r,s)),self.mul(B,self.add(self.mul(r,u),self.mul(s,t)))),self.mul(self.mul(two,C),self.mul(t,u))),
                    self.add(self.add(self.mul(A,self.mul(s,s)),self.mul(B,self.mul(s,u))),self.mul(C,self.mul(u,u))))
                # Overall determinant scalar from the induced free-Lie action is irrelevant.
                orb.add(self.normalize(kp))
            assert orb.issubset(lines)
            unseen-=orb
            orbits.append((self.projective_roots(K),len(orb)))
        return sorted(orbits)

def check_jacobi(F):
    # Exact basis Jacobi identities in every tested characteristic.
    bracket={(0,1,2):1,(0,2,3):1,(1,2,4):1,
             (0,3,5):1,(1,3,6):1,(0,4,6):1,(1,4,7):1}
    def b(i,j):
        if i==j:return [0]*8
        lo,hi=sorted((i,j));sgn=1 if i<j else F.neg(1)
        v=[0]*8
        for (a,c,d),coeff in bracket.items():
            if (a,c)==(lo,hi):v[d]=F.mul(sgn,coeff)
        return v
    def nested(i,j,k):
        out=[0]*8
        for l,v in enumerate(b(j,k)):
            if v:
                for z,c in enumerate(b(i,l)):
                    out[z]=F.add(out[z],F.mul(v,c))
        return out
    for i,j,k in product(range(8),repeat=3):
        terms=[nested(i,j,k),nested(j,k,i),nested(k,i,j)]
        assert all(F.add(F.add(terms[0][a],terms[1][a]),terms[2][a])==0 for a in range(8))

for q in (2,3,4,5):
    F=Field(q)
    check_jacobi(F)
    expected_orbits=sorted([(0,(q*q-q)//2),(1,q+1),(2,q*(q+1)//2)])
    assert F.orbit_partition()==expected_orbits,(q,F.orbit_partition(),expected_orbits)
    if q in (2,3,4):
        lines={F.normalize(v) for v in product(range(q),repeat=3) if any(v)}
    else:
        # Three representatives; every other line is related by a checked GL_2 orbit.
        lines={(1,0,0),(0,1,0),(1,0,2)}
    for K in lines:
        actual=F.spectrum(K)
        predicted={k:v for k,v in F.expected(K).items() if v}
        assert actual==predicted,(q,K,actual,predicted)
    print('q=',q,'tested ideals=',len(lines),'orbit types=3; OK')
print('CENTRAL_QUOTIENT_RANKS_OK')
