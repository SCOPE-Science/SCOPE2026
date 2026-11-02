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

# Reproducibility
Run `python3 verify_kernel_growth.py` using Python 3.8 or newer. The checker independently computes valuations of polynomial values, enumerates every residue-subsequence through the stated *finite* depth, computes the rank of the matrix of the first 200 terms over the prime field of order 1,000,003, and checks simple-root lifts. Expected output:

```
LEVEL_OK p=5 depth=1 rank_mod_1000003=3 predicted=3 rows=6
LEVEL_OK p=5 depth=2 rank_mod_1000003=6 predicted=6 rows=31
LEVEL_OK p=5 depth=3 rank_mod_1000003=8 predicted=8 rows=156
LEVEL_OK p=5 depth=4 rank_mod_1000003=10 predicted=10 rows=781
LEVEL_OK p=13 depth=1 rank_mod_1000003=3 predicted=3 rows=14
LEVEL_OK p=13 depth=2 rank_mod_1000003=6 predicted=6 rows=183
LEVEL_OK p=31 depth=1 rank_mod_1000003=4 predicted=4 rows=32
LEVEL_OK p=31 depth=2 rank_mod_1000003=8 predicted=8 rows=993
VERIFY_OK all tested finite-depth sample ranks agree
```

The first family is \(Q(X)=X^2+1\); the last is \(Q(X)=X^3-2\). A rank of a finite sampled evaluation matrix over a finite field is not, by itself, an exact rank determination for infinite rational sequences. The proof's local-singularity independence is the unrestricted argument. Independent mathematical validation remains unperformed.
