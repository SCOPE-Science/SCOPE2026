"""Independent finite checks for leaf/odd-degree dependence in uniform labeled trees."""
from fractions import Fraction as F
from itertools import product
from math import exp,sqrt

def formulas(n):
    N=n-2
    u=F(n-1,n)**N
    v=F(n-2,n)**N
    w=F(n-3,n)**N
    z=F(n-4,n)**N
    meanL=n*u
    meanO=F(n,2)*(1+v)
    cov=F(n,2)*(u+(n-1)*w-n*u*v)
    varL=n*u+n*(n-1)*v-n*n*u*u
    varO=F(n,4)*(1+(n-1)*z-n*v*v)
    return meanL,meanO,cov,varL,varO

def enumerate_n(n):
    length=n-2
    total=n**length
    a=b=c=d=e=0
    for word in product(range(n),repeat=length):
        cnt=[0]*n
        for k in word: cnt[k]+=1
        x=sum(t==0 for t in cnt)
        y=sum(t%2==0 for t in cnt)
        a+=x;b+=y;c+=x*y;d+=x*x;e+=y*y
    ex=F(a,total);ey=F(b,total)
    return ex,ey,F(c,total)-ex*ey,F(d,total)-ex*ex,F(e,total)-ey*ey

checks=0
for n in range(2,9):
    observed=enumerate_n(n); expected=formulas(n)
    assert observed==expected, (n,observed,expected)
    checks+=5
    if n>=4:assert expected[2]>0
    else:assert expected[2]==0
    checks+=1
for n in range(4,120):
    u,v,c,l,o=formulas(n)
    assert c>0 and l>0 and o>0
    checks+=3
for n in range(4,100):
    # off-diagonal covariance negative for each pair of distinct labels
    N=n-2
    u=F(n-1,n)**N;v=F(n-2,n)**N;w=F(n-3,n)**N
    assert (w-u*v)/2<0
    checks+=1
c_limit=(exp(-1)-3*exp(-3))/2
l_limit=exp(-1)-2*exp(-2)
o_limit=(1-5*exp(-4))/4
for n in (1000,10000):
    # evaluate with ordinary floats at large size avoiding Fraction blowup
    a=(1-1/n)**(n-2);b=(1-2/n)**(n-2);d=(1-3/n)**(n-2);f=(1-4/n)**(n-2)
    calc=n/2*(a+(n-1)*d-n*a*b)/n
    vl=(n*a+n*(n-1)*b-n*n*a*a)/n
    vo=(n/4*(1+(n-1)*f-n*b*b))/n
    if n==1000:
        assert abs(calc-c_limit)<.001 and abs(vl-l_limit)<.001 and abs(vo-o_limit)<.001
        checks+=3
print('PASS',checks,'exact/limit checks; asymptotic correlation=',c_limit/sqrt(l_limit*o_limit))
