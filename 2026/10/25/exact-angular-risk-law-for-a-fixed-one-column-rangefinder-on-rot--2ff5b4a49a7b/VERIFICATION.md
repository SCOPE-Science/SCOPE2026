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

# Verification record

The statement follows analytically from a rank-one orthogonal projection formula, a strict angular monotonicity derivative, circle-arc geometry, projective-angle uniformity, and an elementary trigonometric integral. Finite evaluations do not stand in for proof of an infinite family of power depths or a continuum of parameters.

A self-contained standard-library checker is included as `verify.py`. Run `python3 verify.py` from the extracted package directory. The checker independently multiplies rational \(2\times2\) matrices and compares their exact squared residual norms to the theorem formula at power depths \(q=0,1,2\). It additionally tests the angular optimum on finite grids, midpoint-integrates the half-turn error for multiple spectra and input directions, and compares the predicted worst-error distribution to finite deterministic angular samples. Its observed output was:

`VERIFY_OK: exact matrix identities, sharp-angle checks, half-turn quadrature, atom geometry`

The numerical grids do not certify the minimax over a continuum, the entire probability distribution, or all \(q\); those are proved in `RESULT.md`. No external independent audit has been performed.
