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

For the density printed in Lemma 4.1, the factor multiplying the power of \(z\) tends to a finite positive constant at zero, so \(\pi(z)\asymp z^{-2+2r/\sigma_{11}^2}\) there. The endpoint integral is finite exactly when \(-2+2r/\sigma_{11}^2>-1\), equivalently \(r>\sigma_{11}^2/2\). At equality the divergence is logarithmic and below it is a power divergence. At infinity the two algebraic exponents add exactly to \(-4\) and the exponential tends to one, so the tail is always integrable. Thus the displayed density is normalizable if and only if \(r>\sigma_{11}^2/2\). The source then defines its extinction threshold by integrating against that density, so the condition is required for the threshold and Theorem 4.2 as printed. A fresh exact check reproduced the exponent sum \(-4\), the critical exponent \(-1\), and the source example's safe inequality \(1/2>9/50\).

## originality

PASS

The open primary article states Lemma 4.1 with a normalizing constant for the displayed density, then immediately uses that law to define the extinction threshold and states Theorem 4.2 without the required boundary integrability condition. The stronger stationary-distribution hypothesis appearing earlier in Theorem 3.3 is not restated in the separate extinction theorem. Current Resultary and targeted searches found no erratum or source-specific correction. The cited 2018 predecessor could not be obtained from public full-text routes; an authorized institutional retrieval attempt was interrupted by an expired verification tab and was not retried. That access limitation is retained as a residual risk rather than converted into a failure.

## value

PASS

Normalizability is not cosmetic here: the extinction threshold is defined by integration against the asserted invariant probability density. Identifying the exact missing boundary \(r>\sigma_{11}^2/2\) therefore repairs the mathematical domain of a published theorem. Although the endpoint calculation is elementary, its consequence for the theorem statement supplies the substantive motivation required for a normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
