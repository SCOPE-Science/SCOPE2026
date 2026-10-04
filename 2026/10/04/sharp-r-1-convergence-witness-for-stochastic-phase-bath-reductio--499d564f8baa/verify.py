import cmath, math

def i0(x):
    y = x*x/4.0
    term = 1.0
    total = 1.0
    for k in range(1, 200):
        term *= y/(k*k)
        total_new = total + term
        if abs(term) < 1e-16*abs(total_new):
            return total_new
        total = total_new
    raise RuntimeError("I0 series did not converge")

beta = 1.1
omega = 1.3
g = 0.7
t = 0.8
x = beta*omega/2.0
a = g*g*(1.0-math.cos(omega*t))
c = 1.0/math.tanh(x)
s = 1.0/math.sinh(x)
Linf = math.exp(-2.0*a*c)

def LR(R):
    return Linf * i0(2.0*a*s/R)**R

R = 1
M = 20000
acc = 0j
for k in range(M):
    th = 2.0*math.pi*(k+0.5)/M
    acc += cmath.exp(-(2.0*a*c/R)*(1.0-math.cos(th)) + 1j*(2.0*a/R)*math.sin(th))
quad = acc/M
closed_one = math.exp(-2.0*a*c/R)*i0(2.0*a*s/R)
assert abs(quad.imag) < 2e-12
assert abs(quad.real-closed_one) < 2e-12

for R in (1, 2, 4, 16):
    assert LR(R) > Linf

coef = Linf*a*a*s*s
R = 20000
scaled = R*(LR(R)-Linf)
assert abs(scaled-coef)/coef < 5e-4
print("VERIFY_OK")
