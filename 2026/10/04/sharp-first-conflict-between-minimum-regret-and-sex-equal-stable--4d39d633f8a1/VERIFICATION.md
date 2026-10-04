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
The embedded `verify_minregret_sexequal_boundary.py` is an exact finite replay using only the Python standard library.

It implements stability twice: one checker uses precomputed rank maps and one performs direct preference-list position comparisons. Their complete stable-matching sets must agree for every profile.

The replay verifies:
- all \(16\) strict \(2\times2\) profiles have identical minimum-regret and sex-equal optimum sets;
- all \(46656\) strict \(3\times3\) profiles are exhausted;
- exactly \(38880\) profiles have equal optimum sets;
- exactly \(7488\) have the sex-equal optimum set strictly contained in the minimum-regret optimum set;
- exactly \(144\) have the minimum-regret optimum set strictly contained in the sex-equal optimum set;
- exactly \(144\) have disjoint optimum sets;
- no profile has nonempty nonnested overlap;
- the stable-count marginal is \(34080,11484,1092\);
- every disjoint profile has exactly two stable matchings with objective pairs \((2,3)\) and \((3,2)\);
- the disjoint profiles form exactly two size-\(72\) orbits under independent side relabelings and side exchange;
- the displayed witness has exactly the two stated stable matchings.

Run:

`python3 verify_minregret_sexequal_boundary.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated finite boundary and does not infer a larger-market classification.
