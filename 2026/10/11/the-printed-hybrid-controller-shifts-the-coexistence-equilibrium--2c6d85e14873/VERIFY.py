from mpmath import mp
mp.dps = 70

# Printed numerical parameters in Example 7.1/7.2.
h1=h2=mp.mpf('0.5'); a1=a2=mp.mpf('2'); d1=mp.mpf('0.4')
b=mp.mpf('0.1'); d=mp.mpf('0.45'); alpha=mp.mpf('0.6'); k=mp.mpf('0.5')

def bisect(f, lo, hi, n=300):
    flo=f(lo); fhi=f(hi)
    assert flo*fhi < 0
    for _ in range(n):
        mid=(lo+hi)/2; fm=f(mid)
        if fm == 0: return mid
        if flo*fm <= 0:
            hi=mid; fhi=fm
        else:
            lo=mid; flo=fm
    return (lo+hi)/2

# Positive equilibria. After eliminating u2, the prey coordinates solve these cubics.
p_ctl=lambda x: 12*x**3+237*x**2+1186*x-200
p_unc=lambda x: 20*x**3+395*x**2+1946*x-400
xc=bisect(p_ctl, mp.mpf('0'), mp.mpf('1'))
xu=bisect(p_unc, mp.mpf('0'), mp.mpf('1'))
y_of=lambda x: mp.mpf('0.25') + 9*x/(10*(10+x))
yc=y_of(xc); yu=y_of(xu)
assert 0 < xc < 1 and 0 < yc < 1 and 0 < xu < 1 and 0 < yu < 1
# p_ctl' > 0 and p_unc' > 0 for x>0, hence each positive root is unique.
assert 36*xc**2+474*xc+1186 > 0
assert 60*xu**2+790*xu+1946 > 0

# The uncontrolled positive equilibrium is not an equilibrium of the printed controlled system.
F1_old = alpha*xu*(h1-a1*xu)-d1*xu*yu/(1+b*xu)
F2_old = yu*(h2-a2*yu)+d*d1*xu*yu/(1+b*xu)
assert abs(F1_old) > mp.mpf('0.008') and abs(F2_old) < mp.mpf('1e-55')

# Correct linearization of the printed controlled system at (xc,yc).
c1 = alpha*h1 - 2*alpha*a1*xc - d1*yc/(1+b*xc)**2 - k
c2 = d1*xc/(1+b*xc)
c3 = d*d1*yc/(1+b*xc)**2
c5 = a2*yc
C = c2*c3

# At delta=0 the matrix is [[c1+k,-c2],[c3,-c5]].
tr0=(c1+k)-c5
det0=-(c1+k)*c5 + C
disc0=tr0**2-4*det0
lam01=(tr0+mp.sqrt(disc0))/2
lam02=(tr0-mp.sqrt(disc0))/2
assert lam01 < 0 and lam02 < 0

# For lambda=i*w and E=exp(-i*w*delta),
# Delta=(lambda-c1-kE)(lambda+c5E)+c2*c3.
# Eliminating cos(w delta),sin(w delta) yields H(z), z=w^2.
A3 = -2*c1**2 + 4*C + c5**2 - 2*c5*k + k**2
A2 = (-c1**4 + 4*c1**2*C + 2*c1**2*c5**2 - 2*c1**2*c5*k + c1**2*k**2
      - 6*C**2 - 2*C*c5**2 + 4*C*c5*k - 2*C*k**2 + 2*c5**3*k - 2*c5**2*k**2 + 2*c5*k**3)
A1 = (c1**4*c5**2 - 2*c1**2*C**2 - 2*c1**2*C*c5**2 + 2*c1**2*c5**3*k - 2*c1**2*c5**2*k**2
      + 4*C**3 + C**2*c5**2 - 2*C**2*c5*k + C**2*k**2 - 2*C*c5**3*k - 2*C*c5*k**3
      + c5**4*k**2 - 2*c5**3*k**3 + c5**2*k**4)
A0 = c1**2*C**2*c5**2 + 2*c1**2*C*c5**3*k + c1**2*c5**4*k**2 - C**4 + 2*C**2*c5**2*k**2 - c5**4*k**4
H=lambda z: -z**4 + A3*z**3 + A2*z**2 + A1*z + A0
# Descending coefficients have signs -,-,+,+,+: one sign change, hence at most one positive root.
assert A3 < 0 and A2 > 0 and A1 > 0 and A0 > 0
assert H(mp.mpf('0')) > 0 and H(mp.mpf('1')) < 0
zc=bisect(H, mp.mpf('0'), mp.mpf('1'))
wc=mp.sqrt(zc)
# Recover theta=w*delta from the two linear equations in cos(theta), sin(theta).
pr=C-zc; pi=-c1*wc; qr=-c1*c5; qi=(c5-k)*wc; R=-k*c5
den=(pr+R)*(pr-R)+pi*pi
co=((-qr)*(pr-R)-(-pi)*(-qi))/den
si=((pr+R)*(-qi)-pi*(-qr))/den
assert abs(co*co+si*si-1) < mp.mpf('1e-45')
theta=mp.atan2(si,co)
if theta < 0: theta += 2*mp.pi
tauc=theta/wc

# Transversality at the first controlled crossing.
lam=1j*wc; E=mp.e**(-lam*tauc)
Q=(c5-k)*lam-c1*c5; R=-k*c5
Delta=(lam-c1-k*E)*(lam+c5*E)+C
dDl=2*lam-c1 + (c5-k)*E - tauc*Q*E - 2*tauc*R*E**2
dDt=-lam*Q*E - 2*lam*R*E**2
dl=-dDt/dDl
assert abs(Delta) < mp.mpf('1e-40') and mp.re(dl) > 0

# Uncontrolled first crossing for comparison.
a11=h1-2*a1*xu-d1*yu/(1+b*xu)**2
a12=-d1*xu/(1+b*xu)
c21=d*d1*yu/(1+b*xu)**2
q=a2*yu
Cu=-a12*c21
B=(-2*Cu+a11*a11-q*q)
D=Cu*Cu-q*q*a11*a11
roots=(( -B+mp.sqrt(B*B-4*D))/2, (-B-mp.sqrt(B*B-4*D))/2)
zu=max(roots); assert zu>0 and min(roots)<0
wu=mp.sqrt(zu)
Pu=(1j*wu)**2-a11*(1j*wu)+Cu
Qu=q*(1j*wu-a11)
ratio=-Pu/Qu
ang=mp.arg(ratio)
# ratio=e^{-i*w*tau}; choose the least positive phase.
ph=(-ang)%(2*mp.pi)
tauu=ph/wu
assert tauu > 0 and tauc > tauu

print('controlled_equilibrium', mp.nstr(xc,18), mp.nstr(yc,18))
print('old_point_controlled_residual', mp.nstr(F1_old,18), mp.nstr(F2_old,18))
print('controlled_H_coeffs', *[mp.nstr(v,18) for v in (-1,A3,A2,A1,A0)])
print('controlled_frequency', mp.nstr(wc,18))
print('controlled_first_crossing', mp.nstr(tauc,18))
print('controlled_crossing_speed_real', mp.nstr(mp.re(dl),18))
print('uncontrolled_equilibrium', mp.nstr(xu,18), mp.nstr(yu,18))
print('uncontrolled_first_crossing', mp.nstr(tauu,18))
print('threshold_shift', mp.nstr(tauc-tauu,18))
print('VERIFY_OK')
