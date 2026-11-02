"""Exact rational checks for finite truncations of Bergman--Hilbert exterior minors.

Python >=3.9, standard library only. These checks supplement an analytic theorem;
they do not prove infinite-dimensional limits or publication priority.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial

COUNT = 0

def check(condition, message):
    global COUNT
    assert condition, message
    COUNT += 1

def weight(gamma, degree):
    v=Q(1)
    for j in range(1, degree + 1):
        v *= Q(j) / (gamma+j+1)
    return v

def det(mat):
    n=len(mat)
    mat=[list(map(Q,row)) for row in mat]
    out=Q(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if mat[j][i]),None)
        if pivot is None: return Q(0)
        if pivot!=i:
            mat[i],mat[pivot]=mat[pivot],mat[i]
            out=-out
        p=mat[i][i]
        out *= p
        for j in range(i+1,n):
            z=mat[j][i]/p
            for h in range(i+1,n):
                mat[j][h]-=z*mat[i][h]
            mat[j][i]=Q(0)
    return out

def cauchy(I,J):
    return det([[Q(1,i+j+1) for j in J] for i in I])

def norm_sq_ratio(I,beta):
    return Q(1) if len(I)==0 else prod(weight(beta,i)/weight(beta,r) for r,i in enumerate(I))

def prod(it):
    ans=Q(1)
    for x in it: ans*=x
    return ans

def main():
    a=Q(-1,2)
    for n in range(3,11):
        ws=[weight(a,j) for j in range(n)]
        for k in range(1,min(4,n)+1):
            I=tuple(range(k))
            # Exact Cauchy--Binet: squared norm of the lowest exterior output row.
            minors=Q(0)
            for J in combinations(range(n),k):
                c=cauchy(I,J)
                check(c>0,('Cauchy minor',n,k,J))
                minors += c*c/prod(ws[j] for j in J)
            gram=[[sum((Q(1,(r+j+1)*(s+j+1))/ws[j] for j in range(n)),Q(0))
                    for s in range(k)] for r in range(k)]
            check(det(gram)==minors,('Cauchy--Binet',n,k))
            check(det(gram)>0,('positive moment Gram',n,k))
    # Exact rational monotonicity and midpoint log-convexity of each
    # normalized compound row multiplier squared.
    for k in range(1,6):
        i0=tuple(range(k))
        for I in combinations(range(11),k):
            t3=norm_sq_ratio(I,Q(3))
            t5=norm_sq_ratio(I,Q(5))
            t7=norm_sq_ratio(I,Q(7))
            check(t3>=t5>=t7>0,('row order',k,I))
            check(t5*t5<=t3*t7,('log convex',k,I))
            check((t3==t7)==(I==i0),('strict off minimal row',k,I))
    # The weights are coefficients of (1-z)^(-a-2), giving the Gram kernel.
    coeff=Q(1)
    for j in range(101):
        if j: coeff*= (a+j+1)/j
        check(coeff==1/weight(a,j),('binomial generating weight',j))
    print('EXACT_BERG_SPECTRAL_OK',COUNT)

if __name__=='__main__':main()
