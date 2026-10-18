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

For n=2..11 the source consists of binary words with length>=2 leading/trailing zero runs, singleton one runs, and at least two zeros between ones. Independently generated all source words, formed each distinct length-(n-1) deletion shadow and built the compatibility graph. Exhaustive recursive clique enumeration returned source cardinalities 1,1,1,2,3,4,6,9,13,19, exact optima 1,1,1,1,1,1,2,2,3,4 and labeled maximizing-code counts 1,1,1,2,3,4,1,6,3,3. At n=11 exactly three maxima exist; absence of clique size five is certified by complete 19-word compatibility-graph enumeration, not a heuristic. Their displayed codewords are compatible. Distinct shadow intersections are equivalent to LCS length >= n-1. No all-n statement was inferred.

## originality

PASS

Kulkarni-Kiyavash prove a general constrained-source fractional matching bound and use exactly the strict endpoint-run convention, but do not in their Section V supply the exact n<=11 maxima or the three equality cases. Subsequent RLL synchronization constructions address code families and asymptotic rates rather than these exact small-block optimum multiplicities in searched sources.

## value

PASS

The full initial exact profile through first attainment of size four, with all three n=11 maximizers and reversal symmetry, sharpens a natural but loose published upper bound (integer <=7) to exactly 4. It is a finite but complete and reproducible exact coding-theoretic benchmark under a specific physically motivated constrained-source convention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
