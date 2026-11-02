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

# Exact computational verification

The accompanying `verify.py` runs with Python 3 and its standard library only:

```sh
python verify.py
```

On execution, it produced `VERIFY_OK 12593 exact assertions`. Every rational endpoint matrix is assembled independently from the graph Laplacian, then inverted by fraction-valued Gaussian elimination in small dimensions; the result is compared entrywise to the Walsh formula. It checks the displayed low-dimensional rational identities by full polynomial cross-multiplication, the coefficient and rational-witness conditions for the low-dimensional root counts, the fifth-order stability-function coefficient, and the universal negative diagonal witness. Additional exact samples check the sign of all relevant low-dimensional Hamming shells.

No finite sample test proves a continuum of step sizes or an infinite family of graph dimensions. Those claims rely on the analytic proof in `RESULT.md`. In particular, the numerical decimal values of algebraic roots are not used as certificates. The exact polynomial root definitions and the Descartes/rational-sign arguments supply those certificates. An independent mathematical audit has not been performed.
