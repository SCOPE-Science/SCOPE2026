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

The analytic proof in `RESULT.md` is primary. The included script `artifacts/verify.py` is a standalone Python program that constructs every \(K_{m,n}-M_t\) with
\[
2\le m,n\le6,
\qquad 0\le t\le\min\{m,n\}.
\]
It tests all vertex subsets directly, including the disconnected boundary \(K_{2,2}-M_2\). A direct recursive perfect-matching count is compared with the all-set formula and with the rook inclusion-exclusion count of each matching multiplicity. The direct graph checker does not call either closed formula during its adjacency-level tests.

Actual replay output:

`ALL CHECKS PASSED; profiles=105; subsets_checked=86384; paired_set_matching_pairs_checked=125039; m,n=2..6; all matching deletions`

The finite check is corroborative only and does not prove an infinite family by enumeration. The unrestricted proof uses Hall's marriage theorem and a finite inclusion-exclusion identity, with all size-two and matching-deletion boundary cases handled separately.
