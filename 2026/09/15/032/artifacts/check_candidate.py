"""Verify tensor-diagonal counterexample numerics.
D=M2 (tau_D normalized trace); A1=D x B1, B1=C^3 wts (0.6,0.2,0.2);
A2=D x B2, B2=C^5 uniform 0.2; diagonal inclusions, E_i=id x tau_{Bi}.
Checks: (a) no unitary in ker E1 (0.6 vs 0.4 triangle gap);
(b) unitaries in ker E2 DO exist (5th roots) -> asymmetry, (ii) still fails
since side 1 has none; (c) all Dykema pair sums < 1; (d) free dims.
"""
import cmath, math
lam = (0.6, 0.2, 0.2)
# (a) operator-norm gap: ||0.6 u1|| = 0.6 > 0.4 >= ||0.2 u2 + 0.2 u3||
gap = lam[0] - (lam[1] + lam[2])
print("E1-kernel unitary impossible, gap =", gap)
assert gap > 0
# (b) scalar 5th roots sum to zero -> diag(w^k) I_2 in ker E2
N = 5
s = sum(cmath.exp(2j * math.pi * k / N) for k in range(N))
print("|sum of 5th roots| =", abs(s))
assert abs(s) < 1e-12
# (c) Dykema pairs: min central-proj traces lam_i vs 0.2; also noncentral halves
pairs = [(a, 0.2) for a in lam]
print("max central pair sum =", max(a + b for a, b in pairs))
assert all(a + b < 1.0 for a, b in pairs)
print("max half-proj pair sum =", max(a / 2 + 0.1 for a in lam))
# (d) free dimensions: fdim(B1)=1-(.36+.04+.04)=.56; fdim(B2)=1-5*.04=.8
f1 = 1 - sum(x * x for x in lam)
f2 = 1 - 5 * 0.04
print("fdim B1 =", f1, " fdim B2 =", f2, " sum =", f1 + f2, " > 1 diffuse")
assert f1 + f2 > 1
print("ALL CHECKS PASSED")
