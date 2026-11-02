"""Numerical and algebraic spot-checks of the stated stationary cusp theorem.

Requires Python 3.10+ and mpmath 1.3+. This finite checker supplements, not
replaces, the analytic uniform Taylor expansion and implicit-function proof.
"""
import mpmath as mp

mp.mp.dps = 50
Q = mp.mpf

def original_f(D, h):
    if h == 0:
        return Q('0.5') + mp.sqrt(D) + D
    h = abs(h)
    R = mp.sqrt(1 + 4 * D / h**2)
    t = mp.tanh(h / (2 * D))
    return D * (1 + (1 + (R + 2 * D / h) * t) / (h * (t + R)))

def stable_f(D, h):
    s = mp.sqrt(D)
    if h == 0:
        return D + s + Q('0.5')
    b = abs(h) / D
    u = s / mp.sqrt(4 + s*s*b*b)
    t = mp.tanh(b / 2)
    return D + (u + (1+2*u)*t/b) / (1 + u*b*t)

def s_critical(beta):
    return (beta - 2 + mp.sqrt(beta**2 + 4*beta - 4))/4

def alpha_critical(beta):
    s = s_critical(beta)
    return (s*s+s+Q('0.5'))**beta / s**(2*(beta-1))

def scaled_G(y,z,e):
    beta=1+e
    D=e*e*y
    h=e**Q('2.5')*z
    return (beta*mp.log(stable_f(D,h))-(beta-1)*mp.log(D)-mp.log(alpha_critical(beta)))/e

def universal_F(y,z):
    return 2*(mp.sqrt(y)-1)-mp.log(y)-z*z/(12*y*y)

checks=0

def close(x,y,tol=Q('1e-35')):
    global checks
    if abs(x-y) > tol * max(1,abs(x),abs(y)):
        raise AssertionError(f'check failed: {mp.nstr(x,25)} vs {mp.nstr(y,25)}')
    checks+=1

# Match exact stationary formula in the source against a nonsingular reparameterization.
for D,h in [(Q('.5'),Q('.03')),(Q('2'),Q('.7')),(Q('.0001'),Q('.000001')),
            (Q('3'),Q('.004')),(Q('.05'),Q('.2')),(Q('0.001'),Q('0.00004'))]:
    close(original_f(D,h),stable_f(D,h))

# The zero-field critical point is the unique positive stationary minimum.
for beta in [Q('1.001'),Q('1.01'),Q('1.1'),Q('1.8'),Q('2.2'),Q('4')]:
    s=s_critical(beta)
    close(2*s*s+(2-beta)*s-(beta-1), Q('0'))
    f0=lambda v:Q('.5')+v+v*v
    a=lambda v:f0(v)**beta / v**(2*(beta-1))
    assert a(s*Q('.9'))>a(s) and a(s*Q('1.1'))>a(s)
    checks+=1

# The cubic cusp equations of the universal limiting profile are exact.
y_star=Q(16)/25
z_star=mp.sqrt(Q(1536)/3125)
Fy=lambda y,z:mp.diff(lambda t:universal_F(t,z),y)
Fyy=lambda y,z:mp.diff(lambda t:universal_F(t,z),y,2)
close(Fy(y_star,z_star),0)
close(Fyy(y_star,z_star),0)
close(mp.diff(lambda y:universal_F(y,z_star),y_star,3),1/y_star**3)
close(mp.diff(lambda z:Fy(y_star,z),z_star),z_star/(3*y_star**3))
close(universal_F(y_star,z_star),2*mp.log(Q(5)/4)-Q('.5'))

# Uniform convergence at representative points and the predicted finite-epsilon
# cusp approach, without using finite checks to assert the infinite theorem.
for y,z in [(Q('.64'),Q('.70')),(Q('1.4'),Q('.3')),(Q('.31'),Q('.5'))]:
    d1=abs(scaled_G(y,z,Q('.02'))-universal_F(y,z))
    d2=abs(scaled_G(y,z,Q('.01'))-universal_F(y,z))
    d3=abs(scaled_G(y,z,Q('.005'))-universal_F(y,z))
    assert d3<d2<d1
    checks+=1

cusp_data=[]
for e in [Q('.02'),Q('.01'),Q('.005')]:
    def dy(y,z):return mp.diff(lambda v:scaled_G(v,z,e),y)
    def dyy(y,z):return mp.diff(lambda v:scaled_G(v,z,e),y,2)
    yc,zc=mp.findroot((dy,dyy),(y_star,z_star),tol=Q('1e-32'))
    close(dy(yc,zc),0,Q('1e-25'))
    close(dyy(yc,zc),0,Q('1e-25'))
    assert yc>0 and zc>0
    assert mp.diff(lambda v:scaled_G(v,zc,e),yc,3)>0
    assert mp.diff(lambda z:dy(yc,z),zc)>0
    checks+=3
    cusp_data.append((e,yc,zc,scaled_G(yc,zc,e)))
assert abs(cusp_data[2][1]-y_star)<abs(cusp_data[1][1]-y_star)<abs(cusp_data[0][1]-y_star)
assert abs(cusp_data[2][2]-z_star)<abs(cusp_data[1][2]-z_star)<abs(cusp_data[0][2]-z_star)
checks+=2

print(f'{checks} checks passed')
print('universal cusp y =',mp.nstr(y_star,22),' z =',mp.nstr(z_star,22))
print('universal normalized log-level =',mp.nstr(universal_F(y_star,z_star),22))
for e,y,z,g in cusp_data:
    print(f'epsilon={e}: y={mp.nstr(y,17)}, z={mp.nstr(z,17)}, G={mp.nstr(g,17)}')
