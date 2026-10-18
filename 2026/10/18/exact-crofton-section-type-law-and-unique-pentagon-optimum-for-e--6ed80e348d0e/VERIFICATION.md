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

The proof in `RESULT.md` applies to all real \(h>0\) and all invariant affine sections away from a null set of planes containing vertices. Run `python3 checker.py` with the Python 3 standard library from the extracted artifact directory. The output `BIPYRAMID_CROFTON_CHECK_OK comparison_items=30 samples_per_shape=64800` records success of independent edge-crossing midpoint-integral comparisons across six aspect ratios and separate numerical neighborhood checks for the pentagon optimum.

The finite integrations do not establish the infinitely quantified exact formulas, integral identities, or uniqueness; those are established analytically in `RESULT.md`. The returned decimals for \(h_*\) and the maximum probability are numerical evaluations of an exact implicit equation and carry no separately certified rounding guarantee. Search of the accessible literature is not a proof of absolute priority; historical antecedents may remain unidentified.
