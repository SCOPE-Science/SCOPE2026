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

# Verification scope

Run `python3 verify.py` from this directory. The checker enumerates all normalized admissible polynomial triples for safe primes through \(179\), independently recognizes primitive roots using group orders and compares the exact character sums and counts. It also verifies the small-prime counterexamples and attainment at \(23\) and \(47\). The mathematical argument uses the standard quadratic-character sum and Hasse's theorem; neither is established merely by finite enumeration. No independent audit has been performed.
