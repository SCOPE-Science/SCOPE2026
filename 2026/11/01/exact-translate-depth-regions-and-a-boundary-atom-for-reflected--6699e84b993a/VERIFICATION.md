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

The accompanying reproducible file `verify.py` was executed with Python 3 using only its standard library and returned:

`PASS: 13352 deterministic exact/numerical consistency checks`

Checks include 151 exact Fraction identities for the symmetric overlap branches; direct convex-polygon clipping compared with area inclusion–exclusion for 4,500 randomized translations; 6,500 randomized global upper-bound comparisons for translates missing their test points; 1,200 explicit nearly optimal excluded translations evaluated by clipping; and 998 sampled level-set/area equations. The program also checks several critical endpoints exactly. These are finite consistency tests: they do not establish exhaustive global optimization, which instead relies on Brunn–Minkowski concavity and the exact cap formula in the proof. The strict-exclusion supremum is verified analytically by a limiting argument. Historical priority is not independently certified. No independent mathematical audit was performed.
