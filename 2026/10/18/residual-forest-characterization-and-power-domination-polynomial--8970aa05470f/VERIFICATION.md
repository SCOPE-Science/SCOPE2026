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

# Verification and scope

The exact proof is contained in `RESULT.md`. All computations use the standalone standard-library `verify_power_multipartite.py` script in this package. Running `python verify_power_multipartite.py` builds all complete multipartite graphs with the specified part profiles; creates their line graphs independently as incidence graphs; simulates the closed-neighborhood and one-neighbor forcing dynamics; computes the unused-original-vertex criterion independently; enumerates exact coefficient sequences; and compares those sequences with a separately calculated inclusion–exclusion expansion. It checked 27 graphs and 255318 edge subsets. It also checked the formulas for minimum sets of tested rook graphs and triangular graphs of orders 3 through 8. `verification_output.txt` records the actual execution output; a later replay of the extracted package script matched it.

Finite verification does not certify the theorem for all parameters. The general argument follows from the first-cycle impossibility, forest leaf-stripping and unique unused-vertex support decomposition in the paper. Independently audited verification is not claimed.
