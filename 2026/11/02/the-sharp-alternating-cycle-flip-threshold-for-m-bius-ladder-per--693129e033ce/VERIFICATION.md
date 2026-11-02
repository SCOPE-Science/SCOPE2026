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

# Reproducibility

Execute `python3 direct_checker.py` and `python3 structural_checker.py` using Python 3 standard library only. The first exhaustively enumerates all perfect matchings and single-cycle symmetric differences for every graph from width 4 through 13; checks the sharp connected cutoff and the number of first bridges. The second independently enumerates cyclic independent edge sets through width 18, constructs corresponding perfect matchings, and verifies all length-minimal alternating semicircle flips to one-chord configurations. The expected success markers are `MOBIUS_DIRECT_EXHAUSTIVE_PASS` and `MOBIUS_TILING_ONE_CHORD_PASS`.

The exhaustive tests are finite checks. The infinite-family sharpness proof uses a signed perimeter-displacement congruence and explicit one-chord semicircle constructions; neither infinite claim is inferred from experiment. An independent scholarly audit has not been performed.
