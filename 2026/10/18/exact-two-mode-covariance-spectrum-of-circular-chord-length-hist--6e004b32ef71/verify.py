"""Exact covariance checks for uniform circular chord-length histograms."""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations


def matchings(vertices):
    if not vertices:
        yield ()
        return
    x=vertices[0]
    for k in range(1,len(vertices)):
        y=vertices[k]
        rest=vertices[1:k]+vertices[k+1:]
        for tail in matchings(rest):
            yield ((x,y),)+tail

def theoretical(n):
    den=(2*n-3)*(2*n-1)**2
    a=F(4*n*(n-1),(2*n-1)**2)
    b=F(-8*n*(n-1),den)
    c=F(-4*n*(n-1),den)
    d=F(4*n*(n-1)**2,den)
    return [[a if i==j<n-1 else b if i<n-1 and j<n-1 else c if i!=j else d for j in range(n)] for i in range(n)]

def check(n):
    total=0; first=[0]*n; second=[[0]*n for _ in range(n)]
    for m in matchings(tuple(range(2*n))):
        counts=[0]*n
        for x,y in m:
            j=min(y-x-1,2*n-(y-x)-1)
            counts[j]+=1
        total+=1
        for i in range(n):
            first[i]+=counts[i]
            for j in range(n):
                second[i][j]+=counts[i]*counts[j]
    m=[F(x,total) for x in first]
    assert m == [F(2*n,2*n-1)]*(n-1)+[F(n,2*n-1)]
    exp=theoretical(n)
    for i in range(n):
        assert sum(exp[i]) == 0
        for j in range(n):
            got=F(second[i][j],total)-m[i]*m[j]
            assert got==exp[i][j], (n,i,j,got,exp[i][j])
    print('n=',n,'matchings=',total,'exact covariance entries=',n*n)

if __name__=='__main__':
    for n in range(2,8):
        check(n)
    print('VERIFY_OK')
