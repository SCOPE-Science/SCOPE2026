---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Syntax induction gives dependence on bits 0 through depth d, and monotonicity for the positive syntax. At a point on a t-cycle the positive formula's t-disjunct reads the predecessor in all its conjuncts, and every disjunct has a t-indexed conjunct reading that predecessor. Thus the LCM formula works uniformly. For a pair r,s attaining the maximum LCM L, the valuation with ones just at predecessor residues mod r is dominated by the valuation with zeros just at predecessor residues mod s up to index L−2; their first order violation is at L−1. This proves minimality and works on single cycles, hence also for the disjoint-union class. For n≥2, m=2n−2 bounds r+s−gcd(r,s) and max(r,s) for all allowed pairs. By Fine–Wilf the common prefix has gcd period and its positions r−1 and s−1 agree; a finite Boolean prefix disjunction gives depth m−1. The displayed n and n−1 blocks have a common prefix of length 2n−3 and opposite last bits, proving sharpness including n=2. Length 1 has predecessor equal to the root. Uniform substitution preserves the defining equivalence, not a separate lower bound for each fixed predicate substituted for p. Independent supplementary graph replay /workspace/branches/modal-residue-check.py used equality components and bipartite implications rather than valuation enumeration: 2080 pairs and 64 consecutive sets passed. The unbounded theorem rests on the proof, not this check. The frozen verifier was inspected, not executed.

## originality

PASS

Credit Fine–Wilf and positive modal simulation as prior ingredients. The supported distinct finding is the exact positive uniform depth for arbitrary finite length sets and, together with the Boolean benchmark, the quadratic-versus-linear gap for consecutive lengths. The strongest published-catalogue matches use a different frame relation, a different invariant, or a language without valuations; no checked source covers the stated uniform positive bottleneck.

## value

PASS

The question measures a natural succinctness cost of removing a primitive tense operator on a basic deterministic frame class. Arbitrary allowed periods have an exact, usable positive depth bound and defining formula, with a matching witness, while the Boolean comparison gives an asymptotically different optimal scale. This separation is more informative than an expressibility theorem or textbook periodicity alone. No claim about formula size or eventuality semantics is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
