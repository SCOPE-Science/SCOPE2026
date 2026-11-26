---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For prescribed alternating gradients, y_t=v_t/G² obeys y_t=y_(t−1)−s sign(y_(t−1)−1), s=1−β₂>0. Starting at zero it advances by s until it reaches or crosses one. At integer q=1/s it reaches one and sticks; otherwise it visits Ns and (N+1)s in alternating order from N=floor(q), with Ns on parity N. Direct substitution gives m_t=p[(-1)^(t−1)+β₁^t], p=(1−β₁)G/(1+β₁), including m_0=0. The β₁^t contribution is absolutely summable since the reciprocal denominator is bounded by 1/ε. The eventual periodic part of the normalized update has mean p(-1)^(N−1)Δ/2, so multiplication by −η gives the stated slope and bounded remainder. For exact locking or the separate initialization v_0=G², the denominator is eventually constant and the alternating part has zero mean. The exact decimal settings give q=10,100,1000. The argument is analytic; the packaged floating-point transcription guards were read, not executed. This is exact-real, constant-rate, prescribed-input analysis of the algorithm as printed, not a claim about gradients along a fixed objective, bias-corrected implementations, or exact locking in machine arithmetic.

## originality

PASS

Credit prior coverage for the entire second-moment orbit, its parity as a time index, and the reported reciprocal-step grid. The distinct claim is the nonzero signed parameter drift on exactly balanced alternating input, with its explicit slope and absence on the indicated resonances. The constant-input predecessor does not state that effect: the first moment has a different sign structure, and the new calculation pairs that alternating first moment with the locked denominator. Matching initialization is an immediate fixed point and is not treated as original in isolation.

## value

PASS

An exactly zero pair-sum input is a motivated diagnostic of whether adaptive normalization preserves cancellation. The result identifies an exact parameter boundary and phase-controlled direction of steady motion, distinguishing harmless oscillation in a denominator from its effect on a balanced signed signal. It also shows why the paper's exact decimal settings mask the diagnostic and why matched initialization suppresses it. This is a useful counterexample to cancellation at constant learning rate, not a claim of realistic optimization failure or evidence against the paper's stochastic convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
