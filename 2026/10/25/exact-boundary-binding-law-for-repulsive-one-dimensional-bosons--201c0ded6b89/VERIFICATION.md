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

## Reproducible checks and limits

- The ordered-chamber differential equation gives the stated energy.
- The Robin boundary condition follows from the first exponent \(a_1=\kappa\).
- The contact condition follows from \(a_j-a_{j+1}=g\) for every adjacent pair.
- The norm factors into \(N\) exponential integrals in gap coordinates; the smallest rate is \(A_N=\kappa-(N-1)g\).
- The last-particle energy gap is the square of this rate and is positive in the stated regime, placing the eigenvalue below the one-free-particle cluster threshold; the outermost gap has mean \(1/(2A_N)\).
- No numerical extrapolation or external certification is used.

Limits: this verifies the explicit fully boundary-bound state for \(\kappa>(N-1)g\). It does not classify the full excited spectrum or prove that no other state family exists below this threshold. Independent audit has not been performed.
