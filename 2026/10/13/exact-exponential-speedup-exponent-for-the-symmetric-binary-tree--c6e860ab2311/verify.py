import cmath, math
sqrt3 = math.sqrt(3.0)
q = (sqrt3-1.0)/2.0
u = 3*q/((1-q)*(1+2*q))
alpha = q*(1-q)*(1+2*q)/((1+q)*(1+2*q*q))
t_ratio = 1+2*alpha
rho2 = (1+q)**2/3.0
bq = math.log(1/rho2)
bc = math.log(2.0)
eta = bq/bc
assert abs(u-1.0) < 1e-14
assert abs(t_ratio - 2*(sqrt3-1)) < 1e-14
assert abs(1/rho2 - (12-6*sqrt3)) < 1e-13
assert abs(eta-0.6849938737681645) < 1e-14
# Direct unit-circle check of the algebraic branch. This is a numerical replay,
# not the proof of the global maximum used in RESULT.md.
def F(u):
    return (5*u-3+3*cmath.sqrt(1-(2/3)*u+u*u))/(4*u)
mx = -1.0
arg = None
for j in range(20001):
    th = -math.pi + 2*math.pi*j/20000
    v = abs(F(cmath.exp(1j*th)))/sqrt3
    if v > mx:
        mx, arg = v, th
assert abs(mx-math.sqrt(rho2)) < 2e-10
assert abs(arg) < 4e-4
# Classical first-passage fixed point h=qz+pzh^2 at z=1.
p, r = 2/3, 1/3
h = r/p
hprime = h/(1-2*p*h)
assert abs(h-0.5) < 1e-15
assert abs(hprime/h-3.0) < 1e-14
print('VERIFY_OK')
print('quantum_time_ratio', format(t_ratio,'.15f'))
print('quantum_log_slope', format(bq,'.15f'))
print('classical_log_slope', format(bc,'.15f'))
print('slope_ratio', format(eta,'.15f'))
# At the two unit-circle algebraic branch-switch points |g|=1 but g != 1.
a = complex(-0.5, math.sqrt(3)/2)
def G_from_q(q):
    return math.sqrt(3)*q*(1-2*q)/((1-q)*(1+2*q))
for qq in (1j/math.sqrt(2), -1j/math.sqrt(2)):
    gg = a*G_from_q(qq)
    assert abs(abs(gg)-1) < 1e-12
    assert abs(1-gg) > 1.5
