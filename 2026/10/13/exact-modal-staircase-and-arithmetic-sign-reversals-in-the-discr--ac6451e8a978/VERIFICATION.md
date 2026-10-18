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

The source DADL mass function is Cτ(1+t)exp(-θt) with t=τj for j>=0 and t=k/τ for negative label -k. Merging the two locally finite positive lattices into sites 0=s0<s1<... reduces global mode selection to maximizing strictly concave log(1+t)-θt. Consecutive secant slopes β_i strictly decrease from positive β0 to zero: θ∈(β_i,β_{i-1}) uniquely maximizes site s_i; θ=β_i ties only consecutive sites. Coincident positive/negative labels arise iff τ²=a/b rational, with exact positive/negative lattice support a|m,b|m. Both sign-only sites recur unbounded iff a,b>1 or τ² irrational; therefore infinitely many reversals of unique modal sign near θ=0 exactly when neither τ² nor its reciprocal is a positive integer. Independent direct-PMF finite scans checked six τ regimes including 1,2,1/2,sqrt(3/2),sqrt(2),sqrt(pi), and interior modes and threshold numerics matched; strict concavity and divisibility prove the infinite assertion.

## originality

PASS

Detailed implication comparison to primary prior work, using all four separate originality checks. No identified prior theorem or table implies the exact newly stated invariant; findings are best-of-knowledge with residual risks.

## value

PASS

For an actual two-sided discrete statistical distribution, exact global mode locations and tie multiplicities as parameters vary matter for likelihood interpretation and modal phase regimes. The ordered infinite staircase and sharp number-theoretic criterion for indefinitely alternating modal signs reveal structure obscured by half-line unimodality and finite plots. The result is a motivated model-specific classification rather than an arbitrary substitution of an unrelated lattice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
