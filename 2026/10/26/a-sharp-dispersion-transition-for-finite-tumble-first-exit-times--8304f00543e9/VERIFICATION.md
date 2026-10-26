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

# Reproducibility and limits

**Analytical checks:** The three-state generator gives a scalar second-order ordinary differential equation for the symmetric running-state transform. The outgoing boundary conditions determine its amplitude. Taylor coefficients at zero agree with the explicit mean and variance. A polynomial factorization of the deviation from \(2/3\), together with the one-sign-change property of the derivative cubic, proves the claimed global classification for all \(p,x>0\).

**Executable checks:** Run `python verify.py` in this directory with SymPy and mpmath. The script performs five exact algebraic identity assertions, 60 high-precision first/second moment comparisons at 30 parameter pairs, and ten simulation moment comparisons across 150,000 trajectories. The final printed message indicates success. These tests are finite checks and do not prove a theorem by enumeration. The simulation begins in the zero-speed state, uses exponential waiting with the specified switching rates, and stops at the actual first boundary hit.

**Scientific limits:** Absorption is perfect, the interval symmetric, the particle unbiased and initially at the center in the zero-speed state. No uniform inference for a changing drift or a simultaneous new scaling is asserted. Independent auditing has not been performed.
