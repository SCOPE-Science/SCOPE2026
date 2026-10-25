---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For exactly one free team coordinate x and a fixed finite monadic background signature, source semantics for flat atoms, bottom, conjunction, inquisitive disjunction, implication over all subteams and weak constant quantifiers translate inductively to MSO with a unary R parameter. The monadic EF color-splitting lemma bounds each unary-color population at 2^q, yielding a constructive FO translation over finite and infinite structures and finite witness bound k+2^(r+1+q). Conversely all-structures Lyndon positivity for a downward persistent empty-team FO property produces an FO negative-R formula; translating ¬R(y) to the team flat ¬(x=y) on nonempty teams realizes it with weak quantifiers. Empty teams satisfy the target/property universally. Kontinen–Ciardelli Theorem 3.6 supplies a genuine two-variable non-FO binary team witness. Actual source differential checker tests 13440 cases but full proof rests on the induction/game/Lyndon theorem.

## originality

PASS

Published Kontinen–Ciardelli supplies general InqBT syntax/semantics, first-order power of sentences, and a two-variable non-first-order example; the specific exact one-free-variable FO characterization and decidability on arbitrary monadic vocabularies are not shown in compared source statements. Prior monadic MSO elimination and Lyndon are acknowledged ingredients, not new claims.

## value

PASS

Pinpointing the arity-one/two expressive boundary, complete unary semantic characterization, constructive elimination and decidability is a natural model-theoretic fragment classification rather than a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
