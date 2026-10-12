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

The standalone `checker.py` enumerates every full idempotent transformation for each cardinality \(1\leq n\leq6\). It tests the two full products by direct function composition, independent of the image-restriction proof, and compares **each** bivariate coefficient against the theorem's summation formula. The total skew-pair counts are respectively \(0,0,6,204,5900,190410\). The checker also tests the rank-\((2,2)\) closed formula at the admissible sizes. A correct execution ends with `VERIFY_OK`.

For \(n=6\), all \(1057\) idempotent transformations and their \(1,117,249\) ordered pairs are examined. These are exhaustive finite computations at these specific sizes; no computation has been used as a proof for arbitrary \(n\). The general proof in `RESULT.md` is a bijective counting argument.

The 2006 primary article's full text was unavailable for a complete novelty comparison. Novelty and scientific importance have not been independently validated.
