---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For invariant simplices the oriented chain trace is (-1)^{q+1}, q the number of selected edge-vertex transposition orbits, including empty face. The outside W-graph with cover number <=2 has weighted correction s(Z)=1-1_{I!=empty}-|U|+|I|+|C|. Exhaustive structural cases: a single edge yields n-1, two edges +1, triangle +1, square -1, others zero. Counting them gives reduced Lefschetz C(m-1,3). Published Jonsson H_3 and H_4 ranks plus published four-subset permutation H_4 character imply tr(H_3)=C(m-2,4)-C(m-2,3), hence positive and negative dimensions as claimed; rational finite-group transfer gives quotient invariant homology. Independently enumerated every two-covered outside simple graph n=2..5 and verified each s(Z) against these five types and Lefschetz 1,4,10,20, not merely cached VERIFY_OK. The unbounded proof is the explicit cover classification and binomial identity.

## originality

PASS

Bounded statement-and-implication comparisons with published primary and related research did not identify coverage of the precise new assertion, and the distinct contribution is established by the indicated independently checked argument; priority remains subject to specifically recorded access risks.

## value

PASS

Computing the previously missing degree-three involution character and both rational quotient Betti numbers for the natural two-cover complex is a substantive equivariant refinement. It bridges known integral nonequivariant ranks and a known top-homology representation through a nontrivial signed enumeration valid at every m; neither prior ingredient alone determines the new trace.

The dated certificate retains the supplied scientific assessment, sources and limitations.
