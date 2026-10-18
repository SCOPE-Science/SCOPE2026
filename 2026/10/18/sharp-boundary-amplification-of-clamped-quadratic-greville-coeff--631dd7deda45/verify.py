"""Exact finite checks for open uniform quadratic Greville coefficient stability.
No nonstandard dependencies. The infinite theorem is proved separately in RESULT.md.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def basis(i, p, x, knots):
    if p == 0:
        return F(int(knots[i] <= x < knots[i+1]))
    a = knots[i+p] - knots[i]
    b = knots[i+p+1] - knots[i+1]
    return ((x-knots[i])*basis(i,p-1,x,knots)/a if a else 0) + ((knots[i+p+1]-x)*basis(i+1,p-1,x,knots)/b if b else 0)


def collocation(n):
    knots = [F(0)]*3 + list(map(F,range(1,n))) + [F(n)]*3
    sites = [(knots[j+1]+knots[j+2])/2 for j in range(n+2)]
    a=[]
    for x in sites:
        a.append([F(int(j==n+1)) if x==n else basis(j,2,x,knots) for j in range(n+2)])
    return a


def tridiagonal_solve(a,b):
    n=len(a)
    d=[a[i][i] for i in range(n)]
    u=[a[i][i+1] for i in range(n-1)]
    l=[a[i+1][i] for i in range(n-1)]
    rhs=b[:]
    for i in range(1,n):
        t=l[i-1]/d[i-1]
        d[i]-=t*u[i-1]
        rhs[i]-=t*rhs[i-1]
    x=[F(0)]*n
    x[-1]=rhs[-1]/d[-1]
    for i in range(n-2,-1,-1):
        x[i]=(rhs[i]-u[i]*x[i+1])/d[i]
    return x


def df(fr): return Decimal(fr.numerator)/Decimal(fr.denominator)


def run():
    count=0
    with localcontext() as c:
        c.prec=90
        sq2=Decimal(2).sqrt()
        q=Decimal(3)-2*sq2
        old=None
        for n in range(2,41):
            a=collocation(n)
            m=n+2
            # Test exact clamped-knot stencil independently of the derived formula.
            for i in range(m):
                for j in range(m):
                    if i==0 or i==m-1:
                        expect=F(int(j==i))
                    elif i==1:
                        expect=F(1,4) if j==0 else F(5,8) if j==1 else F(1,8) if j==2 else F(0)
                    elif i==n:
                        expect=F(1,4) if j==n+1 else F(5,8) if j==n else F(1,8) if j==n-1 else F(0)
                    else:
                        expect=F(3,4) if j==i else F(1,8) if abs(j-i)==1 else F(0)
                    assert a[i][j]==expect,(n,i,j,a[i][j],expect)
                    count+=1
            # Independent exact inverses by rational tridiagonal elimination.
            cols=[tridiagonal_solve(a,[F(int(i==j)) for i in range(m)]) for j in range(m)]
            rn=[]
            for i in range(m):
                rn.append(sum(abs(cols[j][i]) for j in range(m)))
                for j in range(m):
                    assert (-1)**(i+j)*cols[j][i]>=0
                    count+=1
            # Explicit formula for all row sums, not only the global maximum.
            for i in range(m):
                target=Decimal(1) if i in (0,n+1) else Decimal(2)+(sq2-1)*(q**(i-1)+q**(n-i))/(1-q**n)
                assert abs(df(rn[i])-target)<Decimal('1e-72'), (n,i,rn[i],target)
                count+=1
            maxnorm=max(rn)
            maximizing=[i for i,v in enumerate(rn) if v==maxnorm]
            assert maximizing==[1,n],(n,maximizing)
            count+=1
            K=Decimal(2)+(sq2-1)*(1+q**(n-1))/(1-q**n)
            assert abs(df(maxnorm)-K)<Decimal('1e-72')
            count+=1
            assert (old is None or K<old)
            old=K
            count+=1
            # The alternating-data input must attain the sharp norm.
            signs=[F((-1)**i) for i in range(m)]
            cc=tridiagonal_solve(a,signs)
            assert max(map(abs,cc))==maxnorm
            count+=1
            for i in range(m):
                assert (-1)**i*cc[i]==rn[i]
                count+=1
            gap=K-(Decimal(1)+sq2)
            asym=(sq2-1)*(1+q)*q**(n-1)/(1-q**n)
            assert abs(gap-asym)<Decimal('1e-72')
            count+=1
        # Pure cardinal (no clamped boundary): uniform sharp upper bound 2.
        for n in range(2,41):
            t=[[F(3,4) if i==j else F(1,8) if abs(i-j)==1 else F(0) for j in range(n)] for i in range(n)]
            inv=[tridiagonal_solve(t,[F(int(i==j)) for i in range(n)]) for j in range(n)]
            r=[sum(abs(inv[j][i]) for j in range(n)) for i in range(n)]
            assert max(r)<2
            count+=1
        assert q>0 and q<1
        count+=1
    print('PASS',count,'exact/decimal assertions, n=2..40, no external dependencies')

if __name__=='__main__':run()
