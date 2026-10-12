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

# Verification of finite covariance and spectral structure

Run `python3 verify.py` with Python 3 from the directory containing the program; it has no dependencies outside the standard library. It enumerates 4! and 5! overlapping order types, uses exact rational arithmetic to reconstruct the six-by-six covariance matrix, tests six eigenvector/block identities at 16 orders, exhaustively checks every permutation for orders 4 to 8, and compares the boundary contrast to its telescoping ascent representation. The complete exhaustive sweep covers 46,224 uniform permutations and 180 distinct covariance cells (36 per order).

Output of the replay from the supplied artifact:

```
n 4 permutations 24 exact-covariance entries 36 boundary-law verified
n 5 permutations 120 exact-covariance entries 36 boundary-law verified
n 6 permutations 720 exact-covariance entries 36 boundary-law verified
n 7 permutations 5040 exact-covariance entries 36 boundary-law verified
n 8 permutations 40320 exact-covariance entries 36 boundary-law verified
VERIFY_OK
```

These checks verify exact finite identities and sample-space enumerations at the stated orders. They do not establish the central limit theorem or an exhaustive historical originality conclusion. The proof's infinite identities follow from finite-overlap stationarity, exact coefficient matrices, and a standard finite-dependent CLT. Independent audit has not been performed.
