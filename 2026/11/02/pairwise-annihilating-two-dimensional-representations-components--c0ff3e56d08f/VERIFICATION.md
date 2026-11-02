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

The two accompanying standalone files are `verify.py` and `verify_output.txt`. Execute `python3 verify.py` with a standard Python 3 installation. The program implements field operations directly for prime fields and a genuine quadratic extension field, constructs the \(2\times2\) multiplication law from entries, forms pairwise mutual-annihilator neighborhoods, and counts ordered tuples by recursively intersecting admissible neighborhoods. It tests the point formula in 27 exact configurations with \(q\in\{2,3,4,5,7\}\) and \(0\le m\le6\) as documented by the output.

For selected lengths, the program independently enumerates all legal tuples and verifies the complete support dichotomy, including that tuples with at least three nonzero entries consist of proportional square-zero matrices. These are finite tests; the geometric component classification and all-field formula are proved mathematically in `RESULT.md` rather than extrapolated from tests. The reduced structure of the raw equation scheme and higher matrix sizes have not been checked or asserted.
