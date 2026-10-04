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

The proof was checked at four levels.

1. **Adjacency reduction.** \(Ra+Rb=R\) is equivalent to no maximal ideal containing both \(a\) and \(b\).
2. **Forcing vertices.** Chinese-remainder representatives with support at one maximal quotient force every total dominating set to meet the corresponding exclusive cell \(T_i\).
3. **Sufficiency.** One chosen vertex from each \(T_i\) is a clique and dominates every vertex outside \(J(R)\), giving the exact lower/upper match.
4. **Paired parity and polynomial.** Perfect matchings in the clique give the even case; one CRT-constructed extra vertex gives the odd case. The polynomial follows because every total dominating set is exactly an arbitrary superset meeting all \(T_i\).

The standalone finite checker reports:

```text
VERIFY_OK
support_graph_exact_n=2..5
structural_checks_n=2..9
Z30_total_domination_classification=exact
```

The exhaustive calculation is only a stress test. The general theorem rests on the symbolic maximal-ideal and Chinese-remainder arguments.
