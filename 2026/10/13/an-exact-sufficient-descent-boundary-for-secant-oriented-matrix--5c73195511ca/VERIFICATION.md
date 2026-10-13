---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The proof has two components. First, substitution of the secant identity \(\nu=(1-t)/\|y\|^2\) into the Matrix Dai--Liao search-direction matrix gives an exact two-by-two symmetric-part representation on \(\operatorname{span}\{s,y\}\). Its determinant is the stated \(\Delta(t;m,z)\), while the orthogonal complement is the identity. This establishes the infinite family statement analytically; no finite experiment is used to infer universal failure.

Second, `verify_matdl_boundary.py` performs exact arithmetic for the explicit quadratic witness. It verifies positive definiteness of the Hessian, \(d_0=-g_0\), the exact step and gradient difference, the Armijo and curvature inequalities for \(c_1=10^{-4}\) and \(c_2=9/10\), the source secant parameters for \(\rho=1\) and \(\eta=1\), the matrices \(T\) and \(P\), \(\det((P+P^\top)/2)=-43/4\), and \(g_1^\top d_1=5/32\). The replay prints `VERIFY_OK` only if every assertion succeeds.

Unproved limits: this package does not establish a full convergence or divergence theorem for MatDL, does not model the internal choice made by every strong-Wolfe line-search implementation, and does not claim failure of the source's separately descent-oriented parameter configurations.
