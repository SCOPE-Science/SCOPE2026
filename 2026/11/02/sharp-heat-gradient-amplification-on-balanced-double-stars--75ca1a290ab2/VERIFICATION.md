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
# Reproducibility and verification

The supporting `check_bistar.py` executable is included in the same package. It requires only Python's standard library. The code constructs the independent tree-edge gradient generator, tests its Taylor-series coefficients through degree eight using exact integer/rational arithmetic, and independently computes heat-kernel probability rows by the uniformization series for the continuous-time Markov chain. For these finite heat rows, the tree-cut formula computes graph-metric \(W_1\) exactly from the row differences, up to floating-point evaluation of the heat kernel.

The actual program was executed successfully:

```
CHECK_OK exact_taylor_orders=9 m_values=9 heat_row_transport_cases=81 checked_graph_families=balanced_double_stars
```

The tested parameters were \(m\in\{1,2,3,4,5,7,10,15,25\}\) and \(t\in\{0,0.0001,0.002,0.04,0.15,0.4,0.8,1.5,3\}\). Analytic proof of the unrestricted statement appears in RESULT.md; these checks are finite diagnostics only. The strict row comparison is proved by the positive convolution identity, and the sharp family-wide limit is obtained by a direct asymptotic argument. Neither conclusion is inferred from the finite tests.

Independent audit was not performed.
