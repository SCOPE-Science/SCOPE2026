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

# Finite verification

Run `python3 verify.py` using Python 3.8 or later. The script reconstructs the Petersen graph as disjointness of two-subsets of five labels. Its 1,024-element exhaustive enumeration, two independent forest tests, free-face/coface dictionary, 389-pair Morse matching, acyclicity check over all 3,470 face incidences, and all 120 exact Lefschetz comparisons are assertion checked. The output must match `verification_output.txt` and end in `VERIFY_OK`.

The simplicial-collapse and discrete-Morse topological consequences use standard exact theorems. The group-character identification uses the exact exterior-square character formula and character orthogonality. There are no random seeds, external dependencies, simulation estimates, or unverified larger-graph assertions. This verification is not independent mathematical validation.
