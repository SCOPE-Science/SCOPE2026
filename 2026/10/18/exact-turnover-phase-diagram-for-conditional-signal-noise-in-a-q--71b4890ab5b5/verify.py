"""Independent algebraic and numerical checks for a cell-signal Gaussian noise theorem.

Run: python verify.py
Requires SymPy >=1.12 and mpmath >=1.3.
This script supplements the analytic proof; finite checks are not a proof of its quantifiers.
"""

import sympy as sp
import mpmath as mp


def symbolic_covariance_checks():
    p, q, B, a, k, r, x = sp.symbols('p q B a k r x', positive=True)
    Delta = p*k - a*q
    w = a*x/k
    s = sp.factor(x*(B*Delta+B*k**2*r+a*q**2)/(Delta*(p+k*r)))
    t = sp.factor(a*x*(B*k*r+p*q)/(Delta*(p+k*r)))
    u = w+(a/k)*t
    S = sp.Matrix([[s,t],[t,u]])
    J = sp.Matrix([[-p,q],[r*a,-r*k]])
    noise = sp.diag(2*x*B,2*r*a*x)
    resid=sp.simplify(J*S+S*J.T+noise)
    assert resid == sp.zeros(2)
    ratio=sp.factor((u-t*t/s)/w)
    target=1+a*(B-q)*(B*k*r+p*q)/((p+k*r)*(B*Delta+B*k*k*r+a*q*q))
    assert sp.simplify(ratio-target)==0
    print('PASS: exact 2-by-2 Lyapunov solution and Schur complement')

    z, rho, eta = sp.symbols('z rho eta', real=True)
    h=1-eta*(1-rho)
    f=(z+rho)/((z+1)*(z+h))
    df=sp.factor(sp.diff(f,z))
    expected=((1-rho)**2*(1-eta)-(z+rho)**2)/((z+1)**2*(z+h)**2)
    assert sp.factor(df-expected)==0
    v=sp.symbols('v',positive=True)
    peak=(1-rho)*v-rho
    fpeak=sp.factor(f.subs({z:peak,eta:1-v*v}))
    assert sp.factor(fpeak-1/((1-rho)*(1+v)**2))==0
    print('PASS: derivative factorization and exact peak formula')

    cases=[
      (sp.Rational(13,10),sp.Rational(8,100),sp.Rational(245,100),sp.Integer(2),sp.Integer(1),'maximum'),
      (sp.Integer(1),sp.Rational(3,5),sp.Integer(1),sp.Rational(1,5),sp.Integer(1),'decreasing'),
      (sp.Integer(2),sp.Integer(1),sp.Integer(1),sp.Integer(1),sp.Integer(1),'constant'),
      (sp.Integer(3),sp.Integer(2),sp.Integer(1),sp.Integer(1),sp.Integer(1),'increasing'),
      (sp.Integer(1),sp.Integer(0),sp.Integer(2),sp.Integer(1),sp.Integer(1),'maximum'),
    ]
    for pp,qq,BB,aa,kk,expected_class in cases:
        assert pp*kk-aa*qq>0
        rh=qq/BB
        et=aa*qq/(kk*pp)
        if rh<1:
            zpeak=(1-rh)*sp.sqrt(1-et)-rh
            cls='maximum' if zpeak>0 else 'decreasing'
        elif rh==1:
            cls='constant'
        else:
            cls='increasing'
        assert cls==expected_class
        for rr in [sp.Rational(1,10),sp.Rational(1),sp.Rational(3),sp.Integer(20)]:
            zz=kk*rr/pp
            HH=1-et*(1-rh)
            F=(zz+rh)/((zz+1)*(zz+HH))
            derivative=((1-rh)**2*(1-et)-(zz+rh)**2)/((zz+1)**2*(zz+HH)**2)
            V=1+aa*(BB-qq)/(kk*pp)*F
            assert V>0
            if cls=='increasing':assert (BB-qq)*derivative>0
            if cls=='decreasing':assert (BB-qq)*derivative<0
            if cls=='constant':assert V==1
    print('PASS: five exactly rational phase-regime examples')


def reference_case_checks():
    mp.mp.dps=75
    XX=sp.symbols('X')
    P=-sp.Rational(33,50)-XX+sp.Rational(536,25)*XX**4-16*XX**5
    lo=sp.Rational(1296749526,10**9)
    hi=sp.Rational(1296749527,10**9)
    assert P.subs(XX,lo)>0 and P.subs(XX,hi)<0
    assert P.subs(XX,1)>0 and P.subs(XX,2)<0
    print('PASS: exact rational bracket for the large positive equilibrium')

    x=mp.findroot(lambda v: -mp.mpf(33)/50-v+mp.mpf(536)/25*v**4-16*v**5,
                  (mp.mpf('1.29674'),mp.mpf('1.29676')))
    w=2*x
    b=mp.mpf('0.5')+2*w**4/(1+w**4)
    p=x
    q=x*8*w**3/(1+w**4)**2
    a=mp.mpf(2)
    k=mp.mpf(1)
    Delta=p*k-a*q
    assert Delta>0 and q<b
    eta=a*q/(k*p)
    rho=q/b
    zstar=(1-rho)*mp.sqrt(1-eta)-rho
    assert zstar>0
    rstar=p*zstar/k
    vmax=1+a*b/(k*p*(1+mp.sqrt(1-eta))**2)
    assert mp.mpf('1.12283727349')<rstar<mp.mpf('1.12283727350')
    assert mp.mpf('2.01464895217')<vmax<mp.mpf('2.01464895218')
    def get_C(r):
        sig_xx=x*(b*Delta+b*k*k*r+a*q*q)/(Delta*(p+k*r))
        sig_xw=a*x*(b*k*r+p*q)/(Delta*(p+k*r))
        sig_ww=w+(a/k)*sig_xw
        J=mp.matrix([[-p,q],[r*a,-r*k]])
        S=mp.matrix([[sig_xx,sig_xw],[sig_xw,sig_ww]])
        noise=mp.matrix([[2*x*b,0],[0,2*r*a*x]])
        R=J*S+S*J.T+noise
        assert max(abs(R[i,j]) for i in range(2) for j in range(2))<mp.mpf('1e-65')
        return (sig_ww-sig_xw**2/sig_xx)/w
    for rr,bracket in [(mp.mpf('.5'),(mp.mpf('1.88052'),mp.mpf('1.88053'))),
                       (mp.mpf('1'),(mp.mpf('2.01152'),mp.mpf('2.01153'))),
                       (mp.mpf('256'),(mp.mpf('1.01835'),mp.mpf('1.01837')))]:
        value=get_C(rr)
        assert bracket[0]<value<bracket[1]
    assert abs(get_C(rstar)-vmax)<mp.mpf('1e-65')
    assert get_C(mp.mpf('1'))<vmax and get_C(mp.mpf('2'))<vmax
    print('PASS: reference model, published variance samples, and unique optimum')
    print('r_star =',mp.nstr(rstar,35))
    print('V_max  =',mp.nstr(vmax,35))


if __name__=='__main__':
    symbolic_covariance_checks()
    reference_case_checks()
