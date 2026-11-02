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

# Verification

Run `python3 checker.py` with Python 3 and no third-party packages. It verifies all dyadic levels \(k=4,\ldots,10\) by two independent descriptions of the regular paperfolding word. The checker enumerates the \(4N\) canonical rotations, builds overlapping length-two count signatures, verifies all twelve formula classes, and compares the set with distinct factors of a direct recurrence-generated prefix of length \(65N\). It also checks circular counts of the four Toeplitz skeletons.

Expected terminal result: `PASS: independent recurrence, canonical rotations, occurrence set, and exact 2-Abelian multiplicities.`

Finite checks alone do not certify all powers of two. The mathematical proof in `RESULT.md` explains why there are exactly four freely specifiable skeletons at each residue phase, invokes Allouche's established \(4N\) factor-complexity theorem for distinctness, derives cyclic bigram totals analytically, and cuts circular edges to count the fibres. No computer-assisted infinite certification or independent mathematical audit is claimed.
