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

The exact transition formula and proof are in `RESULT.md`. Run `python3 verify.py` (standard library only). The checker uses rational interval arithmetic around exponential Taylor polynomials, verifies the exact model-parameter radical enclosures, proves \(1.38<m_-<1.40\), \(-0.50<m_+<-0.47\), \(0.39<m_a<0.40\), \(\rho_1<1<\rho_2\), and \(|m_-m_+|<1\). These strict bounds suffice for the entire analytic theorem: all \(p\)-moment products, the unique \(p_*\in(1,2)\), the logarithmic almost-sure rate, and the finite-a.s./infinite-mean quadratic cost split. RK4 integration independently tests the sampled control on the true plant; finite-step integration does not prove infinite-horizon assertions. The illustrative decimal \(p_*\) is computed by bisection. No independent audit has been performed.
