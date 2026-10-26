import math,itertools,numpy as np

def moments(n, exps):
    # normalized surface measure, and positive orthant only
    exps=np.array(exps,dtype=float)
    return math.exp(-n*math.log(2)+math.lgamma(n/2)-math.lgamma((n+sum(exps))/2)+sum(math.lgamma((e+1)/2)-math.lgamma(.5) for e in exps))

def matrix(n):
    # independent traceless diagonal orthonormal vectors in R^n
    Z=np.eye(n)[:,:n-1]-np.eye(n)[:,-1:]
    V=np.linalg.qr(Z)[0][:,:n-1]
    T=math.sqrt(n*(n+2)/2)
    S=math.sqrt(n*(n+2))
    basis=[]
    for j in range(n-1):
        basis.append([(T*V[i,j], (i,i)) for i in range(n)])
    edges=list(itertools.combinations(range(n),2))
    for i,j in edges: basis.append([(S,(i,j))])
    mat=np.zeros((len(basis),len(basis)))
    for p in range(len(basis)):
       for q in range(p+1):
         z=0
         for c,ij in basis[p]:
           for d,kl in basis[q]:
             es=[0]*n
             for idx in (*ij,*kl):es[idx]+=1
             z+=c*d*moments(n,es)
         mat[p,q]=mat[q,p]=z
    return mat

def expected(n):
  x=2/math.pi
  t=1+2*(n-2)*x+ (n-2)*(n-3)/2*x*x
  a=1+(n-4)*x-(n-3)*x*x
  b=math.sqrt((n-2)/2)*x
  r=math.hypot((1-a)/2,b)
  u=(1+a)/2+r; l=(1+a)/2-r
  e=(1-x)**2
  return np.array(sorted(([t]+[u]*(n-1)+[l]*(n-1)+([e]*(n*(n-3)//2) if n>=4 else []))))/2**n
for n in range(3,11):
 M=matrix(n); actual=np.linalg.eigvalsh(M); pred=expected(n)
 print(n,len(actual),round(actual.max(),12),round(max(abs(actual-pred)),12),'trace',round(np.trace(M),12),'expected trace', round(((n+2)*(n-1)/2)/2**n,12))
 assert len(actual)==len(pred)
 assert np.max(abs(actual-pred))<1e-11
 assert abs(np.trace(M)-((n+2)*(n-1)/2)/2**n)<1e-11
 print('condition',actual.max()/actual.min())

# Quadrature of spherical octant in dimension three, without the gamma moment formula.
from numpy.polynomial.legendre import leggauss
nodes,weights=leggauss(110)
theta=(nodes+1)*(math.pi/4)
phi=(nodes+1)*(math.pi/4)
th_w=weights*math.pi/4
ph_w=weights*math.pi/4
num=np.zeros((5,5),dtype=float)
for i,th in enumerate(theta):
    for j,ph in enumerate(phi):
        x=np.array([math.sin(th)*math.cos(ph),math.sin(th)*math.sin(ph),math.cos(th)])
        vals=np.array([math.sqrt(15)/2*(x[0]**2-x[1]**2),
                      math.sqrt(5)/2*(x[0]**2+x[1]**2-2*x[2]**2),
                      math.sqrt(15)*x[0]*x[1],math.sqrt(15)*x[0]*x[2],math.sqrt(15)*x[1]*x[2]])
        num+=th_w[i]*ph_w[j]*math.sin(th)/(4*math.pi)*np.outer(vals,vals)
# Direct monomial matrix is independent of the particular diagonal basis.
mu=np.linalg.eigvalsh(num)
assert np.max(np.abs(mu-expected(3))) < 1.e-12
print('Octant Gauss-Legendre quadrature: five eigenvalues within 1e-12')

import sympy as sp
N,s=sp.symbols('N s',integer=True)
T=1+2*(N-2)*s+((N-2)*(N-3)/2)*s*s
A=1+(N-4)*s-(N-3)*s*s
B2=(N-2)*s*s/2
E=(1-s)**2
assert sp.simplify(T-A-N*s-N*(N-3)*s*s/2)==0
assert sp.simplify((1-E)*(A-E)-B2 - (N-2)*s*s*(2*s*s-6*s+3)/2)==0
assert sp.simplify(T+(N-1)*(1+A)+(N*(N-3)/2)*E - ((N-1)*(N+2))/2)==0
print('Three exact symbolic spectral and trace identities verified')
print('All independent checks passed.')

rng=np.random.default_rng(20261020)
for n in range(3,11):
    gram=matrix(n)
    edge_count=n*(n-1)//2
    top=np.zeros(gram.shape[0],dtype=complex)
    top[-edge_count:]=1/math.sqrt(edge_count)
    top_eigen=expected(n)[-1]
    assert np.linalg.norm(gram@top-top_eigen*top) < 2e-11
    second=expected(n)[-(n)]  # the second-highest branch
    for _ in range(100):
        z=rng.normal(size=gram.shape[0])+1j*rng.normal(size=gram.shape[0])
        excess=top_eigen*np.vdot(z,z).real-np.vdot(z,gram@z).real
        off=z-np.vdot(top,z)*top
        assert excess+1e-10 >= (top_eigen-second)*np.vdot(off,off).real
print('Top zonal eigendirection and sharp gap: 800 randomized tests passed')
