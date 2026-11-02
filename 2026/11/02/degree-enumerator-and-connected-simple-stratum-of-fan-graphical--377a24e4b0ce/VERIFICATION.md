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

# Mathematical verification

The two included standalone Python programs use only the standard library and can be run directly. `direct_orientation_check.py` tests directed cycles through a full topological sorting algorithm rather than the proof's triangle characterization; it independently enumerates every single-edge flip and checks all degree classes and the connectivity of the induced simple graph for path lengths \(2\) to \(9\). `run_transfer_check.py` counts spoke-sign and run-direction choices independently to validate the rational generating function through length \(11\), and verifies its recurrence through length \(69\). Both terminate successfully and print their respective PASS markers. The formal rational-function and connectedness theorems require the combinatorial reasoning in RESULT.md; finite checks alone are not infinite proofs. No third-party or independent scholarly audit was performed.
