---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Sorting endpoints of n iid continuously distributed chord pairs produces the uniform matching because each unlabeled matching has 2^n*n! label/orientation preimages. The crossing/nesting indicators form order-2 U-statistics of iid chords Z_i=(A_i,B_i). Conditional projections are p_C=2*(B-A)*(1-(B-A)) and p_N=(B-A)^2+2*A*(1-B). I independently integrated them with triangular density 2 and obtained E p_C=E p_N=1/3, E p_C^2=E p_N^2=2/15, E p_C*p_N=1/9; hence projection variances 1/45 and cross covariance zero. Shared-chord indicator pairs have covariances 1/45 (same type) or zero (mixed), while identical chord pairs have mixed covariance -1/9 and each type variance 2/9. Counting gives Var=n(n-1)(n+3)/45 and Cov=-n(n-1)/18 exactly. Hoeffding degenerate residual kernels have variance (8/45)*C(n,2)=O(n^2), negligible after n^(3/2), and the iid bivariate CLT with diagonal projection covariance proves joint Gaussian independence. All finite n>=2 formulas, n->infinity quantifier, and distinction from finite independence/TV are respected.

## originality

PASS

Kasraoui–Zeng 2006 supplies exact two-variable generating functions and crossing/nesting equidistribution; these cover the entire finite joint counting law and could yield finite covariance by differentiation, so the latter is not asserted as independently new. The central claim instead proves joint standardized Gaussian convergence to independent normals and identifies orthogonality of the two one-chord projections. Paguyo and Féray establish crossing-only CLTs. Baik–Jenkins treat *maximal r-crossing and nesting sizes* (Tracy–Widom), mathematically different from total numbers of crossing/nesting chord pairs. No earlier total-count joint Gaussian independence theorem was identified in the inspected material; residual historical risk recorded.

## value

PASS

Crossing and nesting are two canonical, structurally competing local statistics of perfect matchings; a strict negative finite covariance but independent joint Gaussian limit is a meaningful probabilistic phenomenon. The explicit zero mixed Hoeffding projection identifies why finite local competition disappears at the n^(3/2) global scale, and the exact 1/n finite correlation quantifies the crossover. This is a natural two-statistic asymptotic theorem, not merely a recomputation of a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
