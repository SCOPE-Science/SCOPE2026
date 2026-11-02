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

Ultrahomogeneity identifies each nonalgebraic extension with one downset L, one upset U and all l<u cross-pairs. One-sided patterns contribute 2J-1. For mixed patterns, common upper neighbors are counted for singleton lower subset (7n choices), adjacent pair (3n), distance-two pair (n), and cyclic triple (n), with no other common upper neighbors for n>=5. Thus M=12n. An ideal is encoded by choice of upper vertices, with each lower not forced by a selected top vertex providing weight 2: J=sum_{z in {0,1}^n} 2^{#cyclic zero triples}. A four-state weighted transition T has characteristic polynomial z(z-1)(z²-2z-1), yielding J=1+(1+sqrt2)^n+(1-sqrt2)^n. Independent subset enumeration for n=5..11 confirmed t=225,469,1041,2405,5681 for first five n and M=12n; complete all-n proof is transfer-matrix and incidence argument.

## originality

PASS

Best-of-knowledge originality of the precise stated full theorem: mathematical antecedents and equivalent formulations were compared from real source readings. Standard ingredients are credited and genuine historical coverage risks remain; unsuccessful search is not a novelty proof. Provides the general one-point extension downset/upset condition, which is credited; it does not evaluate the named cyclic incidence family. The exact formula c(P)=#(ideal/filter admissible pairs) and #P-completeness apply generally but do not evaluate this cyclic triple-incidence J or the 12n mixed count. Specialization requires a nontrivial transfer and incidence calculation. Shared cyclic trace counts a different hypergraph-polytope vertex invariant; no implication to named random-poset 1-types or exact mixed 12n cut term.

## value

PASS

Pointwise stabilizer one-type counts are natural invariants of named finite subposets of the random poset. The regular cyclic length-three incidence family is a motivated all-size hypergraph poset; complete exact growth and linear versus exponential two-sided cut dichotomy give a useful explicit classification in a generally #P-complete counting setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
