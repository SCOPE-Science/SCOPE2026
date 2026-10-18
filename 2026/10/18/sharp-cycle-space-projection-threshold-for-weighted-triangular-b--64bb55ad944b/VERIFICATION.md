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

# Reproducibility and scope

The complete analytical proof is in `RESULT.md`. To reproduce the finite checks, run `python3 verify.py` with standard Python; the fraction-based section requires no third-party packages. The optional fully unsymmetrized linear programming section additionally requires `numpy` and `scipy` and prints an additional numerical optimization check. The saved checker was executed in an environment with SciPy installed and reported:

```
Exact tests: 112 passed
Independent full LP tests: 20 passed
```

Exact checks compute independent column norms and the projection identities in rational arithmetic, across both phase regions including equality. The unsymmetrized programs minimize the operator norm over every real projection matrix satisfying the exact range equations for finitely many small graphs. They are numerical corroboration only; they do not prove the general statement for all real \(0<t\le 2\). Generality follows from finite group averaging and one-dimensional analytic minimization as given in `RESULT.md`.

At \(t=2\), the weighted hub edge is retained as an edge-space coordinate even though it is redundant for shortest-path distance. Independent scientific audit has not been performed.
