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

The theorem is justified by the elementary bidirectional force/non-force proof in `RESULT.md`. The standalone script `verify.py` provides independent finite tests, and `verify_output.txt` contains its exact captured standard output.

Run `python3 verify.py` from the extracted file directory using Python 3 with no third-party packages. The script tests all initial blue sets for \(2\le n\le6\), then uses a fixed pseudorandom seed per order for \(7\le n\le11\). It checks every small-order coefficient against the labeled-forest recurrence and tests selected large-order Cayley and boundary values through \(n=16\). It reports 54,346 separate direct forcing comparisons. These comparisons do not prove the theorem for all orders; the general proof is mathematical rather than computational. The recorded review is a self-review; no independent audit has been performed.
