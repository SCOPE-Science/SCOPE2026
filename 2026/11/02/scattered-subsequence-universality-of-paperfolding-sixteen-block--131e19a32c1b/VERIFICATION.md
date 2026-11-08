---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Checked the precise 16-letter block B(x,y)=1101100x1100100y, arbitrary x_j and y_1..y_{q-1}, fixed terminal y_q=1, q>=1. The greedy-subsequence endpoint transition is monotone in its start position. The bounded six-input local lemma exhausts 64 binary inputs in four initial and eight subsequent bit contexts, yielding exactly two paths to the extremal next-block endpoint and a strict >=2-position gap otherwise; a prior subextremal path cannot catch up. Induction doubles the extremal count to 2^q at length 6q. Since the prefix ends in 01, both binary extensions from any nonterminal endpoint can be embedded, whereas both extensions from each extremal endpoint fail: universality 6q, shortest-absent count 2^(q+1). Arithmetic odd-part paperfolding fixes 14 symbols of each 16-block and f(2^k)=1, so q=2^(k-4) and the dyadic formulas follow. Independently implemented greedy automaton and enumerated all 170 free-bit assignments over q=1..4, agreeing in all cases; the local finite lemma plus induction proves the universal result, not the finite q checks. Evidence: Source text in assigned RESULT.md §§Finding, Assumptions and scope, Proof, Verification, Relationship to prior work; repository Git tree 952b6b1174833e9d1fc7560839a9bd13b7a17035

## originality

PASS

Best-of-knowledge novelty of the exact final quantitative claim, with classical proof mechanisms and expressly credited subcases excluded. Genuine broad/theorem and full-text comparison risks retained; inaccessible full texts alone do not dictate failure.

## value

PASS

The dyadic paperfolding word is a canonical automatic sequence, and scattered-subsequence universality and shortest-absent-word multiplicity are natural algorithmic and combinatorial invariants. A single local transfer mechanism yields exact exponential counts uniformly for an infinite, nontrivial 16-block class and all dyadic prefixes. This is finer than generic absent-subsequence algorithms or contiguous-factor complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
