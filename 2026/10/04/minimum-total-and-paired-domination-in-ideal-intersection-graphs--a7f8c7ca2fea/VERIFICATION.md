---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

In each chain factor, powers of the maximal ideal are nested, so two product ideals meet nontrivially exactly when their active supports intersect. A two-set can be total dominating only if the selected ideals are adjacent and their active supports cover every coordinate, because the socle-like singleton-support ideal in any omitted coordinate meets neither. These conditions are sufficient for every nonzero ideal to meet at least one selected ideal. Whenever such a pair exists it is also paired, so both minima are two; direct support choices give exactly the three stated obstructions. For the count, P=prod ell_i(ell_i+2) counts ordered ideal pairs with full support union before vertex exclusions, L=prod ell_i and B=prod(ell_i+1) account for zero/ring cases, L(2^r-2) removes disjoint active-support bipartitions, and L-1 removes proper full-support diagonals. The remainder is even and division by swap gives the displayed formula. Independent arithmetic checks reproduce representative values, including 3 for lengths (1,1,1), 18 for (1,1,1,1), 15 for (2,2) and 40 for (3,1,1). The verifier additionally checks exponent-vector graphs and Z/n through 120; the proof is arbitrary-rank.

## originality

PASS

A broader published finite-module theorem already determines the total-domination number and length-two obstruction, so the scalar gamma_t=2 part is not new. However, that theorem neither treats paired domination nor classifies/counts every minimum pair. Abu Osba--Al-Addasi--Abughneim's full same-family paper treats ordinary domination and other graph invariants, not total or paired domination. The audited active-support criterion and exact product multiplicity are therefore a substantive refinement not implied by the checked literature.

## value

PASS

Although the scalar total-domination value now has broader module-theoretic coverage, classifying and counting every minimum strengthened dominating pair across all finite principal ideal rings is a natural exact refinement. The closed product formula records the full local nilpotency-length dependence and simultaneously resolves paired domination, making the surviving content more than a renamed scalar corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
