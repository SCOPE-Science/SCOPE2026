"""Independent arithmetic spot checks for logarithmically weighted Bergman kernels."""
import mpmath as mp
mp.mp.dps = 65

def K(s,z):
    if not z:
        return mp.mpf(1)
    return mp.polylog(-s,z)/z

def predicted(m):
    return (mp.pi**2/(2*m+1) * (2**(2*m+1)-1)/(2**(2*m+2)-1)
            *mp.zeta(2*m+1)/mp.zeta(2*m+2))

print('moment checks: integral [-log(t)]^(s-1) t^n/Gamma(s)')
for s in (mp.mpf('0.7'), mp.mpf('2'), mp.mpf('3.3'), mp.mpf('6')):
    for n in (0,1,4):
        num = mp.quad(lambda x: mp.exp(-x*(n+1)) *x**(s-1)/mp.gamma(s), [0,1,mp.inf])
        ref = (n+1)**(-s)
        err = abs(num-ref)
        assert err < mp.mpf('1e-35'), (s,n,err)
        print('moment',mp.nstr(s,4),n,mp.nstr(err,3))

print('crossing velocities (ratio, odd-zeta formula, numerical finite differences)')
for m in range(1,7):
    s0=2*m
    e=mp.mpf('0.0001')
    vp=-mp.diff(mp.altzeta, -s0)/mp.altzeta(-s0-1)
    vf=predicted(m)
    assert abs(vp-vf)<mp.mpf('1e-50')
    zp=mp.findroot(lambda z: K(s0+e,z),(-1+vp*e, -1+vp*e*mp.mpf('0.7')))
    zm=mp.findroot(lambda z: K(s0-e,z),(-1-vp*e,-1-vp*e*mp.mpf('0.7')))
    vnum=(zp-zm)/(2*e)
    assert abs(vnum-vf)<mp.mpf('0.0001'),(m,vnum,vf)
    print(m,'analytic',mp.nstr(vf,22),'finite_difference',mp.nstr(vnum,22),
          'root_inside?', bool(abs(zp)<1),'root_outside?',bool(abs(zm)>1))

print('Eulerian interior root counts at integer threshold')
import sympy as sp
z=sp.symbols('z')
u=1/(1-z)
for m in range(1,7):
    for _ in range(2 if m==1 else 2):
        u=sp.cancel(u+z*sp.diff(u,z))
    pol=sp.cancel((1-z)**(2*m+1)*u)
    p=sp.Poly(pol,z)
    roots=sp.polys.polytools.intervals(p,eps=sp.Rational(1,100000000))
    neg_roots=[]
    for ((a,b), mult) in roots:
        assert mult==1
        neg_roots.append(float((a+b)/2))
    count=sum(-1<r<0 for r in neg_roots)
    assert count==m-1
    print(m,'total',len(neg_roots),'strict_inner',count,'boundary -1',p.eval(-1))
print('All checks passed')
