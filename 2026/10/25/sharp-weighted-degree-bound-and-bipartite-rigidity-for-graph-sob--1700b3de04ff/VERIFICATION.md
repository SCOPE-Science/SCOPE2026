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

The exact cut-Schur identity and weighted-degree inequality are algebraically proved in RESULT.md. The equality classification follows from equality in two Cauchy–Schwarz steps and propagation along a connected graph component.

`checker.py` independently compares generalized eigenvalues of diagonal masks against the cut-Schur formula and the sharp degree bound for multiple finite weighted and unweighted graphs, including odd and even cycles and bipartite complete graphs. Run with NumPy and SciPy. An executed run passed 3,056 mask comparisons. The script also checks the closed-form rank-one star formula by exhaustive mask enumeration for several sizes and couplings. Such finite comparisons are diagnostic only, not a proof for all graph sizes.

All findings are statements about the explicitly specified real finite-dimensional graph Sobolev norm. There is no assertion about infinite graphs, nonquadratic energies, or general nonlinear activations. Independent scientific validation has not been conducted.
