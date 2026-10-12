import sympy as sp

x, eps, k = sp.symbols("x eps k", positive=True, real=True)
Ds, Di, Dr, chi = sp.symbols("D_S D_I D_R chi", real=True)
beta, gamma, S, I, N = sp.symbols("beta gamma S I N", positive=True)

# Reaction cancellation.
rS = -beta*S*I/N
rI = beta*S*I/N - gamma*I
rR = gamma*I
assert sp.simplify(rS+rI+rR) == 0

# Unequal-diffusion witness S=1+eps cos(kx), I=1-eps cos(kx), R=1.
S0 = 1 + eps*sp.cos(k*x)
I0 = 1 - eps*sp.cos(k*x)
R0 = sp.Integer(1)
assert sp.simplify(S0+I0+R0) == 3
nt = Ds*sp.diff(S0,x,2) + Di*sp.diff(I0,x,2) + Dr*sp.diff(R0,x,2)
assert sp.simplify(nt - eps*k**2*(Di-Ds)*sp.cos(k*x)) == 0

# Chemotactic midpoint witness S=1, I=1+eps cos(kx), R=1-eps cos(kx).
S1 = sp.Integer(1)
I1 = 1 + eps*sp.cos(k*x)
R1 = 1 - eps*sp.cos(k*x)
assert sp.simplify(S1+I1+R1) == 3
logI_xx = sp.diff(sp.log(I1), x, 2)
mid = sp.simplify(logI_xx.subs(x, sp.pi/(2*k)))
assert sp.simplify(mid + eps**2*k**2) == 0

print("VERIFY_OK")
