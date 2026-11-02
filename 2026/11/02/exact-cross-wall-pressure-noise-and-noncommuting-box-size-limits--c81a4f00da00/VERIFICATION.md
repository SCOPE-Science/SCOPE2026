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

# Reproducibility and proof checks

The primary verification is the analytic generator and boundary Poisson calculation in RESULT.md, supplemented by the exact pathwise spin–displacement identity and the stationary fixed-time moment bound. The proof covers every strictly positive speed, flip rate, mobility and finite interval length.

Run the supplied standalone Python 3 program with the command `python verify_pressure_noise.py`. In the checked environment it returned `PASS: 117 exact-arithmetic assertions`. The program uses only Python's standard library and exact rational arithmetic. It tests the Poisson solution and wall boundary conditions for four rational dimensionless widths; independently constructs finite persistent-walk generators with three grid resolutions and solves stationary balance plus two additive-functional Poisson systems. The numerical discretizations converge toward the analytic continuum rates in the tested cases; they are not a substitute for proving the infinitely many continuum parameter instances.

The calculation assumes a hard-wall convention in which the orientation flips at the same rate at a wall and in the interior. Readers comparing earlier work should map its orientation randomization rate to twice this physical flip rate where appropriate. No independent mathematical, priority or external channel audit has been performed.
