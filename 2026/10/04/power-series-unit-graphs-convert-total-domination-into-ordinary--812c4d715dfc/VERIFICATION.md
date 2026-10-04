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

The proof has three exact checkpoints.

1. **Power-series adjacency.** A series in \(R[[x]]\) is a unit exactly when its constant term is a unit, so adjacency depends only on constant terms.
2. **Independent fibers.** Under \(2\notin U(R)\), no element \(2a\) is a unit. Thus every fiber \(a+xR[[x]]\) is independent and every base edge expands to a complete bipartite graph.
3. **Two-sided domination transfer.** A total dominating set of the finite base lifts to a dominating set upstairs. Conversely, the lifted upper bound makes a minimum upstairs dominating set finite, and an unselected vertex can then be chosen in every infinite fiber; domination of those vertices forces the projected constants to totally dominate the base.

The accompanying verifier checks finite truncations where the same constant-term blow-up mechanism is exact:

```text
VERIFY_OK
Z4: gamma_t(G(R))=2, gamma(G(R[x]/(x^2)))=2
F2xF2: gamma_t(G(R))=4, gamma(G(R[x]/(x^2)))=4
finite_truncation_check=constant-term blow-up agrees with theorem
```

The finite truncation checks are corroborative only. The formal-power-series theorem follows from the structural proof above.
