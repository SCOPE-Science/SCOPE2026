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

Run `python3 verify.py` in the directory containing this file and `verify.py`. The standalone standard-library script constructs all cyclic host words for \(k\in\{3,\ldots,200\}\), confirms exact stated host lengths and that all required length-\(k\) weight-two factors occur, checks the neighboring-gap inequality, and independently enumerates all cyclic binary hosts of shorter lengths for \(k=3,4,5\). On success it prints `VERIFY_OK`.

The full infinite lower bound follows from the label-variation argument in `RESULT.md`, and the full infinite upper bound from the explicit gap proof. The script does not formally certify those arguments or the unknown exact optima for large lengths. Independent audit not performed.
