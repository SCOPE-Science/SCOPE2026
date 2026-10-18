---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

At fixed N, H_S=log N-(log Q)/N with Q=∏ a_i^{a_i}, and H_B=(log N!-log F)/N with F=∏ a_i!. Both are decreasing functions of exact positive integers Q and F, so every comparison can be exact. Integer partitions enumerate every unlabeled positive abundance profile; an independent enumerator and an independent dynamic-programming partition-count calculation agree at N=1,...,8 (counts 1,2,3,5,7,11,15,22). Exhaustive pair comparisons yield zero weak-order disagreements through N=6; at N=7 sole disagreement is (1,1,1,4) vs (2,2,3), Q=(256,432) F=(24,24), so not strict reversal; at N=8 exactly two strict reversed pairs (1,1,1,5)/(2,2,4) with Q=(3125,4096), F=(120,96) and (1,1,6)/(4,4) with Q=(46656,65536), F=(720,576). Checked exact integers, avoiding floating logs. The finite N≤8 search is exhaustive because the domain is bounded and partitions completely describe it.

## originality

PASS

Full classical comparison papers establish the formula and high similarity of the indices but do not provide this sharp finite ordinal boundary. Peet 1975 describes Brillouin approaching Shannon for large sample sizes; Palaghianu reports empirical near-perfect correlations. Closeness of values does not imply order equivalence. Searches for exact N=7 and N=8 partitions, multinomial-versus-weighted-power comparisons, or first reversed rank yielded no decisive prior coverage. An unindexed ecology classroom or software example may contain these small profiles; best-of-knowledge qualified PASS.

## value

PASS

Brillouin is an important finite-sample alternative to Shannon and often described as close to it; whether finite-count comparisons can reverse ranks is a substantive diagnostic question. The exact first weak mismatch at seven, first strict mismatch at eight, and exhaustive two-pair first strict layer are natural complete classifications useful as methodological and software test cases rather than arbitrary chosen vectors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
