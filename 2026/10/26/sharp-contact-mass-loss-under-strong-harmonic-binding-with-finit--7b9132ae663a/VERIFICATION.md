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

For fixed positive rates, clipping and the drift comparison give the invariant interval [0,v/μ]; the stationary law exists there and negative runs long enough to hit zero give coupling. The ideal sign indicator keeps its last nonzero sign through either zero state, is negative half the time by symmetry, and dominates true contact. The mismatch reward starts only at +1→0_j→−1 and stops at contact or the next positive sign. To check the key uniform estimate, from either negative state the reward is O(τ_μ(x)): the uninterrupted contact time is at most τ_μ(x), the probability of an earlier jump is O(τ_μ(x)), and the expected remaining time until a positive state is uniformly bounded by finite-state irreducibility. A first jump to −2 thus contributes O(τ_μ(x)^2). A jump to a zero state of rate ρ contributes its full mean holding time 1/ρ, since x>0 stays positive there; any further negative recovery has conditional mean O(τ_μ(x)ρ/(ρ+2μ)) by exponential distance contraction and log(1+z) comparable to z uniformly on [0,2]. Integrating first-jump times gives the stated Bτ_μ(x)+O(τ_μ(x)/μ), since τ_μ≤log(3)/(2μ). Stationary flux multiplies the ensuing reward by π_+1 q_(+1,0_j) q_(0_j,−1) exp(−ρ_j s) ds. The scaled departure distance relaxes in L1 to 1 during the independent +1 holding period. Changing to u=2μs and dominating by 2exp(−u) gives the factor π²/48. Detailed balance and the jump-rate product sum 3αβ/2 give the claimed positive K, with v canceled by scaling. Independently checked the logarithmic integral by the alternating inverse-square sum and K(1,1)=7π²/512≈0.13493599767; inspected the checker without executing it. Weak convergence from the support bound is not convergence of the atom to mass one.

## originality

PASS

The exact six-state process and harmonic jamming model are prior; the supported distinct result is the exact-contact strong-attraction expansion for this combination. The closest primary source explicitly leaves the finite-tumble harmonic stationary computation outside its solutions. Indexed variants do not provide this coefficient or this rare-switch mechanism for the same chain and force law.

## value

PASS

Exact contact is a physically distinguished stationary event not determined by a coarse weak limit. The finite-tumble harmonic model is established and its stationary law difficult; the result nevertheless identifies a precise nontrivial atom, its loss rate and the contribution of aborted contacts in the zero states. A future analysis of the jamming fraction or of strong-binding reductions can use this constant rather than assume all rescaled-zero configurations have jammed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
