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

Reconstructed the induction with finite boundaries. Q_2=010 and Q_3=0100010 give the base tables; Q_4 contains all four bilateral extensions of 0. In Q_r every 1 is in an even position, and 11, 0000 and 1001 are absent. Thus 000 is not bispecial and every bispecial of length at least three contains a 1, has fixed start parity, and must both begin and end at odd positions to allow context 1 on either side. Such an occurrence has a unique preimage v under v -> mu(v)0. Its left and right contexts, including their absence at the two endpoints, map exactly to the complemented preimage contexts. Treating the short factors separately proves completeness and propagates the missing diagonal from 11 in Q_3 to b b at j=k-2. The two length families are disjoint; the orders and missing-pair totals follow. Separate direct factor enumeration matched every row for ranks 2–9, including the first missing-diagonal switch.

## originality

PASS

Pass for the complete finite list and exact bilateral table as a joint classification, not for originating synchronization or any of the specific diagonal absences already obtainable from the earlier antidictionary. In particular the terminal missing diagonal is not a stand-alone novelty here. The strongest inspected finite comparators give lower bounds or extremal absent words, not exhaustion of the bispecials or exact availability of the remaining bilateral extensions in the truncated words.

## value

PASS

The bispecial and bilateral languages are natural finite factor invariants. The complete classification identifies every positive as well as missing context, separates the terminal truncation row from the stable strong family, and yields the exact bilateral-order counts. This is useful beyond the earlier extremal or lower-bound absent-word information, without claiming a complete antidictionary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
