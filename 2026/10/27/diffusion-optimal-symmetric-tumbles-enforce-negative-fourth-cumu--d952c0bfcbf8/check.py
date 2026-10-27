"""Independent Fourier-generator and symbolic checks for an optimal-diffusion fourth-cumulant law.

Run with Python, sympy, mpmath. No external data or network required.
"""
import math
import random
import sympy as s
import mpmath as mp

checks = 0

def demand(ok, context):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(context)

A, B, W, speed, dr = s.symbols('a b w v d', positive=True, real=True)
z = A-s.I*W
z2 = B-2*s.I*W
real_complex = lambda expr: s.factor((expr+s.conjugate(expr))/2)
q2 = speed**2 * A / (2*(A**2+W**2))
q4 = speed**4*(real_complex(1/(z**2*z2))/8 - (A/(A**2+W**2))*((A**2-W**2)/(A**2+W**2)**2)/4)
K4 = s.factor(24*q4)
expected = 3*speed**4*(A**4*B-2*A**3*B**2-12*A**3*W**2+2*A*B**2*W**2+4*A*W**4-B*W**4)/((A**2+W**2)**3*(B**2+4*W**2))
demand(s.simplify(K4-expected)==0, 'fourth cumulant closed form')
demand(s.simplify(K4.subs(A,W)+3*speed**4/(W*(B**2+4*W**2)))==0,'interior optimizer fourth cumulant')
demand(s.simplify(K4.subs({A:dr,B:4*dr})+3*dr**3*speed**4*(7*dr**2-5*W**2)/((dr**2+W**2)**3*(4*dr**2+W**2)))==0,'boundary optimizer fourth cumulant')
opt_interior_excess=s.factor((K4.subs(A,W))/( (2*q2.subs(A,W))**2))
demand(s.simplify(opt_interior_excess+12*W/(B**2+4*W**2))==0,'interior excess kurtosis coefficient')
opt_boundary_excess=s.factor(K4.subs({A:dr,B:4*dr}) / ((2*q2.subs(A,dr))**2))
demand(s.simplify(opt_boundary_excess+3*dr*(7*dr**2-5*W**2)/((dr**2+W**2)*(4*dr**2+W**2)))==0,'boundary excess coefficient')
demand(s.simplify(opt_interior_excess.subs({B:4*dr,W:dr})-opt_boundary_excess.subs(W,dr))==0,'joining optimizer branches')

# Feynman--Kac angular generator in Fourier basis -2,-1,0,1,2;
#  mode +/-2 suffices for quartic perturbation coefficients.
mp.mp.dps=50

def sample_case(d, w, rate, a_turn, b_turn, vv):
    # e^{iθ} decay d+rate(1-c1) - i*w, and e^{2iθ} decay 4d+rate(1-c2)-2i*w
    # symmetric turn distribution is represented via its first two cosine moments.
    an=d+rate*(1-a_turn)
    bn=4*d+rate*(1-b_turn)
    q2_exact=vv*vv*an/(2*(an*an+w*w))
    m1=mp.mpc(an,-w);m2=mp.mpc(bn,-2*w)
    q4_exact=vv**4*(mp.re(1/(m1*m1*m2))/8-mp.re(1/m1)*mp.re(1/(m1*m1))/4)
    k=mp.mpf('0.001')
    M=mp.matrix(5)
    for idx,n in enumerate(range(-2,3)):
        m=mp.mpf(n*n)*d+rate*(1-b_turn if abs(n)==2 else (1-a_turn if abs(n)==1 else 0))
        M[idx,idx]=mp.mpc(-m,n*w)
        if idx: M[idx,idx-1]=vv*k/2
        if idx<4: M[idx,idx+1]=vv*k/2
    eigs,_ = mp.eig(M)
    leading=min(eigs,key=lambda x:abs(x))
    real_lambda=mp.re(leading)
    coeff=(real_lambda-q2_exact*k*k)/(k**4)
    demand(abs(mp.im(leading))<mp.mpf('1e-35'),'leading root imaginary')
    demand(abs(coeff-q4_exact)<mp.mpf('0.00002')*max(1,abs(q4_exact)),('q4 Fourier eigenvalue',float(coeff),float(q4_exact)))
    return float(24*q4_exact),float(an),float(bn)

cases=[
(1,2,1,0,1,1),
(1,2,1,0,math.sqrt(3)/2,1),
(1,2,1,0,0,2),
(1,0,0,0,1,1),
(1,0.7,0,0,1,1),
(0.5,3,1.8,0.2,0.64,1.5),
(2.5,1.4,0.1,-0.2,0.28,0.8),
(0.6,2.4,10,-0.1,0.6,1.3),
]
for p in cases: sample_case(*p)

rng=random.Random(20261020)
for j in range(350):
    d=rng.uniform(.1,5)
    w=rng.uniform(0,8)
    c1=rng.uniform(-1,.9)
    c2=2*c1*c1-1 # symmetric fixed-angle tumble distribution
    r_opt=max(0,w-d)/(1-c1)
    a=d+r_opt*(1-c1);b=4*d+r_opt*(1-c2)
    kk=float(expected.subs({A:a,B:b,W:w,speed:1.0}))
    demand(kk<0,'negative at optimizer')
    sig= a/(a*a+w*w)
    ec=kk/sig**2
    target=(-12*w/(b*b+4*w*w) if w>d else -3*d*(7*d*d-5*w*w)/((d*d+w*w)*(4*d*d+w*w)))
    demand(abs(ec-target)<=3e-10*max(1,abs(target)), 'excess coefficient exact')
    # verify lambda* maximizes the second-cumulant growth
    ks=(0,.5,1,2,4,10)
    for c in ks:
        r_alt=(c*r_opt+1e-3*c) if r_opt else c
        a_alt=d+r_alt*(1-c1)
        sig_alt=a_alt/(a_alt*a_alt+w*w)
        demand(sig_alt<=sig+1e-12,'diffusion optimality')

print(f'{checks} independent symbolic, tilted-generator and parameter assertions passed')
print('example optimized omega=2, Drot=1, c1=0, c2=1:', sample_case(1,2,1,0,1,1))
print('example nonoptimized omega=2, Drot=1, c1=0, c2=sqrt(3)/2, rate=20:',sample_case(1,2,20,0,mp.sqrt(3)/2,1))
