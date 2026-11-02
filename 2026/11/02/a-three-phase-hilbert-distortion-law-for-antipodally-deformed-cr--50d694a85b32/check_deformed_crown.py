"""Reproduce exact rational phase identities for antipodal-pair deformations.
Run: python3 check_deformed_crown.py
Requires only the Python standard library. All comparisons use fractions.
"""
from fractions import Fraction as Q
from itertools import combinations


def formula(n, q):
    assert isinstance(n, int) and n >= 3 and Q(1) <= q <= Q(9)
    low = Q(2*(n-1), n-2)
    high = Q(8*(n-1), n)
    T1 = Q(4*(n-1)) / (n-1+q)
    T0 = Q(4*(n-2), n)
    T3 = Q(n-2, 2*(n-1))*q
    T=max(T1,T0,T3)
    if q <= low:
        a,b,c = Q(4),T1,q*T1
        phase='small'
    elif q <= high:
        a,b,c = Q(4),T0,Q(8*(n-1),n)
        phase='plateau'
    else:
        c=q
        b=T3
        a=Q(n,2*(n-1))*q
        phase='large'
    assert T == max(a/4,b,c/q)
    assert Q(4) <= a <= 4*T and 1 <= b <= T and q <= c <= q*T
    assert abs(b-c) <= a and (n-1)*a <= (n-1)*b+c
    rho=(b-c)/a
    assert -1 <= rho <= 1
    assert a*Q(n-1,n)*(1-rho)==c
    assert a*Q(n-1+rho,n)==b
    assert T == max(T1,T0,T3)
    return T, (a,b,c), rho, phase


def solve4(A, v):
    B=[[Q(t) for t in row]+[Q(z)] for row,z in zip(A,v)]
    for i in range(4):
        j=next((j for j in range(i,4) if B[j][i]),None)
        if j is None: return None
        B[j],B[i]=B[i],B[j]
        factor=B[i][i]
        B[i]=[z/factor for z in B[i]]
        for k in range(4):
            if k!=i:
                fac=B[k][i]
                B[k]=[s-fac*t for s,t in zip(B[k],B[i])]
    return tuple(B[i][4] for i in range(4))


def lp_vertices(n,q):
    # variables: (a,b,c,T); inequalities A x <= B.
    A=[(-1,0,0,0), (0,-1,0,0),(0,0,-1,0),
       (1,0,0,-4),(0,1,0,-1),(0,0,1,-q),
       (-1,-1,1,0),(-1,1,-1,0),(1,-1,-Q(1,n-1),0)]
    B=[-4,-1,-q,0,0,0,0,0,0]
    minima=[]
    for inds in combinations(range(len(A)),4):
        x=solve4([A[j] for j in inds],[B[j] for j in inds])
        if x is not None and all(sum(v*w for v,w in zip(row,x))<=rhs for row,rhs in zip(A,B)):
            minima.append(x[3])
    assert minima
    return min(minima)


def run():
    phases=set()
    count=0
    lpcases=0
    qs=[Q(1),Q(9,8),Q(4,3),Q(2),Q(7,3),Q(3),Q(4),Q(9,2),Q(5),Q(6),Q(7),Q(8),Q(9)]
    for n in range(3,101):
        low=Q(2*(n-1),n-2)
        high=Q(8*(n-1),n)
        sample=sorted(set(qs+[low,high,(low+high)/2,(low+1)/2,(high+9)/2]))
        for q in sample:
            T,coeff,rho,phase=formula(n,q)
            phases.add(phase)
            count+=1
            if n<=10 and q in qs:
                assert T==lp_vertices(n,q), (n,q,T)
                lpcases+=1
    assert phases=={'small','plateau','large'}
    print('CHECK_OK exact_rational_phase_cases=',count,'independent_exact_LP_cases=',lpcases,
          'orders=3..100 phases=3')

if __name__=='__main__': run()
