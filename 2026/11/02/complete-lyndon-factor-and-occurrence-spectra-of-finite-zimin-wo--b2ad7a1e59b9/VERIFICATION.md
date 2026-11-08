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

The ruler representation Z_n[p]=a_(1+ν2(p)) reduces nonsingleton Lyndon factors to odd-to-even aligned substrings. Every other starting or ending parity supplies an immediately smaller proper suffix. The doubled length-two code phi(a_j)=a1 a_j reflects lexicographic comparisons and preserves Lyndon status for lower-rank factors, giving an induction and explicit base case. Each occurrence of a_j is preceded by the exact Z_(j-1) central context, proving j endpoint suffixes; summing endpoint counts gives n(n+1)/2 distinct, 2^(n−i+1)−1 occurrences at each length 2^(i-1), total 2^(n+1)−n−2. The decreasing half-Zimin prefix factorization gives CFL. Independent direct suffix comparison at every endpoint ranks 1..7 exactly matched the theorem; this is a check, not all-n induction.

## originality

PASS

Badkobeh and Crochemore’s 2022 primary paper explicitly exhibits the diagonal half-Zimin Lyndon words Z_(i-1)a_i; those alone are prior and not claimed. The inspected Section 5 does not give all off-diagonal Z_(i-1)a_j, exclusion of other factors, endpoint-specific profiles or multiplicity spectra. General Lyndon complexity for automatic words and Zimin factor membership theory do not state the rank-dependent positional distribution. Resultary matching searches mostly return unrelated attractor profiles. Novelty judged for full combination only, with possible unindexed ruler/Lyndon suffix formulations documented.

## value

PASS

The exponentially long canonical Zimin words are standard unavoidable-pattern objects; an O(n²)-size full Lyndon-factor specification plus pointwise ending-suffix profiles, exact lacunary lengths and multiplicities is a motivated complete classification of a natural string combinatorics invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
