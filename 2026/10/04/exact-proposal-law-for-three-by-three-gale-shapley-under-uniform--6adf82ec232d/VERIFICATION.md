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
The embedded `verify_gs3_proposals.py` is a complete exact replay of the stated finite census.

It generates all \(6^6=46656\) strict labeled three-by-three preference profiles and runs men-proposing Gale–Shapley in two independently organized ways: a one-free-man-at-a-time sequential implementation and a simultaneous-round implementation. Matching and total proposal count must agree profile by profile.

For every profile the script also:
- verifies that proposal count equals the sum of the three men-optimal partner ranks;
- brute-force checks all six perfect matchings for stability;
- reconstructs the proposal-count distribution and rank-multiset distribution;
- reconstructs the joint proposal-count/stable-multiplicity table;
- computes all moments and conditional means with exact `Fraction` arithmetic.

Run:

`python3 verify_gs3_proposals.py`

The first output line must be:

`VERIFY_OK`

The replay proves only the finite three-by-three claims. No asymptotic distribution is inferred from enumeration.
