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

The proof derives the two families from the literal full-state two-step return equations, proves their large-amplitude root count via uniform monotonicity, and computes the two return Jacobians explicitly. The asymptotic law and the attracting-strip assertion follow from estimates valid for all indicated parameters. The numerical program is an independent set of illustrative tests, not a substitute for these arguments.

Run `python3 verify_cycles.py` from the same directory as this document, using Python 3.10+ and only the Python standard library. On this package the checker reported:

`PASS: 72 analytic-cycle witnesses (both families), 18 attraction-strip orbits; return equations, full Jacobians, determinant signs, and growth law checked.`

The cases cover three positive parameter pairs and multiple remote phase cells in each of the two branches. The checked matrices were reconstructed from the original map, and the tests verify literal two-step return, traces, determinants, signs, predicted expansion scales, and inner-strip trajectories. Floating-point assertions allow explicitly coded tolerances. No formal infinite computation, machine-certified proof, global attracting basin, or independent validation has been performed.
