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

# Reproducibility and scope

Execute `python check.py` using Python 3.10 or later. The script has no external dependencies and exits unsuccessfully on any failed assertion. A completed execution printed `PASS 2378 checks`, followed by the constants for \(n=2,3,4,5\); the exact stdout is included as `check_output.txt`.

The checks include exact-fraction enumeration of overlapping-window entries, an independent inclusion--exclusion computation, finite tests for the two-type identity, finite criticality/inequality tests for the Poisson objective, and convergence samples for constructed optimal profiles. The tests are not exhaustive over all probability vectors, all window sizes, or all alphabet sizes. The universal claims depend on the proof in `RESULT.md`, especially the compact subsequence reduction and the unique interior maximizer calculation.

Independent mathematical audit and independent historical-priority verification have not been performed. The leading asymptotic applies with the number of types fixed while window length diverges.
