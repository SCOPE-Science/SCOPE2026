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

PASS: A binary word with at most two ones becomes a palindrome after removing at most one pure-zero end block, giving palindromic length <=2; splitting just before the last one gives the bound 4. Palindromicity of all three ones requires a=d,b=c; two-palindrome factorization either contains a three-one palindromic core (b=c) or separates one and two ones, forcing b=a+d or c=a+d. If b!=c and both outer zero gaps exceed both inner gaps, any palindromic prefix and suffix containing a one is impossible, and at most three factors would require an impossible three-one central palindrome. Otherwise a palindromic prefix containing one or two ones followed by a <=2-marker suffix yields at most three factors. Counting four-factor configurations with max inner gap m>=1 and unequal inner gaps, external a,d=m+1+nonnegative, gives the rational generating function. Its dominant pole order 4 has coefficient 1/6, yielding n^3/36 and fraction 1/6. Independently computed word-level palindrome DP checked 2,401 four-gap quadruples (0..6) and every length-three-to-14 weight-three word and the generating function coefficients. Finite checks support, not replace, the all-gap proof.

## originality

PASS

PASS: The invariant of palindromic length is classical. Ravsky supplies global worst-case K(n) and averages over all binary words, not a complete gap-by-gap fixed-weight-three classification. Frid, Puzynina and Zamboni study lengths of factors of infinite words. The present exact stratification and 1/6 sparse-weight density were not in the inspected primary statements; the length-eight global maximum itself is prior and not separately claimed as new.

## value

PASS

PASS: Weight three is the first sparse binary class that exhibits the fourth palindromic factor and thus a motivated threshold rather than an arbitrary finite length slice. The sharp four-gap inequality, complete 1/2/3/4 case split, rational counting generating function and limiting one-sixth density give a full natural combinatorial classification not implied by a generic factorization algorithm or the prior global K(n) table. The result is self-contained but does not pretend to solve the full palindrome-factorization problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
