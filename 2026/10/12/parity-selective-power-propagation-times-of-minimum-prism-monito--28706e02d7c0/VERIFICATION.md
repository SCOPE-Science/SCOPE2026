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

# Reproducibility checks

The Python standard-library program `verify.py` was executed from the delivered package directory with Python 3. It independently builds the degree-three prism adjacency lists, initializes the observed set to the union of the two closed neighborhoods, and computes all simultaneous unique-white-neighbor forces. For each \(7\le n\le50\) it checks every unordered vertex pair, the complete eligibility criterion, the exact two-term time distribution, and the claimed time for each eligible geometric pair type. It also checks six direct local full-interval identities per order and the failure of a single seed.

Observed output:

`VERIFY_OK n=7..50 all_unordered_pairs every_latency_and_nonforcing checked_pdpairs=13794 base_intervals=264 singleton_nonforcing=44`

The program verifies 13,794 successful minimum seed pairs and all unsuccessful two-vertex pairs across the stated finite range. The theorem for unrestricted \(n\ge7\) follows instead from the six local calculations, the full-rung propagation induction, and the prior exact pair-eligibility lemma. Neither finite verification nor the self-review constitutes independent review or an infinite machine certificate.
