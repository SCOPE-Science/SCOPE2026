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

The graph of four-bit vertices and five-bit edges gives a bijection between cyclic words of the required kind and Euler tours rooted at the unique edge 00000. The pairing-permutation argument is exhaustive: each tour prescribes exactly one in/out bijection per vertex and admissibility is exactly having a single orbit. I independently enumerated via last-exit trees, not the frozen pairing or depth-first programs. Each nonroot's final outgoing edge must point along a directed path to root 0000, since otherwise the last departure time strictly increases around a nonroot cycle. Conversely, order each nonroot's outgoing edges with the chosen tree edge last and put the 00000 loop first at the root. A traversal that stops early must stop at the root by degree balance. Any unused outgoing edge would imply an unused last-exit path to the root (unused indegree equals unused outdegree after a closed partial traversal), a contradiction. This justifies exhausting the 2^15 nonroot last-exit choices. The fresh code evaluated distinct circular factors as fixed-width integers, tested strict comparison against every bit rotation (equal rotations reject nonprimitive factors), reproduced all 2048 original CSV rows exactly, and obtained cutoff distinct-profile/collision-pair counts (2044,4), (2045,3), (2047,1), (2048,0) at 16–19. The sole 18-doubleton and its full common profile were reproduced, with respective 19-coordinates 1 and 2. Both words have the unique 00000 root, and truncation preserves their collision, so sharpness holds at every shorter cutoff. All binary strings through length five occur, yielding (2,1,2,3,6). Replay: python3 /workspace/audit_evidence/3_census.py /workspace/source/2026/10/19/sharp-lyndon-factor-reconstruction-of-binary-order-five-de-bruij--b0fd8712e30d/profiles.csv. This is finite exact arithmetic with a completeness argument, not a result for other orders or quotients.

## originality

PASS

The nearest indexed record tabulates the number of components in the Chen–Fox–Lyndon factorization of linear rotations, not distinct Lyndon substrings by length. The inspected primary literature establishes the relevant predicate, counting questions and constructions, but not the separating profile or cutoff on this finite cyclic family. The independent census verifies the result, not novelty. The literature comparison is bounded and does not certify historical priority.

## value

PASS

Both the object and invariant arise naturally: order-five binary de Bruijn cycles form a standard complete nontrivial family, ordinary circular factor complexity is identical across it, and distinct Lyndon-factor counts are an established refinement of word complexity. The first five coordinates are forced, so it is not evident that retaining just fourteen later counts suffices or that the last needed count is at 19. The exact collision and its resolution give a reusable sharp certificate for reconstruction from counts rather than positions; this is not merely a known cycle census or an arbitrarily selected cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
