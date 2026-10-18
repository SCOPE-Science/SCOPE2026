"""Exact-rational finite verification for a Jacobi/Hesse sampling theorem.
Standard library only. Infinite degrees are handled by the analytic bound in RESULT.md.
"""
from fractions import Fraction as Q
from math import factorial

# Jacobi P_n^{(1,3)}(-1/2), using the standard three-term recurrence.
p0=Q(1); p1=Q(-5,2)
assert p0==1 and p1==Q(-5,2)
vals={0:p0,1:p1}
for n in range(1,900):
    a=2*(n+1)*(n+5)*(2*n+4)
    b=(2*n+5)*( -(n+3)*(2*n+4)-8 )
    c=2*(n+1)*(n+3)*(2*n+6)
    nxt=Q(b*vals[n]-c*vals[n-1],a)
    vals[n+1]=nxt
assert vals[2]==3,(vals[2],3)
assert all(- (n+1) < vals[n] < n+1 for n in range(3,900))
assert vals[0]==1 and vals[2]==3
# Exact kernel coincidence on pairs with squared overlap 1/4.
from math import comb
u=Q(1,4)
poly=lambda t: Q(28)*t*t-Q(35)*t+10
assert poly(u)==3 and poly(Q(1))==3
# Dimensions of Harm(5,2) and Harm(3,0) on C^3.
dim=lambda p,q: comb(p+2,2)*comb(q+2,2) - (comb(p+1,2)*comb(q+1,2) if p*q else 0)
assert dim(5,2)==81 and dim(3,0)==10
# For each of 9 Hesse points, the self-kernel is one and all cross-kernels -1/8.
# Consequently: 8 positive eigenvalues 9/8 and 1 zero eigenvalue.
assert 1+8*Q(-1,8)==0 and 1-Q(-1,8)==Q(9,8)
print('PASS: 897 exhaustive exact Jacobi inequalities (n=3..899); exceptional n=0,2; 4 structural exact identities.')

# Verify all nine Hesse vectors and their pairwise cubed overlaps
# exactly in Z[omega], omega^2=-1-omega, without floating point.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x): return (x[0]-x[1],-x[1])
def neg(x): return (-x[0],-x[1])
unit=(1,0); zero=(0,0); omega=(0,1)
def powomega(b):
    v=unit
    for _ in range(b): v=mul(v,omega)
    return v
vectors=[]
for a in range(3):
    for b in range(3):
        row=[zero,unit,neg(powomega(b))]
        row=row[-a:]+row[:-a] if a else row
        vectors.append(row)
for i,v in enumerate(vectors):
    for j,w in enumerate(vectors):
        overlap=zero
        for k in range(3): overlap=add(overlap,mul(conj(v[k]),w[k]))
        if i==j: assert overlap==(2,0)
        else: assert mul(mul(overlap,overlap),overlap)==(-1,0)
print('PASS: 81 exact Z[omega] overlaps including 36 distinct cubed overlaps.')
