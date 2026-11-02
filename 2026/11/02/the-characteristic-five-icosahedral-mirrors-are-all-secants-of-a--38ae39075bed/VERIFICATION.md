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

# Reproducibility and checked limits

Run `python verify_h3_five.py` with Python 3 and SymPy. The script computes all 31 projective rational points, 15 distinct mirror coefficient vectors, 6 conic points and 15 distinct conic secants, checks the exact equality of the line sets, and counts incident lines at each point. It also symbolically checks both Hilbert–Burch syzygies and the degree-31 numerator calculation. `verify_output.txt` is the execution record from this run.

The finite checks are exhaustive for finite incidence, not an infinite-field proof. The Frobenius-determinantal ideal is reduced on affine charts since derivatives of the equations `u^5-u` and `v^5-v` are units, and its Hilbert–Burch resolution follows from a height-two maximal-minor ideal. Arithmetic counts for all positive extension degrees are derived by inclusion–exclusion among rational lines with only rational intersection points.

Only the *reduced* singular subscheme is identified; the unreduced Jacobian ideal was not computed. Direct historical-priority certification and independent audit have not been performed.
