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
The bundled checker verifies the two algebraic identities used for global boundedness.

For an arbitrary symbolic finite chain of length \(n\), the weighted quantity
\[
Q=
B_0+\sum_{i=1}^n\alpha^{-i}B_i+\alpha^{-n}P
\]
cancels each maturation flux and the terminal plasma-cell production flux. Its derivative is
\[
\dot Q=
-d\left(
B_0+\sum_{i=1}^n\alpha^{-i}B_i
\right).
\]

The checker explicitly reconstructs this cancellation for several symbolic chain lengths and verifies the general coefficient pattern.

It also verifies that the activation and T-follicular-helper differentiation terms cancel in
\[
T=N+H+G,
\]
leaving only the recruitment term and nonpositive losses.

Strict positivity and the exponential antigen bound are proved analytically from variation-of-constants formulas; no numerical trajectory is used.
