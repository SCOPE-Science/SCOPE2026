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

`verify_cluster_cov.py` is a Python-standard-library script using exact `fractions.Fraction` arithmetic; it implements the closed formulas separately from direct enumeration of retained edge configurations. Direct configuration enumeration uses degree-zero vertices for singleton counts, and retained edges whose two retained degrees equal one for doubletons. It tests all labeled Prüfer trees on up to six vertices, not a selected sample; independently tests star and subdivided-star identities and their sign behavior at rational parameter values.

Observed successful output:

```
ALL_LABELED_TREES_EXACT_PASS cases= 2882
STAR_AND_SUBDIVIDED_STAR_EXACT_PASS k=2..7, exhaustive spider k<=6
SIGN_CHECK_PASS k=3..100, path k=2 transition
VERIFY_OK
```

These tests are finite. The all-real-probability, all-arm-count statements rely on the explicit proof, in particular \(2q(1-q)\le 1/2\) and \((k-1)q^{k-1}(1-q)\le ((k-1)/k)^k<e^{-1}\) for \(k\ge3\). Independent external audit has not been performed.
