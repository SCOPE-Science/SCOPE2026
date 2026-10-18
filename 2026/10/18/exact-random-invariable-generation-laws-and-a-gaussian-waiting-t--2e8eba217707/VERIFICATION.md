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

# Verification and reproducibility

Run `python check_invariable.py` from a directory containing the supplied checker. It uses Python's standard library only and enumerates all subgroups, conjugacy classes, and ordered tuples for the stated small semidirect products. The checker compares its independent maximal-subgroup obstruction counts with the theorem's rank/Möbius closed form for nine complete group/length configurations. Expected final output: `ALL_INVARIABLE_CHECKS_PASSED`.

The exact formula for arbitrary semisimple modules uses the proof's finite-field matrix-rank argument; the replay exercises the faithful scalar subfamily. The Gaussian limit and mean-correction inequality are proved using geometric increments, Lyapunov's theorem, and a quotient-generation union bound; their validity is not inferred from finite sampling. Independent audit has not been performed.
