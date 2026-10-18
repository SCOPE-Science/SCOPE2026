---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For states Z/nZ, a is the forward n-cycle and b_j moves j-1 to j. Reverse preimages of a proper nonempty cyclic interval stay cyclic intervals: a shifts its left endpoint backward; b_j enlarges by one only when the old left endpoint equals j, then shifts that endpoint backward, or else remains stationary/shrinks. A reset-word inverse walk must have n-1 marked enlargement visits, producing the lower bound by the minimum cyclic scan length. Conversely each marked old endpoint can enlarge and each unmarked one can be shifted by a^-1, yielding a matching reset word after reversing the inverse-letter list. Decomposing n-1 visits into full tours gives the even/odd two-mark formulas and special n=2 boundary. An independently written forward subset BFS versus the scan formula exhaustively agrees for all 501 nonempty mark sets with 2<=n<=8. The finite BFS is supporting evidence only.

## originality

PASS

The specified surviving claim is not established by any inspected prior statement or directly dominating mathematical implication. The four separate equivalence/coverage/table/implication comparisons below identify exactly which named background results are already known and which new mathematical conclusion remains; unpublished and inaccessible-source risks are explicitly retained.

## value

PASS

The theorem gives a position-dependent exact shortest synchronization length for every subset of local merging letters, not only the known one-merge extremal or a general existence/bound statement; the parity-and-distance two-merge law is a particularly transparent natural specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
