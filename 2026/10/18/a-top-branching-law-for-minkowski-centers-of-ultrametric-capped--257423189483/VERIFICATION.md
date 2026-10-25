---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Coordinate supports attain 0 and cap w_ij. For each oriented triangle functional F=d_ij-d_ik-d_jk, exact min -2 min(w_ik,w_jk) follows from a truncated 1-Lipschitz ultrametric distance-to-{i,j} function and its cut semimetric; max F=0. Reflection feasibility for z=(s+1)c gives z_ij<=s w_ij and z_ik+z_jk-z_ij>=2min(w_ik,w_jk). In any ultrametric triple its shortest pair forces s>=2; z=2w attains 2. At s=2, cap deficits vanish in equilateral triples, have zero short-edge deficit and equal long deficits in isosceles triples. Root-block triangles force all internal deficits zero, all cross deficits zero with three or more blocks, and a common h in two blocks restricted by R-L. Independent LP of n=3 ultrametric (1,5,5) found s=2, center coordinate intervals [2/3,2/3],[2,10/3],[2,10/3].

## originality

PASS

Full inspected robust optimization article gives a generic LP framework for Minkowski centers, not this explicit evaluated ultrametric family/complete loci. Inspected Gartsman–Linial preprint studies uniform-cap metric polytope maximal inscribed/minimal circumscribed ellipsoids rather than Minkowski reflection asymmetry. Resultary nearest neighboring center results concern other polytopes (matroid bases, stellohedra, transportation polytopes). This center-locus dichotomy is not a direct restatement of them.

## value

PASS

A complete all-n all-positive-ultrametric classification with a sharp top-branching uniqueness transition is a natural geometric invariant, including exact dimension and full center segment. It separates reflection asymmetry from ellipsoidal center notions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
