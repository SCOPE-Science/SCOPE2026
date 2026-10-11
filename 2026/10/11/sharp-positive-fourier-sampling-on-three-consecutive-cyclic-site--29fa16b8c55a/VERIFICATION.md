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
# Reproducibility and limits
Run `python verify.py` with Python, NumPy and SciPy available. The script constructs positive Parseval frequency rules for every cyclic order from \(3\) through \(79\), checks the unit and two vanishing complex moments (\(231\) identities), checks the five-node exact interpolation formulas in \(26\) orders, and exhaustively checks the nonvanishing four-root symmetric sum for \(202467\) four-subsets in tested orders coprime to six through \(37\). The recorded terminal marker is `VERIFY_OK`.

The infinite theorem is proved by direct Gram algebra, a generalized Vandermonde/symmetric-sum obstruction, the published Lam–Leung vanishing-sum theorem, and Carathéodory's convex-hull theorem. Numerical tolerances in the checker do not constitute exact certificates or prove the unrestricted case. The checker does not enumerate all five-frequency optimal supports at arbitrary order. Same-model assessment supports the stated theorem; no independent audit has been performed.
