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

# Verification scope and replay

`verification_enumerate.cpp` performs a complete \(\binom{28}{10}=13{,}123{,}110\)-subset C++17 mask census. `verification_branch.py` uses a logically separate branching search with a safe lower capacity bound. Both produce precisely the same set of \(28\) masks, as recorded in their output files. Every such mask was compared to the \(28\) distance-shell witnesses.

`verification_geometry.py` reconstructs the graph from the Fano-plane triple construction, verifies the distance-regular intersection counts at every root and vertex, checks each witness and its unique triple-coverage center, computes all \(378\) pairwise exchange costs, and checks the degree/diameter/distance distribution of the threshold-four exchange graph. It independently checks the contents of `certificate.json`.

Use the standard C++17 and Python 3 commands in `RESULT.md`. No extra package or network service is required. The programs and certificate are the complete finite evidence, not an infinite-family proof. Ordinary self-review were completed successfully; independent audit remains not performed.
