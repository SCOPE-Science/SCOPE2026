---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Exact orthogonal similarity preserves λI+ρvvᵀ. The selected nonzero block has one exceptional eigenvalue because ρ≠0, so diagonalizing a block with r≥2 active coordinates leaves exactly one active coordinate there. A pair with fewer than two leaves the support unchanged under the prescribed rule. Diagonality is equivalent to support size one. Conditional on any past at support j, the next pair succeeds with probability binom(j,2)/binom(n,2); the holding-time law is geometric and its parameter is independent of the entry history, giving independent holding times at successive sizes. This gives the finite moments, including zero time for s=1 and (n−1)² for s=n. For fixed j the scaled waiting time has exponential rate j(j−1) in the limit; the expected scaled tail above K is at most 1/K. Summation gives mean 1, and the variance follows by summing [1/(j−1)²+1/j²−2/(j(j−1))]. The conventional Kingman rate is half as large, so the time here is half the conventional absorption time. For blocks, the active count is hypergeometric and the first-step equation gives the stated expected-sample recurrence, with a positive exit probability at every s≥2 and one sample when b=n. These arguments apply to the exact pivot clock including ineffective samples. The recorded check in reproduce.py is bounded corroboration, not part of the all-size proof; the frozen script was inspected, not executed.

## originality

PASS

The supported distinction is the rank-one Jacobi support-chain reduction and its exact cost consequences. Uniform randomized/block Jacobi and the limiting coalescent law itself are already known and are not credited as new. Neither the nearest primary convergence theorem nor the strongest inspected indexed stochastic analogue covers the matrix-specific stopping-time and block-expectation claims.

## value

PASS

Rank one is a natural test of generic randomized Jacobi estimates. Exact finite termination alone would say little about a rule that wastes pivots; the distribution quantifies that overhead and shows nonvanishing fluctuations at the n² scale. The block recurrence also isolates the effect of block size on the sample clock, without confusing it with arithmetic cost. These are meaningful exact predictions for a canonical model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
