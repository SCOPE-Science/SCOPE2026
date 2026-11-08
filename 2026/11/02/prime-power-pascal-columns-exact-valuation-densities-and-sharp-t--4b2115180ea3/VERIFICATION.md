---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Kummer borrow counting with n=p^a q+r yields W=0 for r=0; for 0<r<p^a it is a-v_p(r)+v_p(q), including all a=1 and small n boundaries. Uniform residues r and geometric quotient valuations produce the exact mass mu(0)=p^-a and mu(v>=1)=(p-1)/(p+1) p^(-abs(a-v)) (1-p^(-2min(a,v))); summing tail gives divisibility density. The predicate W>=v depends on n mod p^(a+v-1), and an explicit witness n (separately for v=1 and v>=2) distinguishes shift by p^(a+v-2) with infinitely many period translates, proving minimality. Identity p^a binom(n,p^a)=n binom(n-1,p^a-1) proves divisibility equivalence. Independently tested 16340 valuations by Legendre formula and 32 period cases; arithmetic proof handles unrestricted primes.

## originality

PASS

Rowland already gives periodicity of normalized binomial fractions for fixed column and covers the p^a divisibility periodicity in a more general formulation; the a=1 zero frequency is known. Spiegelhofer–Wallner give binary fixed-column valuation-density framework, covering that special case. The surviving result is complete explicit all-prime all-v density and **each** threshold v sharp minimum period, not the existence of periodicity or binary marginals alone. Check that Rowland period statements for the full fraction may imply the v=a period upper bound; do not ascribe that boundary to new work without distinction.

## value

PASS

An all-prime all-valuation law and sharp periods of every divisibility threshold are natural quantitative invariants of a fixed prime-power Pascal column and the row-number divisibility problem. Earlier binary marginal and basic periodicity are credited; the all-prime distribution and full filtration hierarchy form a useful classification rather than a single numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
