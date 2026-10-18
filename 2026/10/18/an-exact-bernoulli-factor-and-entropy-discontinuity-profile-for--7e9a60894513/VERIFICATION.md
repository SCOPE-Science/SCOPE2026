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

# Reproducibility and verification

The standalone source `verification/check_rctm.py` uses only the Python standard library, notably `fractions.Fraction`, to construct the inverse affine branches for \(\mu=9/4,\ 5/2,\ 3,\ 11/3,\ 17/4,\ 79/10,\ 201/10\). It verifies all branch-length and side-mass identities and compares rational inverse images against the actual modulo/scaling rule at three interior rational target points per branch. It then enumerates inverse branch words through the parameter-dependent finite depths stated by the program, constructs an interior exact orbit for each word, checks its chronological threshold itinerary, and sums exact cylinder probabilities for every binary word.

A completed local replay passed 156 rational single-branch inverse checks and 4,004 exact-rational inverse branch word contributions; the entropy inequalities were checked numerically for the same parameters. Running `python3 verification/check_rctm.py` in the directory containing this file reproduces the checks and prints detailed counts. No external data or third-party package is required.

The theorem for arbitrary real \(\mu>2\) with \(\{\mu/2\}\in(0,1)\), for arbitrary word length, and the stated entropy profiles are proved by the inverse-branch change of variables and derivative calculation in `RESULT.md`; finite enumeration alone cannot establish these statements. The analysis assumes a Lebesgue-random real seed. An audit independent of the present review has not been conducted.
