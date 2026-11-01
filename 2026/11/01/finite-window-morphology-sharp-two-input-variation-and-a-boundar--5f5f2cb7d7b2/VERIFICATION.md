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

The accompanying `verify.py` is runnable with Python 3 and has no third-party dependencies.

Executed checks: 35 window/radius profiles; 362,878 exhaustive generic selector tests; 2,412 exact local sharpness-witness checks; 140 positive weight profiles; and 4,200 exact-rational direct two-input inequalities. All passed.

The argument for all sizes is analytic: monotone selector indices, a disjoint path-edge partition in each linearization, exact construction of every active index crossing, integration along input line segments, and the graph connectivity of admissible weight comparisons. Enumeration up to eight vertices is neither an exhaustive search of all path lengths nor a substitute for these arguments.

Only self-review has been performed. The claimed novelty is subject to independent literature assessment, especially the older LULU monograph and the original 2002 publication, which were not read in full here.
