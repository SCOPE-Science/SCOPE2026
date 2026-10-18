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
Run `python3 verify.py`. The dependency-free checker reconstructs each target count by a complete convolution of cube residues for the primes \(5,7,11,13,17,19,31,37\), with each tested modulus at most \(2500\). For the 22 complete distributions it confirms the count of all ordered pairs, checks every target against the explicit nonsingular and singular lifting formula, and verifies the exact second moment as a rational equality. The prime-character second-moment identity is also checked directly from the finite-field table.

These computations are finite regression checks, not a proof of the universal statements. The proof of universality consists of cubic-character orthogonality, Hensel lifting, exact recursion, and geometric valuation-shell summation in `RESULT.md`. Residual priority risk from potential general local-zeta results remains; independent audit is not performed.
