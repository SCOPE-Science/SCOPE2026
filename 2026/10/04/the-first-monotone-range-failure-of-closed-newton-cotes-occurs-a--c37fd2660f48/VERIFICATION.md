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
The verification artifact uses the Python standard library and exact rational arithmetic.

For each \(1\le n\le13\), it solves
\[
\sum_{j=0}^{n}w_j(j/n)^r=\frac1{r+1},
\qquad
0\le r\le n,
\]
by exact Gaussian elimination. It verifies normalization, symmetry, and the minimum proper cumulative sum.

At \(n=12\), it checks the full published coefficient vector after scaling by \(63063000\), the central cumulative minimum
\[
-\frac{147227}{750750},
\]
the corresponding step extremizer, and the strictly positive strictly increasing witness.

At \(n=13\), it verifies that exactly six weights are negative while every proper cumulative sum is positive, with exact minimum
\[
\frac{8181904909}{402361344000}.
\]

The infinite-order cumulative-sum criterion is proved analytically in RESULT.md and is not inferred from finite enumeration.
