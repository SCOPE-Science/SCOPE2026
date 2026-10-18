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

# Verification of the analytical theorem

The candidate ellipsoid's containment is proved for **all** separations by an exact nonnegative quadratic remainder on each generating circle. Four explicit contact points satisfy a complete isotropic second-moment identity, and an arithmetic–geometric mean bound proves unrestricted volume optimality and uniqueness. Strict convexity determines the contact set.

Run `python3 verify.py` from this package directory. The code uses Python's standard-library exact `Fraction` arithmetic for 1,074 admissible rational parameters and 44,034 exact circle-substitution checks. It also verifies the tetrahedron-frame identities and evaluates 2,200 floating-point substitutions for arbitrary separations. A successful run prints `VERIFY_OK`. Finite evaluations are diagnostic, not a universal proof, a priority certificate, or independent validation.

The case of zero separation has an entire circle contact locus on both generating circles; the four-point statement applies only to strictly positive separation. The geometric extremum is a Löwner enclosing ellipsoid, not a John inscribed ellipsoid. Historical equivalence outside the specifically inspected literature remains possible.
