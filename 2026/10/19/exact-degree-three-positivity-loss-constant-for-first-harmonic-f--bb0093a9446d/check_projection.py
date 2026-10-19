"""Reproducible numerical checks of the degree-three Fourier-kernel extremum.
The exact global minimization is proved analytically in RESULT.md;
this script checks the isolated critical equations, not their existence in exact arithmetic.
Requires Python 3 and mpmath; run: python check_projection.py
"""
import mpmath as mp

mp.mp.dps = 60
pi = mp.pi

def K(t, a, b):
    return 1 + 2*mp.cos(t) + 2*a*mp.cos(2*t) + 2*b*mp.cos(3*t)

def equations(a, b, alpha, beta, gamma):
    return (
        K(alpha, a, b), K(beta, a, b), K(gamma, a, b),
        mp.sin(2*alpha) - mp.sin(2*beta) + mp.sin(2*gamma),
        mp.sin(3*alpha) - mp.sin(3*beta) + mp.sin(3*gamma),
    )

a,b,alpha,beta,gamma = mp.findroot(
    equations,
    (mp.mpf('0.54'),mp.mpf('0.28'),mp.mpf('1.44'),mp.mpf('1.99'),mp.mpf('2.32')),
    solver='mdnewton',tol=mp.mpf('1e-53'),maxsteps=70)

assert 0 < alpha < beta < gamma < pi
assert all(abs(r) < mp.mpf('1e-50') for r in equations(a,b,alpha,beta,gamma))
root_cos = [mp.cos(t) for t in (alpha,beta,gamma)]
assert root_cos[0] > root_cos[1] > root_cos[2] and all(-1<x<1 for x in root_cos)
assert K(0,a,b) > 0 and K(pi,a,b) < 0

def primitive(t, a, b):
    return t+2*mp.sin(t)+a*mp.sin(2*t)+2*b*mp.sin(3*t)/3

exact_L = (2*(primitive(alpha,a,b)-primitive(beta,a,b)+primitive(gamma,a,b))-pi)/pi
partition_L = mp.fsum(mp.quad(lambda t: abs(K(t,a,b)),[l,r])
                    for l,r in [(0,alpha),(alpha,beta),(beta,gamma),(gamma,pi)])/pi
assert abs(exact_L-partition_L) < mp.mpf('1e-50')
assert 1 < exact_L < 4/pi

gradients = [2*(mp.sin(k*alpha)-mp.sin(k*beta)+mp.sin(k*gamma))/(k*pi)
             for k in (2,3)]
assert max(map(abs, gradients)) < mp.mpf('1e-50')

# Deterministic finite-mesh consistency (not a replacement for analytic proof).
comparisons=0
for length in (512,2048,8192):
    grid = mp.fsum(abs(K((j+mp.mpf('0.5'))*pi/length,a,b))
                   for j in range(length))/length
    assert abs(grid-exact_L) < mp.mpf('0.00005')
    comparisons+=length

# The canonical degree-three delayed de la Vallee-Poussin filter is strictly worse.
vp_a, vp_b = mp.mpf(2)/3, mp.mpf(1)/3
vp_grid = mp.fsum(abs(K((j+mp.mpf('0.5'))*pi/8192,vp_a,vp_b))
                  for j in range(8192))/8192
assert vp_grid > exact_L + mp.mpf('0.02')

# Hessian positivity at the critical point: each boundary is simple.
def Kprime(t):
    return -2*mp.sin(t)-4*a*mp.sin(2*t)-6*b*mp.sin(3*t)
J11=J12=J22=mp.mpf(0)
for t in (alpha,beta,gamma):
    weight=8/(pi*abs(Kprime(t)))
    u,v=mp.cos(2*t),mp.cos(3*t)
    J11+=weight*u*u
    J12+=weight*u*v
    J22+=weight*v*v
assert J11>0 and J22>0 and J11*J22-J12*J12>0

# The Fourier moment constraints are literal, not numerical normalization conventions.
assert abs(mp.quad(lambda t: K(t,a,b),[0,pi])/pi-1) < mp.mpf('1e-50')
assert abs(mp.quad(lambda t: K(t,a,b)*mp.cos(t),[0,pi])/pi-1) < mp.mpf('1e-50')
print('VERIFY_OK: high-precision five-equation residual <1e-50; three simple roots;')
print(f'          exact integral/quadrature agreement <1e-50; {comparisons} mesh evaluations; positive Hessian.')
for key,val in [('a',a),('b',b),('alpha',alpha),('beta',beta),('gamma',gamma),
                ('lambda',exact_L),('canonical_degree3',vp_grid),('degree2',4/pi)]:
    print(key,mp.nstr(val,35))
