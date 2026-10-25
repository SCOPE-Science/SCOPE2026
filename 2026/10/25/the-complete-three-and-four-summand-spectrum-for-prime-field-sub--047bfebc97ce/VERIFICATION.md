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

# Reproducibility and verification

The attached `verify_order13.py` runs under Python 3.8 or later without third-party modules. Its complete integer calculation generates all \(455\) exponent multisets of size three and \(1820\) of size four, partitions them into \(5\) and \(16\) disjoint affine orbits, and verifies full coverage and orbit sizes. For each representative it computes the exact \(12\times12\) multiplication-matrix determinant in the cyclotomic integer ring using Bareiss elimination, followed by exact trial division. The nine exceptional primes are verified by explicit modular witnesses with order-thirteen generators. The original reproducibility run printed `PASS` with all assertions true. An additional independent symbolic-resultant calculation agreed on all \(21\) norm values.

This verifier certifies finite patterns and arithmetic norms, which suffice for the unrestricted all-prime conclusion through the splitting and resultant equivalence proved in `RESULT.md`. It does not give the minimum when that minimum is five or larger, test composite moduli, or establish novelty against every unpublished source. No independent mathematical audit has been performed.
