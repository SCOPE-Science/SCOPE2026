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

Direct distance/geodesic argument: for |S|>=3 a supporting cycle site cannot have both root and leaf. A leaf is never geodesic interior; root at occupied site j can occur exactly if 2(g_(j-1)+g_j)>n, including the tied-path equality as forbidden. Thus each k-subset of supporting sites contributes 2^{eligible roots}. Marking eligible single roots, adjacent pairs and (only k=3) triples yields the stated U,V,W correction formula; nonadjacent eligible roots for k>=4 are impossible by disjoint gap sums >n. Low-degree coefficients and the n=3 vs n>=4 top coefficients checked. Independently computed all vertex-subset distances for n=3..6; obtained the source coefficient vectors exactly, and inspected the original verification program covering n=3..9. This proof, not finite checks, supports all n>=3.

## originality

PASS

The original general-position polynomial theory and comb/path-corona formulas do not furnish the cyclic-gap classification for all cycle coronas. Rather already publishes exactly the n=6 polynomial, which is excluded from the novel part. A generic inclusion-exclusion enumerator is not the specialized all-n, polynomial-time coefficient formula; Resultary nearest related records treat complete-graph coronas and spiders. Best-of-knowledge original contribution: all-cardinality cyclic-gap bijection and explicit finite sums for every n.

## value

PASS

Cycle coronas are the natural cyclic counterpart of path coronas in the initiating literature; computing their complete general-position polynomial, not merely its maximum-set size, is a motivated exact natural graph invariant. The cyclic-gap criterion and O(n^4) coefficient arithmetic provide structural and computational value for the unresolved general corona-unimodality question, without claiming unimodality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
