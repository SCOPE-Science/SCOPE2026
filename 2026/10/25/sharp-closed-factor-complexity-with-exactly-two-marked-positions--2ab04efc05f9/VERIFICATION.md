---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS. Exhaustively classify closed factors by 0,1,2 marker occurrences and number of internal proper-border occurrences. Closed palindromes contribute exactly n; other closed factors have two markers and unequal outer gaps i!=j with i<=min(a,b),j<=min(b,c), giving max(A,B)(min(A,B)+1). Optimization over p<=q, p+2q<=n-2 gives exact 3-residue piecewise maxima and complete maximizing gap triples. The simplex Riemann integral gives mean n²/36+O(n). Independently brute-enumerated the entire set of distinct closed factors for all 680 words length 2..16 with exactly two 1s; verified boundary n=2,3 and maximizing tuples. This finite test alone would not establish all lengths, which use the factor argument.

## originality

PASS

PASS best-of-knowledge for all-length formula at EXACT Hamming weight two, its precise optimizing zero-gap triples, and the minimal fixed minority support for quadratic closed-factor growth. Unrestricted quadratic constructions/finite tables exist but do not mathematically supply this complete restricted classification.

## value

PASS

PASS. A complete exact closed-factor count for every binary word with two occurrences of one letter, all extremal configurations, and a sharp two-marker transition to quadratic complexity is a natural structural refinement of a widely studied word-complexity invariant. This is neither merely a small census nor an arbitrary unmotivated numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
