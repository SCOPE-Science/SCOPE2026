from mpmath import mp
mp.dps=80
f=mp.mpf('1.5'); p=mp.mpf('4'); a=mp.mpf('4.8'); b=mp.mpf('5'); c=mp.mpf('2.1')
mu=mp.mpf('1.2'); d=mp.mpf('0.1'); h=mp.mpf('0.01'); k=mp.mpf('0.9'); alpha=mp.mpf('0.6')
def eq1(x,y): return k/(1+f*y)-alpha*x-p*y/(a*x+b*y+c)
def eq2(x,y): return mu*p*x/(a*x+b*y+c)-d-h*y
x,y=mp.findroot((eq1,eq2),(mp.mpf('.12'),mp.mpf('.57')))
assert x>0 and y>0

def calc(x,y):
    D=a*x+b*y+c
    A11=k/(1+f*y)-2*alpha*x-p*y*(b*y+c)/(D*D)
    A12=-p*x*(a*x+c)/(D*D)
    B12=-k*f*x/(1+f*y)**2
    A22=-d-2*h*y
    C21=mu*p*y*(b*y+c)/(D*D)
    C22=mu*p*x*(a*x+c)/(D*D)
    P=-(A11+A22+C22)
    Q=A11*(A22+C22)-C21*A12
    R=-C21*B12
    disc=(P*P-2*Q)**2-4*(Q*Q-R*R)
    zp=(-(P*P-2*Q)+mp.sqrt(disc))/2
    zm=(-(P*P-2*Q)-mp.sqrt(disc))/2
    assert zp>0 and zm<0
    om=mp.sqrt(zp)
    co=(zp-Q)/R; si=P*om/R
    assert abs(co*co+si*si-1)<mp.mpf('1e-60')
    phi=mp.atan2(si,co)
    if phi<0: phi += 2*mp.pi
    tau=phi/om
    lam=1j*om
    Delta=lam*lam+P*lam+Q+R*mp.e**(-lam*tau)
    dl=R*lam*mp.e**(-lam*tau)/(2*lam+P-R*tau*mp.e**(-lam*tau))
    return (D,A11,A12,B12,A22,C21,C22,P,Q,R,zp,zm,om,tau,Delta,dl)
vals=calc(x,y)
D,A11,A12,B12,A22,C21,C22,P,Q,R,zp,zm,om,tau,Delta,dl=vals
assert P>0 and Q+R>0 and R>0
assert abs(Delta)<mp.mpf('1e-60')
assert mp.re(dl)>0
assert abs(tau-mp.mpf('4.87168883017987792454432151555'))<mp.mpf('1e-28')
reported=mp.mpf('4.5923')
lam=1j*om
res=lam*lam+P*lam+Q+R*mp.e**(-lam*reported)
assert abs(res)>mp.mpf('1e-3')
rounded=calc(mp.mpf('0.1219'),mp.mpf('0.5702'))
tau_r=rounded[13]
assert abs(tau_r-mp.mpf('4.874589989058015'))<mp.mpf('2e-15')
assert abs(tau_r-reported)>mp.mpf('0.28')
print('VERIFY_OK')
print('equilibrium_x =', mp.nstr(x,30))
print('equilibrium_y =', mp.nstr(y,30))
print('P =', mp.nstr(P,30))
print('Q =', mp.nstr(Q,30))
print('R =', mp.nstr(R,30))
print('z_plus =', mp.nstr(zp,30))
print('z_minus =', mp.nstr(zm,30))
print('omega =', mp.nstr(om,30))
print('tau_first =', mp.nstr(tau,30))
print('crossing_speed_real =', mp.nstr(mp.re(dl),30))
print('rounded_equilibrium_tau =', mp.nstr(tau_r,30))
print('reported_tau_residual =', mp.nstr(abs(res),30))
