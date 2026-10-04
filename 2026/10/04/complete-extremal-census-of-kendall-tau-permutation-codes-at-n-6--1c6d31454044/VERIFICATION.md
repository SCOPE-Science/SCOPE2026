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

Run `python3 verify.py` in this directory. The script uses only the Python standard library and reconstructs the complete finite computation from definitions. It verifies the 720 vertices, 60,840 threshold edges, constant degree 169, exactly 3,960 four-cliques, no five-clique, universal six-distance profile equal to 10, and the four orbit sizes 360, 720, 1,440, 1,440 under the stated relabeling-and-reversal action.

The computation is exhaustive over the finite domain; there is no probabilistic step, search cutoff, or timeout certificate. It proves no statement for other values of n or d and does not assert that the natural 1,440-element symmetry group is the full isometry group.
