---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For all 2<=m<=n except (2,2), the given corner boundary degree-preserving 2-switch removes ac,bd and adds ad,bc. The source grid involution exchanges a with b and c with d, so colour-refinement neighbour-color multisets agree at all named vertices at every round by induction; this implies C²-equivalence. Removed edges have separate 3-edge grid detours, retaining connectivity. For m>=3 and the 2-row long strips new edges embed in disjoint exterior boundary arcs; the (2,4) strip avoids any K5 or K3,3 subdivision by degree counts. Two original unit squares disappear; added-edge 3-path counting creates four new cycles only for (3,3), hence c4 gap +2 there and -2 otherwise. C4 itself is identified as the unique four-vertex 2-regular simple graph. Independently built and checked 35 2<=m<=n<=9 grids: all planar, connected, same named-vertex refinement colours to stabilization and claimed 4-cycle delta.

## originality

PASS

General theorems already show that certain grids are not identified by colour refinement among all finite graphs and give balanced-switch preservation of colours. The strengthened statement requires a *connected planar* nonisomorphic competitor for every nonexceptional grid, a single explicit switch, and exact four-cycle difference. Neither unrestricted C² characterizations nor abstract colour-preserving replacements imply the planar witness property as stated without the new geometric construction.

## value

PASS

Graph identification within connected planar graphs is a naturally stricter comparison class than unrestricted graph identification. The explicit universal two-edge switch, exceptional C4 boundary and exact four-cycle difference provide a useful sharp witness theorem, despite elementary ingredients from equitable partition theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
