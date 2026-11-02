"""Independent finite-field determinant census against the Jacobi-sum formula.
Run: python3 verify.py. Only the Python standard library is required.
"""
import cmath
import itertools
from collections import defaultdict

class Field:
    def __init__(self, q):
        self.q=q
        self.p=3 if q==9 else q
        assert q in (3,5,7,9)
    def add(self,a,b):
        if self.q!=9: return (a+b)%self.q
        return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    def neg(self,a):
        if self.q!=9: return -a%self.q
        return (-a%3)+3*(-(a//3)%3)
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=9:return a*b%self.q
        a0,a1=a%3,a//3;b0,b1=b%3,b//3
        return (a0*b0+2*a1*b1)%3+3*((a0*b1+a1*b0)%3)
    def pow(self,a,n):
        ans=1
        while n:
            if n&1:ans=self.mul(ans,a)
            a=self.mul(a,a);n>>=1
        return ans
    def inv(self,a):
        assert a!=0
        return self.pow(a,self.q-2)
    def scalar(self,a,k):
        v=0
        for _ in range(k%self.p):v=self.add(v,a)
        return v
    def generator(self):
        for g in range(2,self.q):
            if len({self.pow(g,i) for i in range(self.q-1)})==self.q-1:return g
        raise AssertionError('No generator')

def det(M,F):
    n=len(M); A=[r[:] for r in M]; out=1
    for i in range(n):
        piv=next((k for k in range(i,n) if A[k][i]!=0),None)
        if piv is None:return 0
        if piv!=i:
            A[i],A[piv]=A[piv],A[i]
            out=F.neg(out)
        x=A[i][i];out=F.mul(out,x);xin=F.inv(x)
        for j in range(i+1,n):
            mul=F.mul(A[j][i],xin)
            if mul:
                for k in range(i,n):A[j][k]=F.sub(A[j][k],F.mul(mul,A[i][k]))
    return out

def resultant(f,g,F):
    while len(g)>1 and g[-1]==0:g.pop()
    n=len(f)-1;m=len(g)-1
    if m==0:return F.pow(g[0],n)
    assert g[-1]
    A=[]
    for s in range(m):A.append([0]*s+list(reversed(f))+[0]*(m-s-1))
    for s in range(n):A.append([0]*s+list(reversed(g))+[0]*(n-s-1))
    return det(A,F)

def discriminant(f,F):
    n=len(f)-1
    deriv=[F.scalar(f[i],i) for i in range(1,n+1)]
    r=resultant(f,deriv,F)
    if (n*(n-1)//2)%2:r=F.neg(r)
    return r

def sqsign(x,F):
    if x==0:return 0
    return 1 if F.pow(x,(F.q-1)//2)==1 else -1

def chars_and_L(F,max_n):
    q=F.q; h=q-1; g=F.generator(); logs={F.pow(g,i):i for i in range(h)}
    char=lambda j,x: 0j if x==0 else cmath.exp(2j*cmath.pi*j*logs[x]/h)
    L={}
    for i in range(h):
        for j in range(h):
            if (i,j)==(0,0):
                L[(i,j)]=[1,q-2]+[(q-1)**2*q**(d-2) for d in range(2,max_n+1)]
            else:
                J=sum(char(i,c)*char(j,F.add(c,1)) for c in range(1,q) if F.add(c,1)!=0)
                L[(i,j)]=[1,J]+[0]*(max_n-1)
    return char,L

def reciprocal(a,N):
    out=[1]+[0]*N
    for n in range(1,N+1):out[n]=-sum(a[k]*out[n-k] for k in range(1,n+1))
    return out

def predicted(F,N):
    q=F.q; h=q-1; char,L=chars_and_L(F,N)
    K={};U={}
    for i in range(h):
        for j in range(h):
            a=L[(i,j)];asq=L[(2*i%h,2*j%h)]
            den=[asq[k//2] if k%2==0 else 0 for k in range(N+1)]
            rec=reciprocal(den,N)
            K[(i,j)]=[sum(a[k]*rec[n-k] for k in range(n+1)) for n in range(N+1)]
            U[(i,j)]=reciprocal(a,N)
    out={}
    for n in range(2,N+1):
        for a in range(1,q):
            for b in range(1,q):
                S=sum(char((-i)%h,a)*char((-j)%h,b)*K[(i,j)][n] for i in range(h) for j in range(h))/(h*h)
                D=sum(char((-i)%h,a)*char((-j)%h,b)*U[(i,j)][n] for i in range(h) for j in range(h))/(h*h)*(-1)**n
                assert abs(S.imag)<1e-5 and abs(D.imag)<1e-5
                ss=round(S.real);dd=round(D.real)
                assert abs(S.real-ss)<1e-5 and abs(D.real-dd)<1e-5
                assert (ss+dd)%2==0 and ss>=abs(dd)
                out[(n,a,b)]=(ss,dd,(ss+dd)//2,(ss-dd)//2)
    return out

def verify(q,N):
    F=Field(q); pred=predicted(F,N)
    obs=defaultdict(lambda:[0,0,0,0]); total=0
    for n in range(2,N+1):
        for low in itertools.product(range(q), repeat=n):
            a=low[0];b=1
            for x in low:b=F.add(b,x)
            if a==0 or b==0:continue
            f=list(low)+[1]
            sign=sqsign(discriminant(f,F),F)
            x=obs[(n,a,b)]
            if sign:x[0]+=1;x[1]+=sign;x[2 if sign==1 else 3]+=1
            total+=1
    for k,p in pred.items():
        actual=tuple(obs[k])
        assert actual==p,(q,k,p,actual)
    return len(pred),total

if __name__=='__main__':
    rows=fields=total=0
    for q,N in ((3,7),(5,5),(7,4),(9,4)):
        n,m=verify(q,N)
        print('OK',q,'degree<=',N,'fibres',n,'polynomials',m)
        rows+=n;total+=m;fields+=1
    # Check the exceptional q=3 formula and sharp maximum at every tested degree.
    Q=predicted(Field(3),7)
    for n in range(2,8):
        vals=[]
        for a in (1,2):
            for b in (1,2):
                u=1 if a==1 else -1
                v=1 if b==1 else -1
                expected=(-1)**n*(1-2*n+(-1)**n*u+v+u*v)//4
                assert Q[(n,a,b)][1]==expected
                vals.append(abs(expected))
        assert max(vals)==(n+1)//2
    # The explicit Jacobi-magnitude bounds for q >=5.
    for q,N in ((5,5),(7,4),(9,4)):
        Q=predicted(Field(q),N)
        for n in range(2,N+1):
            m=max(abs(Q[(n,a,b)][1]) for a in range(1,q) for b in range(1,q))
            assert m+1e-8>=q**(n/2)/(q-1)**2
            assert m<=q**(n/2)+n/(q-1)+1e-8
    print('VERIFY_OK fields=%d degree_value_fibres=%d direct_polynomials=%d exceptional_q3_and_bounds=PASS'%(fields,rows,total))
