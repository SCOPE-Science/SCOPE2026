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

The verification separates the general proof from finite corroboration.

1. **Left-ideal model.** Every nonzero proper left ideal of \(M_n(\mathbb F_q)\) is represented by a nonzero proper subspace \(U\le\mathbb F_q^n\), with adjacency determined by
\[
U+W\ne\mathbb F_q^n.
\]

2. **Ordinary lower bound.** At most \(q\) selected lines lie in fewer than all hyperplanes, so some hyperplane gives a left ideal adjacent to none of them.

3. **Total domination.** For \(n\ge3\), the \(q+1\) lines of one fixed two-dimensional subspace index a dominating clique. For \(n=2\), distinct lines span the whole space and the graph has no edges.

4. **Paired domination.** The same dominating clique has even order exactly when \(q\) is odd. For even \(q\), every paired dominating set must have at least the next even cardinality \(q+2\), and adjoining one line outside the chosen two-space gives a dominating clique of that size.

The standalone checker independently builds the subspace model and exhaustively searches the cases
\[
(n,q)=(2,2),(2,3),(3,2),(3,3).
\]

Exact output:

```text
VERIFY_OK
n=2 q=2 vertices=3 gamma=3 gamma_t=None gamma_pr=None
n=2 q=3 vertices=4 gamma=4 gamma_t=None gamma_pr=None
n=3 q=2 vertices=14 gamma=3 gamma_t=3 gamma_pr=4
n=3 q=3 vertices=26 gamma=4 gamma_t=4 gamma_pr=4
```

The finite enumeration is corroborative only. The arbitrary-prime-power theorem is established by the symbolic argument.
