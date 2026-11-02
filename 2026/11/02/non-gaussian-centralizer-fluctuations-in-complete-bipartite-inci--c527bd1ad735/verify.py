"""Independent finite-field verification for centralizer dimensions in a height-two incidence algebra.

This code implements multiplication and commutator matrices directly, independently of
counting components. It also checks exact finite occupancy moments.
"""
from itertools import product
from collections import Counter
from fractions import Fraction
import random


def multiply(a,b,q,n):
    # a=(left diag n, right diag n, radical n*n) in row-major order.
    out=[a[i]*b[i]%q for i in range(2*n)]
    for i in range(n):
        for j in range(n):
            k=2*n+i*n+j
            out.append((a[i]*b[k]+a[k]*b[n+j])%q)
    return tuple(out)


def centralizer_dimension_by_linear_algebra(a,q,n):
    d=2*n+n*n
    columns=[]
    for i in range(d):
        u=[0]*d;u[i]=1;u=tuple(u)
        x=multiply(a,u,q,n);y=multiply(u,a,q,n)
        columns.append(tuple((v-w)%q for v,w in zip(x,y)))
    rows=[[columns[j][i] for j in range(d)] for i in range(d)]
    pivot=0
    for j in range(d):
        k=next((k for k in range(pivot,d) if rows[k][j]),None)
        if k is None:continue
        rows[pivot],rows[k]=rows[k],rows[pivot]
        inv=pow(rows[pivot][j],-1,q)
        rows[pivot]=[(x*inv)%q for x in rows[pivot]]
        for l in range(pivot+1,d):
            t=rows[l][j]
            if t:rows[l]=[(u-t*v)%q for u,v in zip(rows[l],rows[pivot])]
        pivot+=1
    return d-pivot


def centralizer_by_components(a,q,n):
    diag=a[:2*n]
    parent=list(range(2*n))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    matches=0
    for i in range(n):
        for j in range(n):
            if diag[i]==diag[n+j]:
                matches+=1
                if a[2*n+i*n+j]!=0:
                    x,y=root(i),root(n+j)
                    parent[x]=y
    components=len({root(i) for i in range(2*n)})
    return matches+components,matches,components


def run():
    total=0
    for q,n in [(2,1),(2,2),(3,1)]:
        dimension=2*n+n*n
        counts=Counter()
        for a in product(range(q),repeat=dimension):
            d1=centralizer_dimension_by_linear_algebra(a,q,n)
            d2,S,C=centralizer_by_components(a,q,n)
            assert d1==d2,(q,n,a,d1,d2,S,C)
            if n==1 or q==2:
                # Direct counting by multiplying every other element, not by rank.
                c=sum(multiply(a,b,q,n)==multiply(b,a,q,n)
                      for b in product(range(q),repeat=dimension))
                assert c==q**d1,(q,n,a,c,d1)
            counts[d1]+=1
            total+=1
        print('EXHAUSTIVE',q,n,'elements',q**dimension,'dimensions',sorted(counts.items()))
    random.seed(9273)
    for q,n,steps in [(2,3,150),(3,2,150),(5,2,150)]:
        d=2*n+n*n
        for i in range(steps):
            a=tuple(random.randrange(q) for _ in range(d))
            assert centralizer_dimension_by_linear_algebra(a,q,n)==centralizer_by_components(a,q,n)[0]
        print('SAMPLED',q,n,steps)
    for q in [2,3,5]:
        for n in [1,2,3,4]:
            # Exact multinomial summation independent of the matrix-space formula.
            ss=Fraction(0); ss2=Fraction(0)
            configs=0
            for ll in product(range(q),repeat=n):
                for rr in product(range(q),repeat=n):
                    S=sum(x==y for x in ll for y in rr)
                    ss+=S;ss2+=S*S;configs+=1
            ex=ss/configs;var=ss2/configs-ex**2
            assert ex==Fraction(n*n,q)
            assert var==Fraction(n*n*(q-1),q*q)
        print('MOMENTS',q,'n=1..4')
    print('VERIFY_OK',total,'exhaustive elements')

if __name__=='__main__':run()
