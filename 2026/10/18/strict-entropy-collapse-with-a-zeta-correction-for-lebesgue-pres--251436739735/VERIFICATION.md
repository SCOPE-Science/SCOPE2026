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

Run `python verify.py` in the directory containing that file. The checker requires the standard Python library and `mpmath`. A completed execution reported:

```
VERIFY_OK 8 entropy(2)= 0.590862907413260413 C= 2.20876139454400384 J= -3.11030407191369955
```

The checker independently evaluates the entropy via (i) the substitution \(z=t^{B-1}\), and (ii) direct integration of the two branch derivatives. It checks the inverse-Jacobian sum with exact rational numbers, a decreasing set of sample entropies, the quadratic deficit at \(B=1\), and the two large-parameter coefficients. Rounding tolerances and finite parameter selections are displayed in the script. The analytic generating-partition argument, strict monotonicity for **all** real \(B\ge1\), and the asymptotic remainder estimates are mathematical proof obligations discharged in `RESULT.md`, not consequences of the numerical tests.

Scientific limitations: the invariant probability is normalized Lebesgue on this specified four-piece map. No inference is made about alternate invariant measures, topological entropy, convergence rates for dynamics, or other intermittent families.
