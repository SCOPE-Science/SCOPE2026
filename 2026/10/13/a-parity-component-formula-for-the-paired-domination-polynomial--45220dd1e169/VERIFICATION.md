---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For R_{m,n}=K_m□K_n=L(K_{m,n}), selected rook cells are selected bipartite edges. An unselected cell is undominated iff its row and column both have degree zero in H_S; thus domination iff no isolated row OR no isolated column. L(H_S) has a perfect matching iff each edge-bearing connected component of H_S contains even edge count: necessity by component parity and sufficiency by rooting a spanning tree and pairing its edges plus nontree edges at common endpoints in postorder. The exponential formula for labeled bipartite graphs with edge-weight z, A(u,v;z)=Σ_{a,b≥0}(1+z)^ab u^a v^b/(a!b!), gives even-edge component EGF sqrt(A(z)A(-z)), and no-isolated-side inclusion exclusion multiplies by e^-u+e^-v-e^-u-v. Thus P_{m,n}=m!n![u^m v^n](e^-u+e^-v-e^-u-v)sqrt(A(z)A(-z)). Even-cardinality minimum gives γ_pr=2ceil(min(m,n)/2), except R_1,1 has none. Independently enumerated domination and perfect matchings for 1x1,1x3,2x2,3x3,3x4,4x4; 3x3 polynomial 81z⁴+84z⁶+9z⁸ and 4x4 coefficient vector (80,4464,12150,7992,1820,120,1) for degrees 4,…,16. Formal identity and spanning-tree proof establish all m,n, not finite tests.

## originality

PASS

Brešar, Henning and Rall study paired domination numbers and inequalities in arbitrary Cartesian products, not this all-cardinality polynomial for complete-graph factors. Puttaswamy et al. introduced the polynomial invariant but neither the inspected primary material nor Resultary published corpus gives this rook-graph component-parity EGF. Published complete multipartite graph paired domination polynomial is for K_{n1,…}, NOT Cartesian product K_m□K_n (except incidental tiny coincidences), so no implication. The natural full-size rook-board paired-dominating-set enumerator is distinct and not a routine specialization of checked prior expressions.

## value

PASS

The theorem gives a COMPLETE exact polynomial for all rectangular rook graphs counting feasible paired-dominating vertex SETS, not matchings, by size; the nontrivial even-edge connected-component characterization and bivariate EGF can support further enumeration and algorithmic comparisons. A natural graph family and exact natural invariant are motivated independently of computation; no downstream conjecture required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
