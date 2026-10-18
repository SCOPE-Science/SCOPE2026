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

Cooper's level-13 modular formula supplies Z(X)^2=F(X) in Z[[X]], F(0)=1 and linear coefficient a=3. Expanding sqrt(1+I), 4^n binom(1/2,k) for the k-th term has v2=2(n-k)+s2(k); the inequality s2(n)<=s2(k)+(n-k) puts all k<n contributions above the k=n valuation s2(n). The unique k=n term has odd a^n, proving v2(S_n)=s2(n) for every n>=1. Terms k<=n-2 vanish modulo 2^{s2(n)+2}; the k=n-1 factor (n-1)a^{n-2}b has sufficient 2-adic valuation, yielding the exact Catalan congruence. Division by 4^n gives denominator 2^{2n-s2(n)}; binomial distribution of popcounts yields frequency C(m,k). Checked exact integer recurrence and congruence independently through n=121 plus source checker structure. The all-n theorem depends on Cooper's true modular square identity, not finite evidence.

## originality

PASS

Published square identity + general elementary valuation comparison IMPLIES the claim after an additional proof; no identical theorem found in read prior source. Significance is an exact arithmetic specialization, not a new modular relation. The valuation is a short but nontrivial formal square-root consequence of Cooper's identities. No primary source inspected that states this popcount identity or modulo-four Catalan odd part as an equivalent formulation. Material priority limits are recorded separately.

## value

PASS

This gives the exact arithmetic of a natural Apéry-like integer sequence at every index in response to arithmetic questions from the originating modular-parametrization paper: precise binary valuation, two extra powers of unit precision, reduced denominator valuation, and full frequency. The small amount of additional proof does not make the all-index explicit invariant a mere published-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
