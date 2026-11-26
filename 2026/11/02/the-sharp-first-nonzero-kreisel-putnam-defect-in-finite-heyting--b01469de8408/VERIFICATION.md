---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A failure occurs at some x precisely when Q=↓x∩¬A is covered by B∪C but by neither alone. Hence Q has distinct incomparable maxima u,v, and x has an A-predecessor. A minimal such predecessor s is minimal in P and incomparable with both u and v. The downsets Q without u and ↓u cover Q properly; independently adjoining s to either and reversing the ordered pair gives eight distinct failures with the same A. The induced poset on s,u,v,x is A_3⊕A_1; restriction of downsets is onto its nine-element lattice, and equality of sizes makes restriction an isomorphism. In this poset three singleton antecedents each give eight failures, verified directly over 9^3 ordered triples. In the displayed size-h family the base fork plus an isolated s has ten downsets, and each upper-chain point adds exactly one. Only A={s} can fail, only at an upper-chain witness; then u and v must be assigned to opposite consequents, with independent choices for including s, giving exactly eight for each h≥11. Direct implication over 11^3 triples also confirms the seed count. These finite checks corroborate the multiplicities rather than replace the universal proof.

## originality

PASS

The defensible distinct claim is quantitative: sharp smallest positive KP failure count eight, with exact attainment at every size h≥11. The minimum-order boundary follows from the standard sort of qualitative frame obstruction once one counts its downsets, so do not credit the underlying obstruction as original. The exact multiplicities and sharp quantitative profile are not supplied by the inspected validity and satisfiability results.

## value

PASS

The smallest nonzero count is a natural quantitative boundary for a named intermediate-logic principle. The local counting argument explains why a single failure forces multiplicity eight, and the attaining construction yields a precise optimum at every order h≥11 rather than an isolated small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
