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

# Computational and mathematical verification

Run `python3 verify.py` from the directory containing this document. The script uses only the Python standard library. `verification_output.txt` is the actual recorded standard output.

The verifier generates every simple labelled source graph on \(1\) through \(4\) vertices (\(75\) graphs in total), plus six specified source graphs on five vertices. It independently constructs the subdivided-plus-private-leaf graph, checks every possible vertex subset against the definition of domination, extracts the exact minimum-cardinality family, and compares with the predicted independent-set representatives. It also builds the full independent-set reconfiguration adjacency, checks all-pairs shortest distances against Hamming distance, enumerates every induced coordinate cube and checks the resulting polynomial coefficients.

The recorded execution exhausted **1,369,076** vertex subsets over **81** source graphs, to maximum derived order 20, without any mismatches. It includes complete, empty, path, cycle, star and complete-bipartite source graphs of order five. Every tested claim passed.

The finite checks do not establish the theorem for untested orders. The unlimited statement is proved in `RESULT.md` by private-pair domination forcing, a one-subdivision adjacency criterion, and coordinate-face counting. The counting-hardness consequence uses the independently published \(\#P\)-completeness theorem for independent sets in 3-regular graphs; no computational test certifies an entire complexity class. Independent mathematical review and definitive bibliographic priority checks remain outstanding.
