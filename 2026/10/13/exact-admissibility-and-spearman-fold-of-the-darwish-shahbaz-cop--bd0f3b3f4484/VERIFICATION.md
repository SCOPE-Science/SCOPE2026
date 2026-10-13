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

# Mathematical verification and reproducibility

The rational copula formula, its mixed density, and the covariance-kernel difference were checked by symbolic differentiation using the exact expressions in `check.py`. The exact proof of the copula-valid parameter interval, including all endpoints and exclusion of inadmissible positive parameters, is given in `RESULT.md`; sampled positive densities do not stand in for a global positivity proof.

Numerical reproduction uses Gaussian tensor quadrature with degrees \(64\), \(96\), and \(144\), computing the unique positive solution of \(t^2B(t)=A(t)\). The reported approximations are stable to the shown digits. Finite quadrature cannot prove uniqueness or rigorous error bounds: uniqueness and the global Spearman extremum follow from the derivative and monotonicity arguments in the proof.

Run from the folder containing `check.py`:

```sh
python check.py
```

Required Python packages: NumPy, SciPy, SymPy. Neither external files nor network services are used by the checker. The code is a reproducibility aid, not an independent scientific audit or a formal certificate. The mathematical conclusion is limited to the specified bivariate rational copula.
