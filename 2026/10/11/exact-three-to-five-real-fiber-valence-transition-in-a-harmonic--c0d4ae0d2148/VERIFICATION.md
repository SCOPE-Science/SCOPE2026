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
# Reproducibility and checks

Run `python3 verify_real_fibers.py`. The standalone standard-library script evaluates the threshold, checks the explicit endpoint-ratio constant, and finds two different positive-height roots inside the unit disk for each of three sample parameters above the threshold. Their conjugates and the central real point give five different preimages. It also samples parameters below the threshold.

The critical infinite proof is analytic: writing the imaginary-axis equation as \(\mu_x(y)=m\), the sign of the exact rational function \(\operatorname{Im}(1+3z^4)/(1-z^4)^2\) shows \(\mu_x\) is initially increasing and has at most one interior maximum. Endpoint derivatives and continuity establish both cases for every real parameter, without numerical enumeration. The script does not certify transcendental inequalities or exhaustive counts beyond the written proof.

The two threshold regimes include the equality case in the three-preimage branch. Only real targets are asserted. Independent audit has not been performed.
