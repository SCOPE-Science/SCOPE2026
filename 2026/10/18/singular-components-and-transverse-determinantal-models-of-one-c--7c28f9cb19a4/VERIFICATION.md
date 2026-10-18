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

# Mathematical verification

## Reproducible finite checks
Run `python3 CHECKER.py` with Python 3 and SymPy installed. The checker enumerates all faces as intersections of the facet-vertex incidence sets of the explicitly defined matroid base polytope. For each face it calculates affine rank and active normal rays in the integral cocharacter lattice, uses Smith normal form to distinguish unimodular simplicial cones from singular cones, and verifies that every nonsmooth face lies in precisely the predicted union of singular-component faces. It tests \((n,r)=(6,3),(7,3),(7,4),(8,3),(8,4)\) and prints `VERIFY_OK` upon success. Counts of all nonempty faces for these examples are respectively \(285,921,921,2597,3323\), with predicted irreducible component counts \(16,29,29,48,61\).

## Infinite proof and limitations
The general assertion follows from the exact facet-normal classification and saturated dual-semigroup presentations in `RESULT.md`, not finite extrapolation. The local models use standard lattice-semigroup generators and \(2\times2\) determinantal relations. The checker does not verify the infinite semigroup argument, nongeneric intersection germs, or any new claims in other documents. The result is self-reviewed and has not received independent audit or independent validation.
