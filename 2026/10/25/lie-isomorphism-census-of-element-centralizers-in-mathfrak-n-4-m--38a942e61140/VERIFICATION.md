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

The standalone `verify.py` computes the Lie bracket by exact four-by-four matrix-unit multiplication, constructs for each \(X\) a basis of \(\ker\operatorname{ad}_X\), and uses Gaussian elimination to measure \(\dim C_L(X)\), \(\dim[C_L(X),C_L(X)]\), and \(\dim[C_L(X),[C_L(X),C_L(X)]]\).

Every element of the Lie algebra over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\) (implemented as \(\mathbb F_2[t]/(t^2+t+1)\)), and \(\mathbb F_5\) was tested. Counts by type:

- \(q=2\): abelian3 24, abelian4 8, h3+line 24, full 2, two-step5 6, filiform4+line 0.
- \(q=3\): abelian3 432, abelian4 54, h3+line 216, full 3, two-step5 12, filiform4+line 12.
- \(q=4\): abelian3 2880, abelian4 192, h3+line 960, full 4, two-step5 60, filiform4+line 0.
- \(q=5\): abelian3 12000, abelian4 500, h3+line 3000, full 5, two-step5 40, filiform4+line 80.

The code returned `CENTRALIZER_TYPES_OK`. This finite exhaustive evidence checks implementation and examples; it does not replace the all-field proof. Independent audit and independent validation have not been performed.
