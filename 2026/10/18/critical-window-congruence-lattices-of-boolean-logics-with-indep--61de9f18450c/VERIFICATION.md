---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For N_j(X)=[n]\tau_j^-1(X), congruence theta_S respects N_j exactly iff tau_j^-1(S) subset S, equivalent to no random directed edge entering S from its complement. Every subset of zero-indegree points Z is closed and the whole set always closed. For fixed S size m<n, no outside edge entering has probability (1-m/n)^{r(n-m)}, and an additional internal hit is bounded by min(1,r m^2/n); summing over S and splitting small m, up-to n/(log n)^2, to n/2 and larger complements shows no other closed proper S whp when r=log n+O(1). Falling factorial zero-occupancy moments (n)_m(1-m/n)^{nr} give Poisson(|Z|) total variation along compact-mean subsequences and simplicity probability e^-lambda+o(1). For floor(log n), lambda subsequences range [1,e], giving simplicity cluster set [e^-e,e^-1]. Operator is a dual lattice homomorphism, NOT assumed involution. All quantifiers are asymptotic n>=2 and integer r in the stated window.

## originality

PASS

Finite Boolean/Ockham congruence theory gives deterministic congruence notions, and Cai–Devroye 2015 random k-out digraph analysis contains the coarse strong-connectivity transition and closed-set first-moment method. Their inspected theorem handles k-log n tending to infinity in either direction; the submitted constant-width critical-window full lattice identification with all zero-indegree generators and Poisson limit is stronger and not an immediate coarse-connectivity corollary. Need acknowledge closed-set direction conventions. No checked indexed published result directly implies entire lattice law.

## value

PASS

Provides the entire critical-window congruence inclusion structure of a natural random algebra, not just a simplicity probability. Poisson dimension and lattice law are reusable for random algebra classification, with an explicit oscillatory integer-operator boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
