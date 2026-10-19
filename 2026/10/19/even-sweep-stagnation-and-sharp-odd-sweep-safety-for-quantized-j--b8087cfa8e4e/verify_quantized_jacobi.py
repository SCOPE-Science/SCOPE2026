"""Exact-rational checks for rank-two coupled Jacobi refinements.

No special libraries are needed. This finite checker tests explicit matrix
identities and boundary examples; the written proof establishes generality.
"""
from fractions import Fraction as F

def mmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def madd(A,B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]

def smul(c,A):
    return [[c*x for x in a] for a in A]

def ident(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def matrix(m,p):
    n=2*m
    P=[[F(int((i<m)!=(j<m)),m) for j in range(n)] for i in range(n)]
    d=F(1,2**(p+2))
    r=1-d
    A=madd(ident(n),smul(r,P))
    return P,A,d,r

num=0
for p in range(2,10):
    r=F(1)-F(1,2**(p+2))
    for j in range(4):
        m=2**j; n=2*m; P,A,d,r=matrix(m,p)
        # Direct adjacent-value midpoint argument for round-to-nearest.
        quantized_target=F(1,m)
        adjacent_below=quantized_target*(1-F(1,2**p))
        midpoint=(quantized_target+adjacent_below)/2
        assert midpoint<r/m<quantized_target; num+=1
        I=ident(n); P2=mmul(P,P)
        assert mmul(P2,P)==P; num+=1
        plus=smul(F(1,2),madd(P2,P))
        minus=smul(F(1,2),madd(P2,smul(-1,P)))
        zero=madd(I,smul(-1,P2))
        assert madd(madd(plus,minus),zero)==I; num+=1
        C=[[F(0) for _ in range(n)] for _ in range(n)]
        power=I
        for k in range(1,18):
            C=madd(C,power)
            E=madd(I,smul(-1,mmul(C,A)))
            ep=F(1) if k%2==0 else -r
            em=1-k*d
            expected=madd(smul(ep,plus),smul(em,minus))
            assert E==expected, (p,m,k,E,expected); num+=1
            # A fresh residual with exact original A and k rounded-Jacobi
            # inner sweeps gives the same linear operator.
            z=[F(i+1,n+1) for i in range(n)]
            res=[sum(A[i][h]*z[h] for h in range(n)) for i in range(n)]
            y=[F(0)]*n
            for step in range(k):
                y=[res[i]-sum(P[i][h]*y[h] for h in range(n)) for i in range(n)]
            assert y==[sum(C[i][h]*res[h] for h in range(n)) for i in range(n)];num+=1
            power=smul(-1,mmul(power,P))
        if m<=4:
            b=[1+r]*n; x=[F(0)]*n
            for k in (2,4,6):
                C=ident(n); B=smul(-1,P)
                for step in range(1,k):
                    C=madd(C,B);B=smul(-1,mmul(B,P))
                assert [sum(C[i][h]*b[h] for h in range(n)) for i in range(n)]==[0]*n; num+=1
assert num>1000
print(f'PASS {num} exact-rational checks')

# Additional exact rational scalar eigenvalue comparisons for the full
# symmetric-contraction statement, beyond the rank-two graph witnesses.
for p in range(2,10):
    delta=F(1,2**(p+2)); r=1-delta
    kappa=(1+r)/delta
    assert kappa.denominator==1
    for k in range(1, min(int(kappa),61)+1,2):
        for lam_num in range(-48,49):
            lam=F(lam_num,48)
            P=F(1)
            S=F(0)
            for j in range(k):
                S+=P
                P*=-lam
            g=1-(1+r*lam)*S
            assert -r<=g<=r,(p,k,lam,g,r)
            num+=1
for p in (2,3,5,8):
    delta=F(1,2**(p+2));r=1-delta
    for k in range(1,31,2):
        if k*delta>=2:continue
        for q in range(-48,49):
            t=F(q,48)
            powers=F(1);S=F(0)
            for j in range(k):
                S+=powers;powers*=-t
            g=1-(1+r*t)*S
            assert -1<g<1,(p,k,q,g)
            num+=1
print(f'PASS {num} exact-rational checks including arbitrary contraction eigenvalues')

# A connected non-bipartite regular graph checks the Perron obstruction
# without assuming a negative unit eigenvalue.
for p in (2,3,4,7):
    n=3; d=2
    P=[[F(int(i!=j),d) for j in range(n)] for i in range(n)]
    delta=F(1,2**(p+2));r=1-delta
    A=madd(ident(n),smul(r,P));I=ident(n)
    C=[[F(0) for j in range(n)] for i in range(n)];power=I
    for k in range(1,18):
        C=madd(C,power)
        E=madd(I,smul(-1,mmul(C,A)))
        u=[F(1)]*n
        action=[sum(E[i][j]*u[j] for j in range(n)) for i in range(n)]
        expected=F(1) if k%2==0 else -r
        assert action==[expected]*n;num+=1
        if k%2 and k <= (1+r)/delta:
            q=F(-1,2)
            S=sum((-q)**j for j in range(k))
            g=1-(1+r*q)*S
            assert abs(g)<=r;num+=1
        power=smul(-1,mmul(power,P))
print(f'FINAL PASS {num} exact rational checks')
