---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every m>=2 and every cyclic window 1<=b<=2^m, incidence counting over all nonzero affine words forces a universal bound d_b<=2^m-2^{m-b} for b<=m. The trace basis 1,g,...,g^(m-1) on primitive nonzero field powers has every b-tuple t or t-1 times; inserting coordinate zero increases any all-zero window count by at most one. The minimal-polynomial recurrence p(1)=1 excludes m+1 zero-runs in complemented words. This proves simultaneous attainment and full distance at b>=m+1. Independent direct enumeration of affine words and b-window distances for m=2..5 matched; finite tests are corroboration, not the unbounded proof.

## originality

PASS

Generalized Hamming weights and cyclic trace/simplex code b-weight distributions have superficially matching parameters or numeric coincidences, but generalized support does not supply a single cyclic ordering maximizing each overlapping-window distance. The code here is affine unpunctured length 2^m, not just simplex length 2^m-1. Ding–Zhang–Ge supplies b-symbol theory and bounds; Zhu–Shi character sums supply irreducible cyclic distributions; the theorem-specific field insertion plus universal incidence argument is not a corollary of those inspected statements. Best-of-knowledge priority risk remains explicit; unsuccessful search alone is not claimed as proof of novelty.

## value

PASS

An exact simultaneous optimum for every read-window width, in the natural coordinate-permutation design problem for a classical code, goes beyond a single pair-symbol result or Hamming-weight identity and supplies an explicit reusable field-order construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
