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

# Reproducibility

Run `python verify.py` with Python 3, NumPy and SciPy installed. The checker computes the rational finite-sum constant directly, independently integrates the conditional hinge, and checks both by symmetry for 49 dimension pairs, together with exact small-dimensional values and numerical simulations of the barycentric projector kernel. It checks 20 exact Gram identities and the balanced asymptotic coefficient at equal factor dimensions 50, 100 and 250.

The checker completed successfully in the packaged form. The exact finite tests are not exhaustive over all dimension pairs, and sampling is not a universal proof. The analytical argument in `RESULT.md` establishes the general theorem. The source comparison was a best-knowledge literature check, not an independent novelty certification.
