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

The argument in `RESULT.md` is a finite-dimensional proof valid for every coprime pair of positive integers. Its core independent deductions are the Jordan-decomposition spectral support restriction, a determinant-cycle-cover length lower bound, uniqueness of allowed successor edges, and the exact cyclic word orbit count. The matrix powers are checked algebraically.

Run `python3 verify_resonance.py` using Python 3 with no third-party modules. The expected output is `CYCLIC_RESONANCE_EXACT_FINITE_OK 19 coprime pairs`. The checker exhausts all coprime parameter pairs with \(1\le p,q\le5\), uses exact integer matrix arithmetic, and tests the two non-equivalent shapes at \((p,q)=(2,3)\). This finite exercise is a diagnostic and does not certify the infinite quantifiers. Full-text comparison with the motivating preprint and independent validation remain outstanding.
