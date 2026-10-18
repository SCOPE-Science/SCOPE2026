"""Algebraic and high-precision numerical checks for critical-pencil law."""
import sympy as s
import mpmath as mp

a,b=s.symbols('a b',real=True)
A=s.Matrix([[a,-1],[1,0]])
B=s.Matrix([[b,-1],[1,0]])
C=B**3*A**3
E=A**2
tr=s.expand(s.trace(C))
Q=(a*a-2)*b*b-a*b+4-2*a*a
P=s.expand((E*C)[0,1])
assert s.expand(tr-2-(a*b-1)*Q)==0
assert s.expand(P+(a*a*b-a-b)*(a*a*b*b-2*a*a-a*b-b*b+2))==0
assert s.simplify(Q.subs(b,1))==2-a-a*a
assert s.simplify(Q.subs(b,1/a)+2*(a-1/a)**2)==0
assert s.simplify(Q.subs(b,a*(2-a*a))-(1-a*a)**2*(2-a*a)**2)==0
assert s.rem(s.expand(P+a-C[0,1]),Q,b)==0
assert s.simplify(s.diff(tr,b)-(1-a*b)*(2*(2-a*a)*b+a)-a*Q)==0
assert s.rem(s.expand((2-a*a)**2*C[0,1]+a*a*(b-a*(2-a*a))),Q,b)==0

mp.mp.dps=65
for av in ['0.15','0.5','0.9']:
    aa=mp.mpf(av)
    star=(-aa+mp.sqrt(aa**2+8*(2-aa**2)**2))/(2*(2-aa**2))
    d=(1-aa*star)*(2*(2-aa**2)*star+aa)
    cc=(aa**2)*(star-aa*(2-aa**2))/(2-aa**2)**2
    kappa=aa/cc
    def T(bb):
        return aa**3*bb**3-2*aa**3*bb-2*aa**2*bb**2+2*aa**2-2*aa*bb**3+5*aa*bb+2*bb**2-2
    def PP(bb):
        return -(aa**2*bb-aa-bb)*(aa**2*bb**2-2*aa**2-aa*bb-bb**2+2)
    for m in (30,75,150,300):
        thetaLo=mp.pi/m
        bLo=mp.findroot(lambda x:T(x)-2*mp.cos(thetaLo),(star-mp.mpf('0.1'),star))
        # On this interval the critical Chebyshev endpoint is +a at lower end, negative at star.
        def fun(bb):
            tt=T(bb)
            th=mp.acos(tt/2)
            return PP(bb)*mp.sin(m*th)/th+aa*mp.sin((m-1)*th)/th if th else -m*cc-aa
        lo,hi=bLo,star
        for _ in range(220):
            mid=(lo+hi)/2
            if fun(mid)>0:lo=mid
            else:hi=mid
        root=(lo+hi)/2
        theta=mp.acos(T(root)/2)
        corrected=mp.pi**2/(d*(m+kappa)**2)
        err=star-root-corrected
        print('a=',av,'m=',m,'b_m=',mp.nstr(root,24),'gap=',mp.nstr(star-root,16),'scaled=',mp.nstr(m**2*(star-root),16),'theory=',mp.nstr(mp.pi**2/d,16),'corrected_error=',mp.nstr(err,10))
        assert root<star and theta>0 and theta<mp.pi/m
        # Directly replay all prescribed steps of the legal orbit.
        x,y=mp.mpf('0'),mp.mpf('-1')
        for step,symbol in enumerate('aaabbb'*m+'aa'):
            if x != 0 and abs(x)<mp.mpf('1e-42'):
                x=mp.mpf('0')
            if step > 0:
                assert (x>0 if symbol=='a' else x<0), (av,m,step,symbol)
            x,y=(aa if symbol=='a' else root)*x-y,x
        assert abs(x)<mp.mpf('1e-40') and y>0
        assert mp.isfinite(err)
print('ALL SYMBOLIC AND HIGH-PRECISION CHECKS PASSED')
