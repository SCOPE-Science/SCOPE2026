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

Execute `python3 fermat_quartic_cube_check.py`. Exact computations: degree of \(\gcd(T^{156}-1,(T+1)^{156}-1)\) equals \(41\); its gcd with \((T(T+1))^{208}-1\) equals \(T^5+T^3-T^2-1\) and has degree \(5\); both are separable. Independently, the defining quartic for \(\mathbb F_{625}\) is proved irreducible and the fourth-power map is enumerated, yielding the quotient cubic-character counts \(5,18,18\), lifted counts \(80,288,288\), and total \(668\). An explicit noncube point is checked. The genus-\(19\) conclusion follows algebraically from Riemann--Hurwitz and twelve tame branch points, not from code. The checker verifies exact fixed finite-field arithmetic; no broader field-uniform claim or independent audit is asserted.
