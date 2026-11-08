---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For n>=2k>=4, Johnson G=J(n,k) is regular with d=k(n-k), N=binom(n,k), and line graph X=L(G) is vertex transitive of order Nd/2 and degree 2(d-1). In rank-three FO pure adjacency, the complete possible equality/adjacency diagrams for three variables reduce, by transitivity, to possible third-vertex common, one-sided and neither-neighbor extensions for each pair type. Adjacent e,f in X share endpoint u in G: at least d-2 common, d-1-epsilon one-sided, and an edge outside union of 3 vertices; all four witness types exist. Nonadjacent e,f are disjoint edges of G: one-sided types always exist and neither exists except special n=4 pair. Common witness iff original edges have a cross-edge; an induced 2K2 in J(n,k) exists exactly for n>=6, via six extra elements for n-k>=4 and explicit (123,124,156,256) when (n,k)=(6,3). For n4 and n5, J(n,2)=L(K_n) cannot contain such induced matching because it requires six K_n vertices. Exact pair signature sets separate 4, 5, and >=6 by rank-three sentences; smallest orders 12,30,60. Independent explicit line-graph pair-signature enumeration for n<=8 agrees; the unbounded case is proved by constructions and inequalities.

## originality

PASS

This is an exact fixed-quantifier-rank classification for a familiar infinite graph family after line-graph transformation, not a general Johnson graph automorphism or first-order definability statement. The new Oct 29 2026 full-text Johnson model-theory paper proves a bounded-depth equivalence for J(n,k) itself when the minimum subset parameter is sufficiently large, but its quantified structure is not L(J(n,k)), and its bound does not cover the k=2 regime. Prior EF game machinery furnishes a proof method but not this three pair-spectrum classification. A generic theorem characterizing all vertex-transitive graph classes at rank three could contain the result as a corollary; no concrete dominating statement found.

## value

PASS

Quantifier rank three provides a canonical measure of logical distinguishability. The result classifies a natural infinite family, identifies the exact small exceptional parameters, proves uniform eventual indistinguishability, and supplies the sharp smallest representative 60 despite diverging graph orders and subset dimensions. This is a motivated model-theoretic classification, not a randomly chosen instance enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
