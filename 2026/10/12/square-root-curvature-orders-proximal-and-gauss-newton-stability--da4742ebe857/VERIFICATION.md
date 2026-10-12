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

# Verification of radial model-index ordering

The analytic verification reduces both model problems to a scalar radial interval. For convex square roots, it splits at the tangent's first zero, avoiding invalid squaring of negative tangents. For concave square roots, it separately handles negative unconstrained NGN radial coordinates by comparing the exact proximal envelope with the center candidate. The proof gives explicit algebraic inequalities for that crossing case.

For power profiles, the scalar exact-proximum equation is \(t+\alpha t^{p-1}=r\) for \(p>1\); for \(p=1\) it is a soft-threshold. Taylor expansion and large-parameter limits yield the two stated coefficients. The script `verify.py` was executed from this package's own staging path with Python's standard library and returned `VERIFY_OK 702 cases; exact linear witness`.

The 702 samples cover listed exponents on both sides of \(p=2\), six positive radii and nine positive regularization scales. They are finite checks only; they do not prove the quantified comparisons. Neither an external certification nor an independent audit was performed. The assertion is a static model-index ordering, not a convergence guarantee or a claim of general nonradial model domination.
