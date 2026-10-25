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

# Verification and limits

Running `python CHECK_FVECTOR.py` uses Python's standard library alone. For every \(1\le n\le5\) and all \(p,q,r\ge0\) with \(p+q+r=n\) and both supports nonempty, it independently constructs the two signed coordinate vertex sets, enumerates normal exposures on \(\{-2,-1,0,1,2\}^n\), computes exact rational affine ranks, deduplicates by the intrinsic pair of summand exposed faces, and checks all coefficients against the symbolic formula. It passed all 45 triples. Representative vectors (low to high dimension, including the full face) are \((14,24,12,1)\), \((24,68,64,20,1)\), and \((34,128,192,136,40,1)\) at parameters \((1,1,1)\), \((1,1,2)\), and \((2,2,1)\).

This finite enumeration is not a complete search in arbitrary dimension or over arbitrary real normals. The unrestricted proof rests on the exhaustive theoretical classification of maximizing normal-coordinate patterns and on dimension-rank arguments. The polar facet description is obtained algebraically, independent of the finite checker. No independent scientific audit has been performed.
