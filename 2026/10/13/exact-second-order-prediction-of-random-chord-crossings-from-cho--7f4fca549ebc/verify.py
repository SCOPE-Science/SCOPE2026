"""Symbolic moment and geometric sampling checks for circular chords.

Only the mathematical statements in RESULT.md are assessed. Run with Python 3,
SymPy and NumPy: python verify.py
"""
import math
import numpy as np
import sympy as sp

r, s, n = sp.symbols('r s n', real=True, nonnegative=True)
# R=min(U,1-U) for U uniform(0,1) has density 2 on (0,1/2).
p = sp.Rational(1, 2)
G1 = sp.simplify(8 * sp.integrate(sp.integrate(2 * r, (r, 0, s)), (s, 0, p)))
G2 = sp.simplify(8 * sp.integrate(sp.integrate((2 * r)**2, (r, 0, s)), (s, 0, p)))
q = 2 * r * (1-r)
qmean = sp.integrate(2*q, (r,0,p))
qvar = sp.integrate(2*q**2,(r,0,p))-qmean**2
assert (G1,G2,qmean,sp.simplify(qvar)) == (sp.Rational(1,3),sp.Rational(1,6),sp.Rational(1,3),sp.Rational(1,45))
assert sp.simplify(G1-G2) == sp.Rational(1,6)
vg = sp.simplify(G2-G1**2)
var_condmean = sp.simplify(n*(n-1)*vg/2+n*(n-1)*(n-2)*qvar)
var_resid = sp.simplify(n*(n-1)*(G1-G2)/2)
var_total = sp.simplify(var_condmean+var_resid)
assert sp.simplify(var_condmean - n*(n-1)*(4*n-3)/180)==0
assert sp.simplify(var_resid-n*(n-1)/12)==0
assert sp.simplify(var_total-n*(n-1)*(n+3)/45)==0
assert sp.simplify(var_condmean/var_total-(4*n-3)/(4*(n+3)))==0
# The crossed pairing probability 2*min(a,b) is also checked using
# independent continuous rotations, rather than restating the integral.

def crossings(phases):
    num_trials, count, _ = phases.shape
    out = np.zeros(num_trials,dtype=np.int32)
    for i in range(count):
        start = phases[:,i,0]
        arc = (phases[:,i,1]-start) % 1.0
        for j in range(i+1,count):
            a = (phases[:,j,0]-start) % 1.0 < arc
            b = (phases[:,j,1]-start) % 1.0 < arc
            out += a ^ b
    return out

def phases_from_radii(radii, draws, rng):
    # A rotation of a short arc generates the unoriented chord of that length.
    starts=rng.random((draws,len(radii)))
    return np.stack([starts,(starts+np.asarray(radii)[None,:])%1.0],axis=-1)

rng = np.random.default_rng(291729)
for radii in ([0.11,0.24], [0.07,0.19,0.32,0.44], [0.10,0.22,0.35]):
    trials=140000
    H=crossings(phases_from_radii(radii,trials,rng))
    gs=[2*min(radii[i],radii[j]) for i in range(len(radii)) for j in range(i+1,len(radii))]
    target_mean=sum(gs)
    target_var=sum(g*(1-g) for g in gs)
    mean=float(H.mean()); variance=float(H.var())
    assert abs(mean-target_mean)<0.022,(radii,mean,target_mean)
    assert abs(variance-target_var)<0.035,(radii,variance,target_var)
    print('fixed_radii',len(radii),'mean',round(mean,5),'target',round(target_mean,5),'variance',round(variance,5),'target',round(target_var,5))
for count in (3, 6):
    trials=90000
    angles=rng.random((trials,count,2))
    H=crossings(angles)
    rawdiff=(angles[:,:,1]-angles[:,:,0])%1
    R=np.minimum(rawdiff,1-rawdiff)
    prediction=np.zeros(trials)
    for i in range(count):
        for j in range(i+1,count):
            prediction+=2*np.minimum(R[:,i],R[:,j])
    v_prediction=float(np.var(prediction))
    mean_target=count*(count-1)/6
    var_target=count*(count-1)*(count+3)/45
    v_cond_target=count*(count-1)*(4*count-3)/180
    assert abs(np.mean(H)-mean_target) < 0.045
    assert abs(np.var(H)-var_target)/var_target < .045
    assert abs(v_prediction-v_cond_target)/v_cond_target < .05
    print('iid_chords',count,'cross_mean',round(float(H.mean()),5),'theory',round(mean_target,5), 'cross_var',round(float(H.var()),5),'theory',round(var_target,5), 'pred_var',round(v_prediction,5),'theory',round(v_cond_target,5))
print('VERIFY_OK symbolic=8 conditional_samples=3 unconditional_samples=2')
