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

The packaged script `verify_threshold_ld.py` independently constructs the canonical threshold graph from each positive alternating block profile of total order \(2\) through \(10\), tests the definition of locating-domination on every vertex subset, and compares the complete cardinality count with the admissible-omission formula. For profiles with all block sizes at least \(2\), it also compares against the claimed product factorization.

Replay command:

`python verify_threshold_ld.py`

Observed output:

`VERIFY_OK profiles=511 subset_checks=349524 coefficient_checks=2104 max_order=10`

The finite replay checks implementation and boundary cases only. The proof in `RESULT.md` is the evidence for arbitrary order. No external or independent audit has been performed.
