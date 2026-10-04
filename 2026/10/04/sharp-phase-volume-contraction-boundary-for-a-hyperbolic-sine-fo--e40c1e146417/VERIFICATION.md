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

The vector field was differentiated term by term. The only nonzero diagonal Jacobian entries are
\[
\frac{\beta_1}{5}(1-\epsilon\cosh x_1)
\quad\text{and}\quad -1,
\]
which gives the stated divergence. Exact rational replay in `verification/check.py` verifies the coefficient identities, the incompatibility with the source's printed coefficients, the sharp maximum at \(x_1=0\), and the source-parameter margin \(-1/10\).

The orbitwise determinant formula uses Liouville's identity on an interval of classical existence; no global-existence premise is silently added. The invariant-measure formula is restricted to compactly supported ergodic invariant probability measures, so the derivative cocycle is bounded on the support and the usual Oseledets trace average applies.

Limits: the checks do not establish existence or compactness of an attractor, do not certify numerical Lyapunov spectra, and do not assess synchronization or cryptographic claims. Literature coverage has the residual indexing risks stated in `AUDIT.json`.
