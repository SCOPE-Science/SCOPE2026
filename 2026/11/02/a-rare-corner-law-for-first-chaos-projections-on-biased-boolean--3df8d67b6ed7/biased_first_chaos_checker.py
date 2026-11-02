"""Exact finite checks of the biased first-chaos L-infinity projection formula.

The analytical proof is required for all dimensions; these tests are diagnostics.
Usage: python biased_first_chaos_checker.py
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def row_norm(x, p):
    n=len(x)
    q=1-p
    ans=F(0)
    for y in product((0,1), repeat=n):
        prob=F(1)
        ker=F(0)
        for xi,yi in zip(x,y):
            prob*=p if yi else q
            ker+=(xi-p)*(yi-p)/(p*q)
        ans+=prob*abs(ker)
    return ans


def closed_norm(n,p):
    q=1-p
    m=(n*p.numerator)//p.denominator
    return 2*n*max(p,q)*comb(n-1,m)*p**m*q**(n-1-m)


def by_two_binomials(n,p,k):
    q=1-p
    val=F(0)
    for a in range(k+1):
        pa=comb(k,a)*p**a*q**(k-a)
        for b in range(n-k+1):
            pb=comb(n-k,b)*p**b*q**(n-k-b)
            ker=F(a-k*p,1)/p-F(b-(n-k)*p,1)/q
            val+=pa*pb*abs(ker)
    return val


def run():
    ps=[F(1,7),F(1,5),F(1,3),F(2,5),F(1,2),F(3,5),F(2,3),F(4,5),F(6,7)]
    rowcount=0
    for n in range(1,8):
        for p in ps:
            rows=[row_norm(x,p) for x in product((0,1),repeat=n)]
            expected=closed_norm(n,p)
            assert max(rows)==expected,(n,p,max(rows),expected)
            assert rows[-1 if p<=F(1,2) else 0]==expected
            rowcount+=len(rows)
    packed=0
    for n in range(1,31):
        for p in ps:
            got=max(by_two_binomials(n,p,k) for k in range(n+1))
            assert got==closed_norm(n,p),(n,p,got,closed_norm(n,p))
            packed+=n+1
    print('PASS',rowcount,'exact full kernel rows and',packed,'exact two-binomial support cases')

if __name__=='__main__':
    run()

# Added heterogeneous-bias checks: the rare-state vertex maximizes every row.
def heterogeneous_row_norm(x, ps):
    n=len(ps)
    ans=F(0)
    for y in product((0,1),repeat=n):
        mass=F(1); kernel=F(0)
        for xi,yi,p in zip(x,y,ps):
            q=1-p
            mass*=p if yi else q
            kernel+=(xi-p)*(yi-p)/(p*q)
        ans+=mass*abs(kernel)
    return ans

def check_heterogeneous():
    grid=[F(1,6),F(1,4),F(2,5),F(1,2),F(3,5),F(3,4),F(5,6)]
    cases=0
    for n in range(1,6):
        for k in range(30):
            ps=tuple(grid[(k+3*j+j*j)%len(grid)] for j in range(n))
            rare=tuple(1 if p<=F(1,2) else 0 for p in ps)
            expected=heterogeneous_row_norm(rare,ps)
            rows=[heterogeneous_row_norm(x,ps) for x in product((0,1),repeat=n)]
            assert max(rows)==expected,(n,ps,rare,expected,max(rows))
            cases+=len(rows)
    print('PASS',cases,'heterogeneous exact kernel rows at 150 bias profiles')

if __name__=='__main__':
    check_heterogeneous()
