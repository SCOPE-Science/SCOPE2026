---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The substitution recurrence gives p_i = ν₂(i+1) mod 2 and every 1 has its own preceding zero. Selecting those pairs gives (01)^r as a subsequence; length r is universal and 1^(r+1) is absent. Any candidate of length r+1 containing adjacent 01 fits in r pairs by using one pair for that 01, so only 1^a 0^(r+1−a) need be tested. For a≤r the earliest a ones leave r−a mandatory inter-one zeros plus any surplus and terminal zeros. Failure occurs exactly when no surplus or terminal zeros remain. At a last 1 this gives one additional SAS plus one per consecutive terminal singleton zero gap. For 4|n with odd valuation, positions n−2 and n have valuation parity odd in one-based indexing, but n−4 has valuation 2; the terminal run length is 1. For n≡2 mod 4 and n>2, n−4 always gives a 1, and n−2 gives a 1 precisely in the odd valuation case, where n−6 has valuation 2; the run length is 2 or 0. When the last bit is 0 only the pure-one SAS survives, including n=1. W₂=01 gives exactly 00,10,11. The valuation classes have densities 2^(-h−1), and summing them is justified by a vanishing tail bounded by the density of multiples of 2^H. The n=4q+2 family has odd ν₂(n−2) for one third of q, giving density 1/12 for four SAS and 1/6 for two; multiples of four ending in 1 give 1/12 for three, and the remainder 2/3 for one. No certification is asserted. Separately, `python3 /workspace/branches/frozen_review_checks.py` compared the exact minimum failure length and all SAS via a greedy next-letter automaton at every length 1–2048; this is bounded corroboration, not the all-length proof.

## originality

PASS

The supported scope is the explicit all-prefix SAS sets and their four natural-density classes, not the general SAS theory, valuation coding, or an isolated dyadic formula. No equivalent or dominating result was established in the inspected sources. A later catalogue record has exactly the dyadic restriction, a material but narrower overlap.

## value

PASS

The shortest missing scattered words are a natural fine invariant of prefix universality, more informative than the number of arches. The result answers all prefix queries without testing candidate words and distinguishes four sharply different count regimes, with an exact frequency law, on a canonical automatic word. The finite witness bound four and distribution require the arithmetic structural calculation, not a benchmark at an arbitrary cutoff. It does not claim comparable results for arbitrary factors or universal probabilistic behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
