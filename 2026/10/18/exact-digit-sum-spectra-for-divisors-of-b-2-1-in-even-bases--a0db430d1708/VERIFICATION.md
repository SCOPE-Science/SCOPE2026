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

For even b≥2 and positive d|b−1, n=d(b+1), N divisible by n forces d|s_b(N) from b≡1 mod d and E−O≡0 mod(b+1) from b≡−1 mod(b+1). Since an odd u≤b−1 has nonzero odd E−O of absolute size <b+1, it is impossible. For sufficiency, A=∑_{j=0}^{2d−1}b^j has digit sum 2d and is divisible by d(b+1); B=b⁴+db²+(d−1)b+(b−1) has sum b−1+2d and is likewise divisible by coprime factors d,b+1. Concatenating the representations gives all even multiples of d and all odd multiples above b−1. There are ((b−1)/d+1)/2 gaps, largest b−1, density 1/d. Independent finite-state arbitrary-length search compared 364 target sums for tested small even bases/divisors; unbounded parameters follow only from proof.

## originality

PASS

Best-of-knowledge originality after actual semantic Resultary search and primary-literature comparisons. A full classification is strictly stronger than the earlier partial constraints; the additional odd branch is not an immediate instance of Theorem 2. Unread primary documents are not treated as not covering.

## value

PASS

The infinite natural family of divisors of b²−1 that contain b+1 answers a previously posed complete output-set question; the motivating decimal n=33 example is fully settled rather than supplied with only one missing value. An exact sharp finite hole set and b-independent last gap are useful number-theoretic invariants despite the elementary proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
