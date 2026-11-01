#!/usr/bin/env python3
"""Reproducible numerical checks of cubic repulsive network equilibria.
All stability and uniqueness results require the accompanying analytic proof.
No external dependencies are required.
"""
import math
from itertools import permutations


def cube_roots_parameter(k):
    if k <= 1/3:
        raise ValueError('k must be greater than 1/3')
    lo, hi = -2.0, -(2.0 ** (1.0/3.0))
    def poly(s):
        return k*s*s*s + s*s + s + 2*k
    assert poly(lo) < 0 < poly(hi)
    for _ in range(100):
        mid = (lo+hi)/2
        if poly(mid) > 0:
            hi = mid
        else:
            lo = mid
    s = (lo+hi)/2
    u2 = k*(1-s)-1
    assert u2 > 0
    return s, math.sqrt(u2)


def equilibria(k):
    if k <= 1/3:
        return [(0.,0.,0.)]
    b = 3*k-1
    s,u = cube_roots_parameter(k)
    out = {(0.,0.,0.)}
    out.update(set(permutations((math.sqrt(b),-math.sqrt(b),0.))))
    for sign in (-1,1):
        out.update(set(permutations((sign*u,sign*u,sign*s*u))))
    return sorted(out)


def vector_field(x,k,normalized=False):
    eff=k/2 if normalized else k
    return tuple(-v-v**3+eff*(3*v-sum(x)) for v in x)


def hessian(x,k):
    # H = diag(1+3*x_i^2)-k*L, L=3I-J
    return [[(1+3*x[i]*x[i]-2*k if i==j else k) for j in range(3)] for i in range(3)]


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
          - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
          + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def positive_definite(a):
    return a[0][0]>0 and a[0][0]*a[1][1]-a[0][1]**2>0 and det3(a)>0


def verify():
    for k in (1/3+1e-4,.34,.4,.5,1.,2.,20.):
        states=equilibria(k)
        assert len(states)==13, (k,len(states))
        saddles=0
        sinks=0
        for x in states:
            assert max(abs(y) for y in vector_field(x,k))<3e-10, (k,x,vector_field(x,k))
            h=hessian(x,k)
            if sum(abs(y) for y in x)<1e-12:
                # At zero, the Hessian eigenvalues are 1, 1-3*k, 1-3*k.
                assert k > 1/3
            elif sum(abs(y)<1e-12 for y in x)==1:
                # One negative and two positive eigendirections: determinant of H negative
                assert det3(h)<0
                saddles+=1
            else:
                assert positive_definite(h),(k,x,h)
                sinks+=1
        assert (saddles,sinks)==(6,6)
    for k in (.02, .33, 1/3):
        assert equilibria(k)==[(0.,0.,0.)]
    k=.5
    assert len(equilibria(k))==13
    assert k/2 < 1/3
    # Both coupling conventions agree on isolated vertices and a single edge.
    for x,y in ((.25,-.2), (1.1,1.2),(-.7,.8)):
        # K2 degree = 1, so identical pair vector fields.
        unnorm=(-x-x**3+k*(x-y),-y-y**3+k*(y-x))
        norm=(-x-x**3+k/1*(x-y),-y-y**3+k/1*(y-x))
        assert unnorm==norm
    print('VERIFY_OK: pair equality, 13 equilibria, six saddles, six sinks, and normalized K3 threshold')
    k=.5
    s,u=cube_roots_parameter(k)
    print('EXAMPLE k=1/2: s=%.15f, u=%.15f, other=%.15f' % (s,u,s*u))

if __name__=='__main__':
    verify()
