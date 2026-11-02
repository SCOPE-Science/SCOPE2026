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

# Reproducibility checks

Run `python verify.py` using Python 3.9 or newer; no third-party packages are required. The supplied program checks 1192 rational identities, including the exact beta and Dirichlet moments used in the proof, the variance/covariance/correlation identities for dimensions 2–100, the distinct residual-shape endpoint expectations for six Dirichlet shape values in dimensions 3–100, and the exact conditional integral in dimension three for shape parameter two.

All checks passed during preparation. The checker is intentionally a finite verification tool, not an infinite proof. The general derivation, convergence arguments, parameter conditions, and dimension-two exception are given in `RESULT.md`. The scientific comparison relies on the primary literature identified there; historical priority and independent validation remain open.
