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

# Reproduction of finite arithmetic

All three programs must be run in a directory containing their source files. `python census_monomials.py` requires only Python 3 standard library and computes the exact 20-dimensional kernel of the evaluation map on 15 rational projective points; it enumerates every binary linear combination and records the Gauss-image-size histogram. Independently, `g++ -std=c++17 -O2 -o census_generators census_generators.cpp && ./census_generators` uses 24 ideal generators, finds rank 20, and independently enumerates all resulting gradients. The outputs are stored in `census_monomials.stdout` and `census_generators.stdout`.

`python geometry_checks.py` requires SymPy. It verifies geometric smoothness by exact finite-field Gröbner bases for the projective Jacobian ideal on four charts, tests the specific displayed extremal quartic and all fifteen plane-section restrictions, and exhausts all 256 binary plane-filling quartics to prove that rational nonsingularity implies geometric smoothness for that 8-dimensional family. Reference output is in `geometry_checks.stdout`.

The enumeration is mathematically exhaustive because the 35-column evaluation matrix has rank 15, leaving dimension 20, and the second program's 24 generators have rank 20 in the same kernel. The projective Jacobian tests certify absence of geometric singularities, not merely absence of rational ones. Programs do not prove statements over larger fields or other degrees. Independent external validation has not been performed.
