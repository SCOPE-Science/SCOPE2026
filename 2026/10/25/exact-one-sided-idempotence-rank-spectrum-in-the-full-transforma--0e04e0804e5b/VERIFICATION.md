---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For e-anchor a with kernel fiber P_a and f-image roots B, ef fixes its image e(B) iff f(a)∈P_a for each e-fiber meeting B. Partition rooted e-fibers into those without f-root, those whose anchor is an f-root, and those with an f-root away from the anchor, giving exponential block weights sz exp(sz), v x z exp((s+x)z), v x z² exp((s+x)z). Labeled set exponential formula yields claimed EGF. Extract u^r v^t x^s z^n via coefficients: s^(r-t) t^(s-t) z^(r+s-t)(1+z)^t exp(rs z)/[(r-t)!t!(s-t)!]. This recovers exact rank-triple formula including support n>=r+s-t and ordered composition convention. Independently brute-enumerated all idempotent maps on n=1..5 and every pair, computed actual products and rank triples, obtaining total qualifying ordered pairs [1,9,94,1417,28856] and exact agreement for every triple. Finite checks corroborate the reversible all-n labeled-block proof.

## originality

PASS

Classical transformation-semigroup work on skew pairs, kernel partitions and maximal groups does not in inspected texts give joint (rank e,rank f,rank ef) enumeration. A full 2006 skew-pair article was inaccessible despite authorized attempt, so equivalent historical enumeration is a named priority risk. Distinction from commuting pairs is substantive: n=3 has 94 admissible vs 58 commuting pairs. Qualified originality PASS based on the new exact triple distribution, not idempotent structure itself.

## value

PASS

The three-rank spectrum is a natural structural invariant of ordered idempotent pairs with one-sided composition idempotence in the full transformation monoid. Complete coefficient distribution for all n separates genuinely noncommuting arrangements and determines which rank triples occur. This is an exact natural finite-algebra census of unbounded size, useful without a downstream general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
