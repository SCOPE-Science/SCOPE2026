---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The append-letter recurrence F_{wc}(u)=F_w(u)+1_{u=vc}F_w(v) exactly partitions scattered-subsequence occurrence choices, so all 2^n binary words for n=2..14 and all their nonzero subwords are exhaustively handled by finite integer dynamic programming. The inspected verify.py explicitly loops product(01,repeat=n) for each n, checks no n≤13 exception and exactly four n=14 strings, confirms unique maximizers. The word 01010001110101 has unique most frequent subword 01001101 (length 8) with 144 occurrences versus maximum 136 for lengths≤7, directly refuting the half-length conjecture. Independent binary exhaustive recomputation for every word n≤14 and independent mask recomputation on two witnesses corroborated the source; computation is finite *exhaustive*, not an extrapolation to n>14.

## originality

PASS

Fang revised Conjecture 5.7 explicitly asserts the existence of a maximally frequent scattered subword of length≤ceil(n/2) for every word; the counterexample disproves that published conjecture and adds exact binary minimal length and four-exception census. Fang measures minimum entropy or partial experimental cases, not this complete binary every-word census. Menon–Singh study occurrence frequency of fixed patterns, not the length of an argmax over patterns in fixed ambient words. Resultary binary absent-subsequence and universality records concern different invariants.

## value

PASS

A rigorous smallest counterexample to a published nontrivial universal word-combinatorics conjecture is valuable; exact minimal length and four-example symmetry classification rule out accidental tiny counterexamples and provide a reproducible sharp boundary. The result does not purport to classify all longer/nonbinary words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
