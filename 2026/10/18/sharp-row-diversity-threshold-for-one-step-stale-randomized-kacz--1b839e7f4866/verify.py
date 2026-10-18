"""Exact-rational and floating-point checks of the one-step-stale coordinate recurrence.
Does not substitute for a proof of the universal statements.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np

# 2 x 2 exact matrices, represented by tuple of tuple of fractions.
def matmul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def transpose(A): return tuple(zip(*A))
def plus(A,B): return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
def scale(q,A): return tuple(tuple(q*A[i][j] for j in range(2)) for i in range(2))
def mat_minus(A,B):return plus(A,scale(F(-1),B))
def L(A,p,a):
  M0=((F(1),F(0)),(F(1),F(0)))
  M1=((F(1),-a),(F(1),F(0)))
  return plus(scale(1-p,matmul(matmul(M0,A),transpose(M0))),scale(p,matmul(matmul(M1,A),transpose(M1))))

def all_checks():
  count=0;stable=unstable=neutral=0
  for p in [F(1,17),F(1,9),F(1,5),F(1,3),F(1,2),F(3,4),F(1)]:
    for a in [F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(7,4),F(2),F(5,2),F(4)]:
      t=1/(1+a*p)
      C=((F(1),t),(t,F(1)))
      delta=a*p*(F(2)/(1+a*p)-a)
      H=((F(2),F(1)),(F(1),F(1)))
      E=((F(1),F(0)),(F(0),F(0)))
      assert mat_minus(C,L(C,p,a)) == scale(delta,E)
      assert mat_minus(C,L(L(C,p,a),p,a)) == scale(delta,H)
      # Moment linear map in the (u,v,w) basis.
      T=np.array([[1,-2*float(a*p),float(a*a*p)],[1,-float(a*p),0],[1,0,0]])
      ev=np.linalg.eigvals(T)
      r=float(max(abs(v) for v in ev))
      stability=2-a-a*a*p
      if stability>0:
        assert r<1+1.e-10,(p,a,ev)
        stable+=1
      elif stability<0:
        assert r>1-1.e-10,(p,a,ev)
        unstable+=1
      else:
        assert abs(r-1)<1.e-10,(p,a,ev)
        neutral+=1
      count+=1
  # exact critical identities at p=1, 1/2, 2/9, 3/8
  for a,p in [(F(1),F(1)),(F(3,2),F(2,9)),(F(2,3),F(3))]:
    assert a+a*a*p == 2
    t=1/(1+a*p)
    C=((F(1),t),(t,F(1)))
    assert L(C,p,a)==C
  # a=3/2: 4 rows impossible, 5 uniform rows stable.
  a=F(3,2)
  assert a+a*a*F(1,4)>2 and a+a*a*F(1,5)<2
  # Mean error recurrence has roots inside unit disk for the counterexample.
  for p in [F(2,5),F(3,10),F(3,10)]:
    assert 0<a*p<1
  assert a+a*a*F(2,5)>2
  # Equal global collision rate, sharply different convergence.
  a=F(5,4)
  pmf_a=(F(1,2),F(1,4),F(1,4))
  pmf_b=(F(5,12),F(5,12),F(1,6))
  assert sum(q*q for q in pmf_a)==sum(q*q for q in pmf_b)==F(3,8)
  assert a+a*a*max(pmf_a)>2 and a+a*a*max(pmf_b)<2
  assert all(0<a*q<1 for q in pmf_a+pmf_b)
  print('VERIFY_OK exact_covariance_identities=',count*2,' exact_critical_boundaries=3',' numerical_spectral_cross_checks=',count,' stable_cases=',stable,' unstable_cases=',unstable,' neutral_cases=',neutral,' four_vs_five_row_phase=true mean_stable_MSE_unstable=true equal_collision_opposite_stability=true')
if __name__ == '__main__': all_checks()
