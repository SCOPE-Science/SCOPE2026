---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For s>1/q the unrestricted cylinder partition sum is U_q(s)^n, and strongly separated finite alphabets exhaust the infinite root from below. For no-repeat itinerary the weighted adjacency B_ij=w_j 1_{i!=j} with w_j=r_j^s has positive bounded eigenvector v_i=(lambda+w_i)^(-1) and eigenvalue lambda precisely when sum_j w_j/(lambda+w_j)=1. This identity bounds infinite cylinder partition functions for s>d; finite irreducible graph-directed subsystems produce dimension lower bounds for s<d. Both dimensions lie (1/q,1). As delta=q-1->0, for each b>0, U(1-b delta)->1/(1-b)>1 and U-V=O(delta^2) there, so d,t=1-o(delta) uniformly along every eta(q)->0; on [d,1], -U_prime and -V_prime are uniformly ~1/delta by zeta pole and the O(delta^2 log 1/delta) derivative defect. Mean-value comparison at s=1 gives 1-t~delta eta; at s=t the collision defect U-V~zeta(2q)/zeta(q)^2 produces t-d~delta S2. With S2~zeta(2)delta^2, cubic limit holds even eta dominates. Independent high-precision roots at delta=.10,.05,.02 and exact rational eigenvector examples corroborate, not replace, asymptotic proof. The proof is for symbolic limit sets, not their closures.

## originality

PASS

Best-of-knowledge PASS: finite-alphabet Bowen/pressure formula and general countable conformal IFS are established; neither their main statements nor generic restricted-digit formulations directly yield the exact infinite Zipf no-repeat root and uniform singular cubic penalty for all vanishing leakage profiles. Resultary identified a close Zipf finite-alphabet exponential-cutoff result, but its restriction is a prefix alphabet rather than adjacent-repeat avoidance; only its abstract/index summary could be read, so whole-document noncoverage is not asserted. A broad countable Markov pressure perturbation theorem could yield the coefficient by specialization; residual priority risk remains.

## value

PASS

Forbidding adjacent duplicate symbols is the canonical nearest-neighbor symbolic constraint. Its dimension penalty is measured by the natural second-moment collision mass S2(q), not fitted data, and its cubic law is independent of arbitrary simultaneously vanishing hole profiles. The crossover eta~(q-1)^2 compares two mathematically distinct loss mechanisms and is useful as an exact asymptotic benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
