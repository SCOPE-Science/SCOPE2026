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

# Verification details

## Reproducible exact checks

The C++17 program `bitangent_census.cpp` evaluates all \(32,767\) nonzero homogeneous quartic equations over \(\mathbf F_2\) in a fixed monomial basis. It constructs the Macaulay map in degree ten from the quartic and its three partial derivatives and checks rank 66 by binary elimination. It tests each of the seven rational lines for the two coefficient conditions defining an even divisor and counts the seven rational point evaluations. Its printed joint table has total 10,920 and the column totals 3,072, 5,278, 2,352, 105, 112, and 1 for rational bitangent totals 0, 1, 2, 3, 4, and 7. Zero occurs for 5 and 6.

The independent `bitangent_orbits.py` computes the action of generators of \(\operatorname{PGL}_3(\mathbf F_2)\) on the quartic coefficient space, producing 279 projective-coordinate orbits, then uses SymPy Gröbner bases to test absence of singular geometric points on each of the three affine charts. It obtains 78 smooth orbits, total orbit weight 10,920, and reconstructs bitangent tests from symbolic binary line substitutions rather than precomputed coefficient masks. It asserts all 25 positive entries of the exact joint table, the zero cells implicitly, the column totals, and the concurrency conditions. The computed report ends `INDEPENDENT_ORBIT_GROEBNER_CHECK_PASS`.

Both programs and their actual printed output are included. They were executed successfully. Neither relies on floating-point statistics, randomized search, incomplete sampling, or a finite-extension approximation to geometric smoothness.

## Proof boundaries

The implication from Macaulay rank to geometric smoothness depends on the standard fact that three general degree-four members of a base-point-free degree-four linear system in three variables form a regular sequence and therefore have quotient socle degree nine. The bitangent test uses the characteristic-two square criterion. Counts are exhaustive finite computations, conditional only on these exact algebraic reductions and correct execution of the shipped source. Unindexed equivalent prior enumerations remain possible. No independently audited or externally certified status is asserted.
