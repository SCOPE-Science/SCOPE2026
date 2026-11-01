"""High precision test of the asymmetric hyperbolic two-cut onset.

Directly evaluates the two unequal-cap area and mean-curvature formulas,
solves the exact area constraint, and compares with the proved expansions.
Numerical tests are supporting evidence, not the proof.
"""
import mpmath as mp
mp.mp.dps=55
P=mp.pi
XSTAR=mp.mpf(10)/(9*P)
CGAIN=25*mp.sqrt(3)/(1458*P*P)
CASYM=mp.sqrt(3)/24

def cap_area(v,u):
    a=mp.sqrt(u)
    return v*(mp.cos(a)-1) + mp.sqrt(1+v*mp.sin(a)**2)-1

def cap_curvature(v,u):
    a=mp.sqrt(u)
    return 2*mp.sqrt(v*(v+1))*(mp.cos(a)-1)+mp.sqrt(v)*mp.sin(a)*mp.atan(mp.sqrt(1+v)*mp.tan(a))

def deficit(delta,u1,u2):
    T=mp.mpf('0.5')+delta/(4*P)
    func=lambda v:v+(cap_area(v,u1)+cap_area(v,u2))/2-T
    v=mp.findroot(func,(T-mp.mpf('0.0001'),T+mp.mpf('0.0001')))
    S=4*P*v+2*P*(cap_area(v,u1)+cap_area(v,u2))
    assert abs(S-(2*P+delta))<mp.mpf('1e-46')
    M=8*P*mp.sqrt(v*(1+v))+2*P*(cap_curvature(v,u1)+cap_curvature(v,u2))
    Msphere=8*P*mp.sqrt(T*(1+T))
    return M-Msphere

def check():
    for d in (mp.mpf('.12'),mp.mpf('.06'),mp.mpf('.03')):
        vstar=d*XSTAR
        E=deficit(d,vstar,vstar)
        Eone=deficit(d,vstar,0)
        h=XSTAR/3
        Easym=deficit(d,d*(XSTAR+h),d*(XSTAR-h))
        predicted=-CGAIN*d**3
        asym_pred=CASYM*h*h*d**3
        print('delta',mp.nstr(d,4),'two-opt/d^3',mp.nstr(E/d**3,13),'pred',mp.nstr(predicted/d**3,13))
        print(' one-opt/d^3',mp.nstr(Eone/d**3,13),'pred',mp.nstr(predicted/(2*d**3),13))
        print(' asymmetry-loss/d^3',mp.nstr((Easym-E)/d**3,13),'pred',mp.nstr(asym_pred/d**3,13))
        assert E<Eone<0 and Easym>E
        assert abs(E/predicted-1)<mp.mpf('.12')
        assert abs((Easym-E)/asym_pred-1)<mp.mpf('.20')
    print('PASS: direct independent cap expressions, exact area, two-versus-one-cut, asymmetry cost')
if __name__=='__main__':check()
