#!/usr/bin/env python3
"""Exact arithmetic and direct geometric quadrature for a two-loop metric network.
All computations are self-contained and use only the Python standard library.
Finite numerical tests are corroboration, not a proof of the universal theorem.
"""
from fractions import Fraction as F
from itertools import product


def conditional_moments(a, b, t):
    """Sum the ordered loop/bridge pair classes using their conditional laws."""
    total = a + b + t
    e1 = ((a**3 + b**3) / 4
          + 2*a*b*(t + (a+b)/4)
          + 2*a*t*(a/4 + t/2)
          + 2*b*t*(b/4 + t/2)
          + t**3/3) / total**2
    e2 = ((a**4 + b**4) / 12
          + 2*a*b*(t**2+t*(a+b)/2 + (a*a+b*b)/12 + a*b/8)
          + 2*a*t*(a*a/12+a*t/4+t*t/3)
          + 2*b*t*(b*b/12+b*t/4+t*t/3)
          + t**4/6) / total**2
    return e1, e2


def polynomial_moments(a, b, t):
    s = a+b
    r = t/s
    p = a*b/s**2
    mean_num = (F(1,4) + r/2 + r*r + r**3/3 + p*(r-F(1,4)))
    second_num = (F(1,12)+r/6+r*r/2+2*r**3/3+r**4/6
                  +p*(-F(1,6)+r/2+r*r)+p*p/12)
    return s*mean_num/(1+r)**2, s*s*second_num/(1+r)**2


def variance_scaled(r, p):
    M = F(1,4)+r/2+r*r+r**3/3+p*(r-F(1,4))
    N = (F(1,12)+r/6+r*r/2+2*r**3/3+r**4/6
         +p*(-F(1,6)+r/2+r*r)+p*p/12)
    return (N*(1+r)**2-M*M)/(1+r)**4


def critical_cubic(r):
    return 16*r**3+24*r*r+30*r-3


def critical_quartic(r):
    return 8*r**4+16*r**3+32*r*r-2*r-1


def derivative_variance_numerator(r,p):
    # (1+r)^4 * partial_p (Var(D)/(a+b)^2)
    return (critical_quartic(r)+(1+32*r-44*r*r)*p)/24


def optimal_product(r):
    return -critical_quartic(r)/(1+32*r-44*r*r)


def direct_quadrature(a, b, t, n):
    """Independent network shortest-path quadrature on arclength cell midpoints."""
    af,bf,tf=map(float,(a,b,t))
    segments=(('A',af),('B',bf),('I',tf))
    samples=[]
    for label,length in segments:
        for j in range(n):
            samples.append((label, length*(j+0.5)/n, length/n))
    m1=m2=0.0
    for i,(label,x,w) in enumerate(samples):
        for label2,y,w2 in samples:
            if label==label2:
                if label=='I':d=abs(x-y)
                else:
                    circ=af if label=='A' else bf
                    h=abs(x-y);d=min(h,circ-h)
            elif set((label,label2))=={'A','B'}:
                ra=min(x,af-x) if label=='A' else min(y,af-y)
                rb=min(y,bf-y) if label2=='B' else min(x,bf-x)
                d=ra+tf+rb
            else:
                if label=='A' or label2=='A':
                    xx=x if label=='A' else y
                    yy=y if label2=='I' else x
                    d=min(xx,af-xx)+yy
                else:
                    xx=x if label=='B' else y
                    yy=y if label2=='I' else x
                    d=min(xx,bf-xx)+(tf-yy)
            ww=w*w2
            m1+=ww*d;m2+=ww*d*d
    return m1/(af+bf+tf)**2,m2/(af+bf+tf)**2


def run():
    assert critical_cubic(F(9,100))<0<critical_cubic(F(1,10))
    assert critical_quartic(F(19,100))<0<critical_quartic(F(1,5))
    assert critical_quartic(F(1,10))<0
    assert critical_cubic(F(19,100))>0
    assert F(1,10)<F(19,100)
    assert derivative_variance_numerator(F(1,10),F(0))<0
    assert derivative_variance_numerator(F(1,10),F(1,4))>0
    checked=0
    values=(F(1,7),F(1,3),F(1,2),F(1),F(5,4),F(2),F(5))
    for a,b,t in product(values,repeat=3):
        pair=conditional_moments(a,b,t)
        poly=polynomial_moments(a,b,t)
        assert pair==poly, (a,b,t,pair,poly)
        assert poly[1]>=poly[0]**2
        checked+=1
    r=F(1,10)
    p=optimal_product(r)
    assert p==F(1079,4700)
    assert F(0)<p<F(1,4)
    delta=variance_scaled(r,F(1,4))-variance_scaled(r,p)
    assert delta==F(384,17203175)>0
    # At the midpoint critical window the derivative changes sign on the admissible p interval.
    for rr in [F(0), F(1,20), F(1,10), F(3,20), F(19,100), F(1,5), F(1,2), F(1), F(3)]:
        g0=derivative_variance_numerator(rr,F(0))
        g1=derivative_variance_numerator(rr,F(1,4))
        assert g0==critical_quartic(rr)/24
        assert g1==(2*rr+1)*critical_cubic(rr)/96
    # Midpoint arclength quadrature on each component (not a proof, but separate from moment algebra).
    checks=[]
    for a,b,t in [(F(2,3),F(1,3),F(1,10)),
                  (F(3,5),F(2,5),F(1,2)),
                  (F(1,4),F(3,4),F(2,1))]:
        expected=polynomial_moments(a,b,t)
        observed=direct_quadrature(a,b,t,120)
        error=max(abs(observed[k]-float(expected[k])) for k in (0,1))
        assert error < 0.00015,(a,b,t,error,observed,expected)
        checks.append((str(a),str(b),str(t),format(error,'.8g')))
    print('PASS:',checked,'exact rational moment comparisons; 9 exact derivative endpoint identities;')
    print('3 independent 360-point direct midpoint geodesic integrations;')
    print('critical-root rational brackets and interior-optimum witness;')
    print('r=1/10: p*=1079/4700, strict variance improvement 384/17203175;')
    print('quadrature discrepancies (a,b,t,maximum error):',checks)

if __name__=='__main__':run()
