"""Direct matrix checks for square-zero / cube-zero mutually annihilating pairs.

Recomputes all matrices in the ambient space for small sizes, and compares an
independent Jordan-type expression. No external data or dependencies.
"""
from itertools import product
from math import prod
from fractions import Fraction


def mul(A,B,q):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n))%q for j in range(n)) for i in range(n))


def matrix(rank,n,q):
    A=[[0]*n for _ in range(n)]
    for i in range(rank): A[i][n-rank+i]=1
    return tuple(tuple(row) for row in A)


def genmat(n,q):
    for a in product(range(q),repeat=n*n):
        yield tuple(tuple(a[n*i:n*(i+1)]) for i in range(n))


def gauss(n,k,q):
    if not 0<=k<=n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))


def gl(n,q): return prod(q**n-q**i for i in range(n))


def nilpotent_type_count(t1,t2,t3,q):
    n=t1+2*t2+3*t3
    col=(t1+t2+t3,t2+t3,t3)
    aut=Fraction(q**sum(x*x for x in col))
    for multiplicity in (t1,t2,t3):
        for j in range(1,multiplicity+1):
            aut*=Fraction(q**j-1,q**j)
    num=Fraction(gl(n,q),1)/aut
    assert num.denominator==1
    return int(num)


def zero_pairs(r,t,q):
    return sum(gauss(t,h,q)*prod(q**r-q**i for i in range(h))*q**(r*(t-h)) for h in range(min(r,t)+1))


def jordan_count(n,q):
    total=0
    per_rank=[]
    for r in range(n//2+1):
        s=n-2*r
        cnt=0
        for t3 in range(s//3+1):
            for t2 in range((s-3*t3)//2+1):
                t1=s-3*t3-2*t2
                zcnt=nilpotent_type_count(t1,t2,t3,q)
                bcnt=q**(r*r+2*r*(s-t3-t2))*zero_pairs(r,t2,q)
                cnt += zcnt*bcnt
        acnt=gauss(n,r,q)*gauss(n-r,r,q)*gl(r,q)
        total+=acnt*cnt
        per_rank.append((r,acnt,cnt))
    return total,per_rank


def direct(n,q):
    zero=tuple(tuple(0 for j in range(n)) for i in range(n))
    result=[]
    for r in range(n//2+1):
        A=matrix(r,n,q)
        count=0
        for B in genmat(n,q):
            if mul(A,B,q)!=zero or mul(B,A,q)!=zero:continue
            B2=mul(B,B,q)
            if mul(B2,B,q)!=zero:continue
            count+=1
        result.append((r,count))
    return result


def main():
    for n,q in [(0,2),(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,5)]:
        total,pr=jordan_count(n,q)
        br=direct(n,q)
        if [(r,cnt) for r,acnt,cnt in pr]!=br:
            raise AssertionError((n,q,pr,br))
        print('PASS',{'n':n,'q':q,'total_pairs':total,'per_fixed_A':br})
    print('ALL_EXACT_CHECKS_PASSED')

if __name__=='__main__':main()
