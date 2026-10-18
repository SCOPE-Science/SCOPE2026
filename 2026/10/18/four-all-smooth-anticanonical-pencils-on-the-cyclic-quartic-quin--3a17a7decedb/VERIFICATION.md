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

# Reproducibility and scope

The following checks were performed with the exact standalone programs included in this package:

* `python3 verify_enumeration.py` regenerates `enumeration_output.json` using exact finite-field arithmetic, three-chart Gröbner smoothness tests, all cubic sections, all pencils, all rational projective coordinate changes and the representative base-scheme elimination.
* `python3 verify_independent.py` regenerates `independent_output.json` using only Python standard-library arithmetic, independent enumeration over finite-field extensions of degrees one, two and three, exhaustive singularity testing, and direct degree-four and degree-five irreducibility checks.

The independent smoothness method is exhaustive for plane cubics because every reduced geometrically singular cubic has at most three singular geometric points, so a geometric singularity has Frobenius degree at most three. A nonreduced cubic has a repeated rational line and thus a rational singularity.

The reference output records 63 nonzero sections, 18 geometrically smooth members, four all-smooth pencils, one order-four group orbit, and a representative Gröbner elimination polynomial with an irreducible factor of degree five beyond the degree-four blow-up orbit. The four base-scheme conclusions propagate under the verified automorphism action.

The calculations do not independently certify whether an equivalent theorem is present in otherwise inaccessible or unindexed mathematical literature. No independent audit was performed.
