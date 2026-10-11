---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For H equal to the radial kernel minus the proposed comparison term, direct differentiation gives H'(rho)=-(1-rho)(1-rho^2)^alpha<0 and H tends to zero at rho=1, proving the inequality for every alpha>-1; the endpoint ratio gives sharpness of this kernel constant. Substituting it into the source's nonnegative Fubini reduction cancels alpha+1 and leaves the same angular factor. The companion weight-independent Riesz estimate then gives the stated constant. The negative-alpha extension uses only integrability and the sharpened kernel step, not the source's alpha>=0 comparison.

## originality

PASS

The source two-diameter theorem contains an explicit factor 2^alpha and is restricted at the critical kernel step to nonnegative alpha. The audited sharp kernel inequality replaces exactly that step, removes the factor uniformly and extends the same argument to the natural integrable range alpha>-1. The companion source supplies the needed weight-independent harmonic Riesz estimate. No inspected source or Resultary record states the resulting weight-uniform two-diameter bound.

## value

PASS

The result removes an exponential-in-weight loss from a new weighted Frazer theorem and restores the full natural Bergman weight range. The improvement is quantitatively meaningful and applies uniformly across weights, while making no unsupported claim that the final operator constant is globally sharp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
