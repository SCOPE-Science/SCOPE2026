"""Numerically integrates independently parameterized local cross-face wedges."""
import numpy as np
from scipy.stats import qmc
from math import pi,sin,cos
u=qmc.Sobol(d=2,scramble=True,seed=41).random_base2(22)
for angle in [pi/3,pi/2,2*pi/3,5*pi/6]:
    # each u,v<=1/sin(theta) bounds the admissible ellipse in the first quadrant
    R=1/sin(angle)
    x=R*u[:,0];y=R*u[:,1]
    d2=x*x+y*y-2*x*y*cos(angle)
    I=(R*R)*np.sqrt(np.clip(1-d2,0,None)).mean()
    # ordered pair's z-integrated coefficient is 4 I per unit edge
    empirical=4*I
    formula=4*(pi-angle)/(3*sin(angle))
    print(f'theta={angle/pi:.4f}pi computed={empirical:.9f} formula={formula:.9f} error={empirical-formula:+.3g}')
    assert abs(empirical-formula)<0.001
