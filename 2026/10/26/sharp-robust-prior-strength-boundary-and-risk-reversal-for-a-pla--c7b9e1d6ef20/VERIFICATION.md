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

Execute `python3 verify.py` using Python 3 and SymPy. It independently reconstructs the exact risk algebra, the derivative and discriminant, the isotropic crossing, rational example and selected minimax bounds. The separate angle quadrature integrates the projector loss from Gaussian directions, rather than inserting the closed risk expression in the integrand. Recorded result: `PASS 1777 independent algebraic/rational/quadrature assertions`.

The proof covers all real \(a>b>0\), \(r\ge1\) and \(c\in[0,1]\), including boundary cases; the finite tests do not by themselves establish the universal theorem. The Gaussian moment derivation assumes a nonsingular covariance for finite \(r\). Its deterministic limiting value is taken by continuity as \(r\to\infty\). The matrix-vector access budget is exactly one. No independent audit has been performed.
