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

# Reproducibility and limits

The self-contained analytical proof in `RESULT.md` establishes the exact all-odd-dimension distance by radial symmetry and matching primal and Rayleigh dual witnesses, then derives the zeta-corrected asymptotic from midpoint Euler--Maclaurin. Independent validation is not claimed.

Run `python3 checker.py` with Python 3 and NumPy; it produced `PASS 170 diagnostic assertions` on the checked environment. The checker verifies full-vertex commutator norms against Jacobi compression for dimensions 1, 3, 5, and 7, random signed radial increments, unit Rayleigh certificates, and several asymptotic residuals. It is finite numerical evidence, **not** exhaustive verification or a substitute for the proof. No unproved even-dimensional assertions are included.
