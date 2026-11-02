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

Run the included standalone Python 3 program:

```sh
python3 checks/verify_rectangular_band.py
```

The script enumerates every reduced-row-echelon \(k\)-subspace of \(k^{mn}\) in each selected small field. To decide whether a subspace is a two-sided ideal, it multiplies every generator of that subspace in both orders by each semigroup basis element, using only the original rule \((i,j)(h,\ell)=(i,\ell)\), and independently tests membership in the subspace by Gaussian elimination. The test therefore does not use the proposed row/column ideal classification to decide ideal membership. Predicted counts are computed separately from Gaussian coefficients. The included output records the resulting dimension histograms.

The seven exhaustive cases have \((m,n,q)=(2,2,2),(2,2,3),(2,2,4),(2,3,2),(2,3,3),(3,2,2),(1,4,2)\). The fourth-order field uses an explicit non-prime-field multiplication rule. The \((1,4,2)\) test checks a valid degenerate boundary even though the main statement focuses on \(m,n\ge2\). The final line is:

`RECTANGULAR_BAND_IDEALS_OK 7 EXHAUSTIVE_CASES`

These checks are exhaustive only for the listed finite instances. The all-field theorem follows from the exact algebraic classification proof. No independent audit has been performed.
