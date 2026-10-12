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
# Verification of the finite two-level nucleus census

The accompanying `verify.py` uses Python's standard library only. Execute it from the directory containing this file with `python3 verify.py`.

The direct map implementation identifies every upper set by a bitmask and implements each purported nucleus as an actual transformation of the finite upset lattice. It checks all ordered pairs of these transformations for commutation, computes their composition and image cardinality, verifies the necessary and sufficient support criterion, and independently evaluates each coefficient in the exact bivariate polynomial. An additional enumeration starts instead from **all extensive self-maps** of the upset lattice and filters by idempotence and meet preservation; in the four smallest cases, its output equals the family obtained from subsets. This last comparison avoids assuming the completeness of the support representation in the finite test.

Direct pair counts:
```
HEIGHT_TWO_OK 1 1 upsets 3 nuclei 4 ordered_pairs 16 commuting 14 ranks 4
HEIGHT_TWO_OK 1 2 upsets 5 nuclei 8 ordered_pairs 64 commuting 50 ranks 6
HEIGHT_TWO_OK 2 1 upsets 5 nuclei 8 ordered_pairs 64 commuting 50 ranks 6
HEIGHT_TWO_OK 2 2 upsets 7 nuclei 16 ordered_pairs 256 commuting 162 ranks 9
HEIGHT_TWO_OK 1 3 upsets 9 nuclei 16 ordered_pairs 256 commuting 182 ranks 8
HEIGHT_TWO_OK 3 1 upsets 9 nuclei 16 ordered_pairs 256 commuting 182 ranks 8
HEIGHT_TWO_OK 2 3 upsets 11 nuclei 32 ordered_pairs 1024 commuting 542 ranks 12
HEIGHT_TWO_OK 3 2 upsets 11 nuclei 32 ordered_pairs 1024 commuting 542 ranks 12
HEIGHT_TWO_OK 3 3 upsets 15 nuclei 64 ordered_pairs 4096 commuting 1682 ranks 16
DIRECT_NUCLEI_OK 1 1 candidate_closures 6 all_nuclei 4
DIRECT_NUCLEI_OK 1 2 candidate_closures 90 all_nuclei 8
DIRECT_NUCLEI_OK 2 1 candidate_closures 80 all_nuclei 8
DIRECT_NUCLEI_OK 2 2 candidate_closures 2800 all_nuclei 16
VERIFY_OK
```

The values correspond to \(7056\) directly enumerated ordered pairs of subset-indexed nuclei. The unrestricted result relies on the proof, not numerical extrapolation. No claim is made about higher-level posets, arbitrary self-maps, or full historical priority. Independent audit is not performed.
