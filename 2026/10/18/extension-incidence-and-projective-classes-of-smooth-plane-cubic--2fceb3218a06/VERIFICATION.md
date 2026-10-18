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

# Reproducing the finite proof

The standalone `verify_pencils.py` program uses Python 3 and only its standard library. Run `python3 verify_pencils.py > new_census.json`, then compare the parsed JSON with `census.json`. It independently constructs the 15-by-18 Macaulay matrix over \(\mathbf F_2\), applies exact binary row elimination to all 1023 nonzero cubics, constructs all 5544 pencils, enumerates their extensions, evaluates the seven rational base points, and calculates all 168 projective transformations, 37 orbits, and a Burnside fixed-point table. The code asserts core totals and the incidence relation \(\sum e(P)=7\cdot864\).

The alternate `check_groebner.py` requires Python 3 and `sympy>=1.12`. Run `python3 check_groebner.py > new_independent.json`, then compare with `independent.json`. This implementation tests the homogeneous Jacobian ideal by exact Gröbner bases on the three dehomogenized affine charts and independently deduplicates pencils and calculates the extension and rational base-point distributions. Its smooth-mask population is not imported from the primary verifier.

The two programs were run during this investigation. All 1023 individual cubic smoothness verdicts matched, with 336 smooth masks; the 12 joint strata, pencil total 5544 and net incidence total 864 agree exactly. The 37 orbit representatives and stabilizer orders are in `orbit_representatives.csv`. The primary verifier performs two distinct group checks: explicit orbit partition and Burnside fixed-point enumeration.

The algebraic proof of the Macaulay criterion relies on the three quadratic partials being a homogeneous regular sequence exactly when they lack a common projective zero. The finite calculations are exhaustive over binary coefficient vectors. No computation claims to enumerate smoothness by testing only bounded-degree extension-field points, and no geometric base-scheme splitting or uniqueness of historical publication is certified.
