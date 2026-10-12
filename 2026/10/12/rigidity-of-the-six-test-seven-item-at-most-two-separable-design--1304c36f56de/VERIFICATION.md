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

The standalone verifier is `artifacts/verify.py` and uses only the Python standard library.

It performs these finite checks from first principles:

1. Exhaustively enumerate unordered size-seven families of nonzero six-bit columns, retaining a partial family exactly when all singleton and pairwise Boolean-OR outcomes constructed so far are distinct.
2. Repeat the same exhaustive search at size eight. The completed search returns zero families, so larger families are impossible as well because separability is hereditary under taking subfamilies.
3. Recompute the \(28\) nonempty outcomes for each of the \(30\) maxima without relying on the search state.
4. Apply all \(720\) row permutations to one maximum and compare the resulting orbit with the complete census.
5. Verify, for every maximum, the weight profile \(2,2,2,3,3,3,3\), the perfect matching formed by weight-two supports, the parity-class transversal structure of the weight-three supports, and the \(2\!-(7,3,1)\) property after adding a seventh point.

Expected successful output:

`VERIFY_OK nodes7=49299 nodes8=48919 maximum=7 labeled_row_families=30 fully_labeled_matrices=151200 row_group=720 orbits=1 orbit_size=30 stabilizer=24 weights=2x3,3x4 canonical=000011;001100;010101;011010;100110;101001;110000 census_sha256=7ac7fdffca94f4bf5e1ad4c5842affcbec53aff20bab076757c20c02865f9190`

Limits: this is an exact finite verification only for six binary tests and defective sets of size at most two. It does not certify any asymptotic or larger-parameter statement.
