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

The proof was checked symbolically from the definitions. The finite endpoint is obtained by solving a monotone rational inequality, and its derivative simplifies exactly to
\[
-\frac{B(h-1)(n+1)}{(1+n\lambda-h)^2},
\]
which is negative on the finite branch because \(B>0\), \(h>1\), and \(n\ge1\).

The reserve statement uses the exact infimum
\[
\inf_{v>0}W_\lambda(v)=W(1-\lambda),
\]
so it is an infinite-domain argument rather than an empirical bound.

For an independent replay of the algebraic cases within this package, run:

`python artifacts/verify.py`

The script checks exact rational examples of the phase transition, deterministic pseudo-random nesting instances, and both directions of the reserve frontier. It prints `VERIFY_OK` on success.

The script is supplementary and does not certify historical originality or multi-step optimality.
