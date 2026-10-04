import math
import cmath
import itertools
import numpy as np
import sympy as sp

L = math.log(2.0)
c = 1.0 / L - 1.0

# Symbolic check of the one-dimensional deficit calculus.
d = sp.symbols('d', positive=True)
Ls = sp.log(2)
K = 1 - d + sp.log((1+d)/2)
h = -((1+d)/2)*sp.log((1+d)/2) - ((1-d)/2)*sp.log((1-d)/2)
N = -Ls*K + (1-Ls)*h
N1_expected = Ls*d/(1+d) + (1-Ls)/2 * sp.log((1-d)/(1+d))
N2_expected = (2*Ls - 1 - d)/((1-d)*(1+d)**2)
assert sp.simplify(sp.diff(N,d)-N1_expected) == 0
assert sp.simplify(sp.diff(N,d,2)-N2_expected) == 0
assert sp.simplify(N.subs(d,0)) == 0
assert sp.limit(N,d,1,dir='-') == 0

# Closed-form versus numerical quadrature in one dimension.
def one_d_closed(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    delta = abs(2*q-1)
    K = 1-delta + math.log((1+delta)/2)
    hnat = -q*math.log(q) - (1-q)*math.log(1-q)
    return (-L*K + (1-L)*hnat)/(L*L)

def one_d_quad(q, n=131072):
    theta = (np.arange(n)+0.5) * (2*np.pi/n)
    r = 2*math.sqrt(q*(1-q))
    p = 1 + r*np.cos(theta)
    hout = -np.mean(p*np.log2(p))
    hin = -(q*math.log2(q) + (1-q)*math.log2(1-q)) if 0<q<1 else 0.0
    return float(hout + c*hin)

for q in [0.01,0.1,0.25,0.5,0.73,0.99]:
    assert abs(one_d_closed(q)-one_d_quad(q)) < 2e-7

# Strict positivity away from q in {0,1/2,1} on a dense grid.
vals=[]
for j in range(1,10000):
    q=j/10000
    if abs(q-0.5) < 1e-12:
        continue
    vals.append(one_d_closed(q))
assert min(vals) > 0.0
assert abs(one_d_closed(0.5)) < 1e-14

# Numerical multidimensional entropy deficit on a midpoint product grid.
def entropy_deficit(coeff, d, ngrid=192):
    pts = [np.array(x,dtype=int) for x in itertools.product([0,1], repeat=d)]
    a = np.array([coeff.get(tuple(x),0j) for x in pts], dtype=complex)
    norm = float(np.sum(np.abs(a)**2))
    a = a / math.sqrt(norm)
    probs=np.abs(a)**2
    hin=-sum(float(p)*math.log2(float(p)) for p in probs if p>0)
    grids=[(np.arange(ngrid)+0.5)/ngrid for _ in range(d)]
    mesh=np.meshgrid(*grids,indexing='ij')
    F=np.zeros([ngrid]*d,dtype=complex)
    for coeffval,x in zip(a,pts):
        phase=np.zeros_like(mesh[0])
        for k in range(d):
            phase += x[k]*mesh[k]
        F += coeffval*np.exp(-2j*np.pi*phase)
    p=np.abs(F)**2
    hout=-float(np.mean(np.where(p>0,p*np.log2(p),0.0)))
    return hout+c*hin

# Equality examples: singleton, diagonal affine cube, full cube with linear phase.
assert abs(entropy_deficit({(0,0):1},2)) < 5e-8
assert abs(entropy_deficit({(0,0):1,(1,1):1j},2)) < 5e-6
coeff_full={(x,y): cmath.exp(1j*(0.37*x-0.81*y)) for x,y in itertools.product([0,1],repeat=2)}
assert abs(entropy_deficit(coeff_full,2)) < 5e-6

# Non-extremal checks: 3-point support and unbalanced 2-point support.
assert entropy_deficit({(0,0):1,(1,0):1,(0,1):1},2) > 1e-3
assert entropy_deficit({(0,0):1,(1,1):2},2) > 1e-3

# Exact autocorrelation signature of a phased proper affine cube.
def phased_cube(base, gens, phases):
    m=len(gens)
    out={}
    amp=2**(-m/2)
    for eps in itertools.product([0,1], repeat=m):
        x=tuple(base[k]+sum(eps[j]*gens[j][k] for j in range(m)) for k in range(len(base)))
        ang=sum(eps[j]*phases[j] for j in range(m))
        out[x]=amp*cmath.exp(1j*ang)
    return out

def autocorr(f):
    keys=list(f)
    C={}
    for x in keys:
        for y in keys:
            z=tuple(x[k]-y[k] for k in range(len(x)))
            C[z]=C.get(z,0j)+f[x]*f[y].conjugate()
    return C

base=(0,0,0)
gens=[(1,1,0),(0,0,1)]
phases=[0.4,-0.7]
f=phased_cube(base,gens,phases)
C=autocorr(f)
nonzero=[(z,v) for z,v in C.items() if any(z)]
maxmag=max(abs(v) for z,v in nonzero)
recovered={z for z,v in nonzero if abs(abs(v)-maxmag)<1e-12}
expected={gens[0],tuple(-t for t in gens[0]),gens[1],tuple(-t for t in gens[1])}
assert abs(maxmag-0.5)<1e-12
assert recovered==expected

print('SYMBOLIC_DERIVATIVES_OK')
print('ONE_DIMENSIONAL_PROFILE_OK')
print('MULTIDIMENSIONAL_NUMERICAL_CHECKS_OK')
print('AUTOCORRELATION_RIGIDITY_SIGNATURE_OK')
print('VERIFY_OK')
