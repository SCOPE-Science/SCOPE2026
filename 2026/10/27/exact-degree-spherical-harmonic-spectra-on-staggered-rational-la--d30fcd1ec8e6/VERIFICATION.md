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

The exact-rational verification script `check.py` and its output `check_output.txt` are embedded in this package. Execute `python check.py` with Python, NumPy, SciPy, and SymPy installed. It verifies 130 finite matrix-spectrum comparisons and 2,520 exact rational nonvanishing cases. Its largest reported absolute Gram eigenvalue discrepancy is 1.59872e-14. The infinite-degree theorem is established analytically by the two-adic leading-term proof and discrete-Fourier block decomposition; numerical checks do not certify publication priority, infinite cases, or independent review.
