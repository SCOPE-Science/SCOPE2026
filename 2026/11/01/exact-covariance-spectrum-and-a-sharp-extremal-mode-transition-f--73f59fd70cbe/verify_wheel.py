"""Independent finite checks and rational-interval certificates for the wheel UST covariance theorem.
Run: python3 verify_wheel.py (Python standard library only)."""
import cmath, itertools, math
from fractions import Fraction as Q

class I:
    def __init__(self,a,b=None):
        self.a=Q(a); self.b=Q(a if b is None else b)
        assert self.a<=self.b
    def __add__(self,o):
        o=iv(o);return I(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,o):return self+-iv(o)
    def __rsub__(self,o):return iv(o)+-self
    def __mul__(self,o):
        o=iv(o);v=[a*b for a in (self.a,self.b) for b in (o.a,o.b)];return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=iv(o);assert o.a*o.b>0
        return self*I(1/o.b,1/o.a)
    def __rtruediv__(self,o):return iv(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n%2==0 and self.a<0<self.b:return I(0,max(abs(self.a),abs(self.b))**n)
        if n%2==0 and self.b<=0:return I(self.b**n,self.a**n)
        return I(self.a**n,self.b**n)

def iv(x):return x if isinstance(x,I) else I(x)

def pi_interval():
    def atan_inv(v):
        n=20
        t=sum(((-1)**k)*Q(1,v**(2*k+1)*(2*k+1)) for k in range(n))
        e=Q(1,v**(2*n+1)*(2*n+1))
        return I(t,t+e) # N even: alternating next term positive
    return 16*atan_inv(5)-4*atan_inv(239)

def cos_pi_over(n):
    p=pi_interval();x=p/n
    def series(z):
        N=13 # next term negative, so [S_N-next, S_N]
        val=sum(((-1)**k)*z**(2*k)/math.factorial(2*k) for k in range(N))
        err=z**(2*N)/math.factorial(2*N)
        return I(val-err,val)
    # cos is decreasing on [0,pi/3]
    lo=series(x.b).a;hi=series(x.a).b
    return I(lo,hi)

def signed_interval(n):
    root=math.isqrt(5*10**(2*24))
    sq=I(Q(root,10**24),Q(root+1,10**24))
    rho=(3-sq)/2;r=rho**2;t=rho**n
    g=(1+t)/(sq*(1-t));C=((1+t)/(1-t))*(1-r**2)/5
    y=cos_pi_over(n)
    D=(1+r)**2-4*r*y**2
    LamPlus=g-C*(1-2*y/3)/D
    LamMinus=g-C*(1+2*y/3)/D
    A0=g-C/(1-r)**2-2*n*t/(5*(1-t)**2)
    return 2*A0-LamPlus,2*A0-LamMinus,LamMinus

def certify():
    for n in range(3,11):
        d,small,pos=signed_interval(n)
        assert (d.b<0 if n<=8 else d.a>0),(n,float(d.a),float(d.b))
        assert (small.a>0 if n>=4 else small.a<0<small.b),(n,'smallest comparison',float(small.a))
        assert pos.a>0,(n,'positive',float(pos.a))
    # For n >= 11, use 1-cos(pi/n)>=2/n^2, 1-4r+r^2-2ry >= r,
    # D(y)<=(1+r)^2, and n^3*rho^n strictly decreasing for n>=4.
    root=math.isqrt(5*10**(2*24));sq=I(Q(root,10**24),Q(root+1,10**24))
    rho=(3-sq)/2;r=rho**2
    C0=(1-r**2)/5
    lower=C0*4*r/(3*(1+r)**2*(1-r)**2*11**2)
    upper=4*11*rho**11/(5*(1-rho**22))
    assert lower.a>upper.b, ('large-n dominance',float(lower.a),float(upper.b))
    assert rho.b*(Q(5,4))**3<1
    # For n>=11: 2A0 >= L-infinity - 4n*rho^n/(5(1-rho^n)^2)
    # and lambda_minus(k=1) <= H_n*lambda_minus(y=9/10).
    assert cos_pi_over(11).a>Q(9,10)
    Linf=4/(5*sq)
    smallerr=4*11*rho**11/(5*(1-rho**11)**2)
    H=(1+rho**11)/(1-rho**11)
    y=I(Q(9,10));D=(1+r)**2-4*r*y**2
    fminus=1/sq-C0*(1+2*y/3)/D
    assert (Linf-smallerr).a>(H*fminus).b
    return 'RATIONAL_INTERVAL_CERTIFICATES_OK'

def inverse(A):
    n=len(A);M=[[Q(a) for a in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        pivot=next(k for k in range(i,n) if M[k][i]);M[i],M[pivot]=M[pivot],M[i]
        v=M[i][i];M[i]=[z/v for z in M[i]]
        for k in range(n):
            if k!=i:
                v=M[k][i];M[k]=[a-v*b for a,b in zip(M[k],M[i])]
    return [row[n:] for row in M]

def brute_cov(n):
    edges=[(n,i) for i in range(n)]+[(i,(i+1)%n) for i in range(n)]
    N=2*n;counts=[0]*N;both=[[0]*N for _ in range(N)];trees=0
    for choice in itertools.combinations(range(N),n):
        parent=list(range(n+1))
        def find(x):
            while parent[x]!=x:x=parent[x]
            return x
        ok=True
        for e in choice:
            u,v=edges[e];a,b=find(u),find(v)
            if a==b:ok=False;break
            parent[a]=b
        if not ok:continue
        trees+=1
        for i in choice:
            counts[i]+=1
            for j in choice:both[i][j]+=1
    C=[[Q(both[i][j],trees)-Q(counts[i]*counts[j],trees*trees) for j in range(N)] for i in range(N)]
    return C,trees

def green_cov(n):
    L=[[Q(0) for _ in range(n)] for __ in range(n)]
    for i in range(n):
        L[i][i]=3;L[i][(i-1)%n]=-1;L[i][(i+1)%n]=-1
    H=inverse(L)
    cols=[]
    for i in range(n):cols.append([Q(j==i) for j in range(n)])
    for i in range(n):cols.append([Q(j==i)-Q(j==(i+1)%n) for j in range(n)])
    K=[[sum(cols[i][a]*H[a][b]*cols[j][b] for a in range(n) for b in range(n)) for j in range(2*n)] for i in range(2*n)]
    C=[[Q(i==j)*K[i][i]-K[i][j]**2 for j in range(2*n)] for i in range(2*n)]
    for m in range(n):assert C[m][0]==C[n+m][n]
    return C

def analytic_spectrum(n):
    rho=(3-math.sqrt(5))/2;r=rho*rho;t=rho**n
    g=(1+t)/(math.sqrt(5)*(1-t))
    C=(1+t)*(1-r*r)/(5*(1-t))
    A0=g-C/(1-r)**2-2*n*t/(5*(1-t)**2)
    out=[0.,2*A0]
    for k in range(1,n):
        y=abs(math.cos(math.pi*k/n));D=(1+r)**2-4*r*y*y
        out.extend([g-C*(1+2*y/3)/D,g-C*(1-2*y/3)/D])
    return sorted(out)

def numeric_dft_spectrum(C,n):
    allvalues=[]
    for k in range(n):
        zz=[cmath.exp(-2j*math.pi*k*m/n) for m in range(n)]
        a=sum(float(C[0][m])*zz[m] for m in range(n)).real
        b=sum(float(C[0][n+m])*zz[m] for m in range(n))
        allvalues.extend([a-abs(b),a+abs(b)])
    return sorted(allvalues)

def check():
    count=0
    for n in range(3,9):
        A,ntrees=brute_cov(n)
        B=green_cov(n)
        assert A==B,(n,'exact covariance mismatch')
        eig=numeric_dft_spectrum(B,n);target=analytic_spectrum(n)
        assert max(abs(a-b) for a,b in zip(eig,target))<2e-12
        assert ntrees>0
        count+=1
    for n in range(9,61):
        B=green_cov(n) if n<=14 else None
        if B:
            eig=numeric_dft_spectrum(B,n);target=analytic_spectrum(n)
            assert max(abs(a-b) for a,b in zip(eig,target))<2e-12
        lam=analytic_spectrum(n)
        assert lam[1]>0 and abs(lam[0])<1e-9
        count+=1
    print(certify());print('CHECK_OK: six exact full UST covariance enumerations (n=3..8); finite block spectrum checks; monotonicity/crossover rational certificates; n=3..60 positivity; 58 dimensions')

if __name__=='__main__':check()
