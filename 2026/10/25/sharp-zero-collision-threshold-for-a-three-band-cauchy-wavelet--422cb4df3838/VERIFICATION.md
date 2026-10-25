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

# Reproducibility and verification

The standalone `three_band_cauchy_verification.py` was executed successfully with SymPy and mpmath. It checks the general coefficient and discriminant identities symbolically, the two-interval discriminant, the exact coalescence at \(r=2/5,s=1/15\), and the squared local splitting coefficient \(91/100\). It also compares the endpoint formula against direct high-precision integration for examples in both simple-zero regimes. The exact output includes the threshold \(s_*=0.06666666666666666666666667\) at \(r=0.4\).

The proof of the complete parameter partition is analytic and does not rely on enumeration. Symbolic algebra checks are independent expressions of stated identities but are not an external proof assistant. Literature comparisons are bounded; independent audit and independent validation have not been performed.
