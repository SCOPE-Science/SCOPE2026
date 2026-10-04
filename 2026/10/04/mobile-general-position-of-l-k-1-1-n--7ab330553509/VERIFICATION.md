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
# Verification

The theorem is verified analytically; no numerical experiment is required for the infinite claim.

The graph model is checked directly from incidence in \(K_{1,1,n}\): \(x\) is universal, \(A\) and \(B\) are \(n\)-cliques, and the only cross edges are \(a_i b_i\). This is exactly \(K_1\vee(K_n\square K_2)\).

For correctness of the upper bound, the proof derives the diameter-two general-position criterion and then classifies enough induced clique components to show \(\operatorname{gp}=n+1\). Every maximum configuration is frozen. The special case \(n=2\), where maximum cliques include the matched-pair triangles \(\{x,a_i,b_i\}\), is checked separately and is not absorbed into the \(n\ge3\) argument.

For correctness of the lower bound, begin at \(S_0=\{x,b_1,\ldots,b_{n-1}\}\). Visiting \(b_n\) uses \(b_1\rightsquigarrow b_n\). Visiting \(a_n\) uses \(x\rightsquigarrow a_n\). Visiting \(a_i\) for \(i<n\) uses
\[
b_i\rightsquigarrow b_n,\qquad x\rightsquigarrow a_i,
\]
followed by the reverse moves. At every intermediate stage the occupied induced graph is either a clique or a disjoint union of two cliques, hence remains in general position.

The proof establishes exactly the stated domain \(n\ge2\). It makes no assertion for \(n=1\) and no assertion for broader complete-multipartite line-graph families.
