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
# Reproduction and limits

Execute `python checks/verify.py` from the directory containing `checks/`. Python with SymPy and Shapely is required. The script checks five symbolic equalities arising in the sharp two-regime bound, tests the exact attainment formula using independent polygon clipping at 49 widths, and tests 340 randomly selected finite multi-plank configurations and 340 separate single-plank configurations. The deterministic seed is encoded in the script. The observed message was `VERIFY_OK symbolic_identities=5 attaining_directions=49 families=340 random_single_planks=340`.

The complete infinite-family proof is in `RESULT.md`. In particular, the Bang-map theorem and the unit-vector dispersion identity justify the passage from finite numerical samples to all plank families; the samples themselves do not do so. Floating-point clipping tolerances are explicitly set in the script. The literature search does not establish independent historical priority, and no independent scientific audit has been performed.
