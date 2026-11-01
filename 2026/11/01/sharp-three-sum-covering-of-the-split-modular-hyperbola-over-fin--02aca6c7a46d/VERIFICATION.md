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

Run `python3 artifacts/verify_hyperbola.py` from the package root. The verifier constructs the specified quotient-polynomial field representations independently, enumerates graph points and complete twofold and threefold sumsets, and checks the theorem over each tested field of order at least thirteen. It also checks that \((1,6)\) is absent in the eleven-element field. Exact integer operations and field-table lookup are used; no probabilistic tests or external dependencies are required.

The script was executed successfully before package assembly. It covers all prime fields with primes \(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73\), and extensions of orders \(4,8,16,32,9,27,25,49\). These tests are a finite check, not a proof for arbitrary prime powers.

The proof of the infinite classification checks projective boundary points, all affine singular possibilities, the two exceptional product parameters, and each case where the target has a zero coordinate. Its only non-elementary ingredient is the classical Hasse bound for smooth plane cubics. Historical novelty is assessed from the inspected sources, not certified independently.
