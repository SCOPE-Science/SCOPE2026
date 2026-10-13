"""Reproduce exact finite-dimensional identities supporting the stated theorem.
Use: python check.py (requires SymPy >=1.12)."""
import sympy as s

def mats(N, k, delta):
    m=N-1
    L=s.zeros(N)
    for r in range(N):
        L[r,r]=s.Rational(m,2)-r
        if r<m:
            a=s.sqrt((r+1)*(m-r))/2
            L[r,r+1]=a
            L[r+1,r]=-a
    K=s.diag(*[k-delta*L[r,r] for r in range(N)])
    A=-k*s.eye(N)+delta*L
    S=(L-L.T)/2
    return L,K,A,S

for N in range(2,9):
    m=N-1
    k=s.Rational(m+3,2)
    delta=s.Integer(1)
    L,K,A,S=mats(N,k,delta)
    T=A+k*s.eye(N)
    assert T**N==s.zeros(N)
    assert T**(N-1)!=s.zeros(N)
    assert K==s.diag(*[k-(s.Rational(m,2)-r) for r in range(N)])
    assert A+A.T+2*K==s.zeros(N)
    assert s.simplify((delta*S).T*K.inv()*(delta*S)).is_symmetric()
    for u in [s.Rational(1,3),s.Integer(1),s.Rational(3,2),s.Integer(2)]:
        vec=s.zeros(N,1);vec[N-1]=1
        E=sum(((u*L)**j/s.factorial(j) for j in range(N)),s.zeros(N))
        v=E*vec
        rhs=(u*u/4+(1-u/2)**2)**m
        assert s.simplify((v.T*v)[0]-rhs)==0,(N,u,s.simplify((v.T*v)[0]-rhs))
    entropy=s.simplify(s.trace((delta*S).T*K.inv()*(delta*S)))
    stated=sum(s.Rational(i*(N-i),4)*(1/K[i-1,i-1]+1/K[i,i]) for i in range(1,N))
    assert s.simplify(entropy-stated)==0,(N,entropy,stated)
    print('N',N,'nilpotent Jordan order',N,'diagonal diffusion positive','exact norm four times','entropy',entropy)
print('VERIFY_OK')
