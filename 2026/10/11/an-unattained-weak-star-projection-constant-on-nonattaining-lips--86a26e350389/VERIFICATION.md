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

The full proof, not finite enumeration, establishes the result. The analytical checkpoints are:

1. Both sign extremes of \(T(a)\) are approached and never reached for \(a\ne0\). Every fixed point has strict slope deficit.
2. Every zero-mass unit \(\ell_1\) measure has positive and negative mass each \(1\). When neither endpoint of the function range is attained, the dual pairing is strictly smaller in absolute value than the range diameter.
3. The range is the intersection of weak-star closed kernels of finite point-evaluation relations.
4. Level-\(k\) partner differences produce weak-star continuous projections of exact norm \((k+1)/k\). No weak-star continuous norm-one projection exists by predual norm nonattainment.
5. Hahn--Banach extends usual limits at norm one, yielding an ordinary bounded norm-one projection.

`verify.py` was run on its actual package path using standard-library exact rational arithmetic:

`VERIFY_OK rational_profiles=152 pointwise_bounds=4240 pair_differences=117360 weakstar_projection_levels=5 infinite_limit_requires_proof=True`

The finite program does **not** verify weak-star continuity, nonattainment or arbitrary cardinality. Independent audit has not been performed.
