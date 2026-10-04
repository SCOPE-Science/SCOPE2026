from math import acos, cos, cosh, pi, sin, sinh

def profile(n,d):
    t=pi/n; u=sinh(d/2)**2
    a=acos((u+cos(t))/(1+u))
    return a,n*a*sinh(d),n*a*(1+cosh(d))-2*pi

def reconstruct(n,d):
    t=pi/n
    sr2=(cosh(d)-1)/(1+cos(t))
    cs=1+sr2*(1-cos(2*t))
    ca=(cosh(d)**2-cs)/(sinh(d)**2)
    return sr2,cs,acos(max(-1,min(1,ca)))
for n in range(3,80,2):
    for d in (0.03,0.2,0.7,1.5,3.0):
        a,L,A=profile(n,d); sr2,cs,a2=reconstruct(n,d)
        assert sr2>0 and cs>1 and abs(a-a2)<1e-9
        assert abs((A+2*pi)-L*cosh(d/2)/sinh(d/2))<1e-9
        assert A>0 and L>0 and a<pi/n+1e-12
for n in (3,5,9,21):
    d=1e-4; a,L,A=profile(n,d); t=pi/n
    coeff=n/2*(t-__import__('math').tan(t/2))
    assert abs(L/d-pi)<1e-7
    assert abs(A/d**2-coeff)<5e-6
for d in (0.2,0.8,2.0):
    n=10001; a,L,A=profile(n,d)
    assert abs(L-2*pi*sinh(d/2))<3e-8
    assert abs(A-2*pi*(cosh(d/2)-1))<3e-8
print('VERIFY_OK regular hyperbolic Reuleaux profile')
