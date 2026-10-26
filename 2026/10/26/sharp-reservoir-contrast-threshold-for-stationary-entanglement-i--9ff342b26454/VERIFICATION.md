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

# Reproducibility and verification

Execute `python check_lindblad.py` with Python 3 and NumPy. The standalone script constructs the two-qubit local Lindblad superoperator from physical raising and lowering matrices, independently of the closed-form steady-state calculation. It solves the trace-one stationary linear system and checks matrix elements, normalization, positivity and residuals. It independently computes concurrence from the eigenvalues of the Wootters spin-flip construction rather than trusting the reduced closed-form expression. It tests the exact coupling-window criterion on hundreds of deterministic pseudorandom parameter draws and checks several complementary-bath boundary cases. This program completed successfully in the source package.

The analytic proof in RESULT.md establishes the theorem for all parameters within scope; a finite numerical run is not an exhaustive or infinite proof. In particular, the critical algebra is the identity between the concurrence inequality and a strictly concave quadratic in the dimensionless squared inverse exchange strength, its unique maximizer, the two roots, and the balanced-occupation factorization. The program is a reproducibility check of these conclusions, not independent scientific certification.

Verification limitations: the theorem does not cover unequal total dissipation rates, collective jump operators or reservoirs with memory. The assessed literature is finite; an uninspected equivalent prior formulation remains possible. Independent audit has not been performed.
