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

# Verification of the numerical-index profile

The analytic proof in `RESULT.md` is the evidence for the infinite parameter ranges. Its imported premise is the exact numerical-index identity of Chiclana, arXiv:2606.01675v1. The new deductions follow by: (1) an attained strictly convex hyperbolic supremum; (2) stationary perturbation around the unique maximum of \(z/\cosh z\); (3) the exact identity \(\delta=2(u^\alpha+u)/((1+u^\alpha)(1+u))\), which forces \(u\sim\delta/4\); and (4) the envelope derivative and the exponential inverse transformation.

The executable `check.py` needs only standard Python 3 and the `math` module. It validates 137 finite cases of the stationary equation, global strict inequalities, midpoint convexity, small-parameter coefficients, logarithmic endpoint scale, derivative scale, and conjugate-exponent symmetry. In a clean execution, it reports `PASS: 137 finite diagnostics` and the constants \(z_*=1.19967864025773\), \(c_*=0.66274341934918\), \(d_*=0.15897324042918\).

Scope of verification: the finite code tests are not an exhaustive or machine-certified proof; no independently audited result is asserted. The proof assumes the cited exact identity and makes no assertion about general real \(L_p\), higher-dimensional real \(\ell_p\), or complex \(\ell_p\).
