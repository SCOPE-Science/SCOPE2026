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

Run `python verify.py`, which uses only Python's standard library. The checker enumerates every parent sequence in recursive trees of sizes \(3\le n\le8\), independently reconstructs every root-to-vertex depth and all root-attachment indicators, and checks the claimed exact mixed moment for **every nonempty subset** of nondeterministic insertion times with exact rational arithmetic. It also checks the first-order formula and strict decrease through \(n=100\).

The infinite result is justified by the explicit conditional-mean recursion, iterated mixed discrete differences, and independent-Bernoulli centering, not by finite enumeration. The proof does not need numerical approximations or external certification. No independent audit has been performed.
