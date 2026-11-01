#!/usr/bin/env python3
"""Finite exact examples for the two-branch power-map theorem; not an infinite proof."""
from fractions import Fraction as F


def power_map(x, a, b, c, d):
    if x <= b:
        return 1-(1-a)*(1-x/b)**d
    return c*((x-b)/(1-b))**d


def return_map(x,a,b,c,d):
    y=power_map(x,a,b,c,d)
    assert y>b, (x,a,b,c,d,y)
    return power_map(y,a,b,c,d)


def test_affine():
    for b,c in [(F(3,4),F(1,8)),(F(2,3),F(1,5)),(F(1,3),F(1,9))]:
        for a in [b+F(1,32)*(1-b), b+F(1,4)*(1-b), b+F(1,2)*(1-b)]:
            assert c<b and b<a<1
            denom=b*(1-b)-c*(1-a)
            xi=b*c*(a-b)/denom
            eta=a+(1-a)*xi/b
            rho=c*(1-a)/(b*(1-b))
            assert 0<xi<b<eta<1
            assert power_map(xi,a,b,c,1)==eta
            assert power_map(eta,a,b,c,1)==xi
            assert 0<rho<1
            for x in [F(0),b/2,b]:
                g=return_map(x,a,b,c,1)
                assert g==c*(a-b)/(1-b)+rho*x
    print('PASS: 9 affine parameter sets, exact two-cycle and return identities')


def test_boundary():
    for b,c,d in [(F(3,4),F(1,16),2),(F(3,4),F(1,16),1),(F(2,3),F(1,48),3),(F(4,5),F(1,100),4)]:
        assert 0<c*d*d<b
        assert power_map(F(0),b,b,c,d)==b
        assert power_map(b,b,b,c,d)==1
        assert power_map(F(1),b,b,c,d)==c
        # Positive left points strictly contract under the two-step map.
        for x in [b/F(16),b/F(4),b]:
            y=power_map(x,b,b,c,d)
            assert y>b
            g=power_map(y,b,b,c,d)
            assert 0<g<=c*d*d*x/b < x
        for a in [b+(1-b)/F(8),b+(1-b)/F(32)]:
            for x in [F(0),b/F(4),b]:
                first=power_map(x,a,b,c,d)
                assert first>b
                second=power_map(first,a,b,c,d)
                assert 0<second<=c<b
                assert second == c*(((a-b)+(1-a)*(1-(1-x/b)**d))/(1-b))**d
    print('PASS: rational nonlinear critical-map and alternating-region checks')


if __name__=='__main__':
    test_affine()
    test_boundary()
    print('PASS: analytic theorem remains beyond finite testing')
