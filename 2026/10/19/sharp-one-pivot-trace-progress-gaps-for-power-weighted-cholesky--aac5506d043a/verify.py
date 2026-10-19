"""Exact-rational checks for first-pivot trace-gain comparisons.

This program is ancillary: the proofs in RESULT.md cover all dimensions
and all exponents; finite checks alone do not establish universality.
"""
from fractions import Fraction as F
from math import isqrt


def gains(A):
    n = len(A)
    assert all(len(row)==n for row in A)
    d = [A[i][i] for i in range(n)]
    assert all(x > 0 for x in d)
    return [sum(A[j][i] * A[j][i] for j in range(n)) / d[i] for i in range(n)]


def gain_for_powers(A, beta):
    d=[A[i][i] for i in range(len(A))]
    g=gains(A)
    weights=[z**beta for z in d]
    return sum((w*x for w,x in zip(weights,g)),F(0)) / sum(weights)


def block(r, N, t):
    # Gram matrix of N parallel equal rows and r-1 orthogonal singleton rows
    size=N+r-1
    return [[F(1,N) if i<N and j<N else
             (t if i==j and i>=N else F(0))
             for j in range(size)] for i in range(size)]


def family_analytic(r,N,t):
    u=F(N+(r-1)*t, N+r-1)
    p=(1+(r-1)*t*t)/(1+(r-1)*t)
    return u,p


# The smallest explicit reversal is dimension 3, rank 2.
A=block(2,2,F(2,3))
u=gain_for_powers(A,0)
p=gain_for_powers(A,1)
assert (u,p,u/p)==(F(8,9),F(13,15),F(40,39))
print('three-by-three PSD reversal:', 'uniform',u,'diagonal',p,'ratio',u/p)

# Two-by-two positive semidefinite matrices cannot reverse this ordering.
count2=0
for a in range(1,11):
 for b in range(1,11):
  for c in range(-10,11):
   if c*c>a*b: continue
   B=[[F(a),F(c)],[F(c),F(b)]]
   uu=gain_for_powers(B,0)
   pp=gain_for_powers(B,1)
   difference=F((a-b)**2,2*(a+b))*(1-F(c*c,a*b))
   assert pp-uu==difference>=0
   count2+=1
print('2x2 exact PSD instances:',count2)

# Build the complete matrix in small examples to verify the symbolic family formula.
count_family=0
for r in range(2,6):
 for N in range(1,12):
  for t in (F(1,5),F(2,3),F(1),F(3,2)):
   B=block(r,N,t)
   uu,pp=family_analytic(r,N,t)
   assert (gain_for_powers(B,0),gain_for_powers(B,1))==(uu,pp)
   count_family+=1
print('exact constructed family matrices:',count_family)

# The sharp envelope along perfect-square ranks is approached as N increases.
for s in range(2,8):
 r=s*s
 t=F(1,s+1)
 sharp=F(s+1,2)
 previous=F(0)
 for N in (100,1000,10000,100000):
  uu,pp=family_analytic(r,N,t)
  ratio=uu/pp
  assert previous<ratio<sharp
  previous=ratio
 assert sharp-previous<F(5*r,100000)
 print('rank',r,'exact sharp constant',sharp,'finite ratio at N=100000',float(previous))

# For beta > 1, fixed rank two admits arbitrary loss vs uniform.
for beta in (2,3,4):
 for W in (3,8,20,100):
  N=W**(beta+2)
  topmass=F(W**beta,N**(beta-1))
  delta_u=F(N*W+1,N+1)
  delta_beta=(topmass*W+1)/(topmass+1)
  assert delta_u/delta_beta>F(W,3)
  if beta==2 and W==100:
   print('beta=2, W=100:', 'uniform',float(delta_u),
         'beta-weighted',float(delta_beta),
         'ratio',float(delta_u/delta_beta))
print('all rational identities and strict inequalities passed')
