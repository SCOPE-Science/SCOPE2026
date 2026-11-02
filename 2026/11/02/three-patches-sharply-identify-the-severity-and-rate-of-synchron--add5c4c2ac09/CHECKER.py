"""Exact independent finite-state checks for an exchangeable finite-patch occupancy model.

Run: python3 CHECKER.py
Uses only Python standard library, exact Fraction arithmetic, and deterministic loops.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

checks=0

def eq(a,b,msg=''):
    global checks
    checks+=1
    if a != b:
        raise AssertionError(f'{msg}: {a!r} != {b!r}')

def ge(a,b,msg=''):
    global checks
    checks+=1
    if not a >= b:
        raise AssertionError(f'{msg}: {a!r} < {b!r}')

def solve(A,b):
    A=[list(map(F,row))+[F(val)] for row,val in zip(A,b)]
    n=len(A)
    for i in range(n):
        pivot=next((j for j in range(i,n) if A[j][i]),None)
        if pivot is None:raise ValueError('singular')
        A[i],A[pivot]=A[pivot],A[i]
        v=A[i][i]
        A[i]=[z/v for z in A[i]]
        for j in range(n):
            if j==i:continue
            mult=A[j][i]
            if mult:A[j]=[z-mult*w for z,w in zip(A[j],A[i])]
    return [row[-1] for row in A]

def generator(n,a,b,c,q):
    size=1<<n
    G=[[F(0) for _ in range(size)] for _ in range(size)]
    survival=1-q
    for mask in range(size):
        for i in range(n):
            dest=mask^(1<<i)
            rate=b if mask&(1<<i) else a
            G[mask][dest]+=rate
        # At a shared catastrophe each currently occupied patch is independently cleared.
        subset=mask
        while True:
            if subset!=mask:
                nremove=(mask^subset).bit_count()
                nkeep=subset.bit_count()
                G[mask][subset]+=c*q**nremove*survival**nkeep
            if subset==0:break
            subset=(subset-1)&mask
        G[mask][mask]=-sum(G[mask][j] for j in range(size) if j!=mask)
    for i in range(size):eq(sum(G[i]),0,'row sums')
    return G

def stationary(n,a,b,c,q):
    G=generator(n,a,b,c,q)
    dim=1<<n
    A=[[G[row][col] for row in range(dim)] for col in range(dim)]
    A[-1]=[F(1)]*dim
    rhs=[F(0)]*(dim-1)+[F(1)]
    probs=solve(A,rhs)
    eq(sum(probs),F(1),'sum probs')
    for p in probs:ge(p,0,'nonnegative stationary')
    for j in range(dim):eq(sum(probs[i]*G[i][j] for i in range(dim)),F(0),'balance')
    return probs

def moments_from_chain(probs,n):
    out=[F(1)]
    for k in range(1, min(n,3)+1):
        selected=(1<<k)-1
        out.append(sum(prob for state,prob in enumerate(probs) if state&selected==selected))
    return out

def moments_from_formula(n,a,b,c,q):
    out=[F(1)]
    for k in range(1,n+1):
        out.append(out[-1]*k*a/(k*(a+b)+c*(1-(1-q)**k)))
    return out

def invert(m,p2,p3):
    A=1-m*m/p2
    B=1-m*p2/p3
    q=3-F(3,2)*B/A
    s=2*A/q
    colonization_fraction=m/(1-s)
    catastrophe_ratio=s/(q*(1-s))
    return q,s,colonization_fraction,catastrophe_ratio,A,B

# A second independent stationary enumeration reconstructs all states and
# checks the first three specific-site joint occupancy probabilities.
for n in (3,4):
    for a,b,c,q in product((F(1),F(2),F(3)),(F(1),F(2),F(3)),(F(1),F(2),F(3)),(F(1,4),F(1,2),F(3,4),F(1))):
        pi=stationary(n,a,b,c,q)
        actual=moments_from_chain(pi,n)
        predicted=moments_from_formula(n,a,b,c,q)
        for k in (1,2,3):eq(actual[k],predicted[k],f'moment {k}')
        qi,s,x,z,A,B=invert(*actual[1:])
        eq(qi,q,'recover removal probability')
        eq(s,c*q/(a+b+c*q),'recover scaled event mass')
        eq(x,a/(a+b),'recover colonization share')
        eq(z,c/(a+b),'recover catastrophe-rate ratio')
        ge(A,F(0),'A positive')
        ge(B,F(0),'B positive')
        ge(F(1)-actual[1]-s,F(0),'feasibility bound')
        # Every k-site marginal is a subsampling of the identical n-site stationary law.
        for k in range(1,n+1):
            sel=(1<<k)-1
            measured=sum(pp for state,pp in enumerate(pi) if state&sel==sel)
            eq(measured,predicted[k],f'all moment k={k}')

# The local-identifiability Jacobian is nonzero in the interior and
# its signed formula follows by exact chain-rule determinants.
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
for x,s,q in product((F(1,4),F(2,3),F(4,5)),(F(1,10),F(1,3),F(1,2)),(F(1,4),F(1,2),F(1))):
    m=x*(1-s); A=s*q/2; B=s*(q-q*q/3)
    J1=det3([[1-s,-x,0],[0,q/2,s/2],[0,q-q*q/3,s*(1-2*q/3)]])
    J2=m**5/((1-A)**3*(1-B)**2)
    J=J1*J2
    derived= -x**5*(1-s)**6*s*q*q/(6*(1-s*q/2)**3*(1-s*(q-q*q/3))**2)
    eq(J,derived,'exact Jacobian')
    ge(-J,F(1,10**100),'Jacobian is strictly negative')

# A representable exchangeable law test excludes perfectly valid occupancy
# distributions outside the shared-binomial-catastrophe observation domain.
bad=(F(1,2),F(3,10),F(9,50))
qbad,*_=invert(*bad)
ge(qbad,F(1),'example rejects catastrophe thinning parameter')
P3=bad[2];P2=3*(bad[1]-bad[2]);P1=3*(bad[0]-2*bad[1]+bad[2]);P0=1-P1-P2-P3
for z in (P0,P1,P2,P3):ge(z,0,'bad model observation is valid distribution')
eq(P0+P1+P2+P3,1,'valid 3-count distribution')

# Exact distinguishability example: the first two moments coincide but third differs.
a,b,c,q=map(F,(2,1,3,F(1,2)))
orig=moments_from_formula(3,a,b,c,q)
alternative=moments_from_formula(3,F(32),F(22),F(27),F(2,3))
eq(orig[1],F(4,9),'example single')
eq(orig[2],F(64,297),'example pair')
eq(orig[3],F(1024,9207),'example triple')
eq(orig[1],alternative[1],'two-patch ambiguity single')
eq(orig[2],alternative[2],'two-patch ambiguity pair')
ge(abs(orig[3]-alternative[3]),F(1,10**8),'three-patch difference')
qhat,shat,xhat,zhat,_,_=invert(*orig[1:])
eq((qhat,shat,xhat,zhat),(F(1,2),F(1,3),F(2,3),F(1)),'example inverse')
print('PASS',checks,'exact checks')
print('original p1,p2,p3:',orig[1:])
print('alternative p1,p2,p3:',alternative[1:])
print('third difference:',orig[3]-alternative[3])
