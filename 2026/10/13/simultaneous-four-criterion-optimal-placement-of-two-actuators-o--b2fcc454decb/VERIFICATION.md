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

The analytical identities are derived in `RESULT.md`; the standalone `verify.py` script supplies independent exact-rational algebra checks. It uses only the Python standard library and requires no downloads or other package paths.

Run `python3 verify.py`. Its expected terminal line is `VERIFY_OK 2210 exact rational comparisons and finite-time direct sums`. This output was obtained on the packaged source prior to embedding. It checks 10 dimensions, four rational squared damping values, the complete set of distinct gaps, and four horizon choices (one, two, and three full cycles, and infinite horizon), as well as separate direct finite-time sums. For all these settings it checks the spectrum extrema, determinant, inverse trace, condition number and strict optimizer inequalities. It additionally checks the exact eight-vertex conditioning example.

The finite checker is not a proof for all \(n,r,H\). The infinite theorem rests on the symbolic residue decomposition, concavity of \(\log\cosh(cx)/x\), and convexity of \((1+e^{yx})^{-1}\), all explicitly proved in `RESULT.md`. Excluded cases: partial-cycle horizons, noncoordinate actuators, unequal input powers, nondirected dynamics, and independent scientific validation.
