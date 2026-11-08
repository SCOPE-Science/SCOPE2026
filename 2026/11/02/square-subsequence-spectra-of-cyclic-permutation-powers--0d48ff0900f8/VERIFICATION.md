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

For a target a1...aL in infinite repeated increasing permutation, greedy earliest embedding uses one initial period plus one new period exactly at each weak descent a_{i+1}≤a_i; greediness is optimal. A square uu therefore costs 1+2r(u)+s(u) periods, giving a necessary/sufficient criterion for every q≥2,k,m≥1, including k=1 and equality. The weighted cyclic weak-descent trace tr(M(z²)^{m−1} M(z)), M(t)=(1−t)U+tJ, has rational generating function via nilpotency of strict-upper U and rank-one determinant/inverse formula. For extremal roots |u|≤q floor(k/2) by symbol multiplicities; cyclic increasing runs have length≤q, forcing d=r+s≥floor(k/2), equality only the q rotations of full-period words and exactly one even-k admissible rotation. Independently enumerated literal host square subsequences and criterion for (q,k)=(2,7),(3,4),(4,3), including q=3,k=4 spectrum (3,9,17,15,6,1); no finite cutoff mistaken for all-parameter proof.

## originality

PASS

Inoue/Inenaga/Bannai's general longest square subsequence algorithms solve a different optimization problem on arbitrary input strings, not count all distinct square roots of periodic ordered hosts. Bannai–I–Köppl give periodic-subsequence algorithms; shuffle-square theory uses an interleaving rather than concatenated square. The exact all-q rational length enumerator and extremal root multiplicities were not identified in those earlier main results. An unindexed special-host formula remains possible.

## value

PASS

The repeated increasing-permutation word is a canonical structured host; an exact necessary/sufficient subsequence-square criterion, rational bivariate spectrum and precise longest-root multiplicity solve a complete and motivated discrete-word enumeration, not a mere implementation of a general LSS algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
