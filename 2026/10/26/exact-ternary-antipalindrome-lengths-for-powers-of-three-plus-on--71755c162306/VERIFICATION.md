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

For N=3^n+1, n>=1, reconstruct digit-complement definition and ternary carry count: antipalindrome length equals digit sum; two-summand digits force lengths n and n-2 and a single carry transition. Length gaps >=4 and same-length pair except n=2 are impossible. Complement symmetry forces unique alternating middle digits for even n>=6 and excludes odd n. Verify explicit B_n=3^(n-3)+1+2 sum_(j=1)^(n/2-2)3^(2j), A_n=3^n+1-B_n, and 3-summand 1+U_n+V_n, with n=1,2,4 boundaries. Independently generated all admissible ternary antipalindromes up to N=3^16+1 and exhaustively counted unordered two-sums for n=1..16: exactly claimed H values and unique pair whenever two summands possible. Only the symbolic carry argument proves all n.

## originality

PASS

A primary full-text check finds the antecedent ternary antipalindrome three-summand assertion only as a conjecture, with a finite scan through five million. Neither it nor nearby published Resultary palindrome/word-attractor work determines the infinite exact sequence, parity break, and unique representations. No equivalence or stronger theorem was identified, subject to unindexed historical work.

## value

PASS

The powers-of-three-plus-one sequence is a canonical boundary family for base-three complementary-digit additive decompositions; obtaining the exact least summand number and uniqueness for all indices resolves a motivated infinite phase pattern beyond a finite check or a mechanical reformulation of the three-summand conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
