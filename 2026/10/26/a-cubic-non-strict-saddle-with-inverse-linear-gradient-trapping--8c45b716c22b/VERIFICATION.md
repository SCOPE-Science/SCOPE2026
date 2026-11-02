---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

At a=3^(−1/4), direct differentiation shows gradient zero and Hessian diagonal 8/3 and off diagonal −4/3, giving eigenvalues {0,4,4}. The exact polynomial factorization g(x)=x⁴−4a³x+1=(x−a)²(x²+2ax+3a²) gives invariant diagonal GD update x_(k+1)=x_k−2ηx_k g(x_k). With δ=x−a, δ_(k+1)=δ_k−12ηa³δ_k²+O(δ_k³), and diagonal objective has leading odd cubic 12a³δ³, so the critical point is neither minimum nor maximum. For small positive δ the recurrence is monotone to 0, reciprocal increments tend to 12ηa³ and Cesàro averaging gives kδ→1/(12ηa³). Small negative δ moves away and cannot converge to another fixed point locally. An independent symbolic check verified the factorization, gradient, cubic coefficient and characteristic polynomial. No general off-diagonal basin or global GD convergence is asserted.

## originality

PASS

Best-of-knowledge PASS narrowly: Chen–Jiang–Wang identify a regularized deep-factorization non-strict-saddle boundary and exclude/handle the scalar case separately. The novelty is not the critical parameter equality but the exact scalar cubic one-sided discrete-GD trapping law and its coefficient at the boundary. Their general loss-landscape and error-bound analyses do not explicitly establish this local diagonal law in inspected full text. The underlying parabolic fixed-point rate is standard as a technique; structural specialization, not the technique, is assessed.

## value

PASS

The tuned equality is the natural loss-landscape boundary between strict and non-strict saddles, where a zero Hessian mode defeats linearization. The exact one-sided O(1/k) trapping coefficient demonstrates a concrete optimization slowdown and asymmetry at that mathematically motivated degeneracy, distinct from generic strongly convex descent. Scope remains intentionally one scalar critical example; no general rate theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
