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

# Reproducible arithmetic verification

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses an exact sparse multivariate integer-polynomial implementation with no third-party packages. A successful execution prints:

`VERIFY_OK: exact integral logarithmic basis, cubic syzygies, and p=7 degree jump`

It independently reconstructs the five factors, forms the three derivatives, verifies the integral identities for the Euler and two cubic logarithmic derivations, verifies the determinant \(-3F\), constructs the cubic and quintic syzygy triples and verifies their cross-product identities. Finite-characteristic substitution is checked as a consistency test for primes \(5,7,11,13,17,19,23,31\); the proof of all-prime validity is the integer identity together with squarefreeness and polynomial divisibility.

The exact linear-algebra ranks reported in the result for graded Milnor pieces were obtained separately, not bundled into the short standalone identity verifier. Their role is a supplementary finite consistency check. The proof of the Hilbert series is the displayed graded free resolution, which is valid over all fields in the stated scope.

No formal proof assistant, external certification or independent mathematical audit has been performed.
