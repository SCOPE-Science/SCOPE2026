"""Supplementary finite-volume and symbolic checks of a cusp-ratchet limit.

Dependencies: Python 3, numpy, scipy, sympy.
"""
import numpy as np
import sympy as sp
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.special import exprel


def finite_volume(n, diffusion, right_slope=2., left_slope=3.,
                  velocity=1., switching_rate=1., load=0., waviness=0.):
    length = 1.
    peak = left_slope / (left_slope + right_slope)
    dx = length / n
    x = (np.arange(n) + .5) * dx
    slope = np.where(x < peak,
                     right_slope + waviness * np.sin(2*np.pi*x/peak),
                     -left_slope - waviness * np.sin(2*np.pi*(x-peak)/(1-peak)))
    rows, cols, entries = [], [], []
    right_rates = np.zeros((2,n))
    left_rates = np.zeros((2,n))
    for k, sign in enumerate((1.,-1.)):
        drift = sign*velocity-load-slope
        ze = drift*dx/diffusion
        right_rates[k] = (diffusion/dx**2) / exprel(-ze)
        left_rates[k] = (diffusion/dx**2) / exprel(ze)
        for i in range(n):
            idx = k*n+i
            for row, val in (
                (idx, -(right_rates[k,i]+left_rates[k,i]+switching_rate)),
                (k*n+(i+1)%n, right_rates[k,i]),
                (k*n+(i-1)%n, left_rates[k,i]),
                ((1-k)*n+i, switching_rate),
            ):
                rows.append(row);cols.append(idx);entries.append(val)
    matrix = sparse.csc_matrix((entries, (rows,cols)), shape=(2*n,2*n)).tolil()
    rhs = np.zeros(2*n)
    matrix[0,:] = 1.
    rhs[0] = 1.
    prob = spsolve(matrix.tocsc(),rhs).reshape(2,n)
    assert abs(prob.sum()-1.) < 1e-8
    assert prob.min() > -1e-9
    flux = np.array([right_rates[k]*prob[k]-np.roll(left_rates[k]*prob[k],-1)
                     for k in range(2)])
    current = flux.sum(axis=0).mean()
    production = velocity*dx/diffusion*(flux[0].sum()-flux[1].sum())-load*length*current/diffusion
    return production, current


def predicted(right_slope, left_slope, velocity, switching_rate, load):
    return 2*switching_rate*velocity**2*(
       1/((right_slope+load)**2-velocity**2)
       +1/((left_slope-load)**2-velocity**2))


def verify():
    A, B, v, g = sp.symbols('A B v g', positive=True)
    expression = g*v*(1/(A-v)-1/(A+v)+1/(B-v)-1/(B+v))
    target = 2*g*v**2*(1/(A*A-v*v)+1/(B*B-v*v))
    assert sp.simplify(expression-target) == 0
    assert sp.simplify(target.subs({A:2,B:3,v:1,g:1})-sp.Rational(11,12)) == 0
    print('exact algebra: PASS')
    for label, waviness in [('piecewise-linear',0.),('nonlinear arcs',.4)]:
        vals = []
        for diffusion, n in [(0.05,1200),(0.025,2200),(0.0125,4400)]:
            p, j = finite_volume(n,diffusion,waviness=waviness)
            vals.append(p)
            assert abs(j) < 0.0001
        lim = predicted(2,3,1,1,0)
        assert all(abs(vals[i+1]-lim)<abs(vals[i]-lim) for i in range(len(vals)-1))
        print(label,':',vals,'predicted limit',lim)
    vals = []
    for diffusion,n in [(0.025,2000),(0.0125,4000)]:
        p,j=finite_volume(n,diffusion,load=.25,switching_rate=.7)
        vals.append(p)
        assert abs(j)<0.0001
    lim=predicted(2,3,1,.7,.25)
    assert abs(vals[1]-lim)<abs(vals[0]-lim)
    print('loaded test:',vals,'predicted limit',lim)
    print('all checks passed')


if __name__=='__main__':
    verify()
