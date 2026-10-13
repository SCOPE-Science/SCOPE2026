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

# Computation and proof verification

The mathematical proof establishes the four-core classification and Burnside coefficient formula for each integer \(m\ge5\); this is not a claim based on an experiment. Its key integer invariant is \(\sum_{v\in B}(\deg(v)-1)=3\), where \(B\) is the larger shore. The four core actions are \(S_4,C_2,S_3,C_2\). The double-counting and reciprocal generating-series checks are explicit in `RESULT.md`.

Execute `python3 verify_k4_tree_types.py` using Python 3 standard library. The program enumerates all bipartite Prüfer codes for \(K_{4,5}\) and \(K_{4,6}\), yielding respectively \(32{,}000\) and \(221{,}184\) labelled trees. It independently generates all four core-plus-leaf families and canonicalizes unlabeled trees from unrooted centers to establish exactly \(28\) and \(45\) isomorphism classes, with no overlap between core families. The four generating-function components are also checked by convolution against orbit-count formulas through degree forty.

The text of the recorded replay is embedded in `verify_k4_tree_types.out`. All programs and records belong to this package. Finite tests do not establish the infinitely quantified theorem; the reduction to four cores and full Burnside computation do.

Limitations: classifications for \(m=4\) or for a different smaller shore size are not claimed; a complete wider historical uniqueness guarantee is not available.
