---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For the exact 18 labeled associative ternary multiplication tables, the finite rightward dependency cone makes all initial length-n words realizable. Group rules yield 3^n or 3*2^(n-1); trigger and stabilization languages give the nine listed formula types, including the exceptional n=1 rule 3 and rule 10 one-symbol transient; semilattice rule 13 gives binomial(n+2,2). Each description constructs and excludes all words for all n, not merely experimental n. Independent enumeration verified table associativity and all 144 rule-length cases for n=1..8, corroborating but not replacing the infinite normal-form proof.

## originality

PASS

Fukś 2025 AUTOMATA / arXiv:2601.00486 derives states at fixed time using associative semigroups on the same 18 tables; its accessible full text does not present all-n joint single-site trace-language counts. Cervelle–Formenti–Guillon (STACS 2010) develops general traceability, not this exhaustive 18-rule cardinality table. A potentially overlapping submitted Fukś 2026 follow-up was identified but inaccessible; it creates a genuine priority risk, not automatic failure absent decisive coverage.

## value

PASS

Exact trace complexity and entropy are natural observational invariants distinct from global cellular-automaton entropy. The 18 semigroups are a complete classified finite family, and five exponentially rich traces versus thirteen polynomial/bounded traces demonstrates a structural distinction; the positive entropy of an absorbing-symbol rule is a nontrivial boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
