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
Run `python3 CHECK.py` using Python 3's standard library. The checker asserts: (i) exactly ten complementary triple pairs; (ii) all 1024 masks are covered disjointly by 13 explicitly calculated permutation orbits; (iii) six measurable orbits total 332 labelled masks; (iv) every positive representative's strict integer weight inequalities for every subset; (v) each of seven negative representatives has a four-triple incidence-balanced contradiction; (vi) all negative orbits admit such a contradiction; (vii) all bounded positive integer weighted constructions with singleton weights at most 4 generate precisely the 332 measurable masks; and (viii) the bound-3 search generates only 152 such masks, while the paper gives a symbolic lower bound of 4 by the mask-3 inequalities.

No probabilistic checks, floating-point optimization, or unreviewed external certificates are used. Full enumeration establishes this six-voter statement only. The exact prior-work comparisons and residual originality limits are included in the scientific audit; independent external validation is not claimed.
