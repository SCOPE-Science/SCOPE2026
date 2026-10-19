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

The proof in `RESULT.md` is analytic and applies to every real Fourier zero. The accompanying standard-library-only `verify_tetra.py` script checks the arithmetic classification independently by direct per-scale half-period congruences and by two-adic valuations. In each complete integer cube of radius 7, 15 and 31, every point satisfies the predicted incidence type and mask-factor order. Counts of total lattice points / all junctions / three-line junctions / two-line junctions are respectively:

- Radius 7: 3375 / 1500 / 528 / 972.
- Radius 15: 29791 / 13020 / 4560 / 8460.
- Radius 31: 250047 / 108252 / 37200 / 71052.

The checker also tests examples with a zero high coordinate and a repeated low coordinate, the two-scale example \((1,3,2)\), and the finite geometric sums tending to \(3/7\) and \(1/7\). The checker executed successfully with Python 3 and no dependencies. These are finite checks, not exhaustive certificates of the infinite theorem. The passage to the infinite claim relies on the analytic mask-product proof and Haar valuation computation. Independent validation is not performed.
