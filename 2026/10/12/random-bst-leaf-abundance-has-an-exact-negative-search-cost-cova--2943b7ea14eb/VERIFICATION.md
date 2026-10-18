---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

In a BST built from a uniformly random permutation, root split K is uniform on 0..n−1 and left/right subtrees independently distributed. For n≥2 L_n=L_K+L_R and P_n=P_K+P_R+n−1. Total covariance gives c_n=(2/n)Σ_{k<n}c_k+Cov_K(ℓ_K+ℓ_R,p_K+p_R+n−1). The leaf-mean deviations (relative to (n+1)/3) vanish except four endpoint split types with ±1/3; then the between-split covariance is −4(H_{n−1}−1)/(3n), whose harmonic term cancels the inductive Σc_k. Thus c_n=−(n−2)(n+3)/(9n), including c_2=0,c_3=−2/9. The analogous total-variance recurrence gives Var L_3=2/9, Var L_n=2(n+1)/45 n≥4. Regression slope follows by exact division, limit −5/2. Independently constructed each BST for all 5912 insertion permutations at n=2..7 using exact rational moments; all covariances and variances matched.

## originality

PASS

Classical exact marginal moments and additive-functional recurrences are prior mathematics. Kapur 119-page arXiv dissertation gives internal path length and generic moments; its text search did not find leaf, and inspected §2 examples/§3 theory do not state the mixed leaf/path covariance. Flajolet et al. focus fringe-pattern frequencies, and Drmota–Hwang covariance between *level-profile* populations, a different statistic; latter two available mostly abstract. Resultary nearest random-BST mixed covariance uses root-split imbalance, not leaf count. An equivalent old exercise or generating-function specialization remains possible.

## value

PASS

Key leaf count and total internal path length are canonical shape summaries with clear algorithmic interpretation (terminal branching vs total search depth). The exact all-n rational mixed moment, sign change at n=2, and stable best-linear-predictor slope −5/2 are mathematically natural and non-obvious from either marginal or generic covariance framework; not an arbitrary isolated small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
