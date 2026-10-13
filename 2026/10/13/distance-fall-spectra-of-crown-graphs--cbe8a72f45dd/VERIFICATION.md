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

The infinite proof uses only the crown graph's exact distance structure and its independent sets. For \(n\ge3\), every \(a_i\) has unique distance-\(3\) antipode \(b_i\); all same-shore pairs are at distance \(2\), and all nonmatched cross-shore pairs are at distance \(1\). Therefore an independent color class is distance-\(2\) dominating exactly when it has at least two vertices.

The standalone script `artifacts/verify.py` supplies two finite checks. First, for every \(3\le n\le8\), it enumerates every nonempty independent set and verifies the distance-\(2\) characterization. Second, for \(n=3,4,5\), it enumerates every unlabeled set partition of the \(2n\) vertices, filters by properness and the distance-fall condition, and recovers the exact spectra at distances \(1,2,3\).

A replay produced:

`ALL CHECKS PASSED`

`independent_subset_checks=1029`

`canonical_partition_checks=120318`

`crown_orders_for_full_coloring_enumeration=6,8,10`

`distance2_structural_orders=6..16`

The enumeration is not claimed to prove the formulas for all \(n\); the analytic proof does that. It is an independent finite consistency check on definitions, boundary cases, and the constructive spectrum.
