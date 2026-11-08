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

Work in truncated free noncommutative Q-algebra and map each word w to ∏(1+X_letter). Coefficients exactly count scattered subsequences up to degree r. The difference between μ^j(0), μ^j(1) has first nonzero homogeneous degree j+1; induction uses the commutator with X0+X1 and a nonzero coefficient. Every proper prefix offset d=2^v e with odd e separates the two source-letter block profiles in degree v+1≤r, since complementary length-e prefixes have unequal zero counts. For nonaligned adjacent windows the profiles are H_a^−1 Q^M H_b and H_b^−1 Q^M H_c, and unipotent constant-one conjugation cannot invert a nontrivial E since the first nonzero homogeneous component changes sign. Hence equality iff a=b=c, while aligned windows always agree. Independently checked 7,728 arbitrary-source cases across r=1..3, source sizes 3..6, all available multiplier/offsets using direct scattered-subsequence profile counts. The proof rather than finite tests applies to every source and M. Dyadic Thue–Morse phase corollary is already covered by prior fixed-point work and is NOT asserted original.

## originality

PASS

PASS only for the main arbitrary-binary-source, arbitrary-positive-block-multiplier three-letter characterization, with explicit prior coverage of the restricted Thue–Morse fixed-point corollary by Lejeune–Leroy–Rigo Theorem 48. Their fixed-point theorem and Lemma 30 do not imply the fully source-uniform law as stated. Additional morphism-profile algebra literature could contain an equivalent general transfer lemma; retain this priority risk.

## value

PASS

PASS. A simple local trichotomy (alignment or equality of three boundary source bits) completely decides r-binomial equality of adjacent length-M2^r windows for every binary source and integer M, despite arbitrarily long intervening source substrings. The noncommutative conjugation obstruction is a structural mechanism, giving an infinite all-source theorem rather than only finite Thue–Morse factor statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
