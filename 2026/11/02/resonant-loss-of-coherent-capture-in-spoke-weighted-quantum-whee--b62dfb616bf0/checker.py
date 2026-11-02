"""Self-contained supplementary arithmetic checks for a weighted-wheel capture theorem.

For rim-to-hub hopping alpha, apply a diagonal similarity which maps the
symmetric adjacency to a nonsymmetric rational matrix: rim<-hub weight 1,
hub<-rim weight q=alpha**2. This preserves Krylov rank for rim probes and
also for any collection of vertex probes. The analytic theorem, not these
finite checks, supplies the all-n proof. Uses only Python's standard library.
"""
from fractions import Fraction
from math import cos, gcd, pi

PRIMES = (1000003, 1000033)
QVALUES = (Fraction(1), Fraction(1,4), Fraction(1,2), Fraction(4,9),
           Fraction(2,3), Fraction(3,8), Fraction(2,5))

def row_rank_mod(rows, prime):
    rows = [row[:] for row in rows]
    nr, nc = len(rows), len(rows[0]); rank = 0
    for col in range(nc):
        pivot = next((i for i in range(rank,nr) if rows[i][col] % prime),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        inv=pow(rows[rank][col] % prime, -1, prime)
        for c in range(col,nc): rows[rank][c]=rows[rank][c]*inv % prime
        for i in range(rank+1,nr):
            a=rows[i][col] % prime
            if a:
                for c in range(col,nc):
                    rows[i][c]=(rows[i][c]-a*rows[rank][c]) % prime
        rank+=1
        if rank==nr: break
    return rank

def krylov_rows(n, sources, q, prime=None):
    """N x (N*number_sources) rational Krylov matrix, optional mod prime."""
    q=Fraction(q)
    a=q if prime is None else q.numerator*pow(q.denominator,-1,prime)%prime
    N=n+1; rows=[[] for _ in range(N)]
    for source in sources:
        v=[int(j==source) for j in range(N)]
        for _ in range(N):
            for j in range(N): rows[j].append(v[j])
            vnew=[v[(j-1)%n]+v[(j+1)%n]+v[n] for j in range(n)]
            vnew.append(a*sum(v[:n]))
            v=[x%prime for x in vnew] if prime else vnew
    return rows

def row_rank_fraction(rows):
    """Exact Gaussian rank over Q, for a selected compact matrix."""
    rows=[[Fraction(x) for x in r] for r in rows]
    nr,nc=len(rows),len(rows[0]); rk=0
    for col in range(nc):
        pivot=next((i for i in range(rk,nr) if rows[i][col]),None)
        if pivot is None: continue
        rows[rk],rows[pivot]=rows[pivot],rows[rk]
        z=rows[rk][col]
        for j in range(col,nc): rows[rk][j]/=z
        for i in range(rk+1,nr):
            z=rows[i][col]
            if z:
                for j in range(col,nc): rows[i][j]-=z*rows[rk][j]
        rk+=1
        if rk==nr: break
    return rk

from dataclasses import dataclass

@dataclass(frozen=True)
class Qsqrt5:
    """Exact field element a+b*sqrt(5), a,b rational."""
    a: Fraction
    b: Fraction=Fraction(0)
    def __add__(self,other):
        z=other if isinstance(other,Qsqrt5) else Qsqrt5(Fraction(other))
        return Qsqrt5(self.a+z.a,self.b+z.b)
    __radd__=__add__
    def __neg__(self):return Qsqrt5(-self.a,-self.b)
    def __sub__(self,other):return self+-other if isinstance(other,Qsqrt5) else self+(-Fraction(other))
    def __rsub__(self,other):return -self+other
    def __mul__(self,other):
        z=other if isinstance(other,Qsqrt5) else Qsqrt5(Fraction(other))
        return Qsqrt5(self.a*z.a+5*self.b*z.b,self.a*z.b+self.b*z.a)
    __rmul__=__mul__
    def __truediv__(self,other):
        z=other if isinstance(other,Qsqrt5) else Qsqrt5(Fraction(other))
        norm=z.a*z.a-5*z.b*z.b
        assert norm
        return self*Qsqrt5(z.a/norm,-z.b/norm)
    def __bool__(self):return bool(self.a or self.b)
    def __float__(self):return float(self.a)+float(self.b)*5**0.5

def rank_qsqrt5(matrix):
    rows=[[v if isinstance(v,Qsqrt5) else Qsqrt5(Fraction(v)) for v in row]
          for row in matrix]
    nr,nc=len(rows),len(rows[0]); rk=0
    for col in range(nc):
        pivot=next((i for i in range(rk,nr) if rows[i][col]),None)
        if pivot is None:continue
        rows[rk],rows[pivot]=rows[pivot],rows[rk]
        z=rows[rk][col]
        for c in range(col,nc):rows[rk][c]=rows[rk][c]/z
        for i in range(rk+1,nr):
            z=rows[i][col]
            if z:
                for c in range(col,nc):
                    rows[i][c]=rows[i][c]-z*rows[rk][c]
        rk+=1
        if rk==nr:break
    return rk

def krylov_qsqrt5(n,sources,q):
    rows=[[] for _ in range(n+1)]
    for source in sources:
        v=[Qsqrt5(Fraction(j==source)) for j in range(n+1)]
        for _ in range(n+1):
            for j in range(n+1):rows[j].append(v[j])
            vnew=[v[(j-1)%n]+v[(j+1)%n]+v[n] for j in range(n)]
            vnew.append(q*sum(v[:n]))
            v=vnew
    return rows

def predicted(n,d,q):
    base=n+1-(gcd(n,2*d)-1)//2
    special=0
    # Floating arithmetic is only used to identify the trial's resonance
    # candidate; rank checking remains exact in finite fields or Q.
    for k in range(n//4+1,n//2+1):
        c=2*cos(2*pi*k/n)
        if abs(float(q)-c*(c-2)/n)<1e-9:
            special=int((2*k*d)%(2*n)!=n)
    return base-special

def check():
    cnt=0
    for prime in PRIMES:
        for q in QVALUES:
            for n in range(5,38):
                for d in range(1,n//2+1):
                    got=row_rank_mod(krylov_rows(n,(0,d),q,prime),prime)
                    want=predicted(n,d,q)
                    assert got==want,(prime,n,d,q,got,want)
                    cnt+=1
                got=row_rank_mod(krylov_rows(n,(n,0),q,prime),prime)
                assert got==2+n//2,(prime,n,q,got)
                cnt+=1
    print('modular-checks:',cnt,'(two distinct primes, seven rational squared couplings, n=5..37)')
    exact=0
    for n,q in [(6,Fraction(1,2)),(8,Fraction(1)),(12,Fraction(1,4))]:
        values=[]
        for d in range(1,n//2+1):
            got=row_rank_fraction(krylov_rows(n,(0,d),q))
            want=predicted(n,d,q)
            assert got==want,(n,d,q,got,want)
            values.append(got);exact+=1
        got=row_rank_fraction(krylov_rows(n,(n,0),q))
        assert got==2+n//2,(n,q,got)
        exact+=1
        print('exact-Q ranks at n=%s, alpha^2=%s: rim-pairs=%s, hub-rim=%s'
              % (n,q,values,got))
    print('exact-rational-checks:',exact)
    # Nonrational exact resonance: c=2*cos(4*pi/5)=(-1-sqrt(5))/2.
    # q=c(c-2)/n=(5+3*sqrt(5))/(2*n) for n=5 or n=10
    # with k=2 (n=5), k=4 (n=10), respectively.
    algebraic=0
    for n in (5,10):
        q=Qsqrt5(Fraction(5,2*n),Fraction(3,2*n))
        values=[]
        for d in range(1,n//2+1):
            got=rank_qsqrt5(krylov_qsqrt5(n,(0,d),q))
            assert got==predicted(n,d,q),(n,d,q,got)
            values.append(got);algebraic+=1
        got=rank_qsqrt5(krylov_qsqrt5(n,(n,0),q))
        assert got==2+n//2,(n,q,got)
        algebraic+=1
        print('exact-Q(sqrt5) resonance ranks for n=%d: rim-pairs=%s, hub-rim=%d'
              %(n,values,got))
    print('exact-quadratic-field-checks:',algebraic)
    print('VERIFIED: all assertions passed; finite checks supplement an analytical proof')

if __name__=='__main__':check()
