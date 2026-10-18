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

The prefix property is factorial for richness and additive-cube-freeness. On extension by a symbol, all new cubes end at the last position and are exactly those equal integer-sum triples checked with prefix sums; preservation of richness is equivalent to introduction of one previously unseen palindrome as longest palindromic suffix. To avoid dependence on packaged palindromic-tree implementation, wrote and compiled an independent C++ DFS with explicit suffix-palindrome string matching and a set of all previously occurring palindromes. It explored all 404535 admissible prefixes, independently recovering N(100..105)=(90,80,36,12,8,0) and the eight explicit length-104 words. An independent Python orbit check verifies reversal and a→2−a preserve those words and form exactly two four-word orbits. Any longer word would have an admissible 105-prefix, which the exhaustive search rules out; not an extrapolation from finite prefix samples.

## originality

PASS

Andrade–Mol, arXiv:2408.15390v2 (full relevant sections read), treats rich ternary words avoiding abelian cubes; the published longest such word has length 180. Weighted additive-cube-freeness is strictly stronger than abelian-cube-freeness: equality of Parikh vectors implies equal sums but not conversely. Theorem 1.2 in Andrade–Mol on infinite additive-fourth-power-free rich words does not bar additive cubes. Thus neither published 180 nor fourth-power avoidance implies 104, eight words or two orbits. Resultary rich-word retrievals and exact 104/8 web searches returned different word properties, not this census. Priority is best-of-knowledge, not proof of global novelty.

## value

PASS

An exact extremal threshold for naturally defined palindromically rich ternary words under additive cube avoidance settles a mathematically motivated finite endpoint absent from the nearby abelian-cube classification. The eight explicit equality words and reversal/complement orbits are usable as tests of structural hypotheses about rich avoiders. It is neither arbitrary alphabet reweighting nor recomputation of the different 180 bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
