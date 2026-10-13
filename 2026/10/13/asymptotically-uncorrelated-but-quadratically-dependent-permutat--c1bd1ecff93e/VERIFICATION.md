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
# Reproduction and limits

Execute `python3 verify.py` with Python 3 standard library. It enumerates all \(6+120+5040+362880=368046\) permutations of odd sizes three through nine, verifies exact finite covariance and variance identities, checks each finite mixed squared covariance against exact rational values, and verifies two polynomial contraction integrals with rational integration. Success prints `VERIFY_OK`.

The analytic proof establishes the all-size exact second moment and the infinite asymptotic mixed fourth moment. Finite enumeration does not certify an infinite limit. The non-Gaussian marginal fourth moment is taken from Even-Zohar, arXiv:1511.09469; the new joint contraction is independently derived. Independent audit has not been performed.
