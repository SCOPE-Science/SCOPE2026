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

## Reproduction
Run `python3 triaconta_checker.py` in a directory containing the supplied standalone program. The program uses only the Python 3 standard library and prints `CERTIFICATE_OK` after all assertions. It constructs 32 explicit vertices of two classical orbits, enumerates all 35,960 unordered four-subsets, evaluates each signed determinant by two independent formulas in \(\mathbb Z[\varphi]\), and compares signs without approximation. It proves there are exactly twenty maximizing four-subsets with determinant magnitude \(6+8\varphi\), all with one dodecahedral and three icosahedral vertices, no shared three-vertex face, and the stated large-equilateral-triangle/apex description.

## Analytical steps not delegated to the enumeration
The signed determinant is separately affine in all four corners. Expanding corners as convex combinations of polytope vertices proves a global maximum is vertex-attained. More strongly, a nonvertex maximum would force at least two distinct maximizing vertex quadruples sharing three corners, excluded by the finite certificate. The elementary face-area/inradius decomposition gives containing polytope volume \(20\). All tetrahedra counted as maximizers are distinct unordered subsets, not symmetry-orbit representatives.

## Limits
No computation over arbitrary perturbations or over other polytopes is claimed. The geometric proof and exact exhaustive certificate together establish the complete stated theorem for this fixed body. An independent audit has not been performed.
