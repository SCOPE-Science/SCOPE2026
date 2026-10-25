"""Exact, standard-library verification of short zero-sums in cyclic order-11 subgroups."""
from itertools import combinations_with_replacement
from math import comb, isqrt

MODULUS=11
EXPECTED={
 3:{(0,0,0):59049,(0,0,1):683,(0,1,2):1,(0,1,3):23},
 4:{(0,0,0,0):1048576,(0,0,0,1):44287,
    (0,0,1,1):1024,(0,0,1,2):529,(0,0,1,3):991,
    (0,0,1,5):1541,(0,0,1,7):419,(0,0,1,10):1,
    (0,1,2,3):1,(0,1,2,4):23,(0,1,2,5):89,
    (0,1,3,4):1}}


def exact_det(mat):
    a=[r[:] for r in mat]
    n=len(a); sign=1; previous=1
    for k in range(n-1):
        if a[k][k]==0:
            swap=next((j for j in range(k+1,n) if a[j][k]!=0),None)
            if swap is None:return 0
            a[k],a[swap]=a[swap],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%previous==0
                a[i][j]=num//previous
        for i in range(k+1,n):a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]


def norm(rep):
    # Multiplication by G(zeta), where zeta is primitive of order 11:
    # zeta^10 = -(1+...+zeta^9) and zeta^11=1.
    matrix=[]
    for i in range(10):
        row=[]
        for j in range(10):
            coefficients=[0]*11
            for exponent in rep:coefficients[(exponent+j)%11]+=1
            row.append(coefficients[i]-coefficients[10])
        matrix.append(row)
    return abs(exact_det(matrix))


def orbit_rep(indices):
    return min(tuple(sorted((a*j+b)%11 for j in indices))
               for a in range(1,11) for b in range(11))


def factors(n):
    d=2; out=[]
    while d*d<=n:
        if n%d==0:
            k=0
            while n%d==0:n//=d;k+=1
            out.append((d,k))
        d+=1
    if n>1:out.append((n,1))
    return tuple(out)


def check():
    observed={}
    for length in (3,4):
        tuples=list(combinations_with_replacement(range(11),length))
        assert len(tuples)==comb(10+length,length)
        reps={orbit_rep(t) for t in tuples}
        assert reps==set(EXPECTED[length]), (length,len(reps))
        for rep in sorted(reps):
            n=norm(rep)
            assert n==EXPECTED[length][rep],(length,rep,n)
        observed[length]=set(p for v in EXPECTED[length].values()
                             for p,k in factors(v) if p%11==1)
    assert observed=={3:{23,683},4:{23,67,89,419,661,991}}
    # Direct modulo-p witnesses for each asserted minimum.
    for p in sorted(observed[3]|observed[4]):
        q=next(t for t in range(2,p) if pow(t,11,p)==1)
        assert pow(q,11,p)==1 and q!=1
        if p in observed[3]: length=3
        else:length=4
        witness=next((t for t in combinations_with_replacement(range(11),length)
                      if sum(pow(q,j,p) for j in t)%p==0),None)
        assert witness is not None,(p,q,length)
        print('p=',p,'q=',q,'minimum=',length,'witness=',witness)
    print('PASS: all 1287 multisets, 16 affine orbits, exact norms and witnesses')

if __name__=='__main__':check()
