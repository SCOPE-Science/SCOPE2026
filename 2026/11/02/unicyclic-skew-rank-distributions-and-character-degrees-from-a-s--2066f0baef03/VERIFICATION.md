---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Proof checked: each support has (q−1)^|F| weights and rank at most twice its maximum matching. Pfaffians for a unicyclic graph have at most two terms, because symmetric difference of perfect matchings is the unique even cycle. If an extremal matching does not internally match the entire cycle, a unique-monomial maximal Pfaffian remains nonzero; otherwise all maximal Pfaffians share the same two-cycle product difference. Exactly 1/(q−1) of full-support assignments cancel, and removing endpoints of a cycle edge preserves a unique-forest Pfaffian one rank-step below. Orbit-method count for odd fields follows from radical dimension n−2j. Independent brute weighted rank enumeration matched the formula on 4-cycle and triangle-with-leaf for q=2,3. No representation claim for q even.

## originality

PASS

Rossmann Section 1.6 introduces exact character-degree rank counts as Question 1.10; Resultary provides precise tree and cycle formulas. Neither special family alone covers arbitrary unicyclic with attached trees, since identifying forced cycle-saturated maximum matching supports is additional. Li–Yu Theorem 4.2 concerns unweighted ±1 orientations and individual ranks, not all field weights/rank multiplicities; still near overlap warrants note.

## value

PASS

Rank/character-degree distributions are natural representation-theoretic invariants; the single cycle cancellation gives a closed exact formula for an entire graph class extending motivating tree and cycle cases, with all fields for ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
