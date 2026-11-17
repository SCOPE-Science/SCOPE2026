---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For theta∈(0,1), b≥2, alpha>0, gamma real, psi_theta=1-(1-z)^theta is a positive-coefficient disk selfmap fixing 0. Its unique boundary contact has 1-|psi(e^{it})|² ∼ 2cos(pi theta/2)|t|^theta. Boundary Laplace integral gives U_n=||psi^n||_{H²}² ∼ A_theta n^{-kappa}, kappa=1/theta, with H¹ norm O(n^{-kappa}). The Paley lacunary H¹ estimate yields 0≤U_n-V_n≤C||psi^n||_{H¹}²=O(n^{-2kappa}), uniformly in all beta≤1 weights, so V_n∼U_n. Exceptional normalized column norms then scale as b^{j(alpha-kappa)}(j log b)^gamma, giving exactly the HS thresholds and two Abelian divergence residues A_theta/log b. At alpha=kappa,gamma=0, off-exception input is HS; exceptional Gram entries are majorized by C b^{-kappa|j-k|/2}, hence bounded by Schur. Gamma<0 inserts a decaying diagonal giving compactness, while gamma=0 has weakly-null unit inputs with nonzero limiting output and gamma>0/alpha>kappa produce unbounded columns. The argument covers endpoints gamma=-1,0, and finite scripts do not prove the asymptotics.

## originality

PASS

PASS best-of-knowledge: primary Cruz-Zamorano–Dellepiane–Seco class-equality theorems for lacunary weighted spaces were inspected in arXiv HTML Sections 1, 4, 6. They do not determine the precise fractional cusp symbol C_{1-(1-z)^theta} across all alpha,gamma, the intermediate compact/non-HS region, or either exact HS residue. Resultary semantic search found general class-equality theorems (including all Hadamard ratios) and unrelated affine cases but no exact symbol-specific four-regime statement; algebraic comparison shows class-equality does not imply this symbol’s individual rates. Residual risk of older general Carleson/cusp criteria remains named, not treated as an automatic FAIL.

## value

PASS

Sharp classification of a natural fractional boundary-contact selfmap on sparse weighted Hardy spaces identifies two different logarithmic transitions, a genuine compact/non-HS interval, an explicit bounded noncompact endpoint and exact analytic divergence residues. These are motivated critical invariants rather than an arbitrary small finite slice, and future compactness/Schatten studies can use the precise threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
