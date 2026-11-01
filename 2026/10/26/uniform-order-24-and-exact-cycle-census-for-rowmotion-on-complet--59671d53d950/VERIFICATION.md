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

Encode an ideal by the two hub bits and a length-n word of five valid leaf/edge column types. The minimal-complement rowmotion rule induces a bijection on 48 (hub mask, nonempty support) states. Independent rebuilding from literal ideal membership produces exactly 13 support cycles with symbol-return permutation orders q; on onto words each support cycle of length p and support size k contributes B_k(n)/q orbits of length pq, B_k(n)=k! S(n,k). The sum yields c2=2^(n-1), c3=3^(n-1)-2^n+2, c4=2^n-2, c6=(5^n-7*3^n+11*2^n-6)/6, c8=3*2^(n-1)-2 and c24=3^(n-1)-2^n+1. All lengths divide 24, while 3/8 orbits force exact order 24; B3>0 iff n>=3. Independent direct ideal enumeration and literal complement rowmotion n=2..5 agrees with formulas, plus all support formulas n=2..49. Finiteness of the 48-state reduction, not a bounded n search, proves all n.

## originality

PASS

The complete orbit census for classical rowmotion on the height-two vertex–edge incidence posets of K_{2,n} is not supplied by the inspected foundational toggle/rowmotion theorems or claw-by-chain product families. The isolated order 24 is not claimed as independently novel; the six exact multiplicities, all-n finite-state projection, and 24-cycle threshold are the assessed result. Bounded indexed searches do not exclude an unindexed exact census.

## value

PASS

A complete cycle decomposition of classical rowmotion in an infinite family with exponentially many ideals is a natural dynamical invariant, considerably stronger than a shared small period. The fixed 48-state support/surjection mechanism explains a uniform order 24 and exact primitive-cycle threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
