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

# Verification details

The self-contained standard-library Python file `checker.py` was executed from the supplied package source. Its observed output was:

```
UNLABELLED_FO_FIRST_CORRECTION_FINITE_OK 527 partition_n 297 p3500_digits 62
```

The checker enumerated partitions through size 17, confirmed exact multiplicity finite differences, and checked numerical first-order approximations to partition ratios for selected sizes through 3500, as well as mixed two-cycle differences. The certificate is **finite only**. In particular, it neither enumerates all first-order sentences nor proves the Hanf locality theorem or analytic partition asymptotic. The actual proof of the universal claim is in `RESULT.md`.

A theoretical check of the unusual step is explicit: each bounded short-cycle count has leading defect probability \(\pi j/\sqrt{6n}\), while two distinct bounded defects have probability \(O(n^{-1})\), so summing single-defect truth changes yields an integer coefficient. The zero-one law itself is prior art, not independently established novelty here. Priority remains conditional on older full-text coverage.
