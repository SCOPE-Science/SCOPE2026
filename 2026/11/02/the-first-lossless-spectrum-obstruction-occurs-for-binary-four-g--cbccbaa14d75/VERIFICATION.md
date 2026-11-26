---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For labeled, linear binary words, the overlap graph identifies words with walks and lossless words with trails. A covering walk must cross SCCs in a single acyclic chain and can use only one intercomponent edge at each crossing. Conversely, internal reachability suffices to cover the edges in each SCC between the specified entry and exit. The frozen finite reachability proof is not limited by word length. An independent per-support enumeration using the SCC-chain criterion and the directed Euler criterion reproduced both tables: 121/121 realizable/lossless at k=3 and 5921/2611 at k=4. It recovered exactly the two stated complement-related minimum supports and reproduced both explicit words. For the first support, the entry and exit edges force the 010→101 edge to be taken before and after the 101→010 return. At k=1 every nonempty support is spelled without repetition. At k=2 any realizable support with no crossing consists of one loop; with crossings, traverse the one or two crossing edges once and any selected loops on the first visit to their vertex. Thus the title's 'first' is also valid for k starting at 1.

## originality

PASS

The walk/trail translation and Euler criterion are standard. The supported distinct contribution is the exact comparison between unconstrained multiplicity and unique traversal for binary supports, particularly the first separation at k=4 and its sharp witnesses. The strongest inspected presence-profile record directly overlaps the three-gram model but gives length-indexed capacities and does not cover the four-gram result. Neither inspected primary result supplies the finite census or obstruction.

## value

PASS

This answers the natural exact-reconstruction question of when a feasible presence set first forces redundancy. The exhaustive separation turns the lossless/repeated distinction into an exact, testable boundary rather than an arbitrary sample of words. The two minimum witnesses locate the onset and the table makes its scale explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
