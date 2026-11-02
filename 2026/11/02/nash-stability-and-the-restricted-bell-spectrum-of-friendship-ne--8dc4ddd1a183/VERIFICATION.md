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

# Verification record

The proof is contained in `RESULT.md`, with complete conditions for all integer graph sizes. The direct enumerator `verify.py` was run under Python 3 with standard-library exact integer and rational arithmetic. It enumerated every set partition of \(2m+1\) labeled vertices for \(m=1,2,3,4,5\), independently tested every possible unilateral strict-improvement move using integer cross-products, checked the restricted-Bell equilibrium counts and matched both welfare extremes. Every assertion passed.

The numbers of tested partitions by \(m\) were \(5,52,877,21147,678570\). Observed Nash counts were \(1,3,7,21,71\), observed welfare optima were \(2,3,4,5,6\), and every worst Nash welfare matched \(6m/(2m+1)\). Exactly \(m\) optimal partitions and exactly one welfare-worst Nash partition were found for each tested value.

This computation is finite corroboration, not an infinite proof, a guarantee of unpublished novelty, or an independent audit. The mathematical all-size claims rely on the explicit proof and exact deviation inequalities, not on extrapolation from the computed cases.
