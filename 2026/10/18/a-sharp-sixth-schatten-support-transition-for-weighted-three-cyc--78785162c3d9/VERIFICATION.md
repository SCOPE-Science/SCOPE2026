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

## Reproducible finite verification

Run `python verify_triangle_s6.py` using Python 3 and its standard library only. The script checks 98 exact rational Gaussian-matrix sixth-moment identities for two genuine angle phases, then evaluates Schur's sharp inequality and equality cases on the exact rational simplex, and verifies 8,575 parameter-and-simplex lower-bound instances. It independently reconstructs the transition parameter numerically. Successful completion prints `TRIANGLE_SIXTH_MOMENT_EXACT_CHECK_OK`.

## Limits of computation

The script does not enumerate the real parameter continuum or certify uniqueness. The infinite family of matrix identities, optimization across all nonnegative triples, and classification of equality are supplied by the algebraic sixth-moment expansion and sharp Schur inequality in `RESULT.md`. The literature-priority comparison is incomplete because the directly motivating recent paper could not be examined in full. Independent audit has not been performed.
