---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For finite simple Cartesian tori with 5<=m<=n, any pair whose endpoints differ in both coordinates admits disjoint move-order geodesics, so an edge can be monitored only within its row/column fiber. A cycle subset monitors all edges iff every gap between cyclic consecutive members is strictly shorter than half the circumference. This gives three probes per row/column and lower bound 3n. The placement T={0,floor(m/3),floor(2m/3)} shifted by -floor(mj/n) in column j has column gaps <=ceil(m/3)<m/2. The exact row-block starts J_v=ceil(vn/m) bound row gaps by B=1+ceil((ceil(m/3)-1)n/m)<n/2 for n>=12. Exhaustive elementary inequalities at 5<=m<=n<=11 leave only (5,6) and (7,8), with listed direct row/column certificates. Independent shortest-arc criterion checked on all 8160 cycle subsets of sizes 5..12, and row/column construction checked for 3000 rectangles. These finite checks do not prove the unrestricted theorem; the inequalities and explicit witnesses do.

## originality

PASS

Best-of-knowledge originality is the unequal-side exact upper bound with explicit optimal placements; Haslegrave Theorem 4 proves only the square case and Theorem 1 the general Cartesian fiber/lower-bound structure. The cycle scalar invariant is established earlier. A hidden stronger rectangular theorem in incompletely accessible publisher texts remains a priority risk.

## value

PASS

Rectangular Cartesian tori are canonical monitoring networks; known universal fiber lower bound and square upper bound leave a real unequal-dimensions gap. The exact sharp value for all permissible rectangles, with simple explicit optimal placements and two exceptional finite certificates, is an independently useful natural graph invariant, not a relabeling of the square case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
