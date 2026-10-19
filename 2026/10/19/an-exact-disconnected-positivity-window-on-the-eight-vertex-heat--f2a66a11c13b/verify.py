#!/usr/bin/env python3
"""Exact polynomial certificate for the two-stage Gauss end-step on P8.

Uses Python's standard library only. No floating-point sign tests are used.
"""
from fractions import Fraction as F
from math import factorial

N = 8

def add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return trim(out)

def scale(a,c):
    return trim([x*c for x in a])

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def evalp(a,t):
    z=F(0)
    for c in reversed(a):z=z*t+c
    return z

def make_l():
    L=[[0]*N for _ in range(N)]
    for i in range(N-1):
        L[i][i]+=1;L[i+1][i+1]+=1
        L[i][i+1]-=1;L[i+1][i]-=1
    return L

L=make_l()
L2=[[sum(L[i][k]*L[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

# Q=12I+6hL+h^2L^2 and M=12I-6hL+h^2L^2.
Q=[[[F(12 if i==j else 0),F(6*L[i][j]),F(L2[i][j])] for j in range(N)] for i in range(N)]
M=[[[F(12 if i==j else 0),F(-6*L[i][j]),F(L2[i][j])] for j in range(N)] for i in range(N)]

# Positive denominator (a product of polynomials with nonnegative coefficients).
D=mul(mul([3,3,1],[36,72,54,12,1]),
      [5184,20736,36288,34560,18936,5760,888,48,1])
assert len(D)==15 and all(c>0 for c in D)

# Expected controlling sign polynomials, ascending coefficient order.
FAR=[-144,0,936,1320,660,126,7]
MIDDLE=[-248832,-1244160,-2820096,-3732480,-3124224,
        -1665792,-525456,-64224,16584,7944,1172,58,1]

def solve(a,b):
    """Gauss-Jordan inverse application over exact rational numbers."""
    n=len(a)
    x=[[F(v) for v in a[i]]+[F(v) for v in b[i]] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if x[i][j]),None)
        assert pivot is not None
        x[j],x[pivot]=x[pivot],x[j]
        z=x[j][j]
        x[j]=[v/z for v in x[j]]
        for i in range(n):
            if i==j:continue
            k=x[i][j]
            if k:
                x[i]=[v-k*w for v,w in zip(x[i],x[j])]
    return [row[n:] for row in x]

def interpolate_on_nonnegative_integers(ys):
    """Exact Newton forward-difference interpolation to power basis."""
    diffs=[F(y) for y in ys]
    result=[F(0)]
    falling=[F(1)]
    for k in range(len(ys)):
        if k:
            falling=mul(falling,[F(1-k),F(1)])
        result=add(result,scale(falling,diffs[0]/factorial(k)))
        diffs=[diffs[j+1]-diffs[j] for j in range(len(diffs)-1)]
    return trim(result)

# Each scaled numerator P_ij=4 D T_ij has degree at most 14.
# The degree bound is independently checked by polynomial identity below.
values=[[[] for _ in range(N)] for _ in range(N)]
for step in range(15):
    t=F(step)
    q=[[evalp(Q[i][j],t) for j in range(N)] for i in range(N)]
    m=[[evalp(M[i][j],t) for j in range(N)] for i in range(N)]
    tran=solve(q,m)
    den=4*evalp(D,t)
    for i in range(N):
        for j in range(N):values[i][j].append(den*tran[i][j])
P=[[interpolate_on_nonnegative_integers(values[i][j])
    for j in range(N)] for i in range(N)]
assert all(all(c.denominator==1 for c in P[i][j]) for i in range(N) for j in range(N))

# Certificate for every real h: polynomial matrix identity Q P=4 D M.
for i in range(N):
    for j in range(N):
        lhs=[F(0)]
        for k in range(N):lhs=add(lhs,mul(Q[i][k],P[k][j]))
        rhs=scale(mul(D,M[i][j]),4)
        assert lhs==rhs,(i,j,lhs,rhs)

assert P[0][7]==mul([F(0)]*7+[F(9)],FAR)
assert P[3][4]==mul([F(0),F(-9)],MIDDLE)
assert all(P[i][j]==P[j][i] for i in range(N) for j in range(N))
assert all(P[i][j]==P[N-1-i][N-1-j] for i in range(N) for j in range(N))

def var(a):
    nonzero=[1 if x>0 else -1 for x in a if x]
    return sum(nonzero[k]!=nonzero[k+1] for k in range(len(nonzero)-1))

assert var(FAR)==var(MIDDLE)==1
assert evalp(FAR,F(3,10))<0<evalp(FAR,F(1,3))
assert evalp(MIDDLE,F(4))<0<evalp(MIDDLE,F(9,2))

# For every other entry, remove its harmless initial h^k factor and
# inspect its coefficient signs. Cases with one sign change are positive
# near zero, have at most one positive real root by Descartes' rule, and
# remain positive at 9/2; hence that root exceeds 9/2.
counts={'all_positive':0,'single_upper_root':0}
for i in range(N):
    for j in range(N):
        if (i,j) in ((0,7),(7,0),(3,4),(4,3)):continue
        a=P[i][j]
        assert a!=[F(0)]
        k=next(r for r,c in enumerate(a) if c)
        b=a[k:]
        assert b[0]>0 and evalp(b,F(9,2))>0,(i,j)
        variations=var(b)
        if variations==0:
            assert all(c>=0 for c in b)
            counts['all_positive']+=1
        else:
            assert variations==1 and b[-1]<0,(i,j)
            counts['single_upper_root']+=1

# Three explicit rational matrices independently checked at a positive-
# interval point and in each negative region.
for t,entry,target in ((F(1,4),(0,7),F(-2291913,780953605188301)),
                       (F(1),(0,7),F(747,17136140)),
                       (F(5),(3,4),F(-701357055435,35412335776468))):
    assert evalp(P[entry[0]][entry[1]],t)/ (4*evalp(D,t))==target

# The checked algebra proves nonnegativity precisely at h=0 or
# alpha <= h <= beta, alpha=unique positive root FAR,
# beta=unique positive root MIDDLE.
print('VERIFY_OK exact_polynomial_identities=64 sign_pattern_entries=60 '
      'all_positive=%d single_upper_root=%d '
      'lower_bracket=(3/10,1/3) upper_bracket=(4,9/2)' %
      (counts['all_positive'],counts['single_upper_root']))
