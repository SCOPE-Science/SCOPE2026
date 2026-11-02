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

# Verification of the all-Courant Fourier certificate

Run \(\texttt{python3 verify.py}\) with Python 3; no third-party libraries are required. The script constructs the complete polynomial \(H(c,T)\) from exact rational Fourier-symbol data, tests the factor \(cT^2\), checks all \(168\) rational tensor-product Bernstein coefficients on the two rectangles, and checks the exact rational positive excess for calibration \(69/100\). It independently evaluates the five-stage recurrence versus its factored stability formula on \(1000\) seeded sample parameters and compares the two forms of the spatial symbol. The algebraic rational checks establish the stated continuous-domain positivity; random tests serve only as supplementary transcription checks, not proof of infinite claims.

Expected exact output facts: the lower slab has \(84\) coefficients with three zeros and least positive coefficient \(16/195\); the upper slab has \(84\) strictly positive coefficients, the least equal to \(2706544/551353635\). The calibration-failure excess is \(14399294983760/708051067974441\). None of these facts assumes an externally audited computation.

The result applies only to periodic, uniform, constant-coefficient, unlimited scalar transport in exact arithmetic. No nonlinear, boundary, nonuniform-grid, variable-implicitness, positivity, or external certification claim is made.
