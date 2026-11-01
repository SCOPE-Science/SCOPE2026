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

The deck separates by substring length and determines the total Parikh vector T and unordered inward prefix/suffix path vertices {L_i,R_i}. Complement identities L_(n-i)=T-R_i, R_(n-i)=T-L_i reconstruct outer layers; at odd n the central symbol T-L_m-R_m is forced and must be one unit vector. When successive layer vertices A!=B and C!=D, both perfect matchings cannot simultaneously use only unit-coordinate increments, because they would force two distinct target vertices to agree. Thus orientation is unique across each non-meeting interval, with independent exchanges only at levels of equal vertices. For n<=5 there is at most one nontrivial separated excursion, hence one reversal orbit; for n=6 a second separated excursion requires L1!=R1, L2=R2, L3!=R3, exactly the displayed four words. The length-one deck and length-three difference from the common length-two vector recover the unordered outer pair and unordered center pair, ensuring distinct fiber indexing. Palindromes give q^3 unique singleton decks; others not in quadruples pair under reversal, yielding the exact formula. Independent DIRECT enumeration of full multiset decks for q=2,3,4,5 gives lengths-six totals 35,369,2044,7775 and the exact (1,2,4)-fiber counts for all four sizes. The finite tests support, but do not prove, the universal q statement.

## originality

PASS

Best-of-knowledge comparison of the complete asserted mathematical implication against actual primary material read and documented searches. The full binary n=6 collision is credited; its all-q classification and new four-symbol q=4 fibers are not implied by a binary-only theorem.

## value

PASS

A natural exact polymer/string-observation reconstruction problem has a sharp first ambiguity at length six; the complete q-ary fiber and code-capacity classification is an exact structural invariant useful independently of broader code construction questions. The q=4 four-symbol fibers and binomial-pair distribution cannot be inferred merely by relabeling the known binary collision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
