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

The proof reconstructs the inverse intensity Fourier transform and its unique Sidon pair contribution, converts the two-mask ratio to an exactly invertible exponent in the prime field, and uses a rank-one triple-product identity for all coefficient moduli. The single-mask translation obstruction and the universal one-/two-atom phase-only obstructions are proved algebraically. No numerical cutoff substitutes for the all-prime argument.

Run `python3 CHECK.py` in this directory (no external packages). The checker uses exact Gaussian integer arithmetic and formal roots of unity; it exhaustively enumerates Sidon support placements of two through five atoms where possible for prime dimensions 3, 5, 7, 11, 13, 17 and 19, and verifies the decoding and swap identities with nonzero deterministic pseudorandom coefficients. It also checks alternate mask parameters for smaller primes. Expected output begins `CHECK_OK configurations=4983`. The checker does not test all complex coefficient choices and is not an independent mathematical audit.

Limits: competitors are required to have directed Sidon support; no general-noise stability or composite-order result is proved. Independent audit: not performed.
