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

The semantic input is expressive completeness for weak ideals on the fixed labelled valuation domain, for support only. A nonempty finite weak ideal contains its union U by binary closure. Convexity then makes it an upset inside P(U), and every nonempty upset of P(U) has maximum U and is a weak ideal globally. The empty family counts once and is globally upward closed; the nonempty globally upward-closed families are exactly the layer U=V. This gives both counts including k=0. Dedekind numbers are nondecreasing by embedding upsets with extra coordinates ignored, so the tail from k≤N−2 is at most 2^N M_{N−2}. At even N the middle coefficients at N, N−1 and N−2 have successive ratios tending to 2 (the first ratio is exactly 2). The established estimate log₂ M_m∼binom(m,⌊m/2⌋) thus makes the log gaps of order B_N, which dominates N. This yields the first-order equivalents, the −B_N/2 logarithmic rate, and conditional probability N(M_{N−1}−1)/E_N→1. A separate exhaustive direct classification for N≤4 and arithmetic at N=8 reproduced the reported values (python3 /workspace/reproductions/frozen_checks.py 2). The N=8 check uses published Dedekind inputs, independently read in OEIS A000372; it is not a new enumeration of M_8.

## originality

PASS

Credit the prior weak-ideal semantics, maximum-team representation, and Dedekind estimates in full. The exact census is a direct enumeration using that representation. The distinct contribution supported here is the quantitative BSL rarity law as a synthesis: a relative-error equivalent for the entire exceptional count, a logarithmic exponent, and concentration of the defect on the one-omission layer. It requires connecting and controlling the strata, not just quoting the estimate for a single Boolean lattice. None of the inspected statements already gives or dominates that quantitative conclusion; historical priority is not certified.

## value

PASS

Uniform sampling of labelled semantic classes has a well-defined distribution independent of syntax or a choice of formula length. The probability statement is more informative than the census alone: the logic admits non-upward meanings, they occupy an asymptotically vanishing fraction at an explicit rate, and almost all exceptions have precisely one missing valuation in their largest supporting team. These are useful facts about the semantic space; they do not imply analogous syntactic or full bilateral sampling laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
