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

The independent-audit channel has not been performed or evaluated. Only the mathematical proof and a self-review are provided.

Run `python3 orthotope_surface_moments_verify.py` with standard Python 3. The exact-fraction verifier calculates second and fourth distance moments twice: first from a closed invariant formula and independently by summing over all ordered facet-normal pairs and their coordinate moments. It also checks sample inequalities, equality, aspect-ratio degenerations, and dimension comparisons. The observed output is `VERIFY_OK exact_fractional_checks=320 dimensions=4..8`. Finite tests are diagnostics rather than an infinite proof; the proof in RESULT.md establishes all-dimension inequalities analytically.

Documented limitations: exact population moments, integer dimension at least four, boundary area sampling and Euclidean distance, nondegenerate orthotopes. Primary-source coverage remains provisional where historical manuscripts were inaccessible.
