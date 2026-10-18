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

The proof reduces the classification to a complete finite normal-fan computation for the stable-set polytope of the five-cycle. The independent standalone verifier `CHECK.py` uses exact rational and integer arithmetic, includes the complete facet and vertex descriptions, and exhausts all eleven-facet intersections.

The executable checks the 462 candidate vertex-defining facet sets and 2,048 candidate face-defining facet subsets. It recomputes the 143 nonempty faces, exact lattice ranks and indices of their normal cones, all ten maximal singular faces, unimodular affine triangles, four-ray conifold normal data, and singular-component incidence. Execute `python3 CHECK.py`; the success marker is `VERIFY_OK`.

Finite exhaustive computation settles these finite combinatorial claims, while toric orbit-cone and affine-singularity theorems are used separately in the written proof. No scheme-theoretic Jacobian assertion, global all-odd-cycle classification, or independent external certification is supplied.
