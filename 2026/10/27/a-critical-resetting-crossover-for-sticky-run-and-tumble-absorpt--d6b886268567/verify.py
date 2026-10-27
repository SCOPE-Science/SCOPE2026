#!/usr/bin/env python3
"""Standalone deterministic checks for the half-index sticky-boundary scaling law.

Requires Python 3 and mpmath. It checks identities and finite-parameter
convergence, not the infinite-limit proof, originality, or external validation.
"""
import mpmath as mp
mp.mp.dps = 55
checks = 0

def check(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks += 1

def close(a, b, tol, label):
    check(abs(a-b) <= tol, label + ': error=' + mp.nstr(abs(a-b), 12))

def bare(u, alpha, v, x0, direction):
    root = mp.sqrt(u*(u+2*alpha))
    b = alpha/(u+alpha+root)
    xfac = mp.exp(-x0*root/v)
    return xfac if direction == '-' else b*xfac

def wall(u, alpha):
    return alpha/(u+alpha+mp.sqrt(u*(u+2*alpha)))

def reset_first(s, r, alpha, v, x0, direction, post):
    a = bare(s+r, alpha, v, x0, direction)
    g = a if post=='home' else wall(s+r, alpha)
    return (s*g+r*a)/(s+r*a)

def bound_laplace(s, scale):
    # P(W>t) = (1+t/scale)^(-1/2).
    ss=s*scale
    return 1-mp.sqrt(mp.pi*ss)*mp.exp(ss)*mp.erfc(mp.sqrt(ss))

def exact(theta, z, R, alpha, v, x0, direction, post, scale):
    s=theta**2*z
    r=theta**2*R
    a=reset_first(s,r,alpha,v,x0,direction,'home')
    b=reset_first(s,r,alpha,v,x0,direction,post)
    phi=bound_laplace(s,scale)
    return theta*a*phi/(1-(1-theta)*phi*b)

def A_coeff(alpha,v,x0,direction,post):
    aw=mp.sqrt(2/alpha)
    return aw if post=='wall' else x0*mp.sqrt(2*alpha)/v+(aw if direction=='+' else 0)

def predicted(z,R,alpha,v,x0,direction,post,scale):
    A=A_coeff(alpha,v,x0,direction,post)
    c=mp.sqrt(mp.pi*scale)
    return 1/(1+c*mp.sqrt(z)+A*z/mp.sqrt(z+R))

# Independent verification of bare first-passage ODE and initial direction.
for alpha,v,x0 in [(mp.mpf('0.6'),mp.mpf('1.5'),mp.mpf('0.9')),
                   (mp.mpf('2.0'),mp.mpf('0.7'),mp.mpf('1.8'))]:
    for s in map(mp.mpf,['0.01','0.2','1.7','4.0']):
        for x in map(mp.mpf,['0.0','0.15','1.2']):
            up=lambda y: wall(s,alpha)*mp.exp(-y*mp.sqrt(s*(s+2*alpha))/v)
            um=lambda y: mp.exp(-y*mp.sqrt(s*(s+2*alpha))/v)
            close(v*mp.diff(up,x)+alpha*(um(x)-up(x)),s*up(x),mp.mpf('1e-45'),'backward +')
            close(-v*mp.diff(um,x)+alpha*(up(x)-um(x)),s*um(x),mp.mpf('1e-45'),'backward -')
        close(um(mp.mpf('0')),1,mp.mpf('1e-45'),'target boundary')

# Explicit finite resetting-transform versus independent first-reset renewal identity.
for direction in ['-','+']:
    for post in ['wall','home']:
        for r in map(mp.mpf,['0.02','0.3','2']):
            for s in map(mp.mpf,['0.05','0.5','3']):
                alpha=mp.mpf('1.2');v=mp.mpf('1.5');x0=mp.mpf('0.8')
                a=bare(s+r,alpha,v,x0,direction)
                g=wall(s+r,alpha) if post=='wall' else a
                init=(s+r)*a/(s+r*a)
                rhs=g+r*(1-g)/(s+r)*init
                lhs=reset_first(s,r,alpha,v,x0,direction,post)
                close(lhs,rhs,mp.mpf('1e-45'),'first reset renewal')

# Direct finite-parameter transform must approach the asserted crossover.
for alpha,v,x0,direction in [(mp.mpf('.8'),mp.mpf('1.7'),mp.mpf('1.3'),'-'),
                             (mp.mpf('1.8'),mp.mpf('1.1'),mp.mpf('.7'),'+')]:
    for post in ['wall','home']:
        for z,R in [(mp.mpf('.1'),mp.mpf('0')),(mp.mpf('1.7'),mp.mpf('.4')),
                    (mp.mpf('3.2'),mp.mpf('5.5'))]:
            a=exact(mp.mpf('.016'),z,R,alpha,v,x0,direction,post,mp.mpf('1'))
            b=exact(mp.mpf('.004'),z,R,alpha,v,x0,direction,post,mp.mpf('1'))
            target=predicted(z,R,alpha,v,x0,direction,post,mp.mpf('1'))
            check(abs(b-target)<abs(a-target)*mp.mpf('.36'),'convergence refinement')
            check(abs(b-target)<mp.mpf('0.008'),'finite-transform accuracy')

# Critical tail constants: R>0 is purely bound-controlled; R=0 adds excursion.
for alpha, v, x0, direction, post in [(.8,1.7,1.3,'-','home'),
                                       (.8,1.7,1.3,'-','wall'),
                                       (2.,1.4,.3,'+','home')]:
    alpha,v,x0=map(mp.mpf,[alpha,v,x0])
    A=A_coeff(alpha,v,x0,direction,post)
    c=mp.sqrt(mp.pi)
    for R in [mp.mpf('0'),mp.mpf('0.2'),mp.mpf('5')]:
        z=mp.mpf('1e-16')
        l=predicted(z,R,alpha,v,x0,direction,post,mp.mpf('1'))
        desired=c+(A if R==0 else 0)
        close((1-l)/mp.sqrt(z),desired,mp.mpf('2e-7'),'survival Tauberian coefficient')

# Laplace-order monotonicity under increased critical bulk reset.
for direction in ['-','+']:
    for post in ['wall','home']:
        for z in map(mp.mpf,['0.01','.3','1.9','8']):
            vals=[predicted(z,mp.mpf(str(R)),mp.mpf('1.2'),mp.mpf('1.5'),mp.mpf('.8'),direction,post,mp.mpf('1'))
                  for R in [0,.05,2,12]]
            check(all(a<b for a,b in zip(vals,vals[1:])),'critical reset Laplace ordering')

# Levy density inverse relation: derivative of z/sqrt(z+R) is
# the Laplace transform of t times the proposed positive Levy density.
for R in [mp.mpf('0'),mp.mpf('.4'),mp.mpf('3')]:
    for z in [mp.mpf('.1'),mp.mpf('1.5'),mp.mpf('6')]:
        fprime=(z+2*R)/(2*(z+R)**mp.mpf('1.5'))
        g=lambda t: mp.exp(-(z+R)*t)*(1/(2*mp.sqrt(mp.pi*t))+R*mp.sqrt(t/mp.pi))
        integral=mp.quad(g,[0,1,mp.inf])
        close(fprime,integral,mp.mpf('1e-26'),'Levy kernel derivative')

# The critical home/wall equivalence length is x0=v/alpha for direction '-'.
for alpha,v in [(mp.mpf('.6'),mp.mpf('3')),(mp.mpf('2.2'),mp.mpf('.5'))]:
    x0=v/alpha
    close(A_coeff(alpha,v,x0,'-','home'),A_coeff(alpha,v,x0,'-','wall'),
          mp.mpf('1e-45'),'orientation threshold')
    check(A_coeff(alpha,v,x0/2,'-','home')<A_coeff(alpha,v,x0/2,'-','wall'), 'left small-distance')
    check(A_coeff(alpha,v,x0*2,'-','home')>A_coeff(alpha,v,x0*2,'-','wall'), 'left large-distance')
    check(A_coeff(alpha,v,x0,'+','home')>A_coeff(alpha,v,x0,'+','wall'), 'right orientation')
print(f'PASS: {checks} deterministic analytical/numerical checks')
