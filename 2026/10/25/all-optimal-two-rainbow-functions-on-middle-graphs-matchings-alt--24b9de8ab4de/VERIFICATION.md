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

# Reproducible verification

Run `python verify.py` with a standard Python installation; no external modules or data files are required. The program builds middle-graph neighborhoods independently of the proof's local-charge argument, enumerates all token placements up to the original vertex count and checks the actual two-rainbow condition for every empty vertex. It independently enumerates matching sets, alternating even cycles, and allowable residual vertex colorings and compares the exact cardinalities.

The recorded checks cover 86 finite graphs, 1,671,091 potential token assignments, and up to 15 middle-graph vertices. Every below-bound labeling fails, and all extremal counts agree with the classification. The program also verifies the path recurrence through order twelve and explicit star counts. Its recorded output is `verification_output.txt`.

These checks do not by themselves certify an unrestricted theorem; the exact for-all-graphs argument is the local-charge proof in `RESULT.md`. No independent scientific audit has been performed.
