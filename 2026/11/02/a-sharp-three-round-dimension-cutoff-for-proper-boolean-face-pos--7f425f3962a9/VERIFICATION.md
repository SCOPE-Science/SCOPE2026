---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For n,m>=8 the three-round EF duplicator maintains sizes of all Venn cells either equal below 2^r or both >=2^r, preserving nonempty proper status and all atomic inclusion comparisons at r=0. For n=2..8, the nested extension-type sets B(x,y), U(x), H_n exactly encode the three-round EF game; permutation symmetry reduces x to each cardinality and all y,z are checked. An independently written brute-force bitset enumeration recomputed H_n at 2<=n<=8, finding 1,2,3,4,5,6,7 distinct pointed-type spectra respectively, hence seven mutually unequal classes. The finite computation is exhaustive only through n=8; EF induction proves the unbounded stable class. Rank-two pointed relation profiles distinguish n=2,3 and n>=4.

## originality

PASS

Published Resultary theorem for full Boolean-algebra language implies stable equivalence from eight atoms by the quantifier-free interpretation excluding 0 and 1, but lower-size inequivalence in richer Boolean language does not imply pure inclusion-reduct distinguishability. Published full Boolean inclusion poset has a different cutoff with endpoints. Armstrong–Hersh concern topology and a Boolean-to-Bruhat map. Exact seven-class proper-subset order-reduct classification therefore survives those comparisons; historical low-rank EF classifications may still overlap.

## value

PASS

Exact finite model-theoretic rank-3 classification of a canonical family of simplex boundary face posets, identifying a sharp minimal stable finite representative (254 faces). Comparing with Boolean-algebra and full-poset thresholds isolates effect of deleting endpoints and forgetting operations, beyond a routine textbook EF bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
