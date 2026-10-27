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

# Verification information

The included `check_h5.py` script runs with Python 3, SymPy, and mpmath. It establishes symbolic identities for the three-factor spherical multiplier, real-part sign polynomial, the quadratic discriminant, both key coefficient comparisons, and the high-frequency negative witness. It also compares the closed-form radial multiplier with twelve independent high-precision quadratures covering interior positive cases, the exact \(a=6\) boundary, and both types of negative-frequency witness.

The numerical quadrature omits the interval \([0,10^{-6}]\) to avoid removable-singularity evaluation. Since normalized spherical functions obey \(|\varphi_\lambda(r)|\le1\), the omitted magnitude for the stated test cases is bounded by \(\int_0^{10^{-6}}\sinh^4r\,dr<2.1\times10^{-31}\). The largest absolute difference observed was \(1.99999167\times10^{-31}\), consistent with this tiny omission. This finite testing is supplementary; the proof's universal claim is the analytic all-frequency sign certificate in `RESULT.md`.

Reproduce with `python check_h5.py`. This package contains no external computed data or additional file dependencies beyond the declared libraries.

The new result has been reviewed for mathematical correctness, nonimplication by inspected nearby literature, and mathematical value. That review is not independent certification. Independent audit remains not performed.
