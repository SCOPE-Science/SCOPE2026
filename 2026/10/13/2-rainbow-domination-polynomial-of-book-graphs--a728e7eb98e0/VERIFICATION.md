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

The proof is symbolic and valid for every integer \(n\ge1\). Computation is used only to stress-test the local-state decomposition.

`verify.py` performs two checks:

1. It directly enumerates every labeling of \(B_n\) by \(\emptyset,\{1\},\{2\},\{1,2\}\) for \(1\le n\le4\), applies the defining neighborhood-union condition, and compares the full coefficient vector with the formula.
2. It independently propagates page states recording the union of colors used on each page side for \(1\le n\le10\), without using the inclusion-exclusion derivation, and again compares every coefficient.

It also checks the stated minimum layers for \(1\le n\le10\) and the displayed total counts for \(1\le n\le7\).

Expected successful output:

`VERIFY_OK brute_n=1..4 labelings=1118464 state_n=1..10 coefficient_checks=330 minimum_checks=10 total_checks=7 max_order=22`

The finite checks do not establish the result for unbounded \(n\); that follows from the fixed-spine page factorization and inclusion-exclusion in `RESULT.md`.
