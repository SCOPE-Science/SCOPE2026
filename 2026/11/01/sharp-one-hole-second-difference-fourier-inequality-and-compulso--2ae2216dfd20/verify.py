from sympy import Matrix, eye, Rational, binomial, simplify

def H(n):
    return Matrix(n,n,lambda i,j: {0:6,1:-4,2:1}.get(abs(i-j),0))

def exact(n):
    A=H(n); G=A.inv(); U=Matrix([Rational(j*(j+1)*(n+1-j)*(n+2-j),24) for j in range(1,n+1)])
    V=Matrix([Rational(j*(j+1)*(n+1-j),(n+2)*(n+3)) for j in range(1,n+1)])
    e=eye(n)[:,n-1]
    assert A*U == Matrix.ones(n,1)
    assert A*V == e
    assert all(G[i,j]>0 for i in range(n) for j in range(n))
    assert sum(U)==binomial(n+4,5)/6
    assert U[n-1]==Rational(n*(n+1),12)
    return G

for n in range(1,19): exact(n)
for l in range(1,9):
 for r in range(1,9):
    n=l+r
    A=Matrix.zeros(n,n);A[:l,:l]=H(l);A[l:,l:]=H(r);A[l-1,l]=A[l,l-1]=-1
    sig=Matrix.ones(n,1)
    C2=(sig.T*A.inv()*sig)[0]
    p=lambda k:Rational(k*(k+1),(k+2)*(k+3))
    t=lambda k:Rational(k*(k+1),12)
    S=lambda k:binomial(k+4,5)/6
    claimed=S(l)+S(r)+(p(r)*t(l)**2+p(l)*t(r)**2+2*t(l)*t(r))/(1-p(l)*p(r))
    assert simplify(C2-claimed)==0, (l,r,C2,claimed)
    y=A.inv()*sig
    assert all(z>0 for z in y)
print('PASS: 18 exact inverse/Green checks and 64 exact two-block sharp constant and sign checks')
for l,r in [(1,1),(2,2),(3,4)]:
 n=l+r;A=Matrix.zeros(n,n);A[:l,:l]=H(l);A[l:,l:]=H(r);A[l-1,l]=A[l,l-1]=-1
 print((l,r),(Matrix.ones(n,1).T*A.inv()*Matrix.ones(n,1))[0])
