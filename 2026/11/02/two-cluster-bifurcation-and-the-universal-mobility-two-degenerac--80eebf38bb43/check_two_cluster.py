"""Exact algebra and direct stationary-equation checks for two-level complete-graph chemotaxis."""
import math
import sympy as sp

z, a, d, t = sp.symbols('z a d t', real=True)
b = 1-a
s = (1+sp.sqrt(1-4*a*b*z*z))/2
h = s+b*z
ell = s-a*z
B = (h*(1-h)+b*d*(-z/2+(h+ell)*sp.tanh(t*z)/2))/z
poly = sp.series(B,z,0,4).removeO().expand()
coeff = [sp.factor(poly.coeff(z,j)) for j in range(3)]
crit = sp.Rational(1,2)+1/d
assert sp.simplify(coeff[0]-b*d*(t-crit))==0
assert sp.simplify(coeff[1].subs(t,crit)-b*(1-2*a)*(d-2)/4)==0
assert sp.simplify(coeff[2].subs({d:2,t:1})+2*b/3)==0
assert sp.simplify(coeff[2].subs({a:sp.Rational(1,2),t:crit})+(d**3+3*d+2)/(12*d**2))==0
assert sp.simplify(s*(1-s)-a*b*z*z)==0
print('EXACT_STATIONARY_REDUCTION_AND_MASS_IDENTITY_PASS')
print('EXACT_TRANSCRITICAL_COEFFICIENT_PASS')
print('EXACT_MOBILITY_TWO_DEGENERACY_PASS')
print('EXACT_BALANCED_PARTITION_COEFFICIENT_PASS')

# Evaluate the original N-patch right sides, not just the scalar reduction.
def test_case(N,p,mobility,delta):
    import scipy.optimize as so
    q=N-p
    aa=p/N; bb=q/N; r=K=alpha=beta=1.0; eta_c=2.0
    tt=.5+1/mobility+delta
    chi=2*tt*(beta+eta_c/2)/(alpha*K)
    def stationarity(Z):
        mm=(1+math.sqrt(1-4*aa*bb*Z*Z))/2
        H=mm+bb*Z; L=mm-aa*Z
        flux=(-Z+(H+L)*math.tanh(tt*Z))/2
        return (H*(1-H)+bb*mobility*flux)/Z
    grid=[-.035+j*.00014 for j in range(501)]
    roots=[]
    for x,y in zip(grid[:-1],grid[1:]):
        if abs(x)<1e-13 or abs(y)<1e-13:continue
        if stationarity(x)*stationarity(y)<0:
            Z=so.brentq(stationarity,x,y,xtol=1e-14)
            if not any(abs(Z-r0)<1e-7 for r0 in roots):roots.append(Z)
    expected=2 if (mobility==2 or p==q) and delta>0 else (0 if (mobility==2 or p==q) else 1)
    assert len(roots)==expected,(N,p,mobility,delta,roots)
    for Z in roots:
        mm=(1+math.sqrt(1-4*aa*bb*Z*Z))/2
        H=mm+bb*Z; L=mm-aa*Z
        CH=mm+(bb*Z)/(beta+eta_c/2)
        CL=mm-(aa*Z)/(beta+eta_c/2)
        densities=[H]*p+[L]*q
        chemicals=[CH]*p+[CL]*q
        dn=[];dc=[]
        for i in range(N):
            flow=sum((math.exp(chi*chemicals[i])*densities[j]-math.exp(chi*chemicals[j])*densities[i])/(math.exp(chi*chemicals[i])+math.exp(chi*chemicals[j])) for j in range(N) if i!=j)
            dn.append((mobility/N)*flow+densities[i]*(1-densities[i]))
            dc.append((eta_c/(2*N))*sum(chemicals[j]-chemicals[i] for j in range(N) if i!=j)+densities[i]-chemicals[i])
        assert max(map(abs,dn+dc))<2e-10, (N,p,mobility,Z,dn,dc)
    return roots

assert len(test_case(3,1,1,.0001))==1
assert len(test_case(3,1,2,.0001))==2
assert len(test_case(4,2,1,.0001))==2
assert len(test_case(4,2,3,.0001))==2
assert len(test_case(3,1,2,-.0001))==0
assert len(test_case(4,2,1,-.0001))==0
print('DIRECT_FULL_GRAPH_POSITIVE_STATIONARY_RESIDUALS_AND_ROOT_COUNTS_PASS')
