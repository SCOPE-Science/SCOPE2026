---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Grouping j by gcd(n,j) proves H(n)=h(n)/n with multiplicative h and h_p(a)=(p^(2a+1)+1)/(p+1), so denominator has ell iff v_ell(n)>sum_{p != ell}v_ell(h_p(v_p(n))). All h_p(a) are odd, hence delta_2=1/2. When ell=3 or ell=1 mod6, Phi_6 has a nonzero root mod ell; infinitely many primes in that residue class contribute positive ell-valuation already at exponent one. Divergence of reciprocal primes in the progression and finite-prime CRT independence, bounded variance and Chebyshev force numerator valuation above any fixed threshold for density one; hence denominator ell density zero. For ell=5 mod6 Phi_6 has no root, so only p^a with a>=2 can contribute. Tail density sum_{p>Y}1/p² vanishes; finite-prime valuation independence gives the stated convergent positive Euler product, each factor 1+O(p^-2). A p=-1 mod ell and a=(ell-1)/2 gives a positive valuation by LTE and proves strict <1/ell. At ell=5 primitive residue order shows only p=-1 mod5 contribute, with v_5(h_p(a))=v_5(2a+1). Independent rational summation checks H(n)=h(n)/n for n<=350; independently counting n<=10000 with 5|den gives 1994. This is not a proof of asymptotics.

## originality

PASS

Compared theorem-level implications and all four named originality checks against relevant primary literature, published Resultary records, numerical sources and compatible general statements; conclusion is best-of-knowledge with explicit residual risks.

## value

PASS

The previously studied arithmetic function had a difficult sparse integrality problem. The set of primes dividing reduced denominators is a natural complementary local invariant. A complete fixed-prime density dichotomy and genuinely positive product at inert primes, including a concrete 5-adic value, provide a usable arithmetic classification rather than isolated numerical tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
