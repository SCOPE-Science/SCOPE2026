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

The proof is symbolic. The necessary condition \(I(n)\ge3\), the exchange inequality, and the complete list of exponent partitions of \(5\) establish the universal part. The finite checker is only a replay of exact rational values and explicit partition certificates.

Run `python3 verify.py`. A successful replay prints:

`VERIFY_OK omega_boundary=5 candidates=5 partitions=5`

The checker verifies that each listed partition is disjoint and covers the full positive-divisor set, that its three sums agree, that each candidate has \(\Omega(n)=5\), and that every rational extremal value used in the proof is exactly as stated. It does not enumerate all integers and is not used as a substitute for the universal argument.
