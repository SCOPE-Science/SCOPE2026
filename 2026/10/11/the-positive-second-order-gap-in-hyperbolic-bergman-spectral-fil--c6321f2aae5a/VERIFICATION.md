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

# Verification

The analytic checks are: (i) the monomial eigenvalue equals the beta integral with parameters \(k+d\) and \(\alpha+1\), with multiplicity \(\binom{k+d-1}{d-1}\); (ii) monotone likelihood ratio orders the eigenvalues by degree; (iii) uniformly dominated rescaled beta densities provide all needed logarithmic moments and the digamma expectation; (iv) summation over shells contributes the \(-1/d\) weighted logarithmic shift; (v) the exact hyperbolic filling-radius integral has its own second-order expansion; and (vi) strict Jensen proves a positive difference coefficient. These are infinite proofs with exact domains, rather than inferences from a finite experiment.

`numeric_check.py` is a supplementary reproducible finite-\(N\) check using Gauss–Jacobi quadrature and direct integration. Executed with NumPy and SciPy, it printed:

```
d=2, alpha=0, p=1, N=2016: scaled finite-N gap=0.4657778; predicted limit=0.4618946
d=2, alpha=1.5, p=2, N=2016: scaled finite-N gap=0.1232278; predicted limit=0.0953426
```

These finite and approximate outputs demonstrate consistency only; they do not constitute certified error bounds or proof of asymptotic convergence. The theorem states a pointwise limit for every fixed \(d\ge1\), \(\alpha>-1\), \(p>0\) and neither uniformity in parameters nor independent external verification.
