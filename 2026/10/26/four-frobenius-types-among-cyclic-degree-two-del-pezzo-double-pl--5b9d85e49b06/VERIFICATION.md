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

Run `python3 del_pezzo_cyclic_verifier.py` with Python 3 and no third-party packages. The script checks that the five named quartics are precisely the five cubic-orbit sums, verifies the weighted-coordinate shift formula as a polynomial identity, and calculates the singularity-condition gcd over `F2[t]` for all 32 coefficient choices. Because absence of nonzero roots of a polynomial over the algebraic closure is equivalent to its gcd being a nonzero monomial, the gcd checks are algebraic-geometric, not finite-point sampling. Endpoint checks are included.

For each degree from one to eight the script constructs an explicit finite field, checks inverses for all nonzero elements, counts rational points by the Artin–Schreier trace test and additionally solves the quadratic in `w` directly in degrees one to three. It reconstructs the Picard Frobenius characteristic polynomial by Newton identities and asserts the four factorizations. All eight point counts are finite exhaustive computations; the inference of zeta functions at every degree uses the known eight-dimensional Picard realization of smooth degree-two del Pezzo cohomology.

Verified terminal result: `VERIFY_OK: 32 cyclic models, 12 smooth, 4 zeta types; fields degrees 1..8 and low-degree direct lifts`.

The full geometric Picard classification and trace formula are standard mathematical inputs, not certified by the script. Independent audit has not been performed.
