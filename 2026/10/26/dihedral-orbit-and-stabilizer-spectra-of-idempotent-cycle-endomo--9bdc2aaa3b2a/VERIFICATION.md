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

# Reproducible computation

The file `cycle_retraction_orbit_checker.py` enumerates strict graph endomorphisms of each cycle with 3 through 14 vertices using adjacency-constrained words. It retains idempotents only after direct composition checks, then computes complete conjugation orbits under rotations and reflections. Independently it evaluates the path-walk matrix-entry predictions by an iterative integer recurrence.

Run `python3 cycle_retraction_orbit_checker.py` with no nonstandard dependencies. Compare the printed output with `cycle_retraction_orbit_checker.out`.

The checks cover twelve complete finite monoids and 3176 idempotents. They do not constitute a proof for all graph sizes or an independent audit. The general theorem is proved by retraction structure, walk bijections, and dihedral orbit-stabilizer counting in `RESULT.md`.
