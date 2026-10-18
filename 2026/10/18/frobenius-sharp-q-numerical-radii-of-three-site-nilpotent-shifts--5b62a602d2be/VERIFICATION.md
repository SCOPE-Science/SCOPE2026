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

## Reproducibility

Run `python CHECK.py` with Python 3, NumPy and SciPy. The actual extracted script reports **PASS 1645 finite exact/numerical assertions**. Its exact integer checks validate the characteristic polynomial identity (2) for representative values; numerical norm minimizations and top-singular-vector witnesses sample strict allocation ordering, the balanced plateau, rank-one formula and Hilbert endpoint. The checks are finite diagnostics, not a formal proof and not independent audit.

The complete continuum proof is in RESULT.md. Critical points independently verified analytically are: real-overlap support reduction by diagonal phase conjugacy; exact scalar-shift envelope attained through singular vectors; strict convexity for nonzero nilpotent matrices; the cubic determinant; strict derivative of its simple top root in the product invariant; and minimizer existence for every overlap below one. Full-text comparison was possible for the recent motivating preprint and portions of a 2008 exact q-range study; the available 2010 and 2013 papers could be inspected only through official abstracts, leaving stated priority risk.
