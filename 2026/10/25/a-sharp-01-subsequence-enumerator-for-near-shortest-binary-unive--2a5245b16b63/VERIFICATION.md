---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For binary words, the greedy shortest-complete-arch count equals k-subsequence universality index. Composition (k+1 zeros,k ones) and length 2k+1 force exactly k full arches, each with one 1, with either k two-letter 01/10 arches and trailing 0, or k arches and no suffix with exactly one length-three arch necessarily 001. The first contributes z^C(k,2)(1+z)^k; the second contributes z^C(k,2)(1+z)^(k-1) sum_{j=1}^k z^(k-j+2). Factoring gives stated polynomial, and its convolution coefficients, symmetric support 0..2k, three-point maximum and total follow algebraically. New exhaustive fixed-composition enumeration independently verified each coefficient for k=1..8, with explicit all-pattern universality cross-check k<=4. These finite checks do not replace the all-k structural proof.

## originality

PASS

Best-of-knowledge original exact q-enumerator of a natural first-redundancy fixed-composition class, not original greedy arch criterion or unrefined count. Closest 2026 primary paper gives existence/all index questions for fixed Parikh matrices; original 2025 partition work counts all fixed-01 words, not those that are subsequence universal.

## value

PASS

A complete coefficient distribution for a canonical first-redundancy universality layer, refining previously known unweighted counts by the natural scattered pair statistic used in Parikh matrices. The polynomial yields exact support, a symmetric unimodal law and sharp plateau; not an arbitrary numerical slice, and its exact self-contained classification does not require a larger theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
