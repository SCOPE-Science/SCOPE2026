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

# Verification and reproducibility

Run `python verify.py` from the directory containing this file. The script uses Python 3 and SymPy; the reviewed run used SymPy 1.14.0. It computes the actual matrix determinant rather than trusting a written polynomial, verifies both Hurwitz minors, independently substitutes each sharp gain threshold, proves the second-threshold shifted-polynomial identity, and checks an exact first-mode instability witness at gain \(g=21\).

The reviewed run printed six `PASS` results, covering the determinant, Hurwitz identities, all higher spatial modes, the first-mode spectral witness, both algebraic crossing thresholds, and the Neumann eigenvalue reduction. The all-mode statements are analytical consequences of exact polynomial coefficient positivity and gain concavity, not of finite simulations. No computations on an inaccessible or stale artifact are cited.

**Boundary of verification:** these are self-review. No separate expert or machine-formal proof review was performed. No nonlinear periodic-orbit or global-in-time solution assertion is being verified.
