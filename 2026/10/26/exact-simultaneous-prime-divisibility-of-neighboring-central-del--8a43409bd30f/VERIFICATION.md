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

The identity D_n=sum_k binom(n,k)^2*2^k yields digitwise D_n≡∏D_(n_j) (mod p) by Lucas/Fermat. For prime p>=5, 0,1,p-1 are allowed digit residues. Let a=p-|Z_p|, c=#adjacent allowed digits d,d+1 for d<=p-2. Among 0<=n<p^L, the count I_L of pairs both nonzero satisfies I_0=1 and I_L=c*a^(L-1)+I_(L-1) because d=p-1 carries to an allowed zero digit and recurses. Hence simultaneous zero count is p^L-2a^L+1+c(a^L-1)/(a-1), including the endpoint n=p^L-1 via D_(p^L)≡D_1. For p≡3 mod4, m=(p-1)/2 odd, the involution x→2-x negates f=x(x-1)(x-2), while the coefficient of x^(p-1) in f^m equals (-1)^m D_m; finite-field power sums force D_m≡0. Thus a<p and each such fixed p divides gcd(D_n,D_(n+1)) on a density-one set; finite products of infinitely many p≡3 mod4 give gcd>B on a density-one set. Independent direct integral recurrence tested the exact p and p² counts for primes 5,7,11,13,17,19 up to n<500; confirmed Z7={3}, the 7² count 6. The proof alone establishes all p,L. An additional independent direct integer recurrence counted 84 adjacent multiples of seven below 7^3, exactly as the formula predicts.

## originality

PASS

Noe (2006) Theorem 8.5 already gives the all-digit one-point p-divisibility criterion for generalized central trinomial numbers (including Delannoy), and this is fully credited. Inspected source neither formulates consecutive-index carry counts nor the density-one unbounded neighboring gcd. The present joint distribution and the use of a forbidden midpoint for p≡3 mod4 constitute the assessed additional claim, subject to possible known automatic-sequence or neighboring-gcd equivalents.

## value

PASS

The gcd of consecutive terms of a familiar combinatorial sequence is a natural exact arithmetic invariant. The prime-power block formula gives all joint zero frequencies and, for each p≡3 mod4, implies almost-sure-in-density simultaneous divisibility; combining primes proves the striking density-one unboundedness of consecutive gcds. This is a motivated distributional strengthening of the known single-index Lucas condition, not a mere small-n recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
