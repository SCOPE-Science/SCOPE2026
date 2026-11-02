#!/usr/bin/env python3
"""Independent numerical and symbolic checks of local fixed-point expansions.

Analytical completeness and asymptotics are proved in RESULT.md; finite checks
are reproducibility aids, not substitutes for the proof.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 90
x, y, a, b = sp.symbols('x y a b', positive=True, real=True)
phase = a*sp.pi/x+b*y
other = b*sp.pi*y+a*x
F = sp.Matrix([sp.sin(phase)**2,sp.sin(other)**2])
J = F.jacobian([x,y])
J0 = sp.Matrix([[-a*sp.pi/x**2*sp.sin(2*phase), b*sp.sin(2*phase)],
                [a*sp.sin(2*other),b*sp.pi*sp.sin(2*other)]])
assert all(sp.simplify(z)==0 for z in J-J0)
expected_det = -a*b*(sp.pi**2/x**2+1)*sp.sin(2*phase)*sp.sin(2*other)
assert sp.simplify(J.det()-expected_det)==0
jet = a**2*x**2 + 2*a**3*b*sp.pi*x**3
assert sp.simplify(sp.series(sp.sin(b*sp.pi*jet+a*x)**2,x,0,4).removeO()-jet)==0
checks=6

# Local inverse Y(x) solved on the small branch with a bracket based on its
# analytic y ~ a^2*x^2 germ.
def Y(x,a,b):
    def h(y): return y-mp.sin(b*mp.pi*y+a*x)**2
    hi=4*a*a*x*x
    while h(hi)<0 and hi<mp.mpf('0.05'):
        hi*=2
    assert h(0)<0 and h(hi)>0, (a,b,x,hi,h(hi))
    lo=mp.mpf(0)
    for _ in range(320):
        mid=(lo+hi)/2
        if h(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def point(n,s,a,b):
    def equation(x):
        return a*mp.pi/x+b*Y(x,a,b)-n*mp.pi-s*mp.asin(mp.sqrt(x))
    # for large n, endpoints bracket the root
    lo=a/(n+mp.mpf('0.6'))
    hi=a/(n-mp.mpf('0.6'))
    assert 0<lo<hi<1
    assert equation(lo)>0 and equation(hi)<0, (n,s,a,b)
    for _ in range(245):
        m=(lo+hi)/2
        if equation(m)>0: lo=m
        else:hi=m
    z=(lo+hi)/2
    return z, Y(z,a,b)

for aa,bb in [('0.8','0.6'),('1.2','1.1'),('2.1','1.5')]:
    aa=mp.mpf(aa);bb=mp.mpf(bb)
    for n in ([400,800,1600] if aa>2 else [100,200,400]):
        points={}
        for s in [-1,+1]:
            xx,yy=point(n,s,aa,bb)
            points[s]=(xx,yy)
            theta=aa*mp.pi/xx+bb*yy
            phi=bb*mp.pi*yy+aa*xx
            assert abs(mp.sin(theta)**2-xx)<mp.mpf('1e-65')
            assert abs(mp.sin(phi)**2-yy)<mp.mpf('1e-65')
            checks+=2
            assert abs(yy/(aa**2*xx**2)-1) < mp.mpf('0.2')
            checks+=1
            st=mp.sin(2*theta); su=mp.sin(2*phi)
            A=-aa*mp.pi/xx**2*st
            B=bb*st
            C=aa*su
            D=bb*mp.pi*su
            tr=A+D;det=A*D-B*C
            disc=tr**2-4*det
            assert disc>0
            unstable=(tr-mp.sqrt(disc))/2 if A<0 else (tr+mp.sqrt(disc))/2
            stable=det/unstable
            assert abs(unstable)>1 and abs(stable)<1
            assert (-s*unstable)>0 and stable>0
            ratio_u=unstable/(-s*2*mp.pi/mp.sqrt(aa)*n**mp.mpf('1.5'))
            ratio_s=stable/(2*aa**2*bb*mp.pi/n)
            assert abs(ratio_u-1)<mp.mpf('0.04') and abs(ratio_s-1)<mp.mpf('0.08'),(n,s,ratio_u,ratio_s)
            checks+=5
            leading=aa/n-s*aa**mp.mpf('1.5')/(mp.pi*n**mp.mpf('2.5'))
            assert abs(xx-leading)<(mp.mpf(1000)/n**mp.mpf('3.5'))
            checks+=1
        assert points[-1][0]>points[+1][0]
        gap=points[-1][0]-points[+1][0]
        ratio=gap/(2*aa**mp.mpf('1.5')/(mp.pi*n**mp.mpf('2.5')))
        assert abs(ratio-1)<mp.mpf('0.04'), (aa,bb,n,ratio)
        checks+=2
    print(f'a={aa}, b={bb}: three bands, both branches, residuals and multipliers checked')
print(f'PASS: {checks} symbolic/numerical assertions')
