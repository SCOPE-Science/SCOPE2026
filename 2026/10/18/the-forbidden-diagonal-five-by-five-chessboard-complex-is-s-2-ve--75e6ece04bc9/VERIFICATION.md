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

Run `python3 artifacts/verify.py` from the package root. This uses only the Python 3 standard library and prints exactly `artifacts/verification_output.txt`. It independently enumerates by row-injection and recursive row assignment, checks all 780 face sets, builds the complete 382-pair Morse matching, checks all 2500 covering relations by topological sorting, and performs exact rational signed boundary-rank elimination.

The topological argument from critical cells and rational ranks to the integral wedge is mathematical, not an assertion that finite sampling proves a family theorem. The program exhausts one explicitly finite complex and its exact chain matrices.

The homotopy result does not identify the integral group-module action, the natural inclusion's map on integral homology, or the corresponding classification for other board sizes. Independent audit has not been performed.
