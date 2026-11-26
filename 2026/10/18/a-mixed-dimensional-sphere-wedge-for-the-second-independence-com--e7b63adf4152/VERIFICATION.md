---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The edges selected from K6 have nonempty edge components K2 or P3, giving at most four edges. Independent reproduction (`python3 /workspace/branches/independent_checks.py 2`) assembled components on the original six vertices, obtained (15,105,195,90) nonempty face counts by size, and checked the frozen order on the whole nonempty face poset: all 1,155 oriented covers form a DAG with 185 pairs and critical counts (1,0,24,10). Rather than using the supplied signed Morse elimination or mod-two check, the replay reduces the ordinary oriented simplicial boundaries over the rationals; the top rank is 80 of 90, so H3 has rational dimension 10. Thus the integer boundary out of the ten critical 3-cells has rational rank zero and is identically zero over the integers. The Morse 2-skeleton is a wedge of 24 two-spheres; Hurewicz on that skeleton identifies each attaching class in pi_2 with its integral cellular degree vector, so the ten attaching maps are null. This checks the non-equivariant homotopy statement, not just Betti numbers or an equivariant decomposition. The uploaded checker was inspected, not executed.

## originality

PASS

The exact mixed-dimensional integral wedge is not implied by the inspected earlier primary literature. The same wedge appears in a distinct later-dated Resultary entry as its n=6 case; that is exact mathematical coverage, not an antecedent shown to predate this frozen result. The inspected same-day entry computes a different complex. This is a scoped best-of-knowledge finding, not a certification of priority.

## value

PASS

Six is the first size at which disjoint pairs of two-edge paths coexist with perfect matchings as maximal packings of different cardinalities. The exact integral splitting of this natural nonpure base case distinguishes actual mixed-dimensional spheres from merely mixed-dimensional facets or modular homology. It is a usable benchmark for Morse constructions and for any attempted triangular-family classification. The value is specific to the non-equivariant finite result; no pattern for larger n is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
