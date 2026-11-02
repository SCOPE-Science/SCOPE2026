---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Exact factorial moments E(S_n)_j=(n)_j(lambda/n)^j for 0<=j<=k follow from k-wise independence. Uniform integrability below k: E[(S_n)_j 1_{S_n>R}] <= E(S_n)_{j+1}/(R-j), and bounded continuous truncation plus monotone convergence gives kth moment inequality. For sufficiency, truncate target and Poisson at n (move tail to zero), form (1-eps_n)mu^[n]+eps_n pi^[n], eps_n=sqrt(t_n+1/n); lower factorial errors O(1/n) and fixed masses at 0..k at least c_i eps_n. If top moment deficit delta>0, add q_n=d_n/(n)_k at n and correct moments 0..k-1 at 0..k-1 using invertible falling-factorial triangular matrix with diagonal j!; low-order added errors O(n^-1) and q_n=O(n^-k). If delta=0, correct all moments 0..k at 0..k; needed O(t_n+n^-1)=o(eps_n), preserving positivity. Uniform random subset of exact count transforms factorial moments into all-one joint events and inclusion-exclusion proves full k-wise independence. The tail ratio (Y)_j/(Y)_k <= (n-k+1)^-(k-j) for Y>n secures o(n^-1) when j<k. Algebra and moment-correction bounds independently reviewed; no finite sampling inference.

## originality

PASS

PASS qualified: Previously published pairwise (general lambda) and three-wise (lambda=1) weak-limit classifications explicitly do not cover fixed k>=4 arbitrary lambda. Peled–Yadin–Yehudayoff studies finite count moment constraints and maximal all-one event, not universal asymptotic weak-limit classification. Construction generalizes the triangular moment idea; older arbitrary-order discrete moment theory may implicitly imply it, unresolved priority risk.

## value

PASS

PASS: This is a complete natural hierarchy for a canonical rare-event limit problem, identifying precisely which finite-order factorial moments survive weak convergence and exactly which one can leak to escaping mass. Realizability for every admissible limiting law, not just necessary bounds or an example, is mathematically useful; extends known k=2 and k=3 cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
