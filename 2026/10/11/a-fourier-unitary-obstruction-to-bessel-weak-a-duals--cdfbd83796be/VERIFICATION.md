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

Let \(H=\ell^2(\mathbb Z)\), let \(M:H\to L^2[0,1]\) be the Fourier unitary, and let
\[
(Ac)_n=2^{-|n|}c_n.
\]
For
\[
\phi_x=(2^{-|n|}e^{-2\pi i n x})_{n\in\mathbb Z},
\]
one has
\[
C_\phi=MA
\]
and, by Plancherel,
\[
\|C_\phi c\|_{L^2}^2=\|Ac\|^2=\|A^*c\|^2.
\]
Thus all hypotheses of the disputed weak-\(A\)-frame implication are satisfied.

If \(\psi\) were a Bessel weak \(A\)-dual, its bounded analysis operator would obey
\[
A=C_\phi^*C_\psi.
\]
Since
\[
C_\phi^*=AM^*,\qquad A=C_\phi^*M,
\]
and \(A\) is injective, \(C_\phi^*\) is injective. Hence \(C_\psi=M\). Applying both sides to every Fourier-coordinate basis vector gives, on one common full-measure set,
\[
|\langle u_n,\psi_x\rangle|=1\qquad(n\in\mathbb Z).
\]
This contradicts the square-summability of the coordinates of \(\psi_x\in H\).

The primary full text was checked at the weak-\(A\)-frame definition, weak-dual definition, Theorem 3.20, and Proposition 3.21. The theorem/proposition pages were visually inspected. No numerical approximation, truncation, or computational extrapolation is used.
