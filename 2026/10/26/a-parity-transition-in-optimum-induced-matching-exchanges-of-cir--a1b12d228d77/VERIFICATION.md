---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible mathematical checks

Run `python verify.py` using Python 3.9 or later. No external packages are required.

The program builds \(P_n\) and derives pairwise forbidden induced-matching edges from its *actual* vertex adjacency. It searches maximum independent sets in this conflict graph by exact branching with memoization, then generates the proposed closed-form configurations separately. It compares the two complete sets of edge subsets and checks every one-edge-exchange adjacency against the predicted formulas for all \(4\le n\le19\).

Observed terminal line: `ALL_VERIFY_OK`. Boundary cases include \(n=4\) (six isolated optima), \(n=5\) (25 connected optima, 60 edges), \(n=6\) (two isolated optima), and \(n=19\) (361 connected optima, 760 edges). The exact degrees at \(n=19\) are four with multiplicity 304, five with multiplicity 38, and six with multiplicity 19.

Finite tests independently check enumeration and the proposed formula at those sizes. They are not substitutes for the proof's all-order occupancy argument and classification. The proof relies on direct analysis of the possible column occupancy words and replacement of one whole selected graph edge. No independent review has been performed.
