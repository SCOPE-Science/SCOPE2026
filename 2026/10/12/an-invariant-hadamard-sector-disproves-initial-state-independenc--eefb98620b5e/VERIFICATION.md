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

The claim has two distinct verification layers.

First, exact finite-dimensional algebra verifies the specialized four-state coin. After multiplication by \(\sqrt2\), its integer matrix \(N\) satisfies \(N^{\mathsf T}N=2I_4\) and \(\det N=4\), hence the physical coin is unitary with determinant one. The entries coupling \(\operatorname{span}\{|x+\rangle,|y-\rangle\}\) to its complementary pair vanish, and the surviving block is the standard Hadamard matrix.

Second, the infinite-time assertion is analytic. On the invariant sector, \(Z_t=X_t+Y_t\) is the ordinary one-dimensional Hadamard walk and \(X_t=(t+Z_t)/2\) pathwise. Fourier diagonalization gives velocity
\[
v(k)=\frac{\cos k}{\sqrt{1+\cos^2 k}},
\]
with opposite first-moment signs for the two basis initial states and the same second velocity moment
\[
I=\frac1{2\pi}\int_{-\pi}^{\pi}v(k)^2\,dk=1-\frac1{\sqrt2}.
\]
Because \(|Z_t/t|\le1\), weak convergence implies convergence of the first two moments. Substitution yields the two stated \(X_t^2/t^2\) limits.

The bundled `verify.py` uses only the Python standard library. It checks the integer coin identities, invariant block, exact finite-time reflection identities through several step counts, and the final radical formulas. Its successful terminal line is `VERIFY_OK`. These finite checks are supplementary and are not treated as a proof of the asymptotic limit.
