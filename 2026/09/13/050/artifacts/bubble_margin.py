import numpy as np

# Reproducible bounded recovery test for lane-1679:
# (1) Heisenberg bubble D0, L4 norms -> finite positive quotient; Rossi radial
#     relative O(t^2) increase (1+t^2)/(1-t^2)-1 << 1-1/sqrt(2) margin.
# (2) S^3 Monte Carlo for Z2-even phi=Re(z1^2): mean ~0, second moment ~O(1).
rng = np.random.default_rng(0)
r = np.concatenate([np.linspace(0, 5, 2000), np.linspace(5, 30, 2000)])
tau = np.linspace(-60, 60, 6000)
R, T = np.meshgrid(r, tau, indexing='ij')
D = ((1 + R * R) ** 2 + T * T)
Ur = -2.0 * R * (1 + R * R) * D ** (-1.5)
Ut = -T * D ** (-1.5)
A = Ur / 2.0
B = R * Ut
densD = 0.5 * (A * A + B * B) * R
dens4 = D ** (-2.0) * R
D0 = 2 * np.pi * np.trapz(np.trapz(densD, tau, axis=1), r)
Q4 = 2 * np.pi * np.trapz(np.trapz(dens4, tau, axis=1), r)
print("D0 =", D0)
print("L4^4 =", Q4)
print("Q_Heis =", D0 / np.sqrt(Q4))
print("margin 1-1/sqrt2 =", 1 - 1 / np.sqrt(2))
for t in [0.1, 0.2, 0.3, 0.49]:
    print(f"t={t}: rel={(1 + t * t) / (1 - t * t) - 1:.4f}")

N = 200000
u = rng.random(N)
s = np.arcsin(np.sqrt(u))
a = rng.random(N) * 2 * np.pi
phi = np.cos(s) ** 2 * np.cos(2 * a)
print("mean phi =", float(phi.mean()))
print("mean phi^2 =", float((phi ** 2).mean()))
