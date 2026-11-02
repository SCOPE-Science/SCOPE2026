---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Janson Lemma 11 identifies tree permutations with L{L,R}^(n-2)R and characterizes inversions between marked positions by L..R with intermediary gap in L*, R* or R+L+. A finite marked-position scanner with six gap states per earlier mark gives 71 reachable states for 1243 and 45 for 1324, counting each increasing four-subsequence exactly once. Hence each total-count GF is z² times a rational 71/45-dimensional transfer expression. Its denominator degrees are <=71/45, and numerator bounds <=72/46. After multiplying the proposed difference by Q=(1-z)^2(1-2z)^3 and both denominator polynomials, the numerator has degree <=122; independent exact dynamic programming verifies all 123 coefficients 0..122 vanish except the prescribed 2 z^5 term. This establishes the all-n rational identity, not a finite extrapolation. Direct independent codeword and all-permutation enumerations independently corroborate initial coefficients. Positivity follows from the product of power series with positive coefficients and the asymptotic from the pole at 1/2.

## originality

PASS

Best-of-knowledge source/implication comparison: A counterexample to the stated extension cannot be equivalent to the existing positive theorem whose hypothesis explicitly requires tree patterns. General leading asymptotics and a coding construction do not dominate an all-n exact nonzero difference, so no implication from these earlier statements. All specific risks are retained; inaccessible literature alone did not determine the outcome.

## value

PASS

Explicit all-size counterexample to Janson Problem 7 finite-n equality extension from tree to forest patterns, at the smallest natural length four, with exact positive gap and a finite-state rational certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
