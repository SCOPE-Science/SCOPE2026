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

# Verification record

The proof of the stated mathematical result is in RESULT.md, with complete payoff definitions and the explicit parametric example. The standalone file `verify.py` checks the algebraic coboundary using symbolic payoffs, the binomial defector-payoff polynomial for group sizes 2 through 8, exact rational equilibrium/Jacobian identities, and the linear-response coefficient. The numerical checks shoot a full forced period and integrate the periodic orbit with high tolerance, testing four positive/negative forcing amplitudes. The positive small-amplitude branch is justified by a hyperbolic fixed point of the Poincaré map, not by the finite numerical sample.

Run `python verify.py` after installing `requirements.txt`. In one successful run the program reported an exact first-harmonic square amplitude of `625/52372`; at forcing amplitude 0.12 it reported mean cooperation `0.499828306469` and variance `8.5817286862e-05`, consistent with the exact variance identity. The calculation uses standard floating-point ODE integration and is not an independent proof of an infinite family of periodic solutions.

Literature comparison includes the main 2019 and 2023 model articles and the 2022 preprint's analytical appendix. The 2023 supplementary sensitivity file was located but its full PDF could not be read from the accessible source. This is an explicit residual bibliographic limitation, not a claim that the material was inspected.

Independent mathematical audit and external validation have not been performed.
