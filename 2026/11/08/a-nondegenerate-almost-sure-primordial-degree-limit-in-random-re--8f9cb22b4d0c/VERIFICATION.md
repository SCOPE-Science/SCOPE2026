---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For RRSC(2), at n vertices E_n=n−1+T_n, J_n (choose edge) has conditional success probability q_n=E_n/(n+E_n), and the first degree increments by Bernoulli 1/n for vertex choice, D_n/E_n for edge choice. The source proves E(T_n−rn)²=O(n), r=(sqrt5−1)/2, using the affine drift and a second-moment recursion; this gives almost-sure convergence of the correction series for reciprocal edge count and J_n/k. Hence the environment product G_n=∏(1+J_k/E_k) has a strictly positive random n^(3−sqrt5)/2 normalization limit. Writing A_n=D_n+1 yields the exact conditional affine recursion with inhomogeneous beta_k and martingale increments xi; the drift series and conditional quadratic variation converge, giving W≥0 finite with conditional L². On {J_2=0}, probability 2/3, A_3 takes 2 and 3 with equal conditional probability, and the expected normalized limit differs by g(J)>0, proving Var(W|J)≥g(J)²/4. Examined source checker.py exact Markov-chain and full-shape matching n≤6 and reduced chain n≤9; no claim of rerunning its 3300 assertions in this audit. The infinite conclusion is supported by series and martingale arguments, not checks.

## originality

PASS

PASS best-of-knowledge: Krapivsky–Lucas 2026 derives/predicts the same exponent from mean-field estimates and reports numerical non-selfaveraging; their stated proof gap is bridged by the conditional martingale theorem. Published 2026 empirical degree-distribution result for RRSC(2) counts degrees of a uniformly sampled vertex and cannot imply the a.s. scaled degree of the initial vertex. Fountoulakis et al. studies fixed-dimensional simplex attachment, not pooled edge/vertex choice.

## value

PASS

PASS: resolving a highlighted open stochastic-limit question in the natural original-vertex observable is mathematically motivated. Proving existence and retained conditional randomness beyond a mean-field exponent is structural information about reinforcement and initial-condition memory; the limit is not asserted positive a.s. nor does it imply unconditional degree-variance asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
