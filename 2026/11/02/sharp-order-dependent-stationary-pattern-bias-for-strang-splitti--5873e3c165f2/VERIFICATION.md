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

# Verification and limits

The proof is self-contained in `RESULT.md` and establishes the exact result for arbitrary finite connected unweighted regular bipartite graphs, all positive time steps, and all integer odd-power indices. The auxiliary `CHECK.py` was executed with Python 3 and SymPy and returned:

```
PASS: 7704 symbolic and numerical probes; odd-power p=1..4 and 4-cycle exact subflows
```

Symbolically checked relations include both fixed-point hyperbolic formulas, their ratio and critical crossing, and their quadratic small-step coefficients for the first four odd nonlinearities. Numerical checks compare direct subflow composition against the closed scalar maps and the complete four-cycle graph-heat projection for 640 seeded parameter instances; they also check fixed points, stationary bias signs and local derivative formulas. These finite checks supplement rather than prove the arbitrary-graph or arbitrary-power assertions. The proof itself relies on invariant eigenspaces, exact solution of a scalar separable reaction flow, reciprocal-power linearization, and monotonicity of \(\sinh z/z\).

No theorem is asserted outside the checkerboard invariant line; transverse stability, fully spatially continuous PDE effects and finite-precision implementation behavior have not been established. An independent mathematical audit has not been performed.
