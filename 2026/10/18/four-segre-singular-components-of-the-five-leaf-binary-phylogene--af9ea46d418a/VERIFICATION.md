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

`verify.py` reconstructs the seven-dimensional polytope from its sixteen binary parity networks, checks that its twelve local tetrahedral inequalities are facets, and enumerates all \(711\) faces by integer facet intersections. Hermite normal forms and maximal-minor gcds detect exactly four inclusion-maximal nonsmooth faces, namely the two binary-value faces for each of the two internal edges. Exact saturated-lattice tests identify the generic normal cones as primitive square cones and the component/intersection faces as unimodular products of simplices. Direct degree-one to degree-three monomial counts corroborate the Hilbert formula. Run `python verify.py` with Python 3 and SymPy; the expected terminal marker is `VERIFY_OK`.

The enumeration is exhaustive for the stated finite polytope, not numerical sampling or a surrogate proof for a larger family. The proof of identification with the network polytope uses the local-tetrahedron gluing argument. The reduced singular-support scheme is distinct from the nonreduced Jacobian singular scheme, which is not calculated. Characteristic-independent claims rely on saturated integral toric semigroups. No separate independent audit was performed.
