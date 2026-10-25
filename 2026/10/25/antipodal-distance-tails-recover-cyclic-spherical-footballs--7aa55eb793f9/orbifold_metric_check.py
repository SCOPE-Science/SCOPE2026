"""Reproducibility checks for the cyclic spherical-quotient near-diameter theorem.
No external files needed; Python 3, numpy, scipy. Uses independent Cartesian rotations.
"""
import numpy as np
from math import pi
from orbifold_quadrature_check import tail,c_formula

def quotient_distance(theta1,phi1,theta2,phi2,q):
    # Independent formula: minimum over all q spherical group rotations.
    p=np.array([np.sin(theta1)*np.cos(phi1),np.sin(theta1)*np.sin(phi1),np.cos(theta1)])
    best=pi
    for k in range(q):
        ang=phi2+2*pi*k/q
        qq=np.array([np.sin(theta2)*np.cos(ang),np.sin(theta2)*np.sin(ang),np.cos(theta2)])
        best=min(best,float(np.arccos(np.clip(p@qq,-1,1))))
    return best

def reduced_distance(theta1,phi1,theta2,phi2,q):
    a=pi/q
    delta=abs((phi1-phi2+a)%(2*a)-a)
    cs=np.cos(theta1)*np.cos(theta2)+np.sin(theta1)*np.sin(theta2)*np.cos(delta)
    return float(np.arccos(np.clip(cs,-1,1)))

if __name__=='__main__':
    rng=np.random.default_rng(5342)
    for q in [2,3,5,8]:
        errs=[]
        for i in range(400):
            c1,c2=rng.uniform(-1,1,2)
            t1,t2=np.arccos([c1,c2]); f1,f2=rng.uniform(0,2*pi,2)
            errs.append(abs(quotient_distance(t1,f1,t2,f2,q)-reduced_distance(t1,f1,t2,f2,q)))
        assert max(errs)<1e-7
        ratios=[]
        for e in [0.3,0.15,0.075,0.0375]:
            val=tail(q,e,n=150)/e**4/c_formula(q)
            ratios.append(val)
        assert max(abs(x-1) for x in ratios)<.009
        assert all(abs(ratios[i+1]-1)<abs(ratios[i]-1) for i in range(3))
        print(f'q={q}, maximum metric discrepancy={max(errs):.3g}, finite-epsilon to asymptotic ratios={ratios}')
    print('ALL independent spherical quotient and quadrature checks passed.')
