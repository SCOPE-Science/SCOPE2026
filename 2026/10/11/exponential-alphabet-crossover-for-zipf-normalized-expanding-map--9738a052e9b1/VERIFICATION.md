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

## Scope of verification

All countable-alphabet limits in this result are established analytically from a uniform integral-comparison estimate and the Laurent behavior of the Riemann zeta function at one. The finite-alphabet Hausdorff-dimension formula uses separated self-similar-set dimension theory; the full dimension follows from finite subsystems and cylinder coverings.

## Reproduction

Run `python verify_crossover.py` after installing `mpmath` 1.3.0 or a compatible release. An actual replay of the packaged checker passed 87 diagnostics, checking interval-gap identities, pressure equations using Hurwitz-zeta differences rather than infeasible direct enumeration, the limiting integral roots, and the cutoff-threshold signs.

## Limits

The numerical diagnostics are not a substitute for infinite proofs or external validation. At the critical phase \(\tau=1/\lambda\), the manuscript proves only a first-order equality and does not assert a finer signed expansion. The result has received a same-model review; no independent audit has been performed.
