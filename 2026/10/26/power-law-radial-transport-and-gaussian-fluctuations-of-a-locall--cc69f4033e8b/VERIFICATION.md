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

# Verification record

The source Hamiltonian and graph definitions were checked against arXiv:2602.23970v1, Definition 2.1 and Theorem 2.5. The proposed power-law weights satisfy its absolute-summability hypothesis for all \(\alpha>1\). The proof independently verifies the finite-coordinate product law, convergence to the infinite measured distribution, \(V_t=\mu_{2t}/4\), the sharp improper Riemann integral, the gamma constant and the triangular-array central limit theorem. In particular, \(V_t\asymp t^{1/\alpha}\to\infty\) verifies Lindeberg and Berry--Esseen applicability.

The included standalone `verify.py` was executed against the included source from its actual package path. It checks finite-truncation variance identities and compares numeric means and Fano ratios to the analytical constants for \(\alpha\in\{1.5,2,3\}\) at two increasing scales. The results passed its stated tolerances. These finite checks do not certify the infinite-dimensional statements or the completeness of the literature comparison.

The claimed convergence is weak convergence of the single-time Born-distance distribution, not a functional central limit theorem; the normal-approximation rate is an upper bound only.
