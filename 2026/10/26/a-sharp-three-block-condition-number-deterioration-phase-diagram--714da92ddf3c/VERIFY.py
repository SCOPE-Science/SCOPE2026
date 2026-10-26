"""Reproduce algebraic and numerical checks for rank-one block-Jacobi conditioning.
Requirements: Python 3.10+, sympy, numpy.
Mathematical universality follows from the accompanying proof, not from sampling.
"""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp

s,t,x,y = sp.symbols('s t x y', positive=True)
K = 1 + 2*s + t
D = s*s + 8*s*t*(1+s)/(1+t)
B = 2+3*s
# Pair comparison: the squared gap factors exactly.
S=x+y
assert sp.factor(S*S*(1+x)*(1+y)-x*y*(S+2)**2) == (x-y)**2*(S+1)
# Two regimes in the three-block repeated-pair configuration.
assert sp.factor(sp.together(D-(s+2*t)**2)) == 4*t*(s-t)*(2*s+t+1)/(1+t)
assert sp.simplify(D-9*s*s-8*s*(t-s)/(1+t)) == 0
assert sp.simplify(D*(K+1)**2 - B*B*(K-1)**2 - (
    4*(t-s)*(2*s+t+1)*(4*s*s+3*s-(s+1)*t)/(1+t))) == 0
# Sharp 3/2 bound in the second regime, via an explicit positive certificate.
P = 9*s*(t-s)**2+27*s**3+41*s*s+(s-3*t)**2+13*s+6*t+1
assert sp.simplify(B**2*(3*K-2)**2-D*(3*K+2)**2 - (
    4*(2*s+t+1)*P/(1+t))) == 0
assert sp.factor(sp.together(D.subs({s:4,t:1}))) == 96
# Exact matrix example and characteristic polynomial of the preconditioned matrix.
A=sp.Matrix([[5,4,2],[4,5,2],[2,2,2]])
Pdiag=sp.diag(5,5,2)
assert A == sp.eye(3)+sp.Matrix([2,2,1])*sp.Matrix([[2,2,1]])
assert Pdiag == sp.diag(*A.diagonal())
lam=sp.symbols('lam')
char=sp.factor((A-lam*Pdiag).det())
assert sp.expand(char + 50*(lam-sp.Rational(1,5))*(lam**2-sp.Rational(14,5)*lam+1)) == 0
# Witness preconditioned eigenvalues: 1/5 and (7 +/- 2 sqrt(6))/5.
assert sp.simplify(sp.Rational(7,5)+sp.Rational(2,5)*sp.sqrt(6) - sp.Rational(1,5)*(7+2*sp.sqrt(6))) == 0
assert sp.simplify((sp.Rational(7,5)+sp.Rational(2,5)*sp.sqrt(6))/(sp.Rational(1,5))-(7+2*sp.sqrt(6))) == 0

rng=np.random.default_rng(271828)
checks=0
for blocks in (2,3):
    for trial in range(900):
        energies = 10**rng.uniform(-3, 5, size=blocks)
        v=np.sqrt(energies)
        a=np.eye(blocks)+np.outer(v,v)
        diag=1+energies
        z=(a/np.sqrt(diag)[:,None])/np.sqrt(diag)[None,:]
        eig=np.linalg.eigvalsh(z)
        kappa=float(eig[-1]/eig[0])
        original=1+sum(energies)
        assert np.all(eig>0)
        if blocks==2:
            theta=math.sqrt(energies[0]*energies[1]/(diag[0]*diag[1]))
            predicted=(1+theta)/(1-theta)
            assert math.isclose(predicted,kappa,rel_tol=1e-8,abs_tol=1e-8)
            assert kappa <= original*(1+2e-9)
        else:
            s_val=energies[0]; t_val=energies[2]
            # Separate exact repeated-pair case.
            energies[1]=s_val
            v=np.sqrt(energies); a=np.eye(3)+np.outer(v,v)
            d=1+energies; z=(a/np.sqrt(d)[:,None])/np.sqrt(d)[None,:]
            eig=np.linalg.eigvalsh(z); kappa=float(eig[-1]/eig[0])
            dval=s_val*s_val+8*s_val*t_val*(1+s_val)/(1+t_val)
            L0=1/(1+s_val)
            Lminus=(2+3*s_val-math.sqrt(dval))/(2*(1+s_val))
            Lplus=(2+3*s_val+math.sqrt(dval))/(2*(1+s_val))
            assert math.isclose(kappa,Lplus/min(L0,Lminus),rel_tol=2e-8)
            Korig=1+2*s_val+t_val
            threshold=s_val*(4*s_val+3)/(1+s_val)
            theory_bad = t_val<s_val or (s_val<t_val<threshold)
            if abs(t_val-s_val)>1e-7*max(t_val,s_val) and abs(t_val-threshold)>1e-7*max(t_val,threshold):
                assert (kappa>Korig)==theory_bad
            assert kappa < 1.5*Korig*(1+2e-8)
        checks+=1
# Check asymptotic sharpness via an independently constructed sequence.
ratios=[]
for L in (10, 100, 1000, 10000):
    e=np.array([L*L,L*L,L],dtype=float)
    v=np.sqrt(e); aa=np.eye(3)+np.outer(v,v); dd=1+e
    zz=aa/np.sqrt(np.outer(dd,dd))
    ee=np.linalg.eigvalsh(zz)
    ratios.append(float(ee[-1]/ee[0]/(1+sum(e))))
assert ratios[-1] > 1.49 and ratios[-1] < 1.5
print(f'VERIFY_OK: {checks} randomized matrix comparisons, 6 algebraic identities, exact witness and asymptotic sequence; last ratio={ratios[-1]:.10f}')
