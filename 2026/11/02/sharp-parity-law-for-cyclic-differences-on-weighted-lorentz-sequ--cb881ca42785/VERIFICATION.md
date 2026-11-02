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

# Verification and reproducibility

The exact-arithmetic script `checker.py` enumerates all nonzero ternary signed vectors for 39 rational nonincreasing weight instances in dimensions 2 through 9. It compares computed maxima with the analytical candidate on every case. The checked stdout is included as `check_output.txt`; its final status is `PASS 39 full ternary extremal checks; no float arithmetic`.

The all-parameter statement does **not** follow from this finite exercise. It follows from the signed-layer decomposition, exact classification of support boundaries on a cycle, discrete concavity of the cumulative weights, and parity of full alternating signs. The power-weight corollary uses a separate concavity and arithmetic–geometric comparison; neither computational sampling nor symbolic numerical fitting is invoked in its proof.

An independent audit has not been performed. The bibliographic novelty assessment is not a claim that all historical sources have been read.
