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

# Reproducibility

Run `python3 verify_square_legs.py` using Python 3.8 or later. There are no third-party package dependencies. It enumerates primitive triangles through the standard Euclid formula and independently through two quartic constructions for six hypotenuse bounds \(100,1000,10000,100000,1000000,10000000\). It verifies exact set equality and pairwise disjointness, and checks primitiveness, the Pythagorean identity and the hypotenuse bounds.

Expected exact odd/even counts: \((1,3),(3,8),(13,27),(42,84),(132,269),(413,839)\), with totals \(4,11,40,126,401,1252\). The program reports `SQUARE_LEG_EXACT_REGRESSION_OK` on success.

The program does not certify an infinite theorem. The analytical proof uses the Euclid bijections, the explicit parity-coprimality density from odd-divisor Möbius inversion, the beta-integral area, the elementary lattice boundary estimate, and Fermat's established fourth-power descent theorem. The novelty comparison is not an exhaustive survey of unindexed publications.
