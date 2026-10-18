---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Encode a maximal independent set on the 2n-vertex Möbius ladder as rung states U,V,0 with boundary twist U↔V after n rungs. Independence forces adjacent occupied states to differ; domination of both vertices on an empty rung forces its neighbors occupied and of opposite types. Thus zeros never adjacent, the j occupied states strictly alternate around the twisted cycle, and j is odd. Conversely every n-periodic cyclic pattern with j odd occupied positions and isolated empty positions lifts in exactly 2 ways and all are maximal independent. Marking an occupied rung counts n/j*binom(j,n−j) binary cyclic patterns; the 2 lifts give coefficient 2n/j*binom(j,n−j). The generating function follows 2t∂_t artanh(zt(1+t)) and deleting n=1,2. Independent brute force over all 2^(2n) labeled vertex subsets for every n=3..9 compared each graded coefficient exactly, including n=9 {5:18,7:54,9:2}; source verifier independently reports n=3..10 and numerical formula checks through n=200. Infinite identity is a bijection proof, not finite extrapolation.

## originality

PASS

OEIS A290608 gives only the ungraded total number of maximal independent sets of a Möbius ladder, Lucas(n)−2cos(2πn/3), and 2012 Bautista-Ramos & Guillén-Galván count all independent sets, not maximal/independent dominating sets. Dod's independent-domination polynomial supplies the general invariant, not this ladder-specific full size distribution. McSorley (1998) 'Counting Structures in the Möbius Ladder' is a highly plausible directly covering source: the inspected abstract describes multiple enumerations but complete article could not be read after OA/preprint attempts and authorized Oxford returned vpn_disconnected; therefore DO NOT certify it as noncovering. Best-of-knowledge originality PASS, explicitly provisional against that prioritized source because no verified implication or exact graded theorem was found in material actually read. Prior total does not imply full size distribution.

## value

PASS

The exact all-cardinality independent-domination polynomial for a familiar cubic graph family is a natural complete structural refinement of a previously known total count. Odd-cardinality rigidity, exact extrema and multiplicities, and generating function provide graph domination and minimal vertex-cover information not derivable from the ungraded OEIS entry. No downstream general conjecture required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
