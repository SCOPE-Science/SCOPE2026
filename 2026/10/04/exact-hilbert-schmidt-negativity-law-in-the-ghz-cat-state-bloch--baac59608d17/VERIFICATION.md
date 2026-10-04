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

The proof is analytic and self-contained. The verification script is a supplementary consistency check rather than a substitute for the proof.

It checks the following normalized formulas numerically with deterministic quadrature:

- \(f_E(e)=12e\sqrt{1-4e^2}\) integrates to one on \([0,1/2]\).
- Its first two moments agree with \(3\pi/32\) and \(1/10\).
- The derivative of \(1-(1-4e^2)^{3/2}\) agrees with the density at interior test points.
- Integrating the fixed-radius conditional density against the Hilbert–Schmidt radial density reproduces the marginal density.
- The moment identity induced by \(R^2\sim\operatorname{Beta}(3/2,1)\) and \(U\sim\operatorname{Beta}(1,1/2)\) agrees with direct marginal integration for several integer powers.

Scientific limits: these checks do not establish anything about other state-space measures or about states outside the GHZ cat support. The infinite-dimensional quantifiers in the statement are discharged by the analytic partial-transpose and volume arguments in `RESULT.md`, not by finite numerical tests.
