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

The reproducibility checker is `verify_split_graph.py`, executed with `python3 verify_split_graph.py` using only the standard library. It verifies, with exact rational arithmetic, the distance-power matrix actions on clique and independent contrasts, the critical block-constant eigenrelation, the complete quadratic-form identity, and many independent integer zero-sum witnesses. The executed checks passed: 4,788 exact matrix actions; 6,048 zero-sum-vector inequalities/identities; 504 critical-exponent witnesses; and the complete integer classification of the seven-vertex first failures within the stated family.

The script tests bounded sizes and rational values of the parameter \(q=2^p\), not all sizes or all real exponents. The universal proof uses the blockwise quadratic-form identity, Cauchy--Schwarz equality cases, and the centered Gram matrix. Independent scientific audit has not been performed.
