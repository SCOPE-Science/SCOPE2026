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

The analytical proof establishes the matroid basis-exchange property, the exact Gaussian one-swap width-defect identity, independence of label permutations and order statistics, the compatible-pair counting formula, and strict positivity of the resulting variance difference. These steps imply the theorem in every stated rank and ground-set size.

Run `python verify_sparse_paving.py` from the directory containing this file. It uses only the Python standard library. The checker independently searches allowed bases, verifies all rank permutations of several examples, and counts lattice points of five dilates of the two six-element polytopes. It prints `PASS` only after its assertions succeed.

Observed results: 13,800 strict-score support-function comparisons passed. Among all 720 score permutations for the six-element polytopes, complement-family defect multipliers had counts 648 (zero) and 72 (two), while intersecting-family multipliers had counts 576 (zero) and 144 (one). Ehrhart-point counts for dilates one through five were equal: 18, 121, 488, 1459, 3590. For the centered fixed scores (3,2,1,-1,-2,-3), the conditional variance gap was \(1/35\).

Finite verification does not prove the all-ranks assertion, Ehrhart equality for all dilates, or the closed Gaussian expectation. Those parts are justified by the written proof and the cited published sparse-paving Ehrhart formula. Independent auditing has not been performed.
