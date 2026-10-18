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
# Reproducible mathematical checks
Run `python verify.py` with Python 3 and SymPy. It checks the exact values of one-chord projection integrals by symbolic integration and exhaustively enumerates all perfect matchings on \(2n\) endpoints for \(2\le n\le7\), computing rational moments without floating-point approximation. It separately checks the combinatorial covariance and variance reductions. The full sequence of finite experiments is not a proof of the joint central limit theorem: that follows analytically from the independent-chord representation, orthogonal first projections, iid bivariate CLT and \(O(n^2)\) degenerate remainder variances. Independent audit has not been performed.
