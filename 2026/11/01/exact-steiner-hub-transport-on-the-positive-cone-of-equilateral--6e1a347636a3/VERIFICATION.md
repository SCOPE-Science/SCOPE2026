---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Use the proven Cúth–Raunig finite rooted-spanning-tree characterization of Lipschitz-free p-norms. For positive source mass at each a_i, detaching any source-to-source subtree and reattaching it to its grandparent changes that edge length from 1 to <=1 while strictly reducing the flow on the former parent edge. Thus some minimum has no source-to-source edges. A positively loaded hub parented by a source can similarly be reparented to b at unchanged length t, reducing the source-to-b flow; hence each source either goes directly to b or via h and h directly to b. This yields the exact subset minimum sum_{i outside S} c_i^p + t^p(sum_{i in S}c_i^p+(sum_{i in S}c_i)^p); continuity covers zero masses. On N, direct star gives sum c_i^p. For equal c_i=1, k-selected sources cost m-k+t^p(k+k^p), concave in k, so endpoints give min{m,t^p(m+m^p)} and the threshold m>(t^-p-1)^(-1/(1-p)). Series expansions at p=0, p=1 verify stated singular scales (special limit four at t=1/2). Independent Prüfer-tree enumeration for all spanning trees on two- and three-source test configurations, using positive masses, verified 9 parameter/mass comparisons against the subset formula. The universal result follows from the exact tree-exchange proof, not a finite test alone.

## originality

PASS

Best-of-knowledge originality after primary-literature reading and Resultary queries. The explicitly identified prior statements and implication gaps are documented under the four checks. A failed search is not proof of priority, and inaccessible literature was not treated as automatic failure.

## value

PASS

The positive cone of an equilateral metric with a symmetric one-point hub is a natural restricted model for non-isometric canonical embeddings of quasi-Banach Lipschitz-free spaces. The exact norm for all nonuniform positive molecules, sharp equal-mass cardinality threshold and genuinely selective optimal routing distinguish its geometry from mere sufficient upper bounds or general exponential spanning-tree algorithms. No global inverse-operator norm is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
