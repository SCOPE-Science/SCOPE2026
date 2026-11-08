---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For fixed q>=2, alpha>-1 and sigma>0, the inspected radial angular-frequency blocks act on q-dimensional Jacobi polynomial subspaces for the Beta(xi+1,alpha+1) law. Under Y_xi=xi(1-t), every polynomial moment converges to Gamma(alpha+1), with positive limiting Hankel determinants and hence coefficientwise Jacobi-to-Laguerre orthonormal basis convergence. The symbol condition a(t)=c(1-t)^sigma+o((1-t)^sigma) plus boundedness gives a global power envelope, and higher fixed Beta moments yield uniform integrability. Thus xi^sigma M_xi converges in matrix norm to c times a positive-definite q-by-q Laguerre moment matrix. Finite negative-frequency blocks do not affect tails. Each of its q positive eigenvalue branches has xi^-sigma singular-value asymptotic; summing branch counting functions and inverting proves N^sigma s_N=|c|(sum_j nu_j^{1/sigma})^sigma in the limit. This yields compactness, p>1/sigma Schatten criterion and endpoint logarithmic coefficient. For sigma=1, Laguerre Jacobi trace q(q+alpha) gives the stated exact constant. Independently checked the q=2 alpha=1/2 sigma=1 matrix, trace, and positivity; numerical finite-block checks are not infinite proofs.

## originality

PASS

The beta/Jacobi radial-block decomposition and qualitative scalar boundary limits were previously established (Barrera-Castelán–Maximenko–Ramos-Vazquez). This audit credits those inputs; the Laguerre matrix as the leading vanishing boundary-layer coefficient and all-q ordered singular-value law do not appear in the inspected scalar-limit result. Analytic Bergman one-branch asymptotics are related prior results but do not alone yield the full-polyanalytic q-branch constant. Priority risk: general semiclassical Toeplitz boundary symbol calculus might imply this scaling.

## value

PASS

Exact eigenvalue tail and endpoint ideal membership are central compact-operator invariants. Passing from known scalar limit/compactness to the explicit q-branch matrix and ordered tail coefficient provides substantive quantitative information; sigma=1 unexpectedly reduces to |c|q(q+alpha). The natural family is any bounded radial symbol with a fixed nonzero boundary vanishing order, not an artificial isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
