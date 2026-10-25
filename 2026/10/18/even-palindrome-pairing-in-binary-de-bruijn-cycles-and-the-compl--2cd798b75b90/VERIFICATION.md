---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For every n>=2 binary de Bruijn Euler tour, the two in-edges at a (n-1)-word v pair bijectively with its two out-edges. Palindromes of length n+1 centered on palindromic v are precisely fixed points of this binary permutation; it has zero or two. Constant v must use a swap, otherwise the constant n-bit edge is an isolated one-cycle, impossible for the unique Euler tour. Thus each nonconstant palindrome center contributes both 0v0 and 1v1 or neither, giving an even count bounded by 2(2^ceil((n-1)/2)-2). At order five the only possible pairs are A={001100,101101} and C={010010,110011}. Exhaustive independent enumeration of all 2^16=65536 local successor bijection choices, testing exactly one 32-cycle, reproduces the full profile histogram empty:768, A-only:512, C-only:512, both:256, total 2048. Pair-indicator covariance equals 256/2048-(768/2048)^2=-1/64. This finite exhaustive test proves only order-five multiplicities; the all-order pairing follows separately from the Euler tour argument.

## originality

PASS

The Euler-tour de Bruijn representation and count of 2048 order-five cycles are classical. Anisiu et al. discuss palindromic subwords of de Bruijn constructions and general palindrome bounds; inspected passages do not provide the fixed-cycle local binary pair law plus the complete four-set order-five distribution. Successor-rule, unoriented and reverse-complement primary sources address different invariants or selected cycles. Existing order-three, order-four expectation and order-five longest-palindrome results do not imply this joint membership spectrum; residual priority risk remains.

## value

PASS

Length n+1 is the first factor length whose occurrence is not forced by de Bruijn universality. The binary Euler-transition involution gives a general structural constraint, while the complete order-five census quantifies nonindependence of two natural palindrome-center events. The result is an exact self-contained natural spectrum, not an arbitrary slice or a known count recited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
