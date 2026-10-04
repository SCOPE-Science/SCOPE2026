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

The standalone `verify.py` artifact was read from its packaged path before replay.

It generates all subspaces by taking spans over the prime fields used in the finite tests, constructs the intersection graph from nonzero intersections, and exhaustively enumerates minimum total dominating sets in the cases
\[
(\mathbb F_2)^3,\quad
(\mathbb F_3)^3,\quad
(\mathbb F_2)^4.
\]
For every minimum total set it verifies that all members are hyperplanes and that their common intersection has codimension two.

It also exhaustively determines paired domination for
\[
(\mathbb F_2)^3
\quad\text{and}\quad
(\mathbb F_3)^3.
\]

Exact replay output:

```text
F_2^3: |V(G)|=14, gamma_t=3, min_total_sets=7
F_3^3: |V(G)|=26, gamma_t=4, min_total_sets=13
F_2^4: |V(G)|=65, gamma_t=3, min_total_sets=35
F_2^3: gamma_pr=4, min_paired_sets=77
F_3^3: gamma_pr=4, min_paired_sets=13
VERIFY_OK
```

The exhaustive computations are finite corroboration only. The arbitrary-prime-power theorem is established by the symbolic subspace-cover and matching arguments in `RESULT.md`.
