---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification
The exact minimizer is the observed density
\[
m^*(x)=\min\{\phi(x),\max\{\phi(x)/(2n),b\phi(x-r)\}\}.
\]
For any admissible density, the upper-tail excess and lower-tail deficit cannot be reduced below \(A_b(r)\) and \(B_{n,b}(r)\), respectively. The atom at \(\star\) converts the total-variation norm into the larger of those two discrepancy masses, so clipping proves exact optimality.

At the upper crossing, with \(z=L/r-r/2\), the identity \(\phi(z+r)=b\phi(z)\) and the two-term Mills expansion give
\[
A_b(r)\sim b\phi(z)\frac{r}{z^2}
\sim \frac{\sqrt b}{\sqrt{2\pi}L^2}r^3e^{-L^2/(2r^2)}.
\]
Substitution \(S=L^2/(2r^2)\) gives
\[
A_b(r)\sim \frac{\sqrt b\,L}{4\sqrt\pi}S^{-3/2}e^{-S}.
\]
The stated choice of \(S_n(x)\) therefore makes \(nA_b(r_n(x))\to e^{-x}\). The lower crossing lies at order \(- (\log n)^{3/2}\), so \(nB_{n,b}(r_n(x))\to0\).

The bundled numerical verifier checks the exact formulas at high precision for several \(b\) and increasing \(n\), and confirms convergence of \(nD_n(r_n(0);b)\) toward one. Those checks are diagnostic only; the theorem rests on the analytic argument above.

Limits checked: no equality for product total variation is claimed; no matching upper confidence-length constant is claimed; no statement is made for varying \(\epsilon\), unknown \(\sigma\), or non-Gaussian bases.
