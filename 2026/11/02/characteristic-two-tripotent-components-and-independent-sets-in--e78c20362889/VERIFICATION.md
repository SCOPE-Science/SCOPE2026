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

# Verification
From the directory containing `verify.py`, run `python verify.py`. The script uses no third-party dependencies and exhausts all element coefficients for twelve small quivers over fields of sizes two, three and four; it does not extrapolate to infinite families. It independently implements quiver multiplication and evaluates \(a^3=a\) directly, then compares with the closed formulas. Auxiliary odd-characteristic checks guard against an incorrectly implemented field operation but do not support novelty of the odd case.

It checks characteristic-two unipotent orbit sizes by explicit parameter fibers in small cases. The output ends in `TRIPOTENT_GRAPH_CENSUS_OK 12 exhaustive finite-field cases`. The infinite statement is proved in RESULT.md by a coefficient identity, polynomial inverse maps, and an explicit graph reduction. Tests verify finite instances, not publication priority or potentially nonreduced scheme structures. No independent audit or human verification is asserted.
