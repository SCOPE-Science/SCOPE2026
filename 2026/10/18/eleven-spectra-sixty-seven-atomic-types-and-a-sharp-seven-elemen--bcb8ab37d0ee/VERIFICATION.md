---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Partition every interpretation into four nonnegative cells (a,b,c,d). All 64 ordered-noun atomic truth values are fixed by the four cell-positivity bits and signs of s=b−c, t=a−d, s+t, t−s, and conversely those data are recoverable from the atom truths. Classifying supports for (b,c) and (a,d) gives 2 zero-difference support patterns and four nonzero ones per pair, with three relative nonzero magnitude orders, hence 2·2+2·4+4·2+3·4·4−1=67 types after excluding the empty universe. Compress nonzero |s|,|t| to 1,2 preserving signs/order and each positive baseline, giving |M|<=4+3=7 for every type. Requiring four nonempty cells plus s>=1 and t>s forces |M|>=7, realized at (3,2,1,1). Jiang’s unrestricted-vocabulary spectrum-shape theorem yields only ordinary or even tails; the sharp size-7 bound restricts candidates to empty, T1..T7 and E2,E4,E6. The given explicit cell constructions realize all candidates and upward/even extensions. Independent full atomic semantic verification up to size 18 finds 67 types, with minimum-size histogram (4,6,16,9,20,4,8). The all-size reasoning relies on symbolic cell compression and Jiang’s theorem, not finite extrapolation.

## originality

PASS

Jiang’s 2026 unrestricted vocabulary spectrum theorem already supplies the general tail/even-tail shape, and one-noun exact spectra are published. The assessed contribution is the sharp two-noun finite bound, 67 precise complete atomic types and exhaustive eleven-spectrum realization; neither follows merely by specializing Jiang’s theorem without a new sharp bounded model reduction. Best-of-knowledge with Moss full-text risk.

## value

PASS

The exact expressive power of two noun variables in finite cardinality syllogistic is a natural small-vocabulary classification problem, with a sharp model-size cutoff, complete atomic type count, and precise spectrum list. These invariants govern finite satisfiability and distinguish the jump from one noun; the result is not merely restating Jiang’s unrestricted spectrum-shape theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
