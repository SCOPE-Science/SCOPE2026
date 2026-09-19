import math
import numpy as np
import sympy as sp

# Quadratic specialization of Algorithm 1 in arXiv:2609.20327v1:
# f_kappa(x,y)=x^2/2-y^2/(2*kappa), L=mu_x=1, mu_y=1/kappa.

def block(kappa: float):
    s = 1.0 / math.sqrt(kappa)
    D = 96.0 + math.sqrt(2.0) * s
    alpha = 96.0 / D
    beta = (8.0 - math.sqrt(2.0) * s) / D
    c = 1.0 + beta
    A = 1.0 - (s*s*c/6.0) * (1.0 - s*s/6.0)
    B = alpha/6.0 - s*s*c/36.0
    M = np.array([[A, B], [-beta*s*s*A, alpha-beta*s*s*B]], dtype=float)
    return M, A

s = sp.symbols('s', nonnegative=True)
r2 = sp.sqrt(2)
D = 96 + r2*s
alpha = 96/D
beta = (8-r2*s)/D
c = 1+beta
A = 1-(s**2*c/6)*(1-s**2/6)
B = alpha/6-s**2*c/36
M = sp.Matrix([[A,B],[-beta*s**2*A,alpha-beta*s**2*B]])
tr = sp.factor(sp.trace(M))
det = sp.factor(M.det())
disc = sp.factor(tr**2-4*det)
assert sp.simplify(det-alpha*A) == 0

P = (1827904*r2*s**9 + 526403904*s**8 + 25242446808*r2*s**7
     + 801870485544*s**6 - 309016435887*r2*s**5 - 9650891352096*s**4
     + 824804176896*r2*s**3 + 36522430267392*s**2
     + 448900890624*r2*s - 42103807672320)
positive_den = 81*(r2*s+96)**4*(r2*s**3+288*s**2+13824*r2*s+442368)
assert sp.simplify(disc - 4*s**2*P/positive_den) == 0

# Q=-P in the degree-9 Bernstein basis on [0,1].
bernstein = [
    sp.Integer(42103807672320),
    42103807672320 - 49877876736*r2,
    41089295720448 - 99755753472*r2,
    39060271816704 - 159452727552*r2,
    sp.Rational(252653312358288,7) - 238787896320*r2,
    sp.Rational(226391620228560,7) - sp.Rational(4831789840137,14)*r2,
    sp.Rational(196178485679298,7) - sp.Rational(3366538972443,7)*r2,
    23413037295906 - sp.Rational(1284023967911,2)*r2,
    sp.Rational(56375192026360,3) - 817161259604*r2,
    14429871867576 - 989932906345*r2,
]
Q_bern = sp.expand(sum(bernstein[k]*sp.binomial(9,k)*s**k*(1-s)**(9-k)
                       for k in range(10)))
assert sp.expand(Q_bern + P) == 0
assert all(bool(sp.N(q,50) > 0) for q in bernstein)

rho_formula = sp.sqrt(alpha*A)
rho_series = sp.series(rho_formula, s, 0, 3)
sin_theta = sp.sqrt(-disc)/(2*rho_formula)
theta_series = sp.series(sp.asin(sin_theta), s, 0, 2)
H = sp.simplify((2*A-tr)/sp.sqrt(-disc))
H_series = sp.series(H, s, 0, 2)

print('symbolic certificate: discriminant < 0 for every kappa >= 1')
print('rho series:', rho_series)
print('theta series:', theta_series)
print('H series:', H_series)
print()
print('kappa       rho             sqrt(k)(1-rho)  sqrt(k)theta    H            first y<=0')
for kappa in [1, 10, 100, 1000, 10000, 1000000]:
    Mnum, Anum = block(float(kappa))
    eig = np.linalg.eigvals(Mnum)
    rho = float(max(abs(eig)))
    theta = float(abs(np.angle(eig[0])))
    trnum = float(np.trace(Mnum))
    discnum = trnum*trnum - 4.0*float(np.linalg.det(Mnum))
    Hnum = (2.0*Anum-trnum)/math.sqrt(-discnum)
    y, v = 1.0, 0.0
    flip = None
    for t in range(1, 1000000):
        y, v = Mnum @ np.array([y, v])
        if y <= 0.0:
            flip = t
            break
    print(f'{kappa:<11d} {rho:.12f}  {math.sqrt(kappa)*(1-rho):.12f}  '
          f'{math.sqrt(kappa)*theta:.12f}  {Hnum:.12f}  {flip}')

print()
print('limits:')
print('sqrt(k)(1-rho) ->', 1/(96*math.sqrt(2)))
print('sqrt(k) theta   ->', math.sqrt(510)/192)
print('H               ->', 1/math.sqrt(255))
flip_c = (math.pi/2 + math.atan(1/math.sqrt(255))) / (math.sqrt(510)/192)
print('first-sign-flip / sqrt(k) ->', flip_c)
print('one-cycle amplitude ratio ->', math.exp(-2*math.pi/math.sqrt(255)))
