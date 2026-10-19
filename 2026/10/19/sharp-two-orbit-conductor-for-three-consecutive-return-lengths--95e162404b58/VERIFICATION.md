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

# Reproducibility and limits

Run `python3 verify.py` using Python standard library only. It calculates the renewal zeta coefficients and reconstructs exact primitive-orbit counts by Möbius inversion for \(2\le a\le46\) and all \(1\le n\le M(a)+4(a+2)\), checks the optimal endpoint, tests every subsequent integer period in the finite range, and independently enumerates primitive gap necklaces for \(a\le9\). The replay produced `VERIFIED: exact conductor and all larger tested counts; 27550 integer checks; 308 independent necklace comparisons.` The finite range is not an exhaustive proof for arbitrary \(a\) or \(n\); these universal quantifiers are proved in `RESULT.md`. No independent external audit has been performed.
