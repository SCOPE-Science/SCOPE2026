"""Exact-rational verification for a TR-BDF2 graph heat positivity theorem.
Run with: python3 VERIFY.py. Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations

class Q:
    """Exact element x+y*sqrt(2) of Q(sqrt(2))."""
    __slots__=('x','y')
    def __init__(self,x=0,y=0):
        if isinstance(x,Q): self.x,self.y=x.x,x.y;return
        self.x,self.y=F(x),F(y)
    @staticmethod
    def cast(z):return z if isinstance(z,Q) else Q(z)
    def __add__(self,o):
        o=Q.cast(o);return Q(self.x+o.x,self.y+o.y)
    __radd__=__add__
    def __neg__(self):return Q(-self.x,-self.y)
    def __sub__(self,o):return self+-Q.cast(o)
    def __rsub__(self,o):return Q.cast(o)+-self
    def __mul__(self,o):
        o=Q.cast(o);return Q(self.x*o.x+2*self.y*o.y,self.x*o.y+self.y*o.x)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Q.cast(o);den=o.x*o.x-2*o.y*o.y
        if den==0:raise ZeroDivisionError
        return Q((self.x*o.x-2*self.y*o.y)/den,(self.y*o.x-self.x*o.y)/den)
    def __rtruediv__(self,o):return Q.cast(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        y=Q(1)
        while n:
            if n&1:y=y*self
            self=self*self;n//=2
        return y
    def __eq__(self,o):
        o=Q.cast(o);return self.x==o.x and self.y==o.y
    def sign(self):
        x,y=self.x,self.y
        if y==0:return (x>0)-(x<0)
        if x==0:return (y>0)-(y<0)
        if (x>0)==(y>0):return (x>0)-(x<0)
        t=x*x-2*y*y
        assert t!=0
        return (1 if t>0 else -1)*(1 if x>0 else -1)
    def __repr__(self):return f'({self.x}+{self.y}sqrt2)'

rt=Q(0,1); a=1-rt/2;b=rt-1; zmin=4+3*rt; rmin=(1-rt)/2
R=lambda z:(1-b*z)/(1+a*z)**2

def inv(A):
    n=len(A);B=[[Q.cast(A[i][j]) for j in range(n)]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        k=next((k for k in range(i,n) if B[k][i]!=0),None)
        assert k is not None
        B[i],B[k]=B[k],B[i]
        p=B[i][i];B[i]=[x/p for x in B[i]]
        for k in range(n):
            if k==i:continue
            t=B[k][i]
            if t!=0:B[k]=[u-t*v for u,v in zip(B[k],B[i])]
    return [row[n:] for row in B]

def matrix_test(parts,h):
    n=sum(parts); ids=[]
    for k,p in enumerate(parts):ids += [k]*p
    L=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if ids[i]!=ids[j]:L[i][j]=Q(-1);L[i][i]=L[i][i]+1
    B=inv([[Q(int(i==j))+a*h*L[i][j] for j in range(n)] for i in range(n)])
    B2=[[sum((B[i][k]*B[k][j] for k in range(n)),Q()) for j in range(n)] for i in range(n)]
    T=[[(1+rt)*B2[i][j]-rt*B[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        p=parts[ids[i]];q=n-p
        for j in range(n):
            if i==j:
                want=Q(1)/n + (Q(1)/p-Q(1)/n)*R(n*h)+(Q(1)-Q(1)/p)*R(q*h)
            elif ids[i]!=ids[j]:want=(1-R(n*h))/n
            else:want=(1-R(n*h))/n + (R(n*h)-R(q*h))/p
            assert T[i][j]==want,(parts,h,i,j,T[i][j],want)
            if i!=j:assert T[i][j].sign()>0
        assert sum(T[i],Q())==Q(1)
    return 1

def Pcoeff(n,p):
    q=n-p
    def mul(A,B):
        C=[Q() for _ in range(len(A)+len(B)-1)]
        for i,x in enumerate(A):
            for j,y in enumerate(B):C[i+j]=C[i+j]+x*y
        return C
    def pow2(k):return mul([Q(1),a*k],[Q(1),a*k])
    def add(*polys):
        v=[Q() for _ in range(max(map(len,polys)))]
        for poly in polys:
            for i,c in enumerate(poly):v[i]=v[i]+c
        return v
    return add([p*x for x in mul(pow2(n),pow2(q))], [q*x for x in mul([Q(1),-b*n],pow2(q))], [n*(p-1)*x for x in mul([Q(1),-b*q],pow2(n))])

def run():
    checks=0
    assert 2*a+b==1
    assert b/a==rt
    assert R(zmin)==rmin
    assert (a*b)*zmin==1
    assert ((1+rt)*Q(1)-rt*Q(1))==1
    checks+=5
    for n in range(2,36):
        for p in range(1,n):
            q=n-p
            coeff=Pcoeff(n,p)
            assert coeff[0]==p*n
            assert coeff[1]==p*n*(2*a*(n+q)-q)
            assert coeff[3]==a*a*n*q*(2*p*a*(n+q)-b*(q*q+n*n*(p-1)))
            assert coeff[4]==p*a**4*n*n*q*q
            h0=zmin/q
            d=Q(1)/n+(Q(1)/p-Q(1)/n)*R(n*h0)+(Q(1)-Q(1)/p)*R(q*h0)
            H=(p+rt*q)**2-(3+2*rt)*(p+2*q)
            assert d==-H/(2*(1+rt)*(p+rt*q)**2)
            if n>=7:assert H.sign()>0 and d.sign()<0
            if n==6:
                assert H == (3-2*rt)*(p-3)*(p-4)
                if p in (3,4):assert d==0
                else:assert d.sign()<0
            if n<=5:assert (1+(n-1)*rmin).sign()>0
            if n>=6:
                assert coeff[0].sign()>0 and coeff[1].sign()>0
                assert coeff[3].sign()<0 and coeff[4].sign()>0
            checks+=8
    cases=[(1,1),(1,2),(2,2),(2,3),(3,3),(1,5),(2,4),(3,4),(2,2,2),(1,2,3),(1,1,1,3),(1,1,1,1,2)]
    matrices=0
    for comp in cases:
        for h in (F(1,5),F(1),F(5)):
            matrices+=matrix_test(comp,Q(h))
    print(f'VERIFY_OK: {checks} exact algebraic checks and {matrices} full-matrix cases; all offdiagonals strictly positive in checked cases')

if __name__=='__main__':run()
