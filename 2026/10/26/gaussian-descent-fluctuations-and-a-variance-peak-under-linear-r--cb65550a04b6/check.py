"""Exact finite-sample verification of descent statistics for record-weighted permutations.
Run with: python3 check.py
No third-party dependencies.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

assertions=0

def check(a,b):
    global assertions
    assert a==b,(a,b)
    assertions+=1

def formulas(n,theta):
    theta=F(theta)
    p={j:F(j)*(2*theta+j-1)/(2*(theta+j-1)*(theta+j)) for j in range(1,n)}
    cov={j:-F(j*(j+1))*(6*theta**2+4*theta*j-4*theta+j*j-j)/(12*(theta+j)**2*(theta+j-1)*(theta+j+1)) for j in range(1,n-1)}
    mean=F(n*(n-1))/(2*(theta+n-1))
    var=sum((z*(1-z) for z in p.values()),F(0))+2*sum(cov.values(),F(0))
    return p,cov,mean,var

def census(n,theta):
    # independent full-word enumeration, not insertion-rank enumeration
    theta=F(theta)
    W=F(0)
    first=[F(0)]*(n-1)
    pairs={(i,j):F(0) for i in range(n-1) for j in range(i+1,n-1)}
    me=F(0); mom2=F(0)
    for seq in permutations(range(1,n+1)):
        best=0; records=0
        for v in seq:
            if v>best:
                records+=1; best=v
        weight=theta**records
        d=[int(seq[j]>seq[j+1]) for j in range(n-1)]
        number=sum(d)
        W+=weight
        me+=weight*number; mom2+=weight*number*number
        for i in range(n-1):
            first[i]+=weight*d[i]
            for j in range(i+1,n-1):
                pairs[i,j]+=weight*d[i]*d[j]
    return W,[x/W for x in first],{key:value/W for key,value in pairs.items()},me/W,mom2/W-(me/W)**2

for n in range(2,8):
    for theta in (F(1,2),F(1),F(2),F(5,3)):
        p,c,mu,var=formulas(n,theta)
        W,one,pairs,mu2,var2=census(n,theta)
        expected_w=F(1)
        for j in range(n): expected_w*=theta+j
        check(W,expected_w)
        check(mu,mu2)
        check(var,var2)
        for i in range(n-1):check(p[i+1],one[i])
        for (i,j),pair in pairs.items():
            if j==i+1:check(pair-p[i+1]*p[j+1],c[i+1]);check(c[i+1]<0, True)
            else:check(pair,p[i+1]*p[j+1])

# Independent exact computation of the limiting variance via a polynomial antiderivative
# Rational lambdas: integral x(12lambda^3+6lambda^2*x+4lambda*x^2+x^3)/(12(lambda+x)^4)
# equals (6lambda^2+4lambda+1)/(12(lambda+1)^3).
for l in (F(1,5),F(1,2),F(1),F(3,2),F(3)):
    v=(6*l*l+4*l+1)/(12*(l+1)**3)
    assert v>0
    assertions+=1
    # Exact finite variance approaches n times v.
    for n in (100,500,2000):
        var=formulas(n,l*n)[-1]
        check(abs(var/F(n)-v)<F(2,n),True)

print('PASS',assertions,'exact assertions')
