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

# Verification methods and limits

The complete analytic argument is in `RESULT.md`. All nonstandard quantitative assertions reduce to (i) the Gram determinant and cubic, (ii) positivity of the Gram matrix, (iii) explicit endpoint eigenvalues, and (iv) strict signed monotonicity of the three eigenvalue power sum through the second divided difference. The Hermite–Genocchi integral verifies the sign for all \(0<p<1\), \(1<p<2\), and \(p>2\). The largest-root derivative covers the operator norm. Singular endpoints are handled by finite-matrix continuity.

`verify.py` uses Python 3 and NumPy; run `python verify.py`. In this package it produced: `2154 matrix identity / moment-order / endpoint checks passed`. The script checks six distinct overlap values (including both sides of \(1/2\)), eleven sample exponents, interior phases, characteristic moment identities, and closed endpoint formulas. Finite sampled checks are consistency tests only; neither novelty nor universal correctness follows from the script. No external independent audit or formal proof assistant is claimed.
