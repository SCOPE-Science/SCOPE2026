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

`verification/verify.py` is a standard-library Python 3 program operating on graph neighborhood bit masks. It separately evaluates total domination and independence of the outside set; a coalition check requires every part to fail TOIDS individually while at least one two-part union passes. It tests the explicit partition defined in the theorem for the selected vertex of maximum degree.

For exact small graphs, the routine `direct_coalition_number` recursively enumerates every set partition precisely once: starting from an empty partition, each successive labeled vertex is inserted into one existing block or creates a new terminal block. It scores the resulting complete partitions without pruning. In the six-vertex boundary instance there are \(203\) such partitions; it returns coalition number \(3\), strictly below the degree-bound value \(4\).

The exhaustive labeled-graph search covers all \(33{,}864\) graph edge masks across orders three to six, with \(72\) meeting the stated girth and minimum-degree hypotheses. The resulting exact coalition numbers are compared to \(\Delta+1\). Exhaustive coalition checks are also run for the seven- and eight-cycles, the two-five-cycle bouquet, and the Petersen graph. The Heawood graph and the three- and four-cubes are checked constructively only. Three boundary cases are exhaustively verified: \(K_4\), \(P_4\), and \(K_{3,3}\) minus two independent edges.

The recorded output is in `verification/verify_output.txt`; the final success marker is `VERIFY_OK`. The mathematical proof covers arbitrary finite order and does not infer infinite validity from the finite sample. No expert audit has been performed.
