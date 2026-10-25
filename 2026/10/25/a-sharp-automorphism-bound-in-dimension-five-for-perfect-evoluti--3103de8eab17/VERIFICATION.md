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

# Reproducibility and checks

`python3 verify.py` enumerates every directed five-vertex support with a perfect matching that admits a nontrivial diagonal automorphism, using the complete possible prime-order patterns \(3,5,7,31\). For each retained graph it computes diagonal-group order from modular edge equations and the graph-automorphism count from all \(120\) vertex permutations.

Observed: 99 distinct maximal allowed edge sets, 26,989 nonempty candidate subgraphs before the matching test, 3,304 matching-compatible candidates, and exactly 24 maximizing labeled support graphs, all directed five-cycles. The maximum is 155; the checker prints `VERIFY_OK`.

Completeness of the finite graph check uses the supported-matching cycle decomposition, which bounds diagonal torsion to \(3,5,7,31\). Every nontrivial finite diagonal group contains an element of one of these prime orders. The proof in `RESULT.md` independently handles the case of trivial diagonal group with the group-theoretic bound 120. No computational sample is used as evidence for an unbounded dimension statement: the dimension is fixed to five, and the universal field argument is symbolic.

The code uses only Python's standard library. Independent mathematical audit and independent replication are not performed.
