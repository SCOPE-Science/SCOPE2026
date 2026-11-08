---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For each r>=4, the cyclic (r+1)-uniform morphism a->a^r(a+1 mod3) generates all nine letter-adjacency pairs, so every length-(r+1)^m factor can be placed in a concatenation of two level-m blocks. The weighted maximal factor has a general upper bound r*max_a W_m(a)+H_m; the nesting of a maximizer and the two possible ordered block boundaries gives equality for all real letter weights, hence the exact recurrence for the number of zero-count values. The letter-count vector evolves by rI+C; the cyclotomic eigenangle is irrational modulo pi because its twice-cosine is rational but a noninteger algebraic integer were it rational. Modulo two, at m=3t a unique exceptional letter parity makes the range gap even precisely when the irrational rotation visits a fixed proper arc, a nonperiodic word. A k-regular sequence modulo a fixed positive integer is k-automatic, and a k-automatic sequence evaluated at k^m is eventually periodic, contradicting this parity subsequence. Independent enumerations verify the finite base cases only.

## originality

PASS

The closest Allouche et al. 2026 paper proves a 2-automatic/4-automatic nonregular abelian-complexity example at the fixed repetition count r=3, and the present theorem treats all r>=4 via a new uniform induction and parity reduction. Rigo–Stipulanti–Whiteland 2024 positive result assumes Parikh-collinear rank-one incidence, whereas rI+C is full rank and is not covered. A key originality limitation is that the complete 2026 primary text was inaccessible in this audit, so no claim is made that its entire Remarks/Appendices have been excluded; the checked abstract and mathematical implication comparison support a qualified best-of-knowledge O judgment.

## value

PASS

The relevant source asks for nonregularity beyond its first fixed repetition count; the general r>=4 family covers all uniform lengths >=5 and requires a nontrivial weighted-window induction and a parity argument uniform across even and odd r. It provides a systematic boundary for automatic words and abelian-complexity regularity, without pretending to classify all codings or alphabet sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
