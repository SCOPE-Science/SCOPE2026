---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Independently reconstructed the 30-vertex cubic incidence graph with girth8, diameter4 and 45 edges; bipartite distance parity excludes same-side endpoints for odd length5. The S6 action is transitive on the two ordered point-to-matching distance types, with counts 45 incident, 180 nonincident and reversed copies. For representatives, constructed all positive-step length-five endpoint-localized tuples and signed smooth-point deletion matrices ∂3:C3→C2 and ∂4:C4→C3, with ∂3∂4=0. Independently recomputed at distance1 (C2,C3,C4)=(8,36,56), ranks(∂3,∂4)=(8,28), nonzero ∂4 Smith factors 1^28; at distance3 (14,45,40), ranks(14,27), ∂4 Smith factors 1^27. Because im∂4 is primitive in free C3 and contained in ker∂3, ker∂3/im∂4 is torsion-free, of rank zero or four. Summing 2×180×4 proves Z^1440; this is stronger than matching F2 dimensions. The finite enumerations are mathematically exhaustive for this one finite graph, not a sample or a general theorem for all girth-eight graphs.

## originality

PASS

The exact same Tutte–Coxeter bidegree (3,5) with total F2 dimension1440 was published earlier, including endpoint multiplicities and boundary ranks over F2. That full prior RESULT.md was inspected and explicitly disclaims integral or odd-characteristic claims. The new claim is exclusively integer freeness, Smith profiles and the consequent rational/all-prime classification, which the F2 data alone cannot imply (odd torsion is invisible in F2). Earlier girth-vanishing results do not reach (3,5) at girth8. This is a qualified but substantive integral strengthening, not a novelty claim for dimension1440.

## value

PASS

Determining actual integer magnitude homology at the first nonvanishing second-off-diagonal girth-eight boundary for the unique (3,8)-cage is a natural exact invariant, not an arbitrary tiny graph exercise. Existing F2 data leave integral freeness, rational rank and possible odd-prime torsion unknown. Exhaustive signed Smith computations resolve these precise arithmetic questions, providing an all-characteristic refinement with no claim to solve higher magnitude homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
