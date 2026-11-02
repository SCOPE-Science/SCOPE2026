---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed actual frozen RESULT.md (all definitions, length/letter quantifiers, positive-law necessity, and L=1/n<L boundary). For a cross-bifix-free equal-length code, starts closer than L cannot co-occur, whereas starts at least L apart use disjoint independent coordinate blocks; expanding E ∏(1+(z−1)I_i) gives exactly the weighted independence polynomial of the (L−1)-power of a path with weights a_i=P(I_i=1). Neighbor sets split into left/right cliques, hence this graph is claw-free. The published Chudnovsky–Seymour theorem (checked through Bencs Theorem 1.8 complete proof) applies to the nonnegative weighted case through rational clique blow-ups and coefficient limits, and all roots of normalized nonnegative PGF are ≤0, forcing a Bernoulli-product factorization. For a bordered word with shortest period s, at n=L+s the unique possible overlap is starts 1 and s+1, no triple is possible; E N=(s+1)π and P(N=2)=π²/h. A quadratic PGF is PB iff real rooted; direct discriminant Δ=π²((s+1)²−4/h), giving h≥4/(s+1)². Making one shared-prefix letter rare while retaining strictly positive other letter probabilities forces h→0, proving converse. For iid code probability a, k legal start placements are exactly binomial(n−(L−1)k,k), giving stated full PGF. Independently enumerated all 3^8 ternary words for a nonstationary cross-bifix-free 2-code, exact rational agreement; earliest-overlap direct enumeration for four overlapping binary motifs at three positive iid biases each; iid n=11 stationary full four-mass distribution. These finite tests corroborate but do not prove the arbitrary-n theorem.

## originality

PASS

Best-of-knowledge PASS for the complete universal border iff theorem with nonidentical-source and cross-bifix-free sufficiency and the sharp first-overlap converse. The Chudnovsky–Seymour/Bencs real-rooted claw-free polynomial theorem is clearly pre-existing and supplies the main nonstandard algebraic implication; Wang–Wang's exact generating-function treatment already supplies fixed-code uniform-source avoidance formulas and makes the stationary placement enumerator unsurprising. Neither original source was found to establish the full universal Poisson–binomial representation for arbitrary independent source marginals nor the necessity and discriminant criterion for all literal words. The published equivalent formulations were checked mathematically, not only by title; lack of a search hit is not conclusive priority evidence. Residual risk from unindexed classical exact word-pattern literature remains.

## value

PASS

The word border is a natural combinatorial obstruction to nonoverlapping occurrences, and Poisson–binomial representability is a meaningful exact structural property of dependent local-pattern counts. The theorem gives a complete infinite-family iff classification over all n and all independent, potentially non-identical source marginals, a strictly positive-iid necessary counterlaw for every self-overlapping word, and a sharp first-overlap parameter threshold. Cross-bifix-free code sufficiency expands the class of natural word patterns to nonstationary sources. Stationary placement enumeration is related to known avoidance formulas, so the primary value is the distributional real-rootedness/if-and-only-if bridge and sharp converse, not counting a known table again. This supplies exact input for pattern probability, Bernoulli-sum concentration/shape results and diagnostics; it is neither an arbitrary finite slice nor a routine renaming of an already stated word-count theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
