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
The algebraic verification script checks the invariant identity, boundary-completion identities, matrix determinant and trace, and representative exact resonances. It also simulates projected iterations for interior resonant starts and verifies that the projections remain inactive over repeated periods.

The proof of the all-integer resonance family is analytic: the characteristic roots are \(e^{\pm2\pi i/m}\) when \(\tau\sigma=4\sin^2(\pi/m)\). Numerical replay in the checker is supplementary and is not used as a substitute for that proof.

The originality review inspected the full primary 2014 source and the relevant portions of the 2019 alternating-gradient paper. The conserved interior energy is prior art and is not claimed as new. The new claim is limited to the sharp constrained projection-free threshold and consequences stated in RESULT.md.
