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

Run from the package root:

```sh
python3 verify/check_sparse.py
python3 verify/check_transverse.py
```

The scripts require Python 3 with no third-party dependencies. `check_sparse.py` exhaustively compares the exact gradient of the determinant on the matching-zero subspace with the union of the corank-two and full-zero-row/column conditions for \(n=3,4\) over \(\mathbb F_2\), and performs seeded finite-field trials over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\) for \(n=4,5,6\). The total of \(65{,}668\) checked matrices returned `VERIFY_OK` with \(9{,}597\) singular examples.

`check_transverse.py` constructs nine rank-\(n-2\) witnesses over \(\mathbb F_{101}\), covering \(n=4,5,6\) and selected matching sizes. In each case the Jacobian rank of the maximal minors describing the corank-two locus is exactly \(4\). It returns `TRANSVERSE_OK`.

These finite computations do not prove the infinite-family statements. The actual proof uses a rank-one adjugate, geometric irreducibility of independent bilinear quadrics, a uniform partial-permutation construction, Schur complements, and Serre's normality criterion. The matched quadratic models are characteristic-zero results. No external independent audit was performed.
