---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The infinite-domain proof is analytic. The mass comparison uses the exact ratio and its numerator-minus-denominator factorization. The endpoint lemma follows from the derivative of the logarithm of the consecutive endpoint ratio and an induction for the limiting endpoint. The two imported facts are the center-tail inequality of Simmons (as stated in the motivating paper) and the mean identity, which is also derived in the proof from the tail sums of the positive and negative parts.

The unchanged `verify.py` supplies supplemental exact-integer checks of the ratio-sign identity, endpoint bound and disjunctive left-loadedness on its finite grids. It does not certify the infinite theorem or directly check strict positivity of every partial sum. The latter is proved by combining the single-crossing property with the mean identity, with small means and the symmetric boundary handled separately.
