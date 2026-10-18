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

Reconstructed four disjoint finite-field cases by choosing right-hand mth-power values for q≡1(mod m), counting (q−1)² + m(q−1)(q−m)² +2(q−1)(q−m−1)² +(q−1)(q−1−m)(q−2m)². Simplification yields asserted χ(q) for infinitely many good q and hence polynomial identity; Jacobson lattice good reduction follows for all but finitely many primes for fixed m. OS projectivized Poincaré identity gives b0..b3. Independently factored cubic discriminant into strictly negative −[3n^6+44n^5+292n^4+1040n³+1808n²+1408n+416], n=m−2, so irreducibly nonreal conjugate pair prevents free arrangement by Terao. Independent Sympy arithmetic checks verify original count and discriminant identity for small m and all polynomial coefficients, not replacing all-m proof.

## originality

PASS

Best-of-knowledge PASS: original four-cycle family and gain-graph machinery are prior, but explicit closed all-m characteristic polynomial, projective complement Betti vector and uniform non-freeness via discriminant are distinct evaluated claims. Search and full primary comparisons identify no same-family published closed evaluation.

## value

PASS

A uniform non-freeness theorem and explicit projective-complement topology for a natural published family containing a known Purdy counterexample are useful structural invariants. The family-specific cubic evaluation, especially its sign-uniform obstruction, is not merely the universal counting identity or a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
