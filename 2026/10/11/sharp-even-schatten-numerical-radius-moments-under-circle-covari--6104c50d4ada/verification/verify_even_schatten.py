"""Exact finite-matrix and binomial checks for graded Schatten moment inequalities.

Runs with Python 3 standard library only. Finite checks supplement the analytic proof.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product


def mul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)), Q(0)) for j in range(n)] for i in range(n)]


def power(a,m):
    n=len(a)
    out=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for _ in range(m):
        out=mul(out,a)
    return out


def trans(a):
    return [list(x) for x in zip(*a)]


def trace(a):
    return sum((a[i][i] for i in range(len(a))),Q(0))


def add(a,b,t,s):
    return [[t*a[i][j]+s*b[i][j] for j in range(len(a))] for i in range(len(a))]


def coef(m,t):
    s=1-t
    return sum((Q(comb(m,k)**2)*t**(2*k)*s**(2*(m-k)) for k in range(m+1)),Q(0))


def enumerated_balanced(m,t):
    s=1-t
    ans=Q(0)
    # Each factor is (t T*+s T) or (t T+s T*) in alternating positions.
    for bits in product((0,1),repeat=2*m):
        grade=0
        c=Q(1)
        for i,b in enumerate(bits):
            c*=t if b==0 else s
            grade+=(1 if b==1 else -1) if i%2==0 else (1 if b==0 else -1)
        if grade==0:
            ans+=c
    return ans


def check_operator(T):
    n=len(T); TT=trans(T)
    A=mul(TT,T); B=mul(T,TT)
    comm=add(A,B,Q(1),Q(-1))
    comm2=trace(mul(comm,comm))
    for m in range(1,6):
        baseline=trace(power(A,m))
        for t in [Q(0),Q(1,5),Q(1,2),Q(3,4),Q(1)]:
            s=1-t
            C=coef(m,t)
            R=add(T,TT,t,s)
            moment=trace(power(mul(trans(R),R),m))
            assert moment<=C*baseline,(n,m,t)
            if m==1 or t in (0,1):
                assert moment==C*baseline,(n,m,t,'endpoints')
            if m>=2 and 0<t<1 and comm2>0:
                assert moment<C*baseline,(n,m,t,'strict')
            if m==2:
                assert C*baseline-moment==2*t*t*s*s*comm2,(n,m,t,'quartic')


for m in range(1,9):
    for t in (Q(0),Q(1,5),Q(2,5),Q(1,2),Q(4,5),Q(1)):
        assert enumerated_balanced(m,t)==coef(m,t),(m,t)
for n in range(2,10):
    T=[[Q(int(i==j+1)) for j in range(n)] for i in range(n)]
    check_operator(T)
# A genuinely non-scalar three-grade block shift.
T=[[Q(0) for j in range(5)] for i in range(5)]
for i,j,v in [(2,0,1),(2,1,-2),(3,2,3),(4,2,-1)]:
    T[i][j]=Q(v)
check_operator(T)
print('GRADED_SCHATTEN_EXACT_BALANCED_WORDS_AND_COMMUTATOR_OK')
