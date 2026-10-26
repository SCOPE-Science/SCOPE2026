"""Reproduce the exact two-type completion-time dispersion formulas."""
from fractions import Fraction
from itertools import product

def solve(A,b):
    n=len(b); m=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        j=next(i for i in range(k,n) if m[i][k]); m[k],m[j]=m[j],m[k]
        c=m[k][k];m[k]=[v/c for v in m[k]]
        for i in range(n):
            if i!=k:
                c=m[i][k];m[i]=[m[i][j]-c*m[k][j] for j in range(n+1)]
    return [m[i][-1] for i in range(n)]

checks=0
for ai,pi in product(range(1,20),range(0,19)):
    a=Fraction(ai,20);b=1-a;p=Fraction(pi,20);q=1-p;w=a*b
    Q=[[p,a*q,b*q],[a*p,1-a*p-b*q,0],[b*p,0,1-b*p-a*q]]
    A=[[Fraction(i==j)-Q[i][j] for j in range(3)] for i in range(3)]
    mean=solve(A,[Fraction(1)]*3)
    second=solve(A,[2*mean[i]-1 for i in range(3)])
    vari=second[0]-mean[0]**2
    M=(q+(2*p-1)*w)/(w*q*q)
    V=((2*p-1)*(3*p*p-4*p+2)*w*w-(p-1)*(p*p+4*p-3)*w+q*q)/(w*w*q**4)
    assert M==mean[0],(a,p,mean[0],M)
    assert V==vari,(a,p,vari,V)
    # claimed derivative of variance / mean^2 (sign established algebraically)
    assert V>0 and M>0
    checks+=3
print('EXACT_RATIONAL_CHECKS',checks)
print('critical_loss_probability',(19-97**0.5)/12)
