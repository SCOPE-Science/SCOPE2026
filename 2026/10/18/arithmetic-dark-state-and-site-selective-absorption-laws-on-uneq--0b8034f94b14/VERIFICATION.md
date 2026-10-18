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
# Verification evidence and limits

`verify_spider.py` is an independent finite-matrix calculation: it first builds the full undirected star-of-paths adjacency matrix, then diagonalizes that matrix, groups degenerate eigenvalues and projects away the component visible from the absorbing hub. It derives its numerical dark-space dimension and projector diagonal without invoking the closed-form divisor formula in the construction of that projector. The separately calculated exact fraction formula and number-theoretic dimension are then compared with the full-matrix answer.

The verification program was executed on 321 small configurations with two to four arms (the theorem applies to three or more arms), checking 2904 individual vertex probabilities. All assertions passed, including exact equivalence of positive local survival with the site-divisibility obstruction. The maximum projector-diagonal discrepancy was approximately `1.9984e-15`. The script also emits exact fractions for selected asymmetric examples and can be rerun by invoking `python verify_spider.py` with NumPy, SciPy, and SymPy installed.

The derivation in `RESULT.md` is the proof for arbitrary finite integer arm lengths. The finite experiments alone do not prove it. No claim of separate independent audit, physical experiment, finite-time error bound, or external certification is made.
