---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For each N>=2 with independent periodic nonnegative integer claims, positive zero-claim probabilities a_j, ∑E X_j<N, common exponential moment and distinct nonunit kernel roots in closed disk, Q(0)=-∏a_j !=0 gives unique formal F_j in cyclic PGF system zF_j=g_jF_(j+1)+a_j b_(j+1)(z-1). If Ab=0, exact eliminated identity Q F_N=(z-1)z^(N-1)L_b has all kernel zeros removable and L_b(1)=0; simple Q zero at z=1 ensures F_N(1)=0. Analyticity beyond unit circle passes cyclically through equations (apparent z=0 poles are removable), yielding finite signed/complex coefficient measures. The equations exactly express reflected transition w→max(0,w+X_j-1). N-step negative drift outside finite set plus positive chance of all-zero claims ensures unique positive recurrent closed class and every state reaches its zero state; Cesàro ergodicity forces any invariant finite complex measure with zero total mass to vanish, yielding b=0 and det A≠0. Rational example N=2, g1=(3+z²)/4, g2=(2+z²)/3 gives Q=-(z-1)(z+1)(z²-6)/12 and det A=1. No claim about multiple roots, arbitrary premium, critical drift or heavy tails.

## originality

PASS

Best-of-knowledge noncoverage is supported by the statement-level comparisons below; this is not a proof of absolute bibliographic novelty.

## value

PASS

Proves a motivated nontrivial unit-premium subcase of an explicitly published nonsingularity conjecture for a natural seasonal ruin model. The analytic pole-cancellation to Markov signed-measure uniqueness link explains why the specific matrix is invertible for all N under natural light-tail conditions; this is more than an illustrative finite determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
