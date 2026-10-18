"""Numerical and rational tests of a convex-pyramid difference-body identity.

Python 3; numpy and scipy are used only for independent convex-hull tests.
Analytic arguments, not finite tests, establish the theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import numpy as np
from scipy.spatial import ConvexHull


def polygon_area(poly):
    return abs(sum(x*y1 - x1*y for (x,y),(x1,y1)
                   in zip(poly,poly[1:]+poly[:1]))) / 2


def cross(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def convex_hull_2d(points):
    pts=sorted(set(points))
    lower=[]
    for p in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in pts[::-1]:
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def volume_ratio_difference(vertices, scale=1.0):
    x=np.asarray(vertices, dtype=float)
    dx=(x[:,None,:]-scale*x[None,:,:]).reshape((-1,x.shape[1]))
    return ConvexHull(dx).volume/ConvexHull(x).volume


def test_3d(base,apex):
    base=[tuple(F(c) for c in v) for v in base]
    base=convex_hull_2d(base)
    ar=polygon_area(base)
    negdiff=convex_hull_2d([(x-u,y-v) for x,y in base for u,v in base])
    diff_ar=polygon_area(negdiff)
    predicted=F(2)+F(3)*diff_ar/ar
    pyramid=[(float(x),float(y),0.0) for x,y in base]
    pyramid.append((float(apex[0]),float(apex[1]),float(apex[2])))
    measured=volume_ratio_difference(pyramid)
    qq=diff_ar/ar
    for scale in (0.2,0.7,1.0,1.8,3.0):
        expected=1+F(3,2)*qq*(F(str(scale))+F(str(scale))**2)+F(str(scale))**3
        got=volume_ratio_difference(pyramid,scale)
        assert abs(got-float(expected))<5e-9,(scale,expected,got)
    assert abs(measured-float(predicted))<5e-9,(predicted,measured)
    assert 14<=predicted<=20
    return (str(predicted),measured)


def test_4d(base,apex,expected,polynomial):
    x=np.asarray(base,dtype=float)
    pyramid=np.vstack((np.column_stack((x,np.zeros(len(x)))),np.asarray(apex,dtype=float)))
    ratio=volume_ratio_difference(pyramid)
    assert abs(ratio-expected)<2e-8,(ratio,expected)
    for scale in (0.3,0.8,1.7):
        measured=volume_ratio_difference(pyramid,scale)
        predicted=polynomial(scale)
        assert abs(measured-predicted)<2e-8,(scale,measured,predicted)
    return ratio


if __name__=='__main__':
    bases=[
        [('0','0'),('3','0'),('0','2')],
        [('0','0'),('4','0'),('4','3'),('0','3')],
        [('0','0'),('6','0'),('5','2'),('1','3')],
        [('0','0'),('4','0'),('5','2'),('3','5'),('0','3')],
        [('0','0'),('3','0'),('4','1'),('5','3'),('3','5'),('0','4')],
    ]
    out=[test_3d(b,('0.37','-0.41','2.3')) for b in bases]
    assert out[0][0]=='20'
    assert out[1][0]=='14'
    tetra=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    cube=list(product((-1.0,1.0),repeat=3))
    h4=(test_4d(tetra,(0.5,-0.2,0.1,1.8),comb(8,4),lambda s:sum(comb(4,j)**2*s**j for j in range(5))),
        test_4d(cube,(0.5,-0.2,0.1,1.8),2*(2**4-1),lambda s:2*(1+s)**4-1-s**4))
    print('PYRAMID_DIFFERENCE_CHECK_OK rational_3d=5 hull_3d=5 hull_4d=2')
    print('3D base ratios:',out)
    print('4D ratios:',h4)
