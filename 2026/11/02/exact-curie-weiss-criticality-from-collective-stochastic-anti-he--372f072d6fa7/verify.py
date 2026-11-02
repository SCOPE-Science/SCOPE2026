"""Independent finite-size calculations for collective anti-Hermitian noise and Curie--Weiss output.
Only numpy/scipy are used. Run: python verify.py.
"""
import math
import numpy as np
from scipy.special import logsumexp, gammaln, roots_hermitenorm, gamma
from scipy.optimize import brentq

checks=0

def chk(condition,label):
    global checks
    assert condition,label
    checks+=1

def binomial_moments(N,t):
    k=np.arange(N+1)
    M=2*k-N
    logw=gammaln(N+1)-gammaln(k+1)-gammaln(N-k+1)+t*M*M/(2*N)
    p=np.exp(logw-logsumexp(logw))
    return np.dot(p,M)/N,np.dot(p,M*M)/(N*N),(np.dot(p,M*M)-N)/(N*(N-1)) if N>1 else np.nan

def oscillator_matrix(N,t):
    configurations=np.arange(2**N)
    k=np.asarray([int(z).bit_count() for z in configurations])
    S=k[:,None]+k[None,:]
    mat=2.**(-N)*np.exp(t*(-S+S*S/(2*N)))
    return mat/np.trace(mat),k

def gauss_density_matrix(N,t,order=200):
    # Gaussian integration over shared noise in y: N(0,t/N)
    x,w=roots_hermitenorm(order)
    y=np.sqrt(t/N)*x
    configs=np.arange(2**N)
    M=np.asarray([2*int(z).bit_count()-N for z in configs])
    K=np.exp(np.outer(y,M)/2)*2.**(-N/2)
    mat=np.einsum('i,ij,ik->jk',w,K,K,optimize=True)/np.sqrt(2*np.pi)
    return mat/np.trace(mat)

for N in [2,3,4,5]:
  for t in [0.15,0.75,1.0,1.75,3.0]:
    mat,k=oscillator_matrix(N,t)
    alt=gauss_density_matrix(N,t)
    chk(np.max(np.abs(mat-alt))<3e-11,f'Gaussian kernel vs semigroup N={N} t={t}')
    chk(np.min(np.linalg.eigvalsh(mat))>-5e-12,f'positivity N={N} t={t}')
    chk(abs(np.trace(mat)-1)<1e-12,f'trace N={N} t={t}')
    M=2*k-N
    logwt=t*M*M/(2*N)
    diagonal=np.exp(logwt-logsumexp(logwt))
    chk(np.max(abs(np.diag(mat)-diagonal))<1e-12,f'exact Curie Weiss N={N} t={t}')
    chk(abs(np.sum(np.diag(mat)*M))<1e-12,f'global inversion N={N} t={t}')
    # The unnormalized trace cannot exceed the initial unit trace
    trace_orig=np.sum(2.**(-N)*np.exp(-2*k*t+(2*t/N)*k*k))
    chk(0<trace_orig<=1+1e-12,f'physical trace decrease N={N} t={t}')

# Critical magnetization fluctuation: N^{1/4} m distribution tends to exp(-x^4/12).
const=math.sqrt(12)*gamma(0.75)/gamma(0.25)
for N in [200,800,3200,12800]:
    mean,m2,corr=binomial_moments(N,1)
    chk(abs(mean)<2e-11,f'zero first moment at criticality N={N}')
    chk(abs(math.sqrt(N)*m2-const)<1.0*N**(-0.5),f'critical quartic constant N={N}')
    chk(corr>=0,f'critical positive two-spin correlation N={N}')

for t in [0.5,0.8,1.2,1.6]:
    root=brentq(lambda m:np.tanh(t*m)-m,0.01,0.999999999) if t>1 else 0.
    _,m2,corr=binomial_moments(1800,t)
    target=root**2 if t>1 else 0.
    chk(abs(corr-target)<0.022,f'phase correlation N=1800 t={t}')

print(f'PASS {checks} independent finite-size and asymptotic checks')
print('critical sqrt(N) two-spin covariance constant:',const)
