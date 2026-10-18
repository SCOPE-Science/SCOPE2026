---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

At common n,m the centralization order is exactly the order of maximum degree, since its numerator is n*d_max-2m; degree-Gini order is that of L=sum_{i<j}|d_i-d_j|. The supplied proof identifies d_max=4,L=8 versus d_max=3,L=10, so C_F=2/3>1/4 while Gini=2/15<1/6. Independently enumerated the networkx graph atlas of ALL connected unlabeled simple graphs with 2<=n<=5 (counts 1,2,6,21) and compared every pair with identical m; precisely one reversal occurred, at n=5,m=6. The two degree sequences each have one connected class. Finite exhaustive enumeration is valid here precisely because the n<=5 domain is finite; there is no extrapolation to larger n.

## originality

PASS

Best-of-knowledge acceptance follows the actual statement-versus-implication comparisons above; the strongest inspected primary sources establish a general framework, different problem, or strictly narrower subcase, not this final full claim. The explicitly listed plausible full-text access/implicit-coverage risks remain open; lack of search hits alone is not novelty evidence.

## value

PASS

The graph order and edge-count restrictions eliminate the confounding change of average degree in comparisons of widely used heterogeneity measures. Identifying the sharp smallest counterexample and its unique graph classes is a natural finite boundary, not an arbitrary numerical slice, and the reversal illustrates a genuine distinction between maximum-driven and full-dispersion indices. Its mathematical significance is necessarily modest and specific to these two measures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
