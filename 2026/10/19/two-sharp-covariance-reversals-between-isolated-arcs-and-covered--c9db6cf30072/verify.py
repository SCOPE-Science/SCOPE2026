"""Finite numerical and exact checks of the stated random-arc covariance theorem."""
from fractions import Fraction
from itertools import combinations
from decimal import Decimal, getcontext
getcontext().prec=75

def cov_exact(n,a):
    a=Fraction(a)
    b=max(Fraction(0),1-2*a);c=max(Fraction(0),1-3*a)
    return n*b**(n-1)*(1-a)**n-2*b**n-(n-2)*c**n

def mean_J(n,a):
    return n*max(Fraction(0),1-2*a)**(n-1)

def mean_U(n,a):
    return (1-a)**n

def mixed_JU(n,a):
    return 2*max(Fraction(0),1-2*a)**n + (n-2)*max(Fraction(0),1-3*a)**n

checks=0
for n in range(5,51):
    for aa in (Fraction(1,10),Fraction(1,5),Fraction(3,10),Fraction(1,3),Fraction(2,5),Fraction(9,20),Fraction(49,100)):
        assert mixed_JU(n,aa)-mean_J(n,aa)*mean_U(n,aa)==-cov_exact(n,aa)
        checks+=1

# Independent finite simplex-lattice quadrature: increasingly fine uniform compositions
# have asymptotically uniform empirical distribution on the Dirichlet simplex.
def compositions(M,n):
    for cuts in combinations(range(M+n-1),n-1):
        p=(-1,)+cuts+(M+n-1,)
        yield tuple(p[i+1]-p[i]-1 for i in range(n))

def grid_mixed(n,a,M):
    EJ=EU=EJU=0; ct=0
    for s in compositions(M,n):
        gaps=[v/M for v in s]
        J=sum(gaps[i]>a and gaps[i-1]>a for i in range(n))
        U=sum(max(v-a,0) for v in gaps)
        EJ+=J; EU+=U; EJU+=J*U; ct+=1
    return EJU/ct-(EJ/ct)*(EU/ct)

for n,a in [(3,.2),(4,.2),(5,.2),(5,.4),(6,.15)]:
    vals=[grid_mixed(n,a,M) for M in (25,40)]
    exact=-float(cov_exact(n,Fraction(str(a))))
    assert abs(vals[-1]-exact)<.025,(n,a,vals,exact)
    checks+=1

# Numerically bracket every theoretically unique interior root in both subintervals.
root_rows=[]
for n in (5,6,7,8,10,15,20,40):
    N=Decimal(n)
    def F(a):
        b=1-2*a; c=max(Decimal(0),1-3*a)
        return N*b**(n-1)*(1-a)**n-2*b**n-(n-2)*c**n
    def bisect(l,r):
        fl=F(l)
        for i in range(210):
            m=(l+r)/2
            if (F(m)>0)==(fl>0):l=m;fl=F(l)
            else:r=m
        return (l+r)/2
    l=bisect(Decimal('1e-12'),Decimal(1)/3)
    u=bisect(Decimal(1)/3,Decimal('0.499999999999999999'))
    assert F(l)!=0 or abs(F(l))<Decimal('1e-40')
    assert l<Decimal(1)/3<u<Decimal('.5')
    assert F((l+u)/2)<0
    assert F(l/2)>0
    assert F((u+Decimal('.5'))/2)>0
    root_rows.append((n,str(l)[:20],str(u)[:20]))
    checks+=5

print('CHECKS',checks)
print('ROOTS',root_rows)
