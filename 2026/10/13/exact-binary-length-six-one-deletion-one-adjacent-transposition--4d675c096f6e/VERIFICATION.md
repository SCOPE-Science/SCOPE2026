---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Channel definition inspected: at most one transposition of unequal adjacent binary symbols followed by at most one deletion, with both operations optional. Reconstructed each of 64 mixed-length descendant balls and all 2,016 unordered compatibility tests, obtaining exactly 928 compatible edges. Independent unpruned exhaustive maximal-clique enumeration, not a heuristic bound, gives 2921 maximal cliques and sizes 3:218, 4:1861, 5:816, 6:26. Consequently maximum 6 and precisely 26 labeled maximizers; intersection of 26 codebooks consists of 000000 and 111111; reversal/complement orbit sizes sorted 1,1,2,2,2,2,4,4,4,4. The exact n=6 claim is a finite theorem and the enumeration truly traverses its full finite domain; no inference to other lengths.

## originality

PASS

Closest examined primary same-model Gabrys–Yaakobi–Milenkovic defines the same successive deletion-and-transposition ball and builds coding constructions/asymptotic bounds, but does not classify the 64-word compatibility graph. Ye–Ge 2025 gives asymptotic/general bounds. Published Resultary one-deletion-only n6 census (maximum 10) and 0-deletion-OR-transposition census (n6 maximum 17) concern strictly different channels, hence cannot entail the 6,26,10-orbit simultaneous-channel classification. Genuine risk of older unindexed fixed-small-parameter tables remains.

## value

PASS

A naturally smallest nontrivial binary simultaneous synchronization channel has a complete extremal-code census, exact optimizer count, universal constant-word core, and symmetry orbit structure. These are nontrivial equality data not provided by general asymptotic constructions and useful as finite baselines/test cases for deletion-transposition bounds and decoder design; not a generic tiny bit check or an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
