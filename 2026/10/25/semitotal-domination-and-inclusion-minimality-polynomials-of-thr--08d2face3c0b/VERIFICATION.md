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
Run `python verify_semitotal.py` with Python 3 and no nonstandard libraries. The script constructs all three-layer Cartesian graphs from the adjacency rule, computes shortest-path distances by breadth-first search, and independently evaluates semitotal domination and single-vertex deletion minimality on every subset for \(n=3,4,5\). It compares those observations against direct structural enumeration, exact coefficient expansion of the claimed polynomial, and the stated minimality polynomial. It prints `PASS 37376 subsets` upon success.

The package checker is exhaustive only in the stated finite sizes. The infinite assertion is established by the case classification in `RESULT.md`; no claim of external or independent review is made.
