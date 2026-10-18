"""Reproduce analytic identities and independent geometric sampling benchmarks."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.stats import qmc


def primitive(t):
    d = math.sqrt(t*t - t + 1)
    return (1.0-1.0/t)*d + 0.5*(
        math.asinh((2*t-1)/math.sqrt(3)) -
        math.asinh((2/t-1)/math.sqrt(3)))


def Q_closed(s):
    if s == 0:
        return 0.0
    if s == 1:
        return 2/3 + 2*math.log(2)/9
    k = math.sqrt(3)*s/math.sqrt(4-s*s)
    a, b = (1-k)/2, (1+k)/2
    polynomial = ((8-s*s)*(b-a) + (s*s-2)*math.log(b/a) +
                  (1+s*s)*(1/b-1/a))/9
    return polynomial - 2*s/9*(primitive(a)+primitive(b))


def Q_quadrature(s):
    if s == 0:
        return 0.0
    if s == 1:
        return 2/3 + 2*math.log(2)/9
    k = math.sqrt(3)*s/math.sqrt(4-s*s)
    a, b = (1-k)/2, (1+k)/2
    d = lambda t: math.sqrt(t*t-t+1)
    part1 = quad(lambda t: 1-(1+t-s*d(t))**2/(9*t*t),a,b,
                 epsabs=3e-13, epsrel=3e-13)[0]
    part2 = quad(lambda t: 4*s*(1+t)*d(t)/(9*t*t),b,1,
                 epsabs=3e-13, epsrel=3e-13)[0]
    return part1 + part2


def check_symbolic():
    x,y,z,s=sp.symbols('x y z s', real=True, positive=True)
    t=sp.symbols('t', positive=True)
    center = sp.Matrix([sp.Rational(1,3),sp.Rational(1,3)])
    hessian = sp.Matrix([[2,1],[1,2]])
    support_matrix = hessian.inv()/6
    assert support_matrix == sp.Matrix([[sp.Rational(1,9),-sp.Rational(1,18)],[-sp.Rational(1,18),sp.Rational(1,9)]])
    incidence = (3*x*y-x-y)**2 - s*s*(x*x+y*y-x*y)
    assert sp.factor(incidence.subs(s,1)) == 3*x*y*(3*x*y-2*x-2*y+1)
    F=(1-1/t)*sp.sqrt(t*t-t+1)+sp.Rational(1,2)*(
        sp.asinh((2*t-1)/sp.sqrt(3))-sp.asinh((2/t-1)/sp.sqrt(3)))
    assert sp.simplify(sp.diff(F,t)-(1+t)*sp.sqrt(t*t-t+1)/t**2)==0
    assert sp.simplify(F.subs(t,1))==0
    u=sp.symbols('u',real=True)
    endpoint_integral = sp.integrate((1-2*u)/(2-3*u),(u,0,sp.Rational(1,2)))
    assert sp.simplify(endpoint_integral - (sp.Rational(1,3)-2*sp.log(2)/9))==0
    print('symbolic conic/incidence/primitive/endpoint checks: PASS')


def check_quadratures():
    scales=(0.0001,0.01,0.1,0.3,0.5,0.75,0.9,0.99,0.999)
    for s in scales:
        diff=abs(Q_closed(s)-Q_quadrature(s))
        assert diff<5e-11,(s,diff)
    slope=(2/9)*(math.sqrt(3)+math.log(2+math.sqrt(3)))
    assert abs(Q_closed(0.001)/0.001-slope)<1e-6
    print('independent quadrature and small-scale checks: PASS',len(scales),'scales')


def sample_hit_on_triangle(vertices, scales, m=17):
    vertices=np.asarray(vertices,float)
    edges=np.roll(vertices,-1,axis=0)-vertices
    lengths=np.linalg.norm(edges,axis=1)
    weights=lengths/np.sum(lengths)
    B=np.column_stack((vertices[1]-vertices[0],vertices[2]-vertices[0]))
    Q=B@np.array([[1/9,-1/18],[-1/18,1/9]])@B.T
    c=np.mean(vertices,axis=0)
    # Independent quasi-uniform coordinates choose side and location for both endpoints.
    seq=qmc.Sobol(d=4,scramble=False).random_base2(m)
    labels1=np.searchsorted(np.cumsum(weights),seq[:,0],side='right')
    labels2=np.searchsorted(np.cumsum(weights),seq[:,2],side='right')
    labels1=np.minimum(labels1,2);labels2=np.minimum(labels2,2)
    t1=seq[:,1];t2=seq[:,3]
    X=vertices[labels1]+t1[:,None]*edges[labels1]
    Y=vertices[labels2]+t2[:,None]*edges[labels2]
    d=Y-X
    normals=np.column_stack((-d[:,1],d[:,0]))
    signed=np.abs(np.einsum('ni,ni->n',normals,X-c))
    denom=np.sqrt(np.einsum('ni,ij,nj->n',normals,Q,normals))
    distinct=labels1!=labels2
    # As the homothetic ellipse lies inside the triangle, this line test equals the segment test.
    ratios=np.divide(signed,denom,out=np.full(len(signed),np.inf),where=denom>0)
    shape=1.0-np.sum(weights*weights)
    for s in scales:
        observed=np.mean(distinct & (ratios<=s))
        expected=shape*Q_closed(s)
        assert abs(observed-expected)<0.004,(s,vertices.tolist(),observed,expected)
    return shape


def main():
    check_symbolic()
    check_quadratures()
    triangles=[[(0,0),(1,0),(0,1)],[(0,0),(3,0),(0.3,2)],[(1,-1),(5,0),(1.1,0.1)],
               [(0,0),(1.9,0.1),(0.1,1.0)]]
    shape=[sample_hit_on_triangle(T,(0.1,0.3,0.5,0.8,1.0)) for T in triangles]
    print('direct physical ellipse/chord sampling: PASS',len(triangles)*5,'cases')
    print('shape factors:',[round(v,9) for v in shape])
    print('universal maximum at full ellipse:',2*Q_closed(1)/3)
    print('universal unattained infimum:',Q_closed(1)/2)


if __name__=='__main__':
    main()
