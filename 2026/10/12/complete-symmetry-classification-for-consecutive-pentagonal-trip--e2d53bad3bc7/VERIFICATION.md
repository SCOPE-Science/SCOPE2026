---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Reconstructed pentagonal differences and gcd(A,B)=2 iff n≡3 mod4, gcd(B,C)=2 iff n≡2 mod4, gcd(A,C)=5^[5|n]7^[n≡5 mod7]. Correctly separates redundant generators n=2,5. Herzog three-minimal-generator symmetry criterion restricts possible gluing to a nontrivial pair gcd and remaining scaled membership. Pair (A,B) leaves n=3 versus 7; pair (B,C) none; outer pair d∈{5,7,35} bounded by explicit sum-of-coefficients inequalities to n<11,15,71, respectively, and congruence exclusions leave n=40. The relation 2501=7·68+27·75 proves n=40. Independent exact Apéry Dijkstra computations for all 2≤n≤124 confirm only 2,3,5,40 and reproduce each exact F and genus. The universal exclusion is algebraic, not inference from this finite check.

## originality

PASS

The 2002 OEIS A069757 database predetermines the listed Frobenius values including n=40 but not symmetric indices or genera. Fel proves a general three-generator criterion and Fibonacci/Lucas-specific classifications, not the all-index consecutive pentagonal classification. Applying the criterion requires new gcd congruences, global cutoff and exceptional verification rather than a direct substitution of a ready-made parametric result.

## value

PASS

A natural classical consecutive polygonal-number semigroup family exhibits a rare last symmetric index at 40; locating all exceptions and proving finite cutoff with exact Frobenius/genus values is a motivated infinite arithmetic classification, not a renamed textbook two-generator case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
