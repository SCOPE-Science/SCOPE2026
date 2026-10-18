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

# Reproducing the algebraic checks

Execute `python verification.py` in a Python environment with SymPy and NumPy installed. The script directly checks 25 Jacobian entries by differentiating all five dynamical equations; factors the fourth-degree characteristic polynomial and both decisive Routh–Hurwitz expressions exactly; checks the environmental conservation identity and equal-response quadratic factorization; and evaluates 27 independent rational five-dimensional characteristic polynomials with sampled spectral signs. All checks passed in the supplied execution.

The proof in `RESULT.md` establishes the infinite family of parameter claims analytically; finitely many rational cases and floating-point eigenvalues are **not** offered as exhaustive certificates or as proof of publication priority. The neutral-oscillator conclusion is linear only, while exponential point selection uses the standard local stable-foliation theorem with the explicitly established spectral gap on compact subsegments. No external or independent audit has been performed.
