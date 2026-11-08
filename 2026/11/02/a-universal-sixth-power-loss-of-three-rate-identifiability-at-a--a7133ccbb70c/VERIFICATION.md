---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For κ>β>0, δ=(β+κ)^2/(4κ), h<1/(δ+β+κ), and r=(κ−β)/(2κ), the invariant diagonal recurrence x_next=x−hκx(x−r)^2 is strictly decreasing from x0>r to r. Reciprocal increments give t(x_t−r)→1/(hκr), so consecutive gaps scale t^-2. Symbolic independent exact determinant expansion verifies det Φ=h³x_t x_(t+1) x_(t+2) (x_t−x_(t+1))(x_t−x_(t+2))(x_(t+1)−x_(t+2)); hence t^6 det→2/κ³. Centered-row singular perturbation with nonzero v(r)×v_prime(r) gives σ2~t^-2, σ3~t^-4 and the stated t^4 Euclidean condition number. Four noiseless states identify three unconstrained rates, not fold-aware or noisy predictors.

## originality

PASS

The Liang–Cui–Liu source gives a linear three-rate regression and full-rank criterion but not late-time fold determinant or sharp spectral singular values. Vandermonde factorization is standard, while its coupling to the exact fold dynamics, t^6 constant and t^4 condition asymptotic is a specific new assertion. SIR identifiability and higher-order endemic-fold results do not imply this time-window estimate. Priority remains qualified against specialist numerical-analysis literature.

## value

PASS

The regression rank condition in a natural higher-order epidemic model is not a numerical conditioning guarantee; exact critical-fold stability losses quantify a natural difficulty in planning observation windows, with universal determinant leading constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
