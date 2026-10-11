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

# Exact verification

The complete Python 3 checker is `checker.py` and has no dependencies. It constructs all 126 four-point supports and computes every one of their 15,876 Fourier minors by a 24-term determinant in the exact ring \(\mathbb Z[\omega]\), where \(\omega^2+\omega+1=0\). It also checks the geometrical collinearity predicate in \(\mathbb F_3\), the two affine types and their sizes, all four singular-incidence counts, and the 45-regularity for every row. The checker returns `CHECK_PASS` on completion. These are complete exact computations over a finite domain; no probabilistic sampling or floating-point cutoff is used.

This is an internal mathematical/reproducibility verification, not an independent mathematical audit or proof that no earlier equivalent publication exists.
