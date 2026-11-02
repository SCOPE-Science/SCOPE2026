---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For each positive n, order-preserving regressive idempotents are precisely predecessor projections to S containing 1. Direct evaluation of e_S e_T and e_T e_S at last fixed points establishes the if-and-only-if absence of mixed exclusive colors in every gap between common fixed points. A three-state automaton with 0/A/B gap colors and reset on common point gives M=[[2,1,1],[1,2,0],[1,0,2]], a_1=1,a_2=4,a_n=4a_(n-1)-2a_(n-2), rational generating function 1/(1-4z+2z^2), closed form and probability a_n/4^(n-1). Conditioning each position on fixed S gives the displayed 3x3 M0/M1 individual idempotent centralizer product. Independent direct composition/gap/transfer enumeration covered 21,845 ordered pairs for n=1..8; this is finite corroboration, not the all-n proof.

## originality

PASS

Existing OEIS A007070 explicitly contains the exact recurrence and numerical sequence; no novelty is asserted for its unqualified enumeration. Pantazi–Spircu discuss the idempotent structure of classical Catalan monoids and selected commuting relations, while Sapir–Volkov address finite-basis properties and different commuting-idempotent monoid varieties. Neither inspected primary result gives this global exclusive-color gap iff criterion and the centralizer size conditioned on every fixed set. Searched Resultary records do not show direct theorem implication. Historical coverage of a differently formulated predecessor-projection commutation lemma remains possible.

## value

PASS

The characterization is a structural semigroup criterion that answers which actual idempotents commute, not merely a restatement of a known number sequence. The fixed-idempotent transfer produces exact centralizer sizes for all 2^(n-1) idempotents with a uniform algorithm and supplies a natural commutation probability; those object-resolved invariants are useful even though the aggregate recurrence is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
