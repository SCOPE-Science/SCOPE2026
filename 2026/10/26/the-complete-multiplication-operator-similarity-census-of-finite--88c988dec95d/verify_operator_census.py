"""Standalone finite-prime-field checks for the permutation-evolution operator census.
Usage: python verify_operator_census.py
The general theorem is proved symbolically; this script checks finite instances only.
"""
from collections import Counter
from itertools import product
from math import factorial


def parts(n, maximum=None):
    if n == 0:
        yield ()
        return
    maximum = n if maximum is None else min(n, maximum)
    for r in range(maximum, 0, -1):
        for tail in parts(n-r, r):
            yield (r,)+tail


def expected_cycle(n, q):
    out=Counter()
    for lam in parts(n):
        z=len(lam)
        mm=Counter(lam)
        # Count circular ordered gap compositions modulo cyclic starting-gap choice.
        denom=1
        for v in mm.values():denom*=factorial(v)
        mult=n*factorial(z-1)//denom
        assert n*factorial(z-1)%denom==0
        out[('N',lam)]=mult*(q-1)**(n-z)
    for c in range(1,q):
        out[('C',c)]=(q-1)**(n-1)
    return out


def mul(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]


def rank(M,p):
    A=[row[:] for row in M]; n=len(A); r=0
    for j in range(n):
        piv=next((i for i in range(r,n) if A[i][j]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        v=pow(A[r][j],-1,p)
        A[r]=[(v*x)%p for x in A[r]]
        for i in range(n):
            if i != r:
                c=A[i][j]
                A[i]=[(x-c*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==n:break
    return r


def matrix_for_cycle(w):
    n=len(w); M=[[0]*n for _ in range(n)]
    for i in range(n):M[(i+1)%n][i]=w[i]
    return M


def empirical_cycle(n,p,a):
    out=Counter()
    for x in product(range(p),repeat=n):
        w=tuple((i*j)%p for i,j in zip(a,x))
        M=matrix_for_cycle(w)
        if all(w):
            c=1
            for t in w:c=c*t%p
            out[('C',c)]+=1
        else:
            ranks=[n]
            P=[[int(i==j) for j in range(n)] for i in range(n)]
            for k in range(1,n+2):
                P=mul(P,M,p)
                ranks.append(rank(P,p))
            lam=[]
            for j in range(1,n+1):
                number=ranks[j-1]-2*ranks[j]+ranks[j+1]
                assert number>=0
                lam += [j]*number
            assert sum(lam)==n
            out[('N',tuple(sorted(lam,reverse=True)))]+=1
    return out


def check_all():
    cases=[]
    for p,nmax in [(2,8),(3,6),(5,4),(7,3)]:
        for n in range(1,nmax+1):
            coefficients=[tuple(1 for _ in range(n))]
            if p>2: coefficients.append(tuple(1+(i%(p-1)) for i in range(n)))
            exp=expected_cycle(n,p)
            assert sum(exp.values())==p**n
            for a in coefficients:
                got=empirical_cycle(n,p,a)
                assert got==exp, (p,n,a,got-exp,exp-got)
                cases.append((p,n,a,len(got),p**n))
    # distinguish two weighted 2-cycle evolution algebras over F_7 via idempotents
    def idem(c):
        return sum((u==(c*v*v)%7 and v==u*u%7) for u in range(7) for v in range(7))
    assert idem(1)==4 and idem(2)==1
    # all full operator matrices coincide as a set, even with multiplicities
    def mats(c):
        return Counter(tuple(tuple(row) for row in matrix_for_cycle((u,c*v%7)))
                       for u in range(7) for v in range(7))
    assert mats(1)==mats(2)
    print('PASS: finite prime-field cases',len(cases),'; examples',cases[-5:])
    print('PASS: F_7 weighted 2-cycles have idempotent counts 4 versus 1; identical operator pencils')

if __name__=='__main__':check_all()
