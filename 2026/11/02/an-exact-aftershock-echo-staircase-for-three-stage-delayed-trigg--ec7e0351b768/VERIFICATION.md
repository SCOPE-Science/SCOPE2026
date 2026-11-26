---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The j-th generation mean density is q^j times the Erlang(mj,β) density by convolution; summing gives the stated transform and absolutely convergent series, with total mass q/(1−q). In dimensionless time the m=1 exponential is strictly decreasing and the m=2 derivative changes sign once at tanh(sqrt(q)τ)=sqrt(q). For m=3, the three cube-root poles give the stated damped sine/cosine expression. Its time derivative equals β²a(1+a)exp(−(1+a/2)τ)/3 times the frozen F(θ), with a=q^(1/3). For θ>0 the divisor exp(sqrt(3)θ)−cosθ is positive; h has limit 1 at zero and cannot exceed the positive level δ on nonpositive-sine intervals. On each positive half-wave the numerator H in h′ has derivative −4 exp(sqrt(3)θ) sinθ, strictly negative. Hence the first lobe is decreasing, and every later lobe has one strictly nondegenerate maximum d_j. Two crossings when δ<d_j add exactly one strict peak; equality is a quadratic zero of the rate derivative with negative coefficient, so the rate has a stationary inflection, not a maximum. Shift by 2π strictly decreases h on positive-sine angles, proving strict ordering; exponential decay gives finiteness for each q<1. The maximum angle is 2πj+π/6+O(exp(−2πsqrt(3)j)) from the root equation near its simple undamped zero. Thus d_j is asymptotic to (sqrt(3)/2) exp(−sqrt(3)(2πj+π/6)); 1−q_j is asymptotic to 6d_j. This holds for the ensemble descendant rate excluding the seed, not for realized catalog peaks.

## originality

PASS

The supported distinct statement is the exact infinite classification of strict peaks for the subcritical Erlang-three single-seed mean descendant rate, including threshold equality and geometric accumulation. Erlang cascades, renewal densities, and Hawkes moment calculations are prior frameworks. The inspected analogous three-state threshold classifications are not this peak law. Several relevant full texts remain unavailable; priority is provisional.

## value

PASS

A mode count for a delayed branching mean intensity is a natural qualitative question; the proof finds the first integer stage supporting a secondary peak and classifies all additional peaks, including the equality boundary. It also quantifies how close to critical the effect first occurs, an important constraint on practical interpretation. It supplies neither a seismic catalog fit nor a prediction of sample-path peaks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
