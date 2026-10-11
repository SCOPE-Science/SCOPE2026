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
# Verification of the finite distance spectrum

The supplied `verify.py` and `spectrum.csv` must be placed in the same directory. Run:

```sh
python3 verify.py
```

The verifier uses only standard-library `itertools`, `fractions`, `collections`, `pathlib`, and `csv`. It exhausts all 27 choices of marked vertex and unordered triples drawn from the 27 lattice sites; rejects repeated or affinely dependent selections; and checks every surviving distance with **two exact rational methods** (plane projection plus edges; and independent constrained minimum over the triangle's vertices, edges, and feasible interior critical point). There is no numerical approximation or test cutoff.

An actual execution with these exact artifact files returned:

```text
VERIFY_OK: tetrahedra=14632 marked=58528 interior_projection=19744
VERIFY_OK: 88 distinct squared distances, from 1/29 to 17/2
VERIFY_OK: first three levels 1/29:48, 1/21:96 (two orbits), 1/17:24
VERIFY_OK: full 88-level table and all 58528 two-method exact comparisons
```

The result also checks all 48 coordinate permutations/reflections when classifying each of the first three levels into symmetry orbits, verifies the explicit orbit representatives and frequencies, and compares all 88 rational table entries with freshly generated values and multiplicities.

This is a finite exhaustive proof of the **specified discrete domain**. It does not certify an asymptotic statement, the novelty of the result, or properties of larger lattice cubes. No independent audit has been performed.
