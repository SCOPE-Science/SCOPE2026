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

The telescoping difference of floors gives N_j=⌊nα⌋ plus membership in the circular half-open interval [p_j−t,p_j), where p_j=(j+1)α and t={nα}. The frozen proof uses the indicator off endpoints, where the conventions agree; at a coincident event the exact half-open formula takes the state of the chamber immediately to its right, so there is no extra vector. The residual count follows by subtraction. Each captured nonempty proper block has uniquely determined adjacent gaps for the start and end; lifting around the block reduces the allowed start phases to an intersection of two intervals. Only empty and full subsets can recur in different chambers, once per gap strictly longer than t or 1−t respectively. The gaps consist of m−1 copies of α and one longer gap. At 1≤n<m there are exactly m−n coincident events and no repeated extreme chambers since both t and 1−t are at least α. For n≥m irrationality excludes all event coincidences, and exactly one extreme state repeats m times when t<α or 1−t<α, giving 2m−(m−1); otherwise all 2m states differ. Weyl equidistribution gives the two densities unchanged by removing small n. Independently, the alphabet is the collection of m-blocks of the binary Sturmian rotation coding by [0,α), read by lag, with at most one 1 per block. Sliding overlapping windows give a bijection between length-n factors and binary factors of length n+m−1, proving p_w(n)=n+m. Irrational minimality and the half-open chamber convention give the same language at every phase. Inspected the rational-proxy checker without running it; its bounded checks are not the proof for irrational slopes.

## originality

PASS

The ordinary factor complexity is inherited from a higher-block Sturmian presentation and is not the novel component. The distinct claim is the exact ordinary Parikh complexity of these higher-block alphabets for every m≥3, including the slope-dependent collapse and the density of its occurrences. Standard Sturmian m-Abelian complexity is a finer relation and does not count this quotient. The closest exact indexed results have different factor transformations or equivalence relations; the close prior rotation coding studied in the ternary case is outside the bound alphabet size. This is a bounded comparison, not a historical-priority certificate.

## value

PASS

A natural family of higher-block Sturmian codings has simple ordinary complexity but a different, slope-dependent identification when one retains only counts of overlapping windows. The exact collapse from 2m to m+1, its Diophantine criterion and positive occurrence densities answer a concrete quantitative question for every alphabet size in scope. This is not just the ordinary Sturmian count under a change of alphabet.

The dated certificate retains the supplied scientific assessment, sources and limitations.
