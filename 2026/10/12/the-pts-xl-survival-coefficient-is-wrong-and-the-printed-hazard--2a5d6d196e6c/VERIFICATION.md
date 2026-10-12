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
The source PMF can be written as
\[
p_x=Cq^x(x+1)(x^2+Ax+B),
\]
with
\[
q=(1+\theta)^{-1}.
\]
After expansion, the count polynomial has degree three. Summing the cubic geometric tail gives the corrected linear coefficient
\[
\widetilde\omega_1(\theta)
=6\theta^7+36\theta^6+108\theta^5+174\theta^4+146\theta^3+45\theta^2+6\theta.
\]

The coefficient difference is
\[
\widetilde\omega_1-\omega_1^{\mathrm{pub}}
=\theta^4(5\theta^3+30\theta^2+90\theta+87).
\]
Thus, for \(x\ge1\),
\[
S(x)-S_{\mathrm{pub}}(x)
=
\frac{x\theta^4(5\theta^3+30\theta^2+90\theta+87)}{6(1+\theta)^{x+8}}.
\]

The included checker verifies the corrected tail against direct PMF summation, tests the exact one-step survival recurrence, reproduces the hazard counterexample at \((\theta,x)=(5,2)\), and compares corrected versus printed stress-strength reliability at \((\theta_1,\theta_2)=(1,2)\).
