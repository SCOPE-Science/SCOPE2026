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

The exact proof was checked against the vector field as printed in the 23 November 2023 preprint and the 2024 journal article. The Jacobian used by the checker is

\[
J_d=\begin{pmatrix}-40&40&0&1\\10&25&0&0\\0&0&-3&0\\d&0&0&0\end{pmatrix}.
\]

Running `python verify.py` in the package directory must print `VERIFY_OK`. The script checks the symbolic characteristic polynomial, the exact sign evaluations that force the three cubic roots into disjoint intervals, the fact that \(-3\) is not a cubic root, and the numerical \(d=15\) eigenvalues.

The numerical roots are not the proof of the all-parameter result. No assertion is made about global boundedness or any non-equilibrium Lyapunov spectrum.
