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

# Verification of the period-six enumeration

The accompanying standalone `verify.py` runs with Python 3 and no third-party dependencies. It encodes rule 115 from its eight truth-table bits, enumerates every \(p=3\) and \(p=6\) temporal-column triple, constructs all edges and filters the vertices reachable to and from the background. This obtains matrices of dimensions 3 and 27, respectively.

For each reduced matrix it computes exact integer boundary path counts. The code establishes the Fibonacci recurrence through three initial scalar matrix-difference identities and the order-four recurrence through 27 initial scalar matrix-difference identities. Cayley–Hamilton makes these checks sufficient for all subsequent window lengths; the proof in RESULT.md spells out that implication. It separately enumerates all \(\(4^n\)\) initial two-component pairs for each \(0\le n\le7\), using finite deviations from the infinite periodic background, and verifies both time-3 and time-6 counts.

The exact counts begin \(\(B_n=1,2,3,5,8,13,21,34\)\) and \(\(A_n=1,2,7,21,60,165,461,1282\)\). In particular the four least-period-six initial pairs in a two-site window are verified directly. No numerical tolerance, random sample, black-box network service, or finite-prefix extrapolation is involved. The finite-state transfer identity is the universal argument; direct evolution is a separate low-length check.

Limits: this does not verify periods other than 3 and 6, does not certify literature priority, and has not received independent external audit.
