---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each n-tree T, law at census depth k is the exact integer induced-edge histogram H_T,k(j)/binom(n,k). For forests, induced components equal k-j, so full depths reindex the subgraph-component polynomial. Exhaustive proof enumerates all unlabeled trees n<=10 inductively by all leaf attachments and canonical center-rooted AHU codes; each graph is generated and duplicate isomorphism types merged. Directly counting all 2^n subsets gives complete H_T,k histograms, not a partial sample. Independently computed via networkx nonisomorphic_trees and separate subset enumeration: numbers of shapes n=4..10 equal 2,3,6,11,23,47,106. Individual sufficient depths are n4:{3}, n5:{3,4}, n6:{4}, n7:{4,5}, n8:{5}; for n9 all seven individual depths fail with collision counts k=2..8 [1081,117,10,1,1,7,96], and exactly five sufficient depth pairs {4,6},{5,6},{5,7},{6,7},{6,8}. At n10 the complete set of depths has one known collision pair. The proof is a rigorous bounded complete census n<=10, not an infinite classification.

## originality

PASS

Tittmann–Averbouch–Makowsky 2008/2011 define and study the full subgraph-component polynomial, showing uniqueness for tree orders <=9 and an indistinguishable pair at n=10. Those prior global results do not imply that one exact fixed-cardinality slice suffices through n8 or which pairs of slices suffice at n9. The delimited new theorem is the exact cardinality-sampling design and single-slice collision profile, not the prior full-polynomial ten-tree counterexample.

## value

PASS

Observing a fixed number k of taxa rather than every subset size is a natural constrained sampling design. The exact minimal number and identity of sampling depths is an independently useful finite identification result for all tree topologies up to nine taxa, establishing a sharp one-to-two depth transition; despite no claims for larger trees/noisy samples, a complete natural finite classification has substantive value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
