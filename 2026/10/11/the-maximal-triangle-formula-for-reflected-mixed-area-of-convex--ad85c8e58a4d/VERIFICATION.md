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

# Verification notes

The proof is analytic and finite-dimensional. The affine normalization and all hull membership cases are explicit in `RESULT.md`.

The supplied `verify.py` uses Python standard-library exact fractions. It enumerates all \((a,b)=(i/d,j/d)\) with \(1\le i,j<d\) for \(d\in\{7,11,13,17\}\), constructs the difference body's convex hull from all sixteen vertex differences with monotone chain, computes areas by a second shoelace route, and compares with the maximal vertex-triangle area. Select cases are transformed by a matrix of determinant \(13\), providing an additional affine-covariance check. The actual packaged script was executed and returned `VERIFY_OK 642 exact-rational quadrilaterals`.

All arithmetic checks are exact but the finite grid is not an exhaustive parameter proof; the proof of the entire strict quadrilateral domain is in `RESULT.md`. No computational program tests an infinite parameter range and no external certification is claimed.
