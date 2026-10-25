---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Lucas mod-2 makes odd Pascal support E_n exactly all submasks of n, decomposed into disjoint consecutive 1-bit runs of lengths t_i, each contributing 0<=u_i<2^t_i. The mandatory separating zero makes any equality x+y=z+w coordinatewise: the lowest nonzero block difference has magnitude <=2(2^t_i-1), strictly less than 2^{a_(i+1)-a_i}; induction kills all differences. Consecutive three-term identities then force all k-term progressions to factor by blocks, including k=2. The number of oriented length-k progressions in each interval is B_i=L_i(2h_i+1)-(k-1)h_i(h_i+1); subtract ∏L_i constant sequences, pair reversal, divide by 2. The max length, Fibonacci 3-AP-free count, and extremal product are consequences. Independent direct Lucas-index enumeration matched the formula for n=3,11,27,59,87,127 and k=2..5 including n=27 counts 120/24/10. This finite corroboration does not establish all n.

## originality

PASS

Best-knowledge PASS for all-length fixed-Pascal-row AP census, not the Lucas digit support, Fine/Glaisher support size, or generic digit combinatorics. Existing Lucas and Sierpinski results characterize odd entries; Rolnick examines different ternary Stanley sequences, and Kuca additive Ulam-type sequences. Their stated results do not directly count all AP lengths in each binary Pascal support. An unindexed equivalent digital-block AP formula remains possible.

## value

PASS

The parity support of Pascal rows is a natural Sierpinski-type additive set. A uniform exact product formula replaces raw enumeration for every row and progression length, gives a maximal-length extremal count, and sharp Fibonacci characterization of AP-free rows. This is an independently usable exact arithmetic invariant with a concrete combinatorial motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
