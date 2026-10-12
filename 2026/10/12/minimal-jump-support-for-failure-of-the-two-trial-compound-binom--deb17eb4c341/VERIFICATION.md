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

Let
\[
A=q+pf_0,\qquad B=pf_1,\qquad C=pf_2.
\]
The one-trial compound law has pmf \((A,B,C)\), so the two-trial law is its convolution square:
\[
(A^2,\;2AB,\;B^2+2AC,\;2BC,\;C^2).
\]
Direct expansion gives the complete list of log-concavity defects:
\[
g_1^2-g_0g_2=A^2(3B^2-2AC),
\]
\[
g_2^2-g_1g_3=B^4+4A^2C^2>0,
\]
and
\[
g_3^2-g_2g_4=C^2(3B^2-2AC).
\]
Therefore log-concavity is equivalent to \(3B^2\ge2AC\), which is equivalent to
\[
3\delta f_1^2\ge2f_2,\qquad \delta=\frac{p}{pf_0+q}.
\]

The standalone script `verify_three_point_compound_binomial.py` uses exact rational arithmetic to reconstruct these coefficients and defects over a deterministic grid of rational pmfs and success probabilities. It also exactly replays the maximum-jump-\(3\) counterexample printed in the motivating source. A successful run prints `VERIFY_OK`.

The finite replay is supplementary. The theorem for arbitrary admissible real parameters is established by the displayed algebraic identities, not by enumeration.
