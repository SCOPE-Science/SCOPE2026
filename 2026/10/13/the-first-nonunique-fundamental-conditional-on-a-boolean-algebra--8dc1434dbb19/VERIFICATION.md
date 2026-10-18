---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The row reductions from P1–P4 plus identity fix all rows except six flags for 2-atom antecedents in Boolean B3=P([3]). Fix ν(0)=1 and ν(a)=0 for a!=0. P5 restricts each flag (a,i) to exactly {i}, {i,outside}, or top. Independence of six choices is proved by full case-split checking P5 (indeed flattening equality) together with all F axioms, giving precisely 3^6=729 distinct labeled operations. Under the S3 action on six flags Burnside fixed counts 729, 27 three times, 9 twice yield 138 orbits. B2 has two F-preconditionals with different derived negations, B1 one. The independently constructed 729 operations were exhaustively checked against the eight axioms and S3-orbits, including the B2 smaller carrier search.

## originality

PASS

Holliday 2023 introduces drastic preconditionals/ν* constructions, not the complete fixed-negation fibre; Holliday 2025 Proposition4 gives uniqueness under involutive negation whereas ν* is not involutive. Chen 2026 defines F-preconditional semantics; publicly accessible abstract and the actual package point to that same algebraic framework, but the full Chen manuscript was inaccessible. Resultary published finite-chain factorial classifications have same-negation nonuniqueness on a four-element chain; these are not counterexamples to the theorem explicitly restricted to finite Boolean algebras (whose four-element carrier is a diamond). No same B3 729/138 count surfaced.

## value

PASS

The forgetful map from fundamental conditional expansions to their negation reduct is injective for Boolean carriers through four elements and first has a 729-element fibre at eight elements. The sharp first threshold and exact automorphism orbit count quantify a natural loss of conditional structure under reduct and give a canonical finite test family; no general semantic completeness claim is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
