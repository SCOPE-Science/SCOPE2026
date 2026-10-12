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

The analytic proof reduces
\[
q_k(p)-q_{k+1}(p)
\]
to a positive binomial mass times \((1-p)R_k(p)\), where
\[
R_k(p)=\frac{9k^2p^2-15k^2p+4k^2+9kp^2-17kp+6k+2p^2-4p+2}{2(k+1)(2k+1)}.
\]
The two decisive symbolic identities are
\[
R_k'(p)=\frac{(3k+1)(6kp-5k+4p-4)}{2(k+1)(2k+1)}<0
\]
for \(0<p\le1/3\), and
\[
R_k(1/3)=\frac{2(3k+2)}{9(k+1)(2k+1)}>0.
\]
Thus the infinite claim does not depend on numerical enumeration.

The bundled `verify.py` performs three independent exact checks: it computes adjacent binomial tails with `fractions.Fraction`, checks the closed difference formula for a deterministic grid of rational \(p\) and integer \(k\), and verifies the finite three-size block reduction for multiple parameters. It also confirms the endpoint and derivative formulas algebraically by rational evaluation.

Expected successful terminal line:
`VERIFY_OK exact_tail_pairs=180 block_checks=72`.

The finite grid is a reproducibility check only; it is not an exhaustive proof of the real-parameter theorem.
