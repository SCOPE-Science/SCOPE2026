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

A projectivity normalizes any ordered quadrangle to (0,0), (1,0), (0,1), (1,1) in an affine chart. Joins and meets of two distinct singleton vertices on the same side become singletons. The opposite horizontal and vertical edge pairs give the two coordinate directions at infinity, and the principal diagonal gives direction (1,1). From any constructed (a,0), intersect its vertical with y=1, then take the diagonal parallel back to y=0 to obtain (a-1,0). This generates the prime field, including in characteristic two. Transferring the scalars to the y-axis along that diagonal direction and intersecting horizontal and vertical parallels produces all prime-field affine points; joins and meets give the remaining rational points and lines. These constructions also force any Baer subplane through the marked quadrangle to equal the prime subplane. For an exterior point write a homogeneous representative as u+alpha*v over the prime field. The rational triples u,v are independent since otherwise the point is rational. The unique rational line through it is the common annihilator of u,v; projective duality gives the corresponding unique rational point on an exterior line. Each fibre has p^2-p members by subtracting rational incidences. An exterior point with foot line l has one neighbour in the exterior-line fibre of P exactly when P is off l, by uniqueness of the line joining the point to P, and none if P lies on l. The dual count and the singleton incidences give equitability. The proposed partition therefore cannot split under 1-WL, and its different fibres cannot merge after the singleton feet have been distinguished. The replay generates both sides in three planes and compares the actual stable partition, not just sizes, with both types of fibres.

## originality

PASS

The prior subfield criterion already determines exactly the singleton vertices and credits the five-point threshold. The distinct content here is the full quadratic-plane quotient, specifically simultaneous nonsplitting of both families of exterior fibres. The Frobenius and Baer geometry comparisons delimit how much of this was already known.

## value

PASS

A projective frame and its prime-field Baer subplane are canonical in the quadratic extension. The full quotient identifies exactly which residual vertices are indistinguishable by 1-WL and gives the cell sizes and incidence data useful for testing individualization/refinement or quotient-based methods on this family. The singleton criterion alone cannot supply that data. The short equitability argument gives a natural complete invariant beyond the earlier discreteness threshold, not a new theorem about graph-isomorphism complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
