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

The standalone `verify.py` uses exact rational nullspaces, integer facet-normal reduction, full finite intersections of facets, exact affine ranks and Smith normal forms. It independently confirms twelve primitive facets, 153 nonempty faces, face vector \((10,35,55,40,12,1)\), singular orbit counts \((10,25,10)\) in orbit dimensions zero through two, precisely five maximal singular edges and ten maximal singular triangles, lattice saturation for every claimed local transverse cone, all unit-magnitude primitive relations, and ten unimodular triangular component faces.

Run `python verify.py` with Python 3 and SymPy installed; successful exit prints `VERIFY_OK`. The checker was run directly and returned `VERIFY_OK` with expected counts. The proof in `RESULT.md` explains why the finite enumeration is exhaustive. The test is not an assertion of independent audit, and no unverified global extension beyond this one wheel graph is claimed.

The normal fan is formed in the full dual of the integer vertex-difference lattice; the result does not concern the possibly different unnormalized edge-ring model. The nonreduced Jacobian scheme and component-intersection analytic germs were not determined.
