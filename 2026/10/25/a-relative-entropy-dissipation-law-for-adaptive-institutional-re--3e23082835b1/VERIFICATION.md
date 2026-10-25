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

The analytic proof uses direct differentiation of Bernoulli relative entropy, the exact source-model vector field, strict monotonicity of the finite polynomial reward kernel, coercivity of entropy at the open rectangle's boundary, and the compact-set invariance principle. The parameter restrictions and open-rectangle quantifiers are stated in `RESULT.md`.

The standalone `verify.py` checks the exact dissipation identity, its quadratic bound, and the reward-kernel derivative bound in 6,048 rational configurations using `fractions.Fraction`; it does not approximate an infinite proof. It is executed with `python verify.py` in Python 3. The general claim follows from the included symbolic manipulations, not from this finite battery.

One can also independently differentiate the two entropy integrals: their gradients are \((x-x_*)/[x(1-x)]\) and \((a-a_*)/[(a-\alpha)(\beta-a)]\). The feedback cross terms cancel exactly. At the invariant zero-dissipation line \(x=x_*\), the first vector-field component vanishes only at \(a=a_*\), completing the invariance argument.

Limits: only strictly interior initial states and strict interior-coexistence parameters are included; neither boundary-state attraction nor finite-population stochastic behavior was tested or asserted. Independent audit has not been performed.
