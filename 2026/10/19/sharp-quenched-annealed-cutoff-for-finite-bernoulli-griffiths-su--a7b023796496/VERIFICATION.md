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

For a run of length m<L there are L−m−1 interior starts with two markers (probability p²q^m) and two endpoint starts with one marker (probability pq^m), where q=1−p. The all-free case adds its own q^L term. On windows m≈y log L the expected contribution has cost ay+u/y^β uniformly on compact y-windows; the upper tail is bounded by a constant times Σ_{m>K log L}m q^m=O(log L)L^(−aK), and the short-length tail by L^(−u/δ^β), so there is no loss in taking the unrestricted annealed minimum. For a typical landscape, the longest-run union bound cuts off beyond (ξ+η)log L. Markov's inequality and a union bound over O(log L) lengths give the count upper bound L^[max(1−ay,0)+ε]. This yields cost min(ay,1)+u/y^β over the enlarged interval, tending to the constrained cost as η decreases to zero. Conversely, for fixed y<ξ, disjoint blocks with two lossy markers generate independent distinct maximal runs with expected count of order L^(1−ay)/log L and concentrate above L^(1−ay−ε). These give the lower bound, including the edge by approaching ξ from below. The strict convex minimum has y*=(βu/a)^(1/(β+1)), reaches ξ at u_c=ξ^β/β, and gives the asserted strict post-threshold rate gap and second-derivative jump. Log zero on the all-lossy event is harmless since its probability is p^L.

## originality

PASS

The supported distinct claim is the joint finite-size/time, typical logarithmic rate and its quantitative separation from the annealed rate for the defined Bernoulli surrogate. The continuum annealed saddle and rare-region physics are not new. The strongest inspected actual statements supply the annealed saddle or a longest-run input, not the paired run-count/weighted-survival limits.

## value

PASS

The surrogate is motivated by rare-region relaxation, and the order of the size and time limits matters. The explicit threshold tells when its disorder mean ceases to represent a typical finite sample even at leading log order, and the positive exponent quantifies that failure. This is more informative than an annealed saddle or an estimate on the single longest run alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
