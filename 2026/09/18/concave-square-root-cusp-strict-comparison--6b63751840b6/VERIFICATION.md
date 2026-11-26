---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

For a nondecreasing concave φ with φ(0)=0, a right secant from u>0 is at most φ(u)/u, which is nonincreasing. Splitting an increment of length h at u=h gives the claimed global √2 K square-root modulus, including at zero. Both argument maps are 1-Lipschitz. The Yamada–Watanabe uniqueness integral diverges for that modulus; continuity gives weak existence and linear growth gives nonexplosion, hence global strong existence and uniqueness. The coefficients are locally Lipschitz away from 0. In Larsen's variables z=M/D, the modulus gives Δ²≤2K²D for |z|≤1, and the concave secant bound gives Δ²≤2K²D/|z| for |z|≥1 (reflection for the symmetric negative side and zero increment for the one-sided negative side). Both are bounded by DQ for Q=4K²/(1+|z|). On the same positive side Γ−1=aφ(Db)−bφ(Da)≥0 for a≥b≥0 by the ratio property, covering b=0 directly. On a straddling pair Γ−1 is a nonnegative weighted sum of cusp contributions, and reflection or the constant side handles the other cases. Thus Γ≥1 and Δ²≤DQΓ² everywhere. This verifies Larsen Theorem 2.6 including its logarithmic bounds on both integrated tails of Q. For the explicit family L≥2(γ+1) on the nonconstant branch, so the second derivative factor −1/4+γ(γ+1)/L² is negative; the continuation is continuous and drops the slope to zero. Across the cusp, the derivative is locally in L^p for 1≤p<2, and its squared integral reduces by s=log(e/r) to an integral of s^(−2γ), finite iff γ>1/2. At equality the stated logarithmic divergence is logarithmic in s (log-log in the radial cutoff). Taking a pair 0,h bounds any admissible modulus below by φ_γ(h), so the Yamada–Ogura strict-comparison integral is finite for all γ≥0. That failure is separate from the uniqueness modulus, and implies nothing by itself about more general factorizations.

## originality

PASS

Credit the uniform reduction for arbitrary concave square-root-envelope profiles and the explicit damped family with its threshold, not Larsen's two-variable theorem, its pure-root examples, or the known positive Sobolev sufficient class. No claim is accepted that the damped family evades every Yamada factorization.

## value

PASS

The one-variable hypothesis makes a two-variable nonconfluence test directly usable for irregular nondifferentiable profiles. The examples near the Sobolev boundary show that the simple shape criterion yields explicit strict comparison even where the classical modulus and plain Sobolev sufficient conditions provide no answer. That provides both a transferable lemma and a motivated regularity boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
