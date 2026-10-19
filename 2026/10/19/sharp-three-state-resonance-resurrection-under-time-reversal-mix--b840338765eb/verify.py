"""Exact arithmetic checks for the three-state two-step mixing construction.

Run: python3 verify.py. Uses only the Python standard library.
The universal inequality is established by the analytical argument in RESULT.md,
not by finite enumeration.
"""
from fractions import Fraction as F

count=0
class Q:
    """Exact element a+b*sqrt(3), with rational a,b."""
    def __init__(self,a=0,b=0):
        if isinstance(a,Q): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,y):
        y=Q(y);return Q(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,y):return self+-Q(y)
    def __rsub__(self,y):return Q(y)+-self
    def __mul__(self,y):
        y=Q(y);return Q(self.a*y.a+3*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __truediv__(self,y):
        y=Q(y);den=y.a*y.a-3*y.b*y.b
        assert den!=0
        return Q((self.a*y.a-3*self.b*y.b)/den,(self.b*y.a-self.a*y.b)/den)
    def __pow__(self,n):
        assert n>=0 and isinstance(n,int)
        out=Q(1)
        for _ in range(n): out=out*self
        return out
    def __eq__(self,y):
        y=Q(y);return self.a==y.a and self.b==y.b
    def __repr__(self):return '(%s)+(%s)*sqrt(3)'%(self.a,self.b)
    def sign(self):
        a,b=self.a,self.b
        if not a and not b:return 0
        if a>=0 and b>=0:return 1
        if a<=0 and b<=0:return -1
        diff=a*a-3*b*b
        if a>0: return 1 if diff>0 else -1
        return 1 if diff<0 else -1

def ok(cond,desc=''):
    global count
    assert cond,desc
    count+=1

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))]for i in range(len(A))]
def tr(A):return [[A[j][i] for j in range(len(A))]for i in range(len(A[0]))]
def eye(n):return [[Q(int(i==j)) for j in range(n)]for i in range(n)]
def mix(A,B,p):return [[p*A[i][j]+(Q(1)-p)*B[i][j] for j in range(3)]for i in range(3)]
def pw(A,n):
    out=eye(len(A))
    for _ in range(n):out=mm(out,A)
    return out

def test(A,sig2,name):
    Pi=[[Q(F(1,3)) for _ in range(3)]for _ in range(3)]
    I=eye(3)
    zero=[[Q(0)for _ in range(3)]for _ in range(3)]
    for i in range(3):
        ok(sum(A[i])==Q(1),name+' row-stochastic')
        ok(sum(A[j][i] for j in range(3))==Q(1),name+' column-stochastic')
        for j in range(3): ok(A[i][j].sign()>=0,name+' nonnegative')
    ok(mm(A,A)==Pi,name+' finite-time exact mixing')
    N=[[A[i][j]-Pi[i][j] for j in range(3)]for i in range(3)]
    ok(mm(N,N)==zero,name+' centered nilpotency')
    ok(sum(N[i][j]*N[i][j] for i in range(3) for j in range(3))==sig2,name+' singular value square')
    for p0 in [F(0),F(1,8),F(1,3),F(1,2),F(3,4),F(1)]:
        p=Q(p0);c=sig2*p*(Q(1)-p)
        B=mix(A,tr(A),p)
        for m in range(8):
            even_expected=[[Pi[i][j]+c**m*(I[i][j]-Pi[i][j]) for j in range(3)]for i in range(3)]
            odd_expected=[[Pi[i][j]+c**m*(B[i][j]-Pi[i][j]) for j in range(3)]for i in range(3)]
            ok(pw(B,2*m)==even_expected,name+' even power')
            ok(pw(B,2*m+1)==odd_expected,name+' odd power')
            f=[Q(1),Q(-1),Q(0)]
            cf=sum(f[i]*sum(pw(B,2*m)[i][j]*f[j] for j in range(3)) for i in range(3))/sum(v*v for v in f)
            ok(cf==c**m,name+' centered autocorrelation')
    print(name,'checks passed')

u=[Q(F(1,2),F(1,6)),Q(F(-1,2),F(1,6)),Q(0,F(-1,3))]
v=[u[1],u[0],u[2]]
ok(sum(x*x for x in u)==Q(1),'u unit')
ok(sum(x*x for x in v)==Q(1),'v unit')
ok(sum(u[i]*v[i] for i in range(3))==Q(0),'orthogonality')
sig=Q(-1,1)
Pstar=[[Q(F(1,3))+sig*u[i]*v[j] for j in range(3)]for i in range(3)]
Pref=[[Q(F(x,12)) for x in row]for row in [[5,5,2],[3,3,6],[4,4,4]]]
test(Pstar,sig*sig,'sharp extremal')
test(Pref,Q(F(1,12)),'strictly positive rational example')
for A in [Pstar,Pref]:
    for row in A:
        for x in row:ok((Q(1)-x).sign()>0,'branch expansion')
print('PASS: %d exact assertions; analytical global bound requires the paper proof'%count)
