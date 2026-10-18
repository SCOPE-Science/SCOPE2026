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

# Verification of the affine-hull signature theorem

The exact proof is in `RESULT.md`, particularly the affine-existence lemma, syntactic induction, affine hyperplane separation, marked affine-basis compression and Gaussian-binomial double count. The independent semantic cross-check in `check.py` uses the original modal truth clauses; it is not a formal proof for unbounded atom counts or infinite models.

Run `python3 check.py` (no external dependencies). The checked program returned `AFFINE_S5_VERIFY_OK`, 4,212 affine-existence comparisons, 500 generated or structured modal formula templates, 182,088 pointed truth comparisons and exhaustive pointed theory counts 4, 20 and 128 for one, two and three atoms. The Gaussian-product arithmetic was checked for one through five atoms. The equality of all formulas on infinite models follows from the induction and the finiteness of the valuation image, not from the code. The source comparison does not prove global publication priority. No independent mathematical audit or external certification was carried out.
