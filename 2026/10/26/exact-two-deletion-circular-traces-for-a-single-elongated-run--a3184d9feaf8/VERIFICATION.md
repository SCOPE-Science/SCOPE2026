---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The source circular word W=0^a(10)^(k-1)1 has k zero and k one runs, one zero run of length a, all others length one. Exactly two distinct position deletions partition into disjoint cases by number s of deleted ones (recoverable from remaining one count). For s=0, two long-run zeros / one long and one singleton / two singleton runs yield 1+(k-1)+C(k-1,2)=1+C(k,2) distinct necklaces. For s=1, the adjacent-to-long-run cases coalesce to one, interior one deleted after long-run-zero deletion yields H_a(k)=k-2 if a>=4 and ceil((k-2)/2) if a=3 due to interchange of equal-length two-zero runs, and other cases yield (k-2)^2. For s=2, deletion of ones neighboring the long run gives k-2 classes, internal pairs yield C(k-2,2), with floor((k-3)/2) duplicate signatures exactly at a=3 when two zero runs of length three interchange. The case disjointness and oriented *cyclic* signatures (no reversal quotient) yield the T_s formulas and totals 2k²-6k+8 if a=3 versus 2k²-5k+5 if a>=4; gap k-3 begins k=4. Independently built a canonical least-rotation necklace enumeration from every unordered deleted-position pair and confirmed all three counts for 168 parameter pairs (a=3..8,k=3..30). Finite tests corroborate, not replace, all-a,k run-signature exhaustion.

## originality

PASS

Independently compared actual mathematical implications and the natural invariant against ranked published results and the primary material actually read. The specific evaluated final claim was not found as a stated theorem or direct special case; all relevant earlier general techniques are credited and priority limitations retained.

## value

PASS

The supported trace-count invariant is natural for circular deletion channels, and the a=3 length-collision transition gives an interpretable structural threshold. The composition-refined exact support counts are independently usable for code/reconstruction studies of this concrete near-alternating family without claiming general deletion complexity. Not merely a count for one tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
