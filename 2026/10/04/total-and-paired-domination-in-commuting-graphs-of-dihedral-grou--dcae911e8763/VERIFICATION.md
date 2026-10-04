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

The proof was replayed against the standalone `verify.py` artifact.

The checker implements multiplication in
\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,
\]
computes the center, constructs the commuting graph on noncentral elements, and finds its connected components.

For every
\[
3\le n\le10,
\]
the checker verifies that odd \(n\) produces one rotation clique together with \(n\) isolated reflections, while even \(n\) produces
\[
K_{n-2}\sqcup \frac n2 K_2.
\]
It then exhaustively computes total and paired domination minima whenever they exist.

Exact output:

```text
VERIFY_OK
n=3 vertices=5 center=1 components=[1, 1, 1, 2] gamma_t=None gamma_pr=None
n=4 vertices=6 center=2 components=[2, 2, 2] gamma_t=6 gamma_pr=6
n=5 vertices=9 center=1 components=[1, 1, 1, 1, 1, 4] gamma_t=None gamma_pr=None
n=6 vertices=10 center=2 components=[2, 2, 2, 4] gamma_t=8 gamma_pr=8
n=7 vertices=13 center=1 components=[1, 1, 1, 1, 1, 1, 1, 6] gamma_t=None gamma_pr=None
n=8 vertices=14 center=2 components=[2, 2, 2, 2, 6] gamma_t=10 gamma_pr=10
n=9 vertices=17 center=1 components=[1, 1, 1, 1, 1, 1, 1, 1, 1, 8] gamma_t=None gamma_pr=None
n=10 vertices=18 center=2 components=[2, 2, 2, 2, 2, 8] gamma_t=12 gamma_pr=12
```

The finite replay is corroborative only. The arbitrary-\(n\) theorem follows from the explicit commutation equations.
