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

The analytic proof is the primary verification for arbitrary \(n\). It uses only the standard definition of a legal closed-neighborhood sequence and the prior scalar identity \(\gamma_{\mathrm{gr}}(C_n)=n-2\).

The included `verify.py` independently enumerates every legal dominating sequence for \(3\le n\le10\), retains the maximum-length ones, and checks: the maximum length; the formula \(3n2^{n-4}\) for \(n\ge4\); the classification of omitted pairs by cyclic distance \(1\) or \(2\); the six-set boundary at \(n=4\); and, for \(n\ge5\), multiplicities \(2^{n-3}\) for an adjacent omitted pair and \(2^{n-4}\) for a distance-two omitted pair.

This finite exhaustive check does not prove the infinite family; it stress-tests the proof and boundary cases. No external or independent audit has been performed.
