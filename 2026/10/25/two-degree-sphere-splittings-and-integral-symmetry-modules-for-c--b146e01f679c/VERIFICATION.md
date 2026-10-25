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

Run `python3 verify.py` in a directory containing `verify.py` and `verify_output.txt`. The script uses only the Python 3 standard library and terminates with `VERIFY_OK`. Its output should byte-match the embedded `verify_output.txt`.

The verifier constructs a bouquet graph from a common central vertex and disjoint complete private blocks. It independently enumerates all order-\(t\) cliques using literal graph adjacency, enumerates all nonempty simplices, and checks agreement with the stated per-block face quotas for *every* vertex subset. It computes all reduced mod-two Betti numbers using exact binary boundary ranks and compares them with the formula for 23 configurations. It also computes signed simplicial Lefschetz numbers for 235 separate within-block permutations and compares them with exterior-augmentation module characters computed from permutation cycle lengths.

The recorded execution examined 7,278 nonempty simplicial faces. These tests are finite and field-two checks; the general integral homotopy type and group-lattice statements depend on the written skeleton, nullhomotopy and natural-chain proofs. No external or independent audit has been performed.
