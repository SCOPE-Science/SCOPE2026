"""Independent exact arithmetic checks for cyclic Markov end-steps.
The infinite-dimensional (all cycle lengths) statement is proved in RESULT.md,
not inferred from these finite checks.
Run: python verify.py
"""
from fractions import Fraction as F
from math import factorial, comb

def mat_mul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def mat_step(n,p,h):
    P=[[F(int(i==(j+1)%n)) for j in range(n)] for i in range(n)]
    Q=[[P[i][j]-int(i==j) for j in range(n)] for i in range(n)]
    power=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    result=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(1,p+1):
        power=mat_mul(power,Q)
        for i in range(n):
            for j in range(n):
                result[i][j]+=h**k*power[i][j]/factorial(k)
    return result

def truncated(k,z):
    return sum((z**r/F(factorial(r)) for r in range(k+1)),F(0))

def residue(n,p,h):
    return [sum((h**j/F(factorial(j))*truncated(p-j,-h) for j in range(r,p+1,n)),F(0)) for r in range(n)]

def polyrange(h):
    P3=2*h**3-3*h*h+3*h-3
    P42=h**3-2*h*h+3*h-3
    P43=h**4-4*h*h+8*h-8
    return P3,P42,P43

checks=0
for n in range(2,13):
    for p in range(1,5):
        for ih in range(0,41):
            h=F(ih,16)
            M=mat_step(n,p,h)
            c=residue(n,p,h)
            for i in range(n):
                assert sum(M[i][j] for j in range(n))==1
                assert sum(M[j][i] for j in range(n))==1
                for j in range(n):
                    assert M[i][j]==c[(i-j)%n]
            # independently predicted signs from the analytic classification
            if p<=2 or (p==3 and n>=3) or (p==4 and n>=4):
                good=(h<=1)
            elif p==3 and n==2:
                good=(polyrange(h)[0]<=0)
            elif p==4 and n==2:
                good=(polyrange(h)[1]<=0)
            else:
                good=(polyrange(h)[2]<=0)
            assert (all(x>=0 for x in c))==good,(n,p,h,c)
            checks+=1

# Rational witness: the exact 3-state step is stable on mean-zero modes
c=residue(3,4,F(3,2))
assert c==[F(-1,128),F(39,128),F(90,128)]
assert c[0]**2+c[1]**2+c[2]**2-c[0]*c[1]-c[1]*c[2]-c[2]*c[0]==F(79**2,128**2)
checks+=2

# R4(-z) is strictly positive: this finite grid is only a diagnostic.
for j in range(1001):
    z=F(j,41)
    assert truncated(4,-z)>0
    checks+=1

# Full two-state generators, including absorbing boundaries, at rational steps.
for a0 in range(6):
    for b0 in range(6):
        if a0+b0==0:continue
        a,b=F(a0,5),F(b0,5)
        lam=a+b
        Pi=[[b/lam,b/lam],[a/lam,a/lam]]
        Q=[[-a,b],[a,-b]]
        for j in range(36):
            h=F(j,12)
            R=truncated(4,-h*lam)
            T=[[Pi[i][k]+R*(F(int(i==k))-Pi[i][k]) for k in range(2)] for i in range(2)]
            # direct Taylor powers for this generator
            power=[[F(int(i==k)) for k in range(2)] for i in range(2)]
            V=[[F(int(i==k)) for k in range(2)] for i in range(2)]
            for t in range(1,5):
                power=mat_mul(power,Q)
                for i in range(2):
                    for k in range(2):V[i][k]+=h**t*power[i][k]/factorial(t)
            assert V==T
            assert (all(x>=0 for row in V for x in row))==(R<=1)
            checks+=1

# Sharp root isolating rational intervals, each polynomial strictly increasing
assert polyrange(F('1.2563726633'))[0]<0<polyrange(F('1.2563726634'))[0]
assert polyrange(F('1.3926467817'))[1]<0<polyrange(F('1.3926467818'))[1]
assert polyrange(F('1.4933773767'))[2]<0<polyrange(F('1.4933773768'))[2]
checks+=3
print('ALL_CHECKS_PASSED',checks)
