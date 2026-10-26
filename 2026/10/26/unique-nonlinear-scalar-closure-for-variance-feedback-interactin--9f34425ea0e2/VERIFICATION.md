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

# Reproduction and boundaries

The companion `verify.py` uses only Python 3 standard-library facilities and runs with `python3 verify.py`. It checks exact rational three-point fourth-power identities, the linear pairwise-square identity, explicit matched-variance witnesses against power-law scalar closure, the reciprocal-variance Itô coefficients, and selected limiting inverse chi-square moment evaluations. The script prints `PASS 841 checks` on success.

The limit theorem also requires mathematical arguments not established by finite testing: strict convexity of the classification witness, positivity/nonexplosion and transience of squared-Bessel paths for dimension above two, the noncentral chi-square transition theorem, the Poisson-mixture representation, and analytic gamma integration. These are presented with hypotheses in RESULT.md. No independent mathematical audit has been performed.
