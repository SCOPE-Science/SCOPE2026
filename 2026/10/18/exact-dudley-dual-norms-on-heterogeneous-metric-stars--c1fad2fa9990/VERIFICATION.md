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

The general theorem is established by a center-and-leaf feasibility reduction, a finite-knot endpoint lemma, and exact monotone piecewise-affine optimization. No finite case enumeration is invoked as a universal proof.

The standalone exact-rational test program `CHECK.py`, run with Python 3, produced `PASS 4800 exact rational fast-root versus grid comparisons, with ties and signed masses` and `PASS 1200 exact rational attaining-potential and norm-bound checks`. Independent primal linear programming in `LP_CROSSCHECK.py` (Python 3 with SciPy) produced `PASSED 2100 exact/general and zero-total LP comparisons; 1050 exact closed formula equivalences`. Both commands completed without assertion failures.

These checks exercise radii with ties, positive/negative/zero leaf weights, arbitrary hub masses, and vanishing or nonvanishing total mass. The LP oracle is numerical, with tolerance below \(10^{-7}\); the core grid/root comparisons are exact rational identities. The explicit analytic argument covers all finite input sizes and positive real lengths, which no sample can independently certify.

Independent audit remains not performed.
