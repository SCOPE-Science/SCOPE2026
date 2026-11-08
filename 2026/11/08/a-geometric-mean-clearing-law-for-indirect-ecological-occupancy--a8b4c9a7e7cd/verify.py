"""Finite exact cross-checks for a Markovian indirect-occupancy marker theorem.

Standard-library Python 3; no external datasets. The finite tests check independent
stationary equations and closed-form identities, not the infinite proof.
"""
from fractions import Fraction as F
from itertools import product

STATES=((0,0),(0,1),(1,0),(1,1))

def linear_solve(A, b):
    m=[list(map(F,row))+[F(y)] for row,y in zip(A,b)]
    n=len(b)
    for j in range(n):
        k=next(i for i in range(j,n) if m[i][j])
        m[j],m[k]=m[k],m[j]
        div=m[j][j]
        m[j]=[v/div for v in m[j]]
        for i in range(n):
            if i!=j:
                mult=m[i][j]
                m[i]=[x-mult*y for x,y in zip(m[i],m[j])]
    return tuple(row[-1] for row in m)

def stationary(a,b,l,d):
    Q=[[F(0) for _ in range(4)] for _ in range(4)]
    for i,(z,m) in enumerate(STATES):
        jumps=[]
        if z==0:jumps.append(((1,m),a))
        else:jumps.append(((0,m),b))
        if z==1 and m==0:jumps.append(((1,1),l))
        if m==1:jumps.append(((z,0),d))
        for new,rate in jumps:
            j=STATES.index(new)
            Q[i][j]+=rate
            Q[i][i]-=rate
    equations=[[Q[i][j] for i in range(4)] for j in range(3)] + [[F(1)]*4]
    vec=linear_solve(equations,[F(0)]*3+[F(1)])
    assert min(vec)>0 and sum(vec)==1
    assert all(sum(vec[i]*Q[i][j] for i in range(4))==0 for j in range(4))
    return vec

def formula(a,b,l,d):
    D=d*d+d*(a+b+l)+a*l
    sens=l*(a+d)/D
    fpr=a*l/D
    return sens,fpr,sens-fpr

cases=0
for a,b,l,d in product([F(1,3),F(1,2),F(1),F(2),F(3),F(5)],repeat=4):
    p=stationary(a,b,l,d)
    pi=p[2]+p[3]
    assert pi==a/(a+b)
    sens=p[3]/pi
    fpr=p[1]/(1-pi)
    assert (sens,fpr,sens-fpr)==formula(a,b,l,d)
    j=formula(a,b,l,d)[2]
    reciprocal=a*l/d
    assert j==formula(a,b,l,reciprocal)[2]
    assert j>0
    cases+=1
print('PASS stationary-law and sensitivity/FPR: ',cases,'exact rational parameter quadruples')
print('PASS reciprocal-erasure identity: ',cases,'exact rational parameter quadruples')
print('PASS all four stationary master equations: ',cases,'exact rational parameter quadruples')
# The derivative and unique maximizer are derived algebraically in RESULT.md.
