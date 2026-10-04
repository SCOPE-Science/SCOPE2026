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

The verifier reconstructs the abstract zero-divisor graph from valuation layers and performs independent arithmetic checks.

It verifies:

- \(|V_i|=(q-1)q^{\ell-i-1}\) in each tested parameter pair.
- Adjacency is exactly the threshold \(i+j\ge\ell\).
- The degree of layer \(V_i\) is \(q^i-1\) for \(2i<\ell\) and \(q^i-2\) otherwise.
- Distinct layers have distinct degrees, while vertices inside one layer are twins up to their mutual edge.
- The all-but-one-per-layer set has cardinality \(q^{\ell-1}-\ell\) and resolves the graph.
- In every tested graph with at most \(15\) vertices, exhaustive search rules out all smaller resolving sets.
- Direct multiplication in \(\mathbb Z/8\mathbb Z\) and \(\mathbb F_2[x]/(x^3)\) gives the same valuation-layer graph profile.
- Direct multiplication in \(\mathbb Z/16\mathbb Z\) and \(\mathbb F_2[x]/(x^4)\) gives the same valuation-layer graph profile.

Exact output:

```text
VERIFY_OK
abstract_cases=6
metric_dimension_exhaustive_for_all_cases_with_at_most_15_vertices
same_graph_profile=Z8_vs_F2[x]/(x^3)
same_graph_profile=Z16_vs_F2[x]/(x^4)
```

These computations are finite stress tests. The arbitrary-\((q,\ell)\) theorem is established by the valuation, degree-separation, twin-class, and explicit resolving-set arguments in `RESULT.md`.
