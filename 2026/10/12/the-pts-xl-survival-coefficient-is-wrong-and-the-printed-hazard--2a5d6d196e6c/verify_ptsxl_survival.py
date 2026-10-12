from fractions import Fraction
import mpmath as mp

mp.mp.dps = 70

def p_frac(x, theta):
    t = Fraction(theta)
    return t**4 * (x+1) * (x*x + x*(17+6*t*(t+3)) + 6*(3+t*(t+3))**2) / (6*(1+t)**(x+8))

def coeffs_pub(theta):
    t = Fraction(theta)
    w0 = 6*(t**3+3*t**2+4*t+1)*(2*t**4+7*t**3+9*t**2+4*t+1)
    w1 = t**7+6*t**6+18*t**5+87*t**4+146*t**3+45*t**2+6*t
    w2 = 3*t**2*(2*t**3+6*t**2+7*t+1)
    return w0,w1,w2

def coeffs_correct(theta):
    t = Fraction(theta)
    w0,_,w2 = coeffs_pub(theta)
    w1 = 6*t**7+36*t**6+108*t**5+174*t**4+146*t**3+45*t**2+6*t
    return w0,w1,w2

def S_frac(x, theta, corrected=True):
    t = Fraction(theta)
    w0,w1,w2 = coeffs_correct(theta) if corrected else coeffs_pub(theta)
    return (w0+w1*x+w2*x*x+t**3*x**3)/(6*(1+t)**(x+8))

def p_mp(x, theta):
    t = mp.mpf(theta)
    return t**4*(x+1)/(6*(1+t)**(x+8))*(x*x+x*(17+6*t*(t+3))+6*(3+t*(t+3))**2)

def S_mp(x, theta, corrected=True):
    t = mp.mpf(theta)
    if corrected:
        w1 = 6*t**7+36*t**6+108*t**5+174*t**4+146*t**3+45*t**2+6*t
    else:
        w1 = t**7+6*t**6+18*t**5+87*t**4+146*t**3+45*t**2+6*t
    w0 = 6*(t**3+3*t**2+4*t+1)*(2*t**4+7*t**3+9*t**2+4*t+1)
    w2 = 3*t**2*(2*t**3+6*t**2+7*t+1)
    return (w0+w1*x+w2*x*x+t**3*x**3)/(6*(1+t)**(x+8))

# Exact recurrence for integer parameter values.
for theta in [1,2,5,9]:
    for x in range(1,8):
        assert S_frac(x-1,theta,True)-S_frac(x,theta,True) == p_frac(x,theta)

# Printed formula fails the recurrence at a concrete point.
assert S_frac(1,5,False)-S_frac(2,5,False) != p_frac(2,5)

# Corrected closed form matches direct numerical PMF tail summation.
for theta in [mp.mpf('0.3'),mp.mpf('1'),mp.mpf('2.5'),mp.mpf('5')]:
    for x in [0,1,2,5,10]:
        direct = mp.nsum(lambda n: p_mp(n,theta), [x+1, mp.inf])
        closed = S_mp(x,theta,True)
        assert abs(direct-closed) < mp.mpf('1e-45')

# Hazard counterexample.
p2 = p_frac(2,5)
h_pub = p2/S_frac(1,5,False)
h_true = p2/S_frac(1,5,True)
assert h_pub == Fraction(1814375,1739338)
assert h_true == Fraction(1814375,2336838)
assert h_pub > 1 and 0 < h_true < 1

# Stress-strength comparison: R=P(X<Y)=sum p1(x) S2(x).
def R(theta1,theta2,corrected=True):
    return mp.nsum(lambda n: p_mp(n,theta1)*S_mp(n,theta2,corrected), [0, mp.inf])
rt = R(mp.mpf('1'),mp.mpf('2'),True)
rp = R(mp.mpf('1'),mp.mpf('2'),False)
assert abs(rt-mp.mpf('0.212272197530864197530864197530864')) < mp.mpf('1e-30')
assert abs(rp-mp.mpf('0.188655407407407407407407407407407')) < mp.mpf('1e-30')
assert rt > rp

print('VERIFY_OK')
print('h_pub_theta5_x2', float(h_pub))
print('h_true_theta5_x2', float(h_true))
print('R_true_theta1_1_theta2_2', mp.nstr(rt,35))
print('R_printed_survival_theta1_1_theta2_2', mp.nstr(rp,35))
