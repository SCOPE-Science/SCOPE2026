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

The analytic claim is proved by exact resolvent/cofactor formulas and a strictly positive polynomial factorization. The accompanying standard-library-only `check.py` reproduces all five polynomial identities symbolically and cross-checks equilibrium solutions, strict stock/catch orderings, transition values and optimality regions using exact fractions.

Execute `python check.py` after extracting the file alongside this document. The verification exercises 27 rational rate triples and 216 exact equilibrium, boundary and optimization checks. These finite examples are consistency tests, **not** a proof for all positive real parameters; the universal proof is in `RESULT.md`. No external audit or observational fisheries validation has been performed.
