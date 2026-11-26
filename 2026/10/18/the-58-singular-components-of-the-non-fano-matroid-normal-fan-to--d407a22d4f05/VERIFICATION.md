---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the relaxed matroid using binary Fano labels and checked basis exchange. Standard matroid subset inequalities give an exhaustive list of candidates. The fresh exact reproduction (python3 reproduction_4.py) selects dimension-five equality faces and closes the resulting 20 facets under nonempty intersection. Its face vector is (29,138,263,242,108,20,1); it certifies saturation via maximal minors for all 800 nonzero normal cones and counts nonsimplicial cones by face dimension as (29,120,111,18). The inclusion-maximal faces among those 278 are 18 lattice tetrahedra, 24 lattice triangles, 15 lattice parallelograms and the sole vertex 012, with face-edge lattice bases checked. Smoothness and Q-factoriality therefore fail on precisely the same orbits. The maximal cones' sole integral relation has unit coefficients and sign sizes (2,2), (2,3), (2,3), (3,4); saturation identifies their dual monoids with nonnegative integer pairs of equal total, not a finite quotient of those monoids. The saturated cone lattice splits off the dense orbit torus. This gives the Segre germs and multiplicities binomial(a+b-2,a-1)=2,3,3,10. The condition for a rational height-one functional on all rays is exactly a=b; there it is integral and gives Gorensteinness (normal affine toric rings are Cohen–Macaulay). The isolated closed orbit is in no positive-dimensional component. This checks reduced support and generic transverse types, not scheme structures or nongeneric local rings.

## originality

PASS

Pass applies to the complete 58-component singular-support stratification and its integral transverse type census. The fixed-point singularity and non-Q-factoriality conclusion is covered by the distinct indexed sparse-paving theorem, and the face vector is within an existing general enumeration framework; neither is credited as new. The strongest inspected sources do not imply the positive-dimensional component and transverse-lattice census without the additional computation here.

## value

PASS

The matroid is a standard small nonuniform relaxation, not an arbitrary finite slice. The exact census goes beyond fixed points and face numbers: isolated behavior is different from the 57 positive-dimensional components, and the local lattice types separate the Gorenstein from the non-Q-Gorenstein generic strata. These data give a concrete test case for how circuit-hyperplane relaxation affects singular support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
