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

The self-contained `check.py` enumerates finite directed-path weak endomorphisms by their binary adjacent increments. For \(1\le n\le9\) it constructs every idempotent clamp and tests commutation using actual composition, comparing every centralizer rank coefficient with the independent binomial formula. It also checks four integer specializations of the bivariate rational generating series through degree nine and the unweighted closed total formula. A successful run prints `ALL_EXACT_CHECKS_PASSED`.

The finite enumeration is a consistency check. The complete, infinite-dimensional correctness argument is the bijective proof in `RESULT.md`; there is no computer-assisted infinite certification. Scientific priority beyond the inspected works, and independent mathematical validation, are not established.
