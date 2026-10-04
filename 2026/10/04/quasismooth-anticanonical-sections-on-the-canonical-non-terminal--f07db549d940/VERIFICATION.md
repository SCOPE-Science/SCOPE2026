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

The proof was checked by direct symbolic reduction of the coordinate-stratum monomial criterion on both canonical non-terminal boundary components.

The standalone script `verify_boundary_anticanonical.py` performs exact integer enumeration for every integer \(r\) from \(2\) through \(150\). It verifies: (i) the canonical non-terminal boundary contains exactly \(3r\) pairs; (ii) the direct singleton monomial tests agree with the explicit divisor classification; and (iii) the accepted count is \(\tau(2r)+\tau(2r-1)+1\).

The computation is a regression test only. The all-dimensional conclusion rests on the divisibility proof in `RESULT.md`.
