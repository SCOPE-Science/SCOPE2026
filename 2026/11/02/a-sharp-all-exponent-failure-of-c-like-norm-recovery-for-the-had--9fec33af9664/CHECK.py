"""Standalone supplementary finite checks for a two-projection matrix-norm theorem."""
from fractions import Fraction
from math import isclose
I=((1,0),(0,1))
J=((0,1),(1,0))
P=((Fraction(1,2),Fraction(1,2)),(Fraction(1,2),Fraction(1,2)))
Q=((Fraction(1,2),-Fraction(1,2)),(-Fraction(1,2),Fraction(1,2)))
def prod(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def add(A,B): return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
assert prod(P,P)==P and prod(Q,Q)==Q
assert prod(P,Q)==((0,0),(0,0)) and prod(Q,P)==((0,0),(0,0))
assert add(P,Q)==I
# At p=1, the 4x2 column (P;Q) has two columns of absolute sum 2.
assert all(sum(abs(B[i][j]) for B in (P,Q) for i in range(2))==2 for j in range(2))
# The 2x4 row (P,Q) has four columns each of absolute sum 1.
assert all(sum(abs(B[i][j]) for i in range(2))==1 for B in (P,Q) for j in range(2))
# The phase multiplier P+iQ has exactly flat entries and H*H=I.
H=[[complex(P[i][j])+1j*complex(Q[i][j]) for j in range(2)] for i in range(2)]
assert all(isclose(abs(H[i][j]),2**-0.5,abs_tol=1e-12) for i in range(2) for j in range(2))
for i in range(2):
 for j in range(2):
  z=sum(H[k][i].conjugate()*H[k][j] for k in range(2))
  assert abs(z-(1 if i==j else 0))<1e-12
# One coordinate tests attain the exact column and phase-multiplier estimates.
for p in (1.,1.25,1.5,1.75,2.,3.,4.,8.):
    endpoint=2**(2/p-1) if p<=2 else 2**(1-2/p)
    pairing=2**(abs(1/p-0.5))
    if p!=2: assert endpoint>pairing>0
    else: assert endpoint==pairing==1
    if p<=2:
      xnorm=(sum(abs(B[i][0])**p for B in (P,Q) for i in range(2)))**(1/p)
      hnorm=(sum(abs(H[i][0])**p for i in range(2)))**(1/p)
      assert isclose(xnorm,endpoint,rel_tol=1e-12)
      assert isclose(hnorm,pairing,rel_tol=1e-12)
    else:
      # Dual exponent has the same sharp operator norm as the adjoint.
      pp=p/(p-1)
      assert isclose(2**(1/pp-0.5),pairing,rel_tol=1e-12)
print('Finite projection identities and sample-exponent checks passed.')
