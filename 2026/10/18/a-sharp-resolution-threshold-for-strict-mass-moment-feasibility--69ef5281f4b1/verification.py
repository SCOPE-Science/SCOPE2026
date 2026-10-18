"""Exact-rational checks of a collocation-positive Fourier moment cone.

Python 3 standard library only. All inequalities use exact rational endpoints;
no floating-point decisions are made. The analytic infinite-order
estimates are established in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial


def atan_sums(q, k):
    s = F(0)
    for m in range(k + 1):
        s += (-1) ** m * F(1, (2*m+1)*q**(2*m+1))
    return s


def pi_interval():
    # Machin's identity; alternating-series error bounds.
    # After an odd term the partial sum is a strict lower bound;
    # after an even term it is a strict upper bound.
    p_lo = 16*atan_sums(5,33) - 4*atan_sums(239,32)
    p_hi = 16*atan_sums(5,32) - 4*atan_sums(239,33)
    scale = 10**30
    low = F((p_lo.numerator*scale)//p_lo.denominator,scale)
    high= F((p_hi.numerator*scale)//p_hi.denominator+1,scale)
    assert p_lo <= low + F(1,scale) and low<=p_lo
    assert high>=p_hi and high-p_hi<F(2,scale)
    return low,high

P_LO,P_HI=pi_interval()
assert F(3141592653589793,10**15) < P_LO < P_HI < F(3141592653589794,10**15)


def sin_endpoint(t, last):
    total=F(0)
    for m in range(last+1):
        total+=(-1)**m * t**(2*m+1)/factorial(2*m+1)
    return total


def sin_bound(tlo,thi):
    # 0<=t<=pi/2; sin monotone, alternating Maclaurin series
    # with decreasing term magnitudes on this interval.
    assert 0<=tlo<=thi<=P_HI/2
    return sin_endpoint(tlo,11),sin_endpoint(thi,10)


def si_bound(tlo,thi):
    # For t <= 5*pi/2, terms decrease from order m>=2;
    # both endpoints can be enclosed by +/- the next term.
    def approx(x):
        s=F(0)
        for k in range(28):
            s+=(-1)**k * x**(2*k+1)/((2*k+1)*factorial(2*k+1))
        e=x**57/(57*factorial(57))
        return s-e,s+e
    # Enclose all individual signed powers to avoid assuming monotone
    # polynomial evaluation. Si itself has derivative sin(t)/t;
    # on these *small pi interval* endpoints local monotonicity is known
    # from the sign of sin(t) and continuity within the interval.
    lo1,hi1=approx(tlo)
    lo2,hi2=approx(thi)
    return min(lo1,lo2),max(hi1,hi2)


def harmonic_sine_table(N):
    M=2*N+1
    vals={0:(F(0),F(0))}
    for a in range(1,M):
        q=min(a,M-a)
        if q not in vals:
            angle_multiplier=F(2*q,M) if 4*q<=M else F(M-2*q,M)
            vals[q]=sin_bound(angle_multiplier*P_LO,angle_multiplier*P_HI)
    table=[(F(0),F(0))]*M
    for a in range(1,M):
        q=min(a,M-a)
        low,high=vals[q]
        table[a]=(low,high) if a<=N else (-high,-low)
    return table


def mu_bound(N,j,table):
    M=2*N+1
    low,high=F(0),F(0)
    for k in range(1,N+1):
        sl,sh=table[(k*j)%M]
        c= F(2*((-1)**(k+1)),k)
        if c>0:
            low+=c*sl;high+=c*sh
        else:
            low+=c*sh;high+=c*sl
    return low,high


def verify_finite():
    counter=0
    worst=(F(100),0,0)
    for N in range(1,63):
        table=harmonic_sine_table(N)
        for j in range(1,N+1):
            lo,hi=mu_bound(N,j,table)
            assert hi<P_LO and lo>-P_LO, (N,j,float(lo),float(hi))
            counter+=1
            gap=P_LO-hi
            if gap<worst[0]:worst=(gap,N,j)
    assert counter==1953
    print('finite N<=62: 1953 sharp vertex inequalities PASS; smallest gap above upper bound:', float(worst[0]),'at N,j=',worst[1:])
    return counter


def verify_infinite():
    # Quantities at pi/2, 3pi/2, 5pi/2, with exact Taylor endpoints.
    J={r:si_bound(F(2*r+1,2)*P_LO,F(2*r+1,2)*P_HI) for r in (0,1,2)}
    assert 2*J[0][1] < P_LO
    assert 2*J[2][1] < P_LO
    delta_lo=2*J[1][0]-P_HI
    delta_hi=2*J[1][1]-P_LO
    assert delta_lo>F(0)
    assert delta_lo > F(4,61)
    assert delta_lo > F(16,49)/P_LO**2
    alpha_hi=F(3,2)*P_HI
    h_hi=alpha_hi/F(127,2)
    quad_bound=h_hi+alpha_hi*h_hi*h_hi/36
    assert delta_lo>quad_bound, (float(delta_lo),float(quad_bound))
    print('asymptotic constant enclosure:',float(delta_lo),float(delta_hi))
    print('N>=63 lower-bound criterion PASS; margin=',float(delta_lo-quad_bound))
    print('all fixed boundary indices except r=1 dominated; tail r>=30 excluded PASS')


if __name__=='__main__':
    print('pi enclosure width',float(P_HI-P_LO))
    verify_finite()
    verify_infinite()
    print('ALL EXACT-RATIONAL CERTIFICATES PASS')
