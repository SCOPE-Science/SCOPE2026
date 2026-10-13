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

Run `python3 verify.py` with a Python 3 standard-library installation. The file implements arithmetic in the fields of two, three, and four elements, enumerates invertible two-by-two matrices modulo nonzero scalar multiples, and evaluates Hamming weights directly from explicit generator-column lists. Its exact ratios use rational arithmetic (`fractions.Fraction`), without floating-point tolerances.

The checker exhausts all realizable ordered projective weight tuples at binary block lengths two through eight and ternary lengths two through five, and tests all ordered pairs of these tuples against exhaustive projective mappings. It checks the sorted formula, universal bound, and both equality branches. It also checks that the quaternary projective group has 60 transformations, every induced five-point permutation is even, and the stated length-ten example has exact distortion \(100/81\). Successful execution prints `VERIFY_OK`.

The general results for unbounded \(n\) follow from the proof's group-action, uncrossing, and ordered-ratio arguments; finite enumeration is not an infinite proof. Independent scientific audit has not been performed.
