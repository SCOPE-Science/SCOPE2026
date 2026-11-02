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

The proof uses exact block cancellation and finite digit-class counts, not numerical extrapolation. In each block of even length \(m\), alternating updates leave \(x_{mk}=c\) exactly, and odd least-significant digits apply the scalar map \(Q_c(u)=G(u)-c\). Digit class densities establish total-variation convergence for arbitrary real-valued iterates.

Running `python3 verify_digit_flip.py` with Python's standard library verifies the finite nonlinear and linear identities, exact rational orbit values, and finite moment formulas. Observed output includes `ALL_EXACT_FINITE_CHECKS_PASS`. This finite test does not prove total-variation convergence, asymptotic moment growth, or mathematical priority; those depend on the analytical argument and literature comparisons in the accompanying result and review.

The critical moment asymptotic is for block lengths \(N=m^K\); full-time divergence and subcritical convergence are also proved, without claiming the same leading constant at arbitrary \(N\).
