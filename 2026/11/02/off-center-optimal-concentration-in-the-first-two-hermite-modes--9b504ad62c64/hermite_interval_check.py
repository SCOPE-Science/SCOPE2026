"""Independent numerical checks for the stated two-mode Hermite interval formulas.
No external files or services are required. Standard mpmath and scipy only.
"""
from mpmath import mp
mp.dps=65

def G(a,L):
    a=mp.mpf(a);L=mp.mpf(L)
    u=a+L;v=a-L
    p=(mp.erf(u)-mp.erf(v))/2
    q=p+(v*mp.exp(-v*v)-u*mp.exp(-u*u))/mp.sqrt(mp.pi)
    b=(mp.exp(-v*v)-mp.exp(-u*u))/mp.sqrt(2*mp.pi)
    return p,q,b

def F(a,L):
    p,q,b=G(a,L)
    return (p+q+mp.sqrt((p-q)**2+4*b*b))/2

n=0
for L in ['0.1','0.3','0.7','1','2','3']:
    L=mp.mpf(L)
    curvature=mp.diff(lambda a: F(a,L),mp.mpf('0'),2)
    target=4*L*mp.exp(-L*L)/mp.sqrt(mp.pi)
    assert abs(curvature-target)<mp.mpf('1e-48'),(L,curvature,target)
    assert F(mp.mpf('0.0001'),L)>F(0,L)
    for a in ['0.17','0.6','1.3']:
        assert abs(F(a,L)-F(-mp.mpf(a),L))<mp.mpf('1e-56')
        p,q,b=G(a,L)
        # independently integrate the two diagonal and off-diagonal Hermite kernels.
        p2=mp.quad(lambda x: mp.exp(-x*x)/mp.sqrt(mp.pi),[mp.mpf(a)-L,mp.mpf(a)+L]);
        q2=mp.quad(lambda x: 2*x*x*mp.exp(-x*x)/mp.sqrt(mp.pi),[mp.mpf(a)-L,mp.mpf(a)+L]);
        b2=mp.quad(lambda x: mp.sqrt(2)*x*mp.exp(-x*x)/mp.sqrt(mp.pi),[mp.mpf(a)-L,mp.mpf(a)+L]);
        assert max(abs(p-p2),abs(q-q2),abs(b-b2))<mp.mpf('1e-55')
        n+=4
    n+=2

for L in ['0.1','0.2','0.3','0.4']:
    L=mp.mpf(L)
    a0=1/mp.sqrt(2)
    a_opt=mp.findroot(lambda a: mp.diff(lambda z:F(z,L),a),(mp.mpf('.65'),mp.mpf('.75')))
    assert a_opt>0 and F(a_opt,L)>F(0,L)
    approximation=a0-mp.sqrt(2)*L**4/180
    # Remainder is O(L^6); normalized deviation bounded safely on the grid.
    assert abs(a_opt-approximation)/L**6<mp.mpf('.02'),(L,a_opt,approximation)
    value_approx=4*L/mp.sqrt(mp.pi*mp.e)*(1-L**2/2+mp.mpf(41)*L**4/180)
    assert abs(F(a_opt,L)-value_approx)/L**7<mp.mpf('.3'),(L,F(a_opt,L),value_approx)
    n+=4
print('PASS',n,'deterministic checks')
