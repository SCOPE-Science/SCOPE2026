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

# Reproducibility and limits

Run `python3 verify_hook.py` with the standard Python library. The checker separately computes the character absolute mass from integer-partition cycle classes and the claimed finite \(r_m\)-sum using exact `Fraction` arithmetic for every \(4\le n\le12\). It checks zero mean and unit second moment of the irreducible character in those dimensions. The observed final line was `VERIFY_OK rational_cycle_classes=4..12 sign_support_and_orthogonality_and_formula`.

The checker cannot establish irreducibility or the infinite-dimensional family, nor the Poisson limit. These follow from the representation-theoretic character, permutation cycle counting and uniform integrability arguments in RESULT.md. The projected subspace is the complete regular isotype of dimension \(d_n^2\), not the exterior-square representation of dimension \(d_n\). Exact general group averaging, not finite testing, proves optimality among all projections. Independent external validation has not been performed.
