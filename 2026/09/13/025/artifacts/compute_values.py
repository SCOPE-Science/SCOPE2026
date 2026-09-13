"""Reproducible 80-digit computation of even/odd variance values for lane-1551.
Reference point: V(x)=x^4/4-2x^2, support [-b,-a] U [a,b], a=sqrt(2), b=sqrt(6).
Outputs: fA, fB, t, C, c, Var_G, mu_unnorm, c0, qd, V_even, V_odd, v_even, v_odd.
Also checks: mass per cut = 1/2, C-independence over x2 grid, tail bounds for theta sums.
"""
from mpmath import mp
mp.dps = 80

a2 = mp.mpf(2); b2 = mp.mpf(6)
a = mp.sqrt(a2); b = mp.sqrt(b2)

def s(x):
    return mp.sqrt((x**2 - a2) * (b2 - x**2))

fA = mp.quad(lambda x: 1/s(x), [a, b])
fB = mp.quad(lambda x: 1/mp.sqrt((x**2 - a2)*(x**2 - b2)), [-a, a])
t = fB / fA

# Zero-A-period constant: C = -K(x2)/(2 fA); K(x2)=int S0/((x-x2)^2 s)
def K(x2):
    def S0(x):
        return x**2*x2**2 - 4*x**2 - 4*x2**2 + 12
    return mp.quad(lambda x: S0(x)/(((x-x2)**2)*s(x)), [a, b])

grid = [mp.mpf(0), mp.mpf('0.5'), mp.mpf(3), mp.mpf(10), mp.mpc(0,1)]
Cs = [-K(x2)/(2*fA) for x2 in grid]
C = Cs[0]
c = 2*C
varG = 8*c + 16

# Equilibrium density on +cut
def rho(x):
    return x*mp.sqrt((b**2-x**2)*(x**2-a**2))/(2*mp.pi)
mass = mp.quad(rho, [a, b])
mu = mp.quad(lambda x: x**3*rho(x), [a, b])
c0 = 4*mu  # = 2*mu/mass with mass=1/2

qd = mp.e**(-mp.pi*t)
Ntr = 40
Se_den = mp.nsum(lambda k: qd**(k**2), [-mp.inf, mp.inf]) if False else sum(qd**(k**2) for k in range(-Ntr, Ntr+1))
Se_num = sum((k**2)*(qd**(k**2)) for k in range(-Ntr, Ntr+1))
Veven = Se_num/Se_den
So_den = sum(qd**((k+mp.mpf('0.5'))**2) for k in range(-Ntr, Ntr))
So_num = sum(((k+mp.mpf('0.5'))**2)*(qd**((k+mp.mpf('0.5'))**2)) for k in range(-Ntr, Ntr))
Vodd = So_num/So_den

v_even = varG + c0**2*Veven
v_odd = varG + c0**2*Vodd

print("fA =", fA)
print("fB =", fB)
print("t =", t)
for x2, cc in zip(grid, Cs):
    print("x2 =", x2, "C =", cc)
print("c =", c)
print("varG =", varG)
print("mass+ =", mass)
print("mu_unnorm =", mu)
print("c0 =", c0)
print("c0^2 =", c0**2)
print("qd =", qd)
print("Veven =", Veven)
print("Vodd =", Vodd)
print("v_even =", v_even)
print("v_odd =", v_odd)
print("gap =", v_odd - v_even)
# tail bound: qd<0.005 so truncation error < 1e-30 at Ntr=40
print("tail_even_k5 =", qd**25)
