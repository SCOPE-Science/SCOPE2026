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

# Verification of the rectangular phase theorem

Run `python3 rectangle_verify.py` with `mpmath` installed. The script evaluates the exact derivative, locates the unique positive zero by bisection on logarithmic thickness, and checks sign changes and nearby values. It also checks three direct derivatives, the exact square exponent, the zero-exponent scaling constant, and the large-negative-exponent law. The saved source passed **50 deterministic assertions** using 65-digit working precision.

The proof is analytic and explicitly quantifies every \(a>0\), \(b>0\) and every real exponent. Finite diagnostic tests support these identities but do not certify the universal theorem or exclude prior literature. The fixed-half-width geometric constraint cannot be omitted. Independent audit remains unperformed.
