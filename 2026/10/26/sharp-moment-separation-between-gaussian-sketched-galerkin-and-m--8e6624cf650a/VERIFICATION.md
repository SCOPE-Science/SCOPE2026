---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For real SPD A, exact nonterminal Lanczos with H=V^TAV strictly irreducible SPD tridiagonal and beta>0, Gaussian sketch regression g=(Z^TZ)^(-1) Z^T w has multivariate Student density f_{k,ell}(g)=Gamma((ell+1)/2)/(pi^(k/2)Gamma((ell-k+1)/2))*(1+||g||²)^(-(ell+1)/2), nu=ell-k+1. Sketched Galerkin projected equation (H+beta g e_k^T)y_F=||b||e_1 leads by Sherman–Morrison to y_F=y0-c H^-1g/(1+a^Tg), a=beta H^-1e_k, c=beta||b||e_k^T H^-1e1!=0 by the off-corner cofactor of irreducible tridiagonal H. Energy orthogonality yields squared error D²+c² g^T H^-1g/(1+a^Tg)². Its strictly positive numerator along the entire affine hyperplane a^Tg=-1 causes exactly p>=1 divergent moments regardless of ell and gives a positive 1/R tail with the stated coarea integral; local transversal integration and Student radial domination prove p<1 convergence and finite tail coefficient. For sketched least squares, independent Gaussian orthogonal regression about nonzero deterministic residual yields an invertible linear image of a multivariate Student vector, giving moment cutoff p<ell-k+1 including divergence at equality. Independently verified 120 random projected systems and the exact algebraic Sherman–Morrison relationship; a separate k=ell=1 Cauchy example confirmed the hyperplane tail coefficient. All asymptotic/integrability claims depend on analytic density proofs, not Monte Carlo.

## originality

PASS

Gaussian regression Student laws and sketched projection/GMRES/FOM constructions are established. The assessed new contribution is a uniform, sharp all-nonterminal-SPD-Lanczos dichotomy of unconditional error moments and an explicit positive Galerkin 1/R tail constant. High-probability subspace-embedding bounds do not imply unconditional moments. Possible specialist papers on oblique Gaussian projectors remain a priority risk.

## value

PASS

Same Krylov subspace and Gaussian sketch budget yield radically different unconditional moment behavior: unsafeguarded Galerkin retains infinite mean under arbitrary oversampling, whereas minimal residual obtains finite higher moments as ell-k increases. Exact frontiers and a tail coefficient are mathematically consequential for interpreting high-probability error guarantees and designing safeguards; they are not generic restatements of the Student density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
