---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At diag(a,-b), differentiating the positive spectral projector multiplies an off-diagonal entry by 1/(a+b), so differentiation of the positive eigenvalue times that projector gives the Hermitian Schur mask (1,q;q,0). The 2-norm is one by the entrywise formula and the first diagonal coordinate. Independently optimize in trace norm: the Hermitian trace unit ball is the convex hull of signed rank-one orthogonal projectors. A unit projector with first diagonal r has output trace norm squared r^2+4q^2 r(1-r), using the nonpositive determinant. On [0,1] this has maximum 1 at r=1 up through q^2=1/2, and otherwise maximum 4q^4/(4q^2-1) at r=2q^2/(4q^2-1). Trace duality and mask symmetry transfer the maximum to operator norm. The exhibited real symmetry has unit input and top output eigenvalue (t+sqrt(4q^2+(1-4q^2)t^2))/2, attaining the maximum at t=1 or t=1/sqrt(4q^2-1), as appropriate. The threshold is a/b>1+sqrt(2) in the stated infinitesimal sense. For global bounds the nonzero determinant polynomial yields finitely many crossings on a segment, with derivative bounds integrated between them; the identically singular segment is rank at most one, with its positive part either the input or zero according to affine trace, and bounded on both pieces. The profile increases on its upper branch to 2/sqrt(3); derivative ratios first at fixed indefinite input then as b/a->0 approach this ceiling. Frobenius sharpness already occurs in the positive cone. The claims apply on the real space of Hermitian matrices, not automatically to unrestricted perturbations. The inspected check.py gives finite corroboration only; 1892 checks is the frozen report, not a fresh run.

## originality

PASS

The supported distinct result is the exact fixed-ratio Hermitian derivative profile, especially the interior transition at q=1/sqrt(2). Divided differences, the triangular endpoint, and Hilbert–Schmidt projection nonexpansion are not new. Neither the known endpoint nor the inspected broader variational characterizations evaluate this fixed-q problem. Later published Resultary statements have real overlap on the global bound and derivative machinery but do not supply the evaluated fixed-q transition in the passages read.

## value

PASS

The local threshold resolves whether infinitesimal perturbations can be amplified at a given mixed-sign input in two commonly used matrix norms. A universal constant or its known endpoint does not answer that question. The exact identity/expanding regimes over the full natural two-eigenvalue family, contrasted with Frobenius nonexpansion, are the substantive sensitivity result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
