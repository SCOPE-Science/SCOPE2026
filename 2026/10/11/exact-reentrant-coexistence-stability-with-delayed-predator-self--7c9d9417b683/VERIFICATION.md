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

At the exact positive parameter vector, substitution gives the equilibrium \((1,1)\). Exact rational differentiation yields instantaneous entries \((-3/2,-6,7/20,0)\) and delayed predator diagonal entry \(-1\). The characteristic frequency identity is \((X-27/20)(X-8/5)\), with exact phase cosines \(-7/8\) and \(-9/11\) and positive sines \(\sqrt{15}/8\) and \(2\sqrt{10}/11\). The sign of the derivative at the two roots is \(-1/4\) and \(+1/4\), respectively. All calculations are reproducible using `python3 check.py`, Python standard library only.

The proof, not finite testing, supplies the exclusion of further frequencies and unstable roots from infinity. The checker does not certify a global spectral enumeration, periodic solutions, or nonlinear stability at the crossing delays. Independent audit has not been performed.
