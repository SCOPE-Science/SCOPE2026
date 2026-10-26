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

# Verification notes

Run `python check.py` from the package directory with Python 3 and NumPy. The checker uses exact rational arithmetic to recompute characteristic coefficients for 42 permutations over seven rational parameter points, and independently compares the six-dimensional symmetrically preconditioned matrix spectrum with the singular-value formula in 36 numerical cases. It prints the strict three-class ordering and a near-boundary ratio.

The exact proof in RESULT.md, rather than sample testing, covers every real parameter in the stated open interval, the strict inequalities, and the limiting ratio. The checker does not perform an independent external audit or certify numerical software.
