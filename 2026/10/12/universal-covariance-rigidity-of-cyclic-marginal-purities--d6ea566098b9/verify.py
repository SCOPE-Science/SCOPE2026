"""Standalone finite checks for cyclic reduced-purity covariance rigidity.

Only Python's standard library is needed. The general theorem is analytical;
these tests independently exercise its finite incidence and Haar expressions.
"""
from fractions import Fraction
from itertools import permutations

PRIME=1000003


def rank_mod(mat, prime=PRIME):
    mat=[[int(x.numerator * pow(x.denominator, -1, prime)) % prime if isinstance(x,Fraction) else int(x) % prime for x in r] for r in mat]
    m=len(mat)
    n=len(mat[0]) if m else 0
    pos=0
    for col in range(n):
        pivot=next((j for j in range(pos,m) if mat[j][col]),None)
        if pivot is None:continue
        mat[pos],mat[pivot]=mat[pivot],mat[pos]
        inv=pow(mat[pos][col],-1,prime)
        for j in range(col,n):mat[pos][j]=mat[pos][j]*inv % prime
        for i in range(pos+1,m):
            a=mat[i][col]
            if a:
                for j in range(col,n):mat[i][j]=(mat[i][j]-a*mat[pos][j]) % prime
        pos+=1
        if pos==min(m,n):break
    return pos


def cut(n,k,i,h):
    left={j%n for j in range(i,i+k)}
    return int((0 in left) != (h in left))


def cuts(n,k,h):
    return [[cut(n,k,i,h0) for i in range(n)] for h0 in [((base+h)%n) for base in range(n)]]  # unused helper


def translated_pair_matrix(n,k,h):
    return [[int(((j in {(s+t)%n for t in range(k)}) != ((j+h)%n in {(s+t)%n for t in range(k)}))) for s in range(n)] for j in range(n)]


def composed(a,b):return tuple(a[b[i]] for i in range(4))


def cycles(a):
    seen=set();count=0
    for i in range(4):
        if i not in seen:
            count+=1;j=i
            while j not in seen:
                seen.add(j);j=a[j]
    return count

PERMS=list(permutations(range(4)))
T1=(1,0,2,3)
T2=(0,1,3,2)
T12=(1,0,3,2)
PROFILE=[]
for perm in PERMS:
    PROFILE.append((cycles(perm),cycles(composed(perm,T1)),cycles(composed(perm,T2)),cycles(composed(perm,T12))))
assert len(PROFILE)==24


def raw_replica(n,p,k,q):
    N=p**n
    numer=sum(p**((n-2*k+q)*a+(k-q)*(b+c)+q*d) for a,b,c,d in PROFILE)
    return Fraction(numer,N*(N+1)*(N+2)*(N+3))


def raw_closed(n,p,k,q):
    N=p**n
    numer=(p**(4*n-2*k)+2*p**(3*n)+4*p**(3*n-2*k)+8*p**(2*n)
            +p**(2*n+2*k)+4*p**(n+2*k)
            +2*p**(2*n-2*k+2*q)+2*p**(n+2*k-2*q))
    return Fraction(numer,N*(N+1)*(N+2)*(N+3))


def gram_cov(n,p,k):
    N=p**n
    mean=Fraction(p**k+p**(n-k),N+1)
    vals=[]
    for d in range(n):
        q=max(0,k-d)+max(0,k-n+d)
        v=raw_closed(n,p,k,q)-mean*mean
        vals.append(v)
    return [[vals[(j-i)%n] for j in range(n)] for i in range(n)]


def test():
    ranks=0;replica=0;covs=0
    for n in range(3,21):
        for k in range(1,n//2+1):
            rows=translated_pair_matrix(n,k,1)
            if 2*k<n: rows+=translated_pair_matrix(n,k,k+1)
            expect=k if 2*k==n else n
            assert rank_mod(rows)==expect,(n,k,'Bell-probe rank')
            ranks+=1
    for n in range(3,10):
        for k in range(1,n//2+1):
            for p in (2,3):
                for q in range(k+1):
                    assert raw_closed(n,p,k,q)==raw_replica(n,p,k,q),(n,k,p,q)
                    replica+=1
                mat=gram_cov(n,p,k)
                assert rank_mod(mat)==(k if 2*k==n else n),(n,k,p,'Haar covariance rank')
                covs+=1
    n,p,k=4,2,2
    C=gram_cov(n,p,k)
    variance=sum(C[0],Fraction(0))/n
    assert abs(float(variance)-0.0030049171371334914)<1e-15
    print(f'VERIFY_OK incidence_cases={ranks} four_replica_cases={replica} covariance_cases={covs}')

if __name__=='__main__':test()
