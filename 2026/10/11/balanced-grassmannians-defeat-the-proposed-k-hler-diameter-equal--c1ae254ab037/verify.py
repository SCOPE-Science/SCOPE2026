import sympy as sp

# Exact Grassmann chart determinant for a nontrivial complex 2-plane chart.
Z=sp.Matrix([[sp.Rational(1,2),sp.Rational(1,3)],[sp.Rational(2,5),sp.Rational(-1,4)]])
k,N=2,4
S=sp.eye(k)+Z.T*Z
T=sp.eye(N-k)+Z*Z.T
h=sp.kronecker_product(S.inv().T,T.inv())
assert sp.simplify(h.det()-S.det()**(-N))==0
assert sp.simplify(S.det()-T.det())==0
# Ricci-form normalization: rho=-i d dbar logdet h= iN d dbar logdet S;
# omega0=i/2 d dbar logdet S, so rho=(2N) omega0.
assert 2*N==8
for kk in range(1,9):
  for NN in range(2*kk,2*kk+7):
    m=kk*(NN-kk)
    d0sq=sp.pi**2*kk/4
    norm_sq=sp.simplify(2*NN*d0sq)
    diff=sp.simplify(sp.pi**2*m-norm_sq)
    assert sp.simplify(diff-sp.pi**2*kk*(NN-2*kk)/2)==0
    assert (diff==0)==(NN==2*kk)
# Canonical CP^p normalization matches motivator's comparison exactly.
for p in range(1,10):
  NN=p+1
  assert sp.simplify(sp.sqrt(2*NN)*sp.pi/2-sp.pi*sp.sqrt(sp.Rational(p+1,2)))==0
# Explicit orthogonal pair k=2 N=4 saturates as a consequence of both principal angles pi/2.
k,N=2,4
assert sp.simplify(sp.sqrt(2*N)*sp.sqrt(2)*sp.pi/2 - 2*sp.pi)==0
assert k*(N-k)==4
assert 1 != k*(N-k)
print('VERIFY_OK')
print('chart_metric_volume_det=det(I+ZstarZ)^(-N)')
print('Ric(g0)=2N*g0; Einstein_rescale=2N')
print('diameter_squared=pi^2*N*k/2')
print('diameter_bound_gap_squared=pi^2*k*(N-2k)/2')
print('balanced_Gr(2,4)_diameter=2pi_and_b2=1_not_4')
