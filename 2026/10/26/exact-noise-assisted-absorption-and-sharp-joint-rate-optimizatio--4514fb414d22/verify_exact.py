import sympy as s

def exact(m,J,k,gL,gH):
  N=m+1
  H=s.zeros(N)
  for i in range(1,N):H[0,i]=J;H[i,0]=J
  E=lambda a,b:s.eye(N)[:,a]*s.eye(N)[:,b].T
  basis=[E(a,b) for b in range(N) for a in range(N)]
  def gen(X):
    ans=-s.I*(H*X-X*H)-k*s.Rational(1,2)*(E(0,0)*X+X*E(0,0))
    for i,r in enumerate([gH]+[gL]*m):
      P=E(i,i)
      ans+=r*(P*X*P-s.Rational(1,2)*(P*X+X*P))
    return ans
  L=s.Matrix.hstack(*[s.Matrix(gen(x)).reshape(N*N,1) for x in basis])
  # sympy row-major flatten differs column-major generator columns. Map directly using row-major basis.
  basis=[E(a,b) for a in range(N) for b in range(N)]
  L=s.Matrix.hstack(*[s.Matrix(gen(x)).reshape(N*N,1) for x in basis])
  initial=s.Matrix(E(1,1)).reshape(N*N,1)
  sol=(-L).inv()*initial
  return s.simplify(sum(sol[i*N+i] for i in range(N)))

for m in (2,3,4):
 for J,k,gL,gH in [(s.Rational(3,2),s.Rational(5,3),s.Rational(7,4),s.Rational(2,5)),(s.Rational(1),s.Rational(2),s.Rational(3),s.Rational(0))]:
  v=exact(m,J,k,gL,gH)
  f=(m+1)/k+(m-1)/gL+(k+gL+gH)/(4*J**2)
  assert s.simplify(v-f)==0,(m,v,f)
 print('exact symbolic rational PASS m',m)
