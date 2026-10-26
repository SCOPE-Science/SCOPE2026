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

# Verification details

Run `python3 verify_full.py` to reconstruct the undirected adjacency lists and apply exact synchronous neighbour-multiset refinement from the root singleton. Run `python3 verify_quotient.py` to construct a separate distance-quotient transition matrix and independently evolve colour signatures. Neither script requires third-party packages.

The first verifies every partition at every strict round for 840 parameter pairs in the main domain, plus the exact three-round boundary behaviour in 29 additional parameter cases; it touches 402,409 vertex-round instances. The second verifies the same 869 parameter cases independently, with 206,045 distance-profile checks in the main domain, and confirms the unique second-round merger at the boundary.

Execution records are included as `full_output.txt` and `quotient_output.txt`; each ends in `ALL_TESTS_PASS`. Inputs of both programs are generated deterministically. The computation is finite; the all-parameter statement is supported by the proof in `RESULT.md`, particularly the initial radius-two separation and the first-adjacent-stratum frontier induction.

There is no formal proof assistant certificate and no independent audit. No extension to smaller values of \(n\), arbitrary root sets or general circulants is asserted.
