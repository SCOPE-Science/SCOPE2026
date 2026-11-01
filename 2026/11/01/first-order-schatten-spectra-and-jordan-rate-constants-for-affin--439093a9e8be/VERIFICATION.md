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

Run `python3 VERIFY.py` with Python 3 standard library. The program was executed on the complete standalone file and printed:

```
epsilon 0.1 finite Taylor remainder Frobenius 0.00768085270645
epsilon 0.05 finite Taylor remainder Frobenius 0.00193673108498
epsilon 0.025 finite Taylor remainder Frobenius 0.000486542727989
PASS: derivative Gram identity, quadratic Taylor scaling, Jordan powers
```

The derivative-functional Gram matrix is independently calculated from Fock monomial derivatives (truncated to total degree nine); its entries agree with the analytic kernel formula within the stated tolerance. The finite matrix of the composition operator is constructed by polynomial substitution to degree eight, and its difference from the linearization has second-order scaling. Fifty exact/Jordan floating-point comparisons are made against the triangular matrix-power identity. These finite computations are auxiliary checks, not a proof of uniform estimates or exhaustive mathematical validation.

The analytic trace-norm bound follows by a uniform Gaussian Hilbert–Schmidt estimate and trace-class summation of finite-rank Taylor coefficients. Exact singular values follow from full Gram identities, and the nonnormal rate from finite-dimensional Jordan calculus. The selected source paper supports the first-public date and the motivating qualitative theorem; the complete article of Choe–Izuchi–Koo was not obtained, so its exact priority implication remains a disclosed literature risk. No independent audit was performed.
