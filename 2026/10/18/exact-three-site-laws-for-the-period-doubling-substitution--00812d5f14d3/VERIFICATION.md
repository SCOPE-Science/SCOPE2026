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

Run `python3 verify.py` from this package using Python 3 and its standard library. It emits `VERIFY_OK: 638 exact dyadic/valuation comparisons, 7936 exact joint-word probabilities` on a successful run. The verifier computes the exact finite-residue Haar averages for dyadic moduli \(2^9\), \(2^{11}\), and \(2^{13}\); checks their discrepancies from the infinite formulas against the rigorous \(6/2^K\) triple and \(4/2^K\) pair bounds; verifies all eight probability masses are nonnegative and sum to one at 992 ordered distinct offset pairs; and checks small exact valuation classes.

No stochastic or floating-point experiment is used. The finite calculation alone does not establish the limit, existence of the invariant measure, or novelty. Those claims depend on the explicit substitution-to-\(2\)-adic reduction, Haar residue partition and primary-literature comparison provided in `RESULT.md` and `REVIEW.md`. This package includes no independent audit or independent scientific validation.
