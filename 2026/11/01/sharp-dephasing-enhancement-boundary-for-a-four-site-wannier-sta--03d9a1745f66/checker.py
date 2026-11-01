#!/usr/bin/env python3
"""Exact algebraic checks for four-site boundary-driven tilted XX transport.

Requires Python 3, sympy and numpy.  All positivity certificates use integer
polynomial coefficients, not floating-point root searches.
"""
import sympy as sp
import numpy as np

G, g, U, z = sp.symbols('G g U z', real=True)

A = G**2 + 6*G*g + 8*g**2 + 16
B = G**3 + 18*G**2*g + 80*G*g**2 + 160*G + 96*g**3 + 480*g
C = G**3*g + 10*G**2*g**2 + 8*G**2 + 32*G*g**3 + 80*G*g + 32*g**4 + 160*g**2
D = 25*G**3 + 436*G**2*g + 1840*G*g**2 + 912*G + 2496*g**3 + 576*g
E = 25*G**2*g + 136*G*g**2 + 72*G + 208*g**3 + 48*g
P = sp.expand(A*B + 4*z*D + 2304*z**2*(G+12*g))
Q = sp.expand(A*C + 4*z*(G+4*g)*E + 2304*z**2*g*(G+4*g))
R = (16+G**2+6*G*g)/(16*G)+z*P/(8*Q)

Phi = (
    5308416*z**5
    +(3538944+460800*G**2)*z**4
    +(9547776+513024*G**2+14608*G**4)*z**3
    +(5603328+157696*G**2+16128*G**4+200*G**6)*z**2
    +(2293760+90112*G**2-1536*G**4+128*G**6+G**8)*z
    -49152*G**2-6144*G**4-192*G**6
)

def current_from_source_equations(n):
    """Independently solve the exact stationary Pauli-string recurrences.

    The current at unit positive boundary bias is four times b_1^(2),
    with hopping and Planck constant both equal to one.
    """
    ids=[]
    for r in range(1,n+1):
        for j in range(1,n-r+2):
            ids.append(('h',r,j))
            if r>=2: ids.append(('b',r,j))
    unknowns=sp.symbols('v:'+str(len(ids)))
    v=dict(zip(ids,unknowns))
    def q(t,r,j): return v.get((t,r,j),sp.S.Zero)
    eqs=[G*(1+q('h',1,1))-4*q('b',2,1),
         G*(1-q('h',1,n))-4*q('b',2,n-1)]
    eqs.extend(q('b',2,j)-q('b',2,j-1) for j in range(2,n))
    for r in range(2,n+1):
        for j in range(1,n-r+2):
            tilt=U*(r-1)
            boundary=G*(int(j==1)+int(j+r-1==n))/4
            eqs.append(q('h',r-1,j)-q('h',r-1,j+1)
                +q('h',r+1,j)-q('h',r+1,j-1)
                +tilt*q('h',r,j)+(g+boundary)*q('b',r,j))
            eqs.append(q('b',r-1,j)-q('b',r-1,j+1)
                +q('b',r+1,j)-q('b',r+1,j-1)
                +tilt*q('b',r,j)-(g+boundary)*q('h',r,j))
    assert len(eqs)==len(unknowns)==n*n
    matrix,rhs=sp.linear_eq_to_matrix(eqs,unknowns)
    values=matrix.inv()*rhs
    return sp.factor(4*values[ids.index(('b',2,1))])

# Known 2- and 3-site identities provide normalization checks.
J2=current_from_source_equations(2)
J3=current_from_source_equations(3)
assert sp.cancel(J2-16*G*(2*g+G)/(16*(2*g+G)+4*G*U**2+G*(2*g+G)**2))==0
assert sp.cancel(J3-16*G*(4*g+G)/(16*(4*g+G)+16*G*U**2+G*(4*g+G)**2))==0

# The 4-site exact current agrees identically with the compact resistance.
J4=current_from_source_equations(4)
assert sp.cancel(J4-1/R.subs(z,U**2))==0

# Strict complete coefficient certificates for positivity and convexity.
W1=sp.Poly(sp.expand(P*sp.diff(Q,g)-sp.diff(P,g)*Q),G,g,z)
W2=sp.Poly(sp.expand(sp.diff(P,g,2)*Q**2-P*sp.diff(Q,g,2)*Q
       -2*sp.diff(P,g)*sp.diff(Q,g)*Q+2*P*sp.diff(Q,g)**2),G,g,z)
assert len(W1.terms())==85 and all(c>0 for c in W1.coeffs())
assert len(W2.terms())==224 and all(c>0 for c in W2.coeffs())
assert min(W1.coeffs())==1 and min(W2.coeffs())==2

# The onset polynomial is the complete derivative-at-zero numerator.
Q0=Q.subs(g,0)
assert sp.expand(-3*Q0**2 + z*W1.as_expr().subs(g,0)-G**2*Phi)==0
phi_z=sp.Poly(Phi,z)
assert all(c>0 for c in phi_z.all_coeffs()[:-1] if c!=phi_z.nth(1))
assert sp.factor(phi_z.nth(1)-(G**8+128*G**2*((G**2-6)**2+668)+2293760))==0
assert sp.expand(phi_z.nth(0)+192*G**2*(G**4+32*G**2+256))==0

# Independent numerical one-body covariance equation for the same model.
def independent_current(gg,uu,dd):
    n=4
    H=np.diag([-2*j*uu for j in range(n)]).astype(complex)
    for j in range(n-1): H[j,j+1]=H[j+1,j]=2
    basis=[]
    for j in range(n):
        Bm=np.zeros((n,n),complex);Bm[j,j]=1;basis.append(Bm)
    for j in range(n):
        for k in range(j+1,n):
            Bm=np.zeros((n,n),complex);Bm[j,k]=Bm[k,j]=1;basis.append(Bm)
            Bm=np.zeros((n,n),complex);Bm[j,k]=1j;Bm[k,j]=-1j;basis.append(Bm)
    def vec(M):
        return np.array([M[j,j].real for j in range(n)]
            +[t for j in range(n) for k in range(j+1,n)
              for t in (M[j,k].real,M[j,k].imag)],float)
    def op(M):
        K=-1j*(H@M-M@H)
        for j in range(n):
            for k in range(n):
                if j!=k:K[j,k]-=(2*dd+gg*((j in (0,n-1))+(k in (0,n-1)))/2)*M[j,k]
                elif j in (0,n-1):K[j,j]-=gg*M[j,j]
        return K
    matrix=np.stack([vec(op(Bm)) for Bm in basis],axis=1)
    src=np.zeros((n,n),complex);src[0,0]=gg/2;src[-1,-1]=-gg/2
    v=np.linalg.solve(matrix,-vec(src))
    return gg*(1-2*v[0])

Jfun=sp.lambdify((G,U,g),J4,modules='numpy')
for gg in (0.05,0.3,1,4,20):
    for uu in (0,0.01,0.15,0.5,2,10):
        for dd in (0,0.02,0.2,1,10):
            direct=independent_current(gg,uu,dd)
            exact=float(Jfun(gg,uu,dd))
            assert abs(direct-exact)<4e-9*max(1,abs(exact)),(gg,uu,dd,direct,exact)

print('PASS: exact L=2/3 baselines and L=4 stationary recurrence identity')
print('PASS: 85 positive coefficients for -F_prime and 224 for F_double_prime')
print('PASS: complete zero-dephasing threshold polynomial identity')
print('PASS: 150 independent direct covariance matrix comparisons')
