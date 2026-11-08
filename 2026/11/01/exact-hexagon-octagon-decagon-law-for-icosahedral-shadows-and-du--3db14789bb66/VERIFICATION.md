---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The icosahedron has 20 oriented face normals and 30 dual adjacencies. An edge silhouettes for generic view u iff adjacent face normal dot-products with u have opposite signs. Exact Q(sqrt5) sign patterns on an icosahedral fundamental spherical triangle of area pi/30 show precisely two active great-circle cuts, partition into 10-, 8- and 6-edge regions. Girard excess with alpha=acos(1/(phi*sqrt3)), beta=acos(1/sqrt3) yields p6=30/pi(alpha+beta-2pi/3), p8=30/pi(pi-alpha-2beta), p10=30/pi(beta-3pi/10). Their sum1, positive, mean 30/pi acos(sqrt5/3). Duality (proj_L I)^polar=I^polar intersection L gives the same count law for central dodecahedral sections. Independently recomputed the exact spherical areas, mean and probabilities; globality depends on exact face adjacency and symmetry tiling, not the 2000 random samples in package.

## originality

PASS

The previously published central *icosahedron section* law counts 10/12 sides, not projected icosahedron shadows or central *dodecahedron* sections. Black--Criado random-shadows bounds concern expectation and general upper/lower estimates, not the full icosahedral 6/8/10 Haar law. No stronger complete law for this object found in inspected literature; possible classical stereological equivalence remains priority risk.

## value

PASS

A natural complete probability distribution of polygon types under Haar observation of a canonical Platonic solid is independently useful for stochastic geometry, visibility, and dual sections. Resolving all three probabilities is not a trivial corollary of the well-known expected projected edge count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
