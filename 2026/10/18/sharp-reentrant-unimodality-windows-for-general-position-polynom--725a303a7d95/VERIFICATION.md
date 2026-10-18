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

Run `python verify.py` with a Python 3 installation supporting `int.bit_count()`. The verifier constructs graph edges independently from coordinate comparisons, computes shortest distances without third-party packages, and enumerates all subsets for nine small graph instances. It compares full coefficient arrays with the claimed combinatorial formula and tests the two sharp thresholds on an additional 2000 parameter combinations. The exact output appears in `verification_output.txt`.

The all-integer theorem is certified by the proof's polynomial sign estimates, not by these finite checks. No independent mathematical audit has been performed. The scope is exclusively these coordinate-deleted multipartite graphs.
