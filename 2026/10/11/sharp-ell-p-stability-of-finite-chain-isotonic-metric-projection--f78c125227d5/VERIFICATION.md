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

The proof uses three independently checkable mechanisms: (i) finite block optimality from the KKT stationarity equation; (ii) the scalar \(p\)-mean gradient and the bound \(w_i\le W/2\) for \(p>2\); and (iii) fully pooled strictly complementary samples realizing the exact Lipschitz ratios. For \(1<p<2\), the residual at the perturbed coordinate is zero and the implicit balance gives \(t_h/h\to1\). For \(p>2\), the local full-pooling Jacobian is \(v\mapsto (v_1+v_n)\mathbf1_n/2\). All observations are real and unweighted.

`verify_isotonic.py` is a standalone Python 3 program using only the standard library. Running `python verify_isotonic.py` performs bisection-based scalar means, generalized pool-adjacent-violators projection, random-pair upper-bound checks, and sharp lower perturbation checks for selected dimensions and exponents. It prints `ISOTONIC_LP_SHARP_NORM_FINITE_CHECK_OK 615` when every check passes. This is numerical corroboration, not an exhaustive or infinite proof. There is no external mathematical audit or independent certification.
