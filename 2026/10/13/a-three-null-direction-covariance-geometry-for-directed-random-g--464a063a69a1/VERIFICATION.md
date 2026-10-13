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

# Finite verification and analytic scope

Run `python3 verify.py` with Python 3 standard libraries. The checker independently enumerates all loopless directed adjacency matrices at orders 2, 3, and 4; for each of `p=1/3` and `p=2/3` it forms the exact rational joint first and second moments of both histograms, validates every covariance entry, and validates the contrast expectation. Its expected terminal output is `VERIFY_OK`. This experiment checks finite cases; the one-arc conditioning argument and binomial orthogonality prove the theorem for every admissible integer order and arc probability.

No independent scientific audit has been performed.
