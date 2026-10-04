#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import isqrt

def formulas(N,a):
    b=N-a
    d=a-b
    p=Fraction(2*a*b,N*(N-1))
    vadj=Fraction((N*N-d*d)*(d*d-N),4*N*N*(N-1)*(N-1))
    vfar=Fraction((N*N-d*d)*(N*(N-2)-(2*N-3)*d*d),2*N*N*(N-1)*(N-1)*(N-2)*(N-3)) if N>=4 else None
    vr=Fraction(2*a*b*(2*a*b-N),N*N*(N-1))
    return p,vadj,vfar,vr

def enumerate_cov(N,a):
    words=[]
    for pos in combinations(range(N),a):
        x=[0]*N
        for i in pos:x[i]=1
        words.append([int(x[i]!=x[i+1]) for i in range(N-1)])
    M=len(words); k=N-1
    means=[Fraction(sum(w[i] for w in words),M) for i in range(k)]
    cov=[[Fraction(sum(w[i]*w[j] for w in words),M)-means[i]*means[j] for j in range(k)] for i in range(k)]
    return means,cov

def run():
    words_enumerated=0
    marginal_checks=0
    adjacent_checks=0
    disjoint_checks=0
    phase_checks=0
    nonzero_far_checks=0
    square_independence_checks=0
    variance_checks=0

    for N in range(4,13):
        for a in range(1,N):
            b=N-a
            means,cov=enumerate_cov(N,a)
            words_enumerated += __import__('math').comb(N,a)
            p,c1,c2,vr=formulas(N,a)
            for i,m in enumerate(means):
                assert m==p
                marginal_checks+=1
            for i in range(N-2):
                assert cov[i][i+1]==c1
                adjacent_checks+=1
            for i in range(N-1):
                for j in range(i+2,N-1):
                    assert cov[i][j]==c2
                    disjoint_checks+=1
            # Direct run-count variance from the enumerated transition vectors.
            vals=[]
            for pos in combinations(range(N),a):
                x=[0]*N
                for i in pos:x[i]=1
                vals.append(1+sum(x[i]!=x[i+1] for i in range(N-1)))
            mu=Fraction(sum(vals),len(vals))
            vv=Fraction(sum(v*v for v in vals),len(vals))-mu*mu
            assert vv==vr
            variance_checks+=1

    for N in range(4,251):
        theta_num=N*(N-2); theta_den=2*N-3
        q=isqrt(N)
        for a in range(1,N):
            b=N-a; d=a-b; d2=d*d
            _,c1,c2,vr=formulas(N,a)
            assert c2!=0
            nonzero_far_checks+=1
            if d2*theta_den < theta_num:
                assert c1<0 and c2>0
            elif d2<N:
                assert c1<0 and c2<0
            elif d2==N:
                assert c1==0 and c2<0
            else:
                assert c1>0 and c2<0
            phase_checks+=1
            expected_zero=(q*q==N and abs(d)==q)
            assert (c1==0)==expected_zero
            square_independence_checks+=1
            p=Fraction(2*a*b,N*(N-1)); v=p*(1-p)
            summed=(N-1)*v+2*(N-2)*c1+(N-2)*(N-3)*c2
            assert summed==vr
            variance_checks+=1

    print('VERIFY_OK',
          f'words_enumerated={words_enumerated}',
          f'marginal_checks={marginal_checks}',
          f'adjacent_checks={adjacent_checks}',
          f'disjoint_checks={disjoint_checks}',
          f'phase_checks={phase_checks}',
          f'nonzero_far_checks={nonzero_far_checks}',
          f'square_independence_checks={square_independence_checks}',
          f'variance_checks={variance_checks}')

if __name__=='__main__':
    run()
