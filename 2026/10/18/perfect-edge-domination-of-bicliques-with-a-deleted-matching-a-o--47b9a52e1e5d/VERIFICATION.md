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
Run `python verify_ped.py` with a standard Python 3 interpreter. The verifier explicitly tests the perfect-edge-domination condition for each candidate edge set, including all missing-edge pairs, and compares the exact histogram with the theorem. The routine also enumerates candidates for the zero-degree vertex set independently, and checks the one-edge jump across 41 balanced graph sizes. See `verify_stdout.txt` for the exact recorded results. The program is a finite validation of proof ingredients, not an exhaustive certification for unbounded dimensions. No independent audit has been performed.
