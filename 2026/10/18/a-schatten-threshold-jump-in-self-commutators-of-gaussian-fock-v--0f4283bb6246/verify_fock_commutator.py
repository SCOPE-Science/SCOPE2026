"""Finite-matrix and exact-coefficient checks for Fock Volterra self-commutators."""
import cmath, math
import numpy as np
from fractions import Fraction

# t_n = b/sqrt(n+1), s_n = 2a*sqrt((n+1)/(n+2)).
def derived_entry(a,b,i,j):
    A,B=abs(a)**2,abs(b)**2
    if i == j:
        if i==0: return (2*A+B)
        if i==1: return (8*A/3-B/2)
        return 8*A/(i*(i+2))-B/(i*(i+1))
    if j == i+1:
        if i==0: return np.conjugate(a)*b
        return -2*np.conjugate(a)*b/((i+2)*math.sqrt(i+1))
    if i == j+1: return np.conjugate(derived_entry(a,b,j,i))
    return 0j

def matrix(a,b,N):
    T=np.zeros((N+3,N+3),dtype=complex)
    for k in range(N+1):
        T[k+1,k]=b/math.sqrt(k+1)
        T[k+2,k]=2*a*math.sqrt((k+1)/(k+2))
    H=T.conj().T@T-T@T.conj().T
    return H[:N+1,:N+1]

def tests():
    count=0
    for N in range(1,26):
        for a,b in ((1.0,0.0),(0.0,2.0),(1.0,1.0),(1.0+0.7j,-0.3+2j)):
            H=matrix(a,b,N)
            M=np.array([[derived_entry(a,b,i,j) for j in range(N+1)] for i in range(N+1)])
            assert np.max(np.abs(H-M)) < 3e-13,(N,a,b,np.max(np.abs(H-M)))
            count+=1
    for N in (20,50,100,250):
        H=matrix(1.0,1.0,N)
        eigen=np.linalg.eigvalsh(H)
        assert np.sum(eigen>1e-8)>=4 and np.sum(eigen< -1e-8)>=4
        count+=1
        dsum=np.trace(H).real
        target= (abs(1.0)**2) * (4*(N+1)/(N+2) + 4*N/(N+1)) + 1/(N+1)
        assert abs(dsum-target)<1e-9,(dsum,target)
        count+=1
    # Verify exact rational diagonal/telescoping identities, independently of sqrt arithmetic.
    for N in range(1,151):
        q=Fraction(0)
        for n in range(N+1):
            if n==0: dn=Fraction(2)+1
            elif n==1:dn=Fraction(8,3)-Fraction(1,2)
            else:dn=Fraction(8,n*(n+2))-Fraction(1,n*(n+1))
            q+=dn
        rhs = Fraction(1,N+1)+Fraction(4*(N+1),N+2)+Fraction(4*N,N+1)
        assert q==rhs,(N,q,rhs)
        count+=1
    print('PASS',count,'matrix, inertia and rational-trace checks')

if __name__=='__main__': tests()
