---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The Gaifman degree of a successor path is at most two, so effective bounded-degree Hanf locality gives a radius and count cap for each fixed rank. Short endpoint balls are fixed by the two length-(2r+1) boundary words; full balls are binary windows. Each interior pattern has linearly many independent disjoint trials in the seed, each of fixed positive success probability. A binomial tail and union bound give simultaneous saturation except with exponentially small probability. Reversal permutes the full-window types; internal seams can only add to a saturated count. For n>2(2r+1), equal endpoint signs use disjoint seed windows, whereas opposite signs give a uniform window and its reverse. Couple the exact boundary laws before discarding the marginal failure probabilities; this proves exponential rank-theory TV even across different fixed copy counts. A long inserted block containing all patterns repeatedly gives a computable representative for each admissible boundary pair. Uniform averaging gives dyadic values, and prefix tests realize all dyadics. Endpoint bit equality separates the two phases; injectivity of the first block gives TV exactly 1−2^(-(m−1)n) for full words. Independent bounded replay passed 336 endpoint cases, 196 injectivity cases, 36 full-word-TV cases and 16 capped-local-profile comparisons.

## originality

PASS

The locality tool, independent-word comparison law, and support-size TV identity are not claimed as standalone contributions. The distinct content is the exact two-phase law for fixed signed repetitions, the attainable spectrum in each phase and the quantitative difference between local theories and the entire distribution.

## value

PASS

The signed repetition operation is natural and enforces macroscopic dependence invisible to each fixed logical rank except for exactly one endpoint distinction. The result supplies a complete phase classification and a uniform-in-sentence-at-fixed-rank comparison, even while full distributions become nearly singular. Neither the dyadic spectrum nor the TV calculation alone is the asserted value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
