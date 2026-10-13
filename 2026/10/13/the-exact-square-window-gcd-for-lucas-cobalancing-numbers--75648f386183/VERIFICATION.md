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

# Verification and boundaries

The unrestricted mathematical proof is in `RESULT.md`. Its essential steps are the exact Pell-window sum identity, the Pell strong-divisibility reduction of an infinite GCD to two integers, and the separate valuations at 2, 3, and all remaining odd primes.

The standalone `verify.py` was executed using exact arbitrary-precision integer arithmetic. It tested window lengths 1 through 320, 25 windows for each length, 8,000 exact moving-window identities, 12,100 Pell strong-divisibility pairs, and 160 even-index two-adic units. The recorded result is in `verification_output.txt`. The computations are finite support only, not an infinite proof or an independent audit.

The formula is conditional on the stated recurrence definitions; it neither classifies \(\gcd(B_k,k)\) further nor establishes the corresponding squared cobalancing formula. Possible unindexed stronger publications remain a bibliographic risk.
