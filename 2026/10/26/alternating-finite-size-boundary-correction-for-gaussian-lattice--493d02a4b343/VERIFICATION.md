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
Run `python3 check.py` with Python 3.10 or later; it uses only the standard library. The saved `check-output.txt` records the successful output from the packaged script.

The checker evaluates the Gaussian Toeplitz matrix inverses with exact rational elimination, independently computes the \(q\)-binomial orthogonal-polynomial formula, checks orthogonality and polynomial norms, and tests the signed asymptotic prediction in high-precision decimal arithmetic. The infinite-dimensional/RKHS equivalence follows from the representer theorem; convergence and the asymptotic error are established analytically in `RESULT.md` using a meromorphic generating function. Numeric checks alone do not prove asymptotics.

All formulas refer to fixed \(0<p<1\), and no uniform endpoint bound in \(p\) is claimed. The full text of the 1991 Gaussian-matrix inverse source was not available; this is a literature-comparison limitation, not a replacement for the mathematical proof.
