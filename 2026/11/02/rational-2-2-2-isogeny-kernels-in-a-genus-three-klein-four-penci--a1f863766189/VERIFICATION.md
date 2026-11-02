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

# Verification of the genus-three maximal isotropic kernel theorem

The standalone `verify_isotropic.py` reconstructs the abstract six-dimensional symplectic space as even subsets of eight symbols modulo complementation, with the intersection-parity pairing. It enumerates all \(135\) three-dimensional Lagrangians by triples, all \(105\) matching Lagrangians independently, and the Frobenius-fixed subspaces for permutations of cycle type \(1^8\), \(1^4 2^2\), and \(2^4\). It checks the exact kernel totals \(135,15,39\), matching counts \(105,9,25\), and complementary affine counts \(30,6,14\); the \(42/49\) affine involution calculation is also checked numerically.

Finite-field routines implement multiplication and modular polynomial exponentiation over fourteen explicitly constructed fields. For every admissible parameter they confirm that \(X^4+tX^2+1\) has either zero or four rational roots and divides \(X^{q^2}-X\). Exhaustive enumeration covers \(5{,}934\) admissible ordered coefficient pairs. The exact output terminates with `GENUS3_LAGRANGIAN_FROBENIUS_ALL_CHECKS_PASS`.

Run `python3 verify_isotropic.py` from the package directory. No dependencies beyond Python 3.8+ are needed. The proof for all odd prime powers is in `RESULT.md`; finite-field checks do not certify infinitely many fields. Independent verification has not been performed.
