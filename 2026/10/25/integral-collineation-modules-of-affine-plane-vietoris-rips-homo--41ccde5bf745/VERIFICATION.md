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
# Verification

Run `python3 verify_affine_equivariant.py` using a standard Python 3 interpreter. The program requires no network access and no external dependencies.

The checker constructs \(\operatorname{AG}(2,3)\) using all nine coordinate points and twelve affine lines, verifies point-pair uniqueness and incidence counts, constructs the scale-two complex both as a union of the two proof subcomplexes and independently as the shortest-path metric clique complex, and requires their complete simplex sets to be identical. It checks the predicted face vector \((21,126,282,255,135,84,36,9,1)\) and computes the complete mod-two homology by exact bitset Gaussian elimination.

For all \(432\) affine transformations, it independently calculates the signed Lefschetz traces of the full Rips complex and the parallel-class line-only join, then compares them with the predicted degree-two and degree-three group characters. It checks the exceptional nonidentity translation traces and the zero invariant dimensions at \(q=3\). It also evaluates the derived translation-quotient formula arithmetically for the prime-power orders \(3,4,5,7,8,9\).

The independent finite checks pass with markers `AFFINE_INTEGRAL_MODULE_VERIFIED` and `AFFINE_TRANSLATION_QUOTIENT_VERIFIED`. Exact arithmetic and complete finite enumeration were used for the stated order-three checks, but these experiments are not a substitute for the proof of the universal integral module isomorphisms, nor do they establish anything about nonexistent affine plane orders.
