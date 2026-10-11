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
The all-parameter theorem is proved symbolically in `RESULT.md`.

Critical checks:
- The polar in the zero-sum space is the unit graph-Lipschitz polytope.
- The published Proposition 3.5 gives all complete-multipartite facet functions in exactly two types.
- Centering a facet function does not alter its functional on the zero-sum space.
- Type-(i) centered squared norm is \(q-(2t-q)^2/N\).
- Type-(ii) centered squared norm is \(t(N-t)/N\).
- The first expression is maximized on a largest part with parity-balanced signs.
- The second is maximized by a balanced binary level size.
- Explicit feasible Lipschitz labelings attain both candidate values.
- Central symmetry converts polar circumradius to primal inradius.
- The graph-spread identity follows from \(\|f-\bar f\mathbf1\|_2^2=N\operatorname{Var}(f)\).

`verify.py` enumerates all source-classified facet functions for representative multipartite size vectors and confirms the exact maximum centered norm and contact-type conditions. The finite computation is corroborative only.
