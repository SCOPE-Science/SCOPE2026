---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

Using independent hollow a_ij coordinates, calculated derivative 2adj(A)_ij: for rank n-1 adj=c vv^T, vanishing off diagonal forces v supported at a single coordinate (exactly a zero row); rank<=n-2 has adj zero. For r=n-2>=3 the rank-r hollow locus is the surjective Gram image of n irreducible isotropic cones in r-space, with generic O(r) fibers of dimension r(r-1)/2; image dimension N-3 affine, so projective dim N-4 and irreducible. Each zero-row linear stratum has projective dim binom(n-1,2)-1 and generic rank n-1 by invertible hollow block construction. Schur complement on a generic rank n-2 matrix restricts the determinant to Sym^2(kernel) and the hollow-perturbation restriction is surjective unless there is a zero row, giving nondegenerate xy-z² Hessian rank3. A rank n-1 zero-row block gives -det(B)*u^TB^{-1}u, Hessian rank n-1. Codimension >=2 singular support plus CM hypersurface yields normality/irreducibility, and hypersurfaces are Gorenstein. Independent exact 5x5 witnesses yielded gradient vanishing/rank3 Hessian on R, gradient vanishing/rank4 Hessian on L, and nonzero gradient at rank4 smooth point. Tests do not prove all n/characteristics.

## originality

PASS

Best-of-knowledge originality based on actual compared primary scientific claims and explicit residual risks; inaccessible texts not presumed to be absent or covering.

## value

PASS

Classifying singular strata for hollow symmetric graph-adjacency determinant spaces is an intrinsic projective-algebraic invariant. Unlike unrestricted symmetric determinants, the full diagonal-zero specialization creates exactly n extra singular components with a distinct generic normal quadratic type; closed counts and normality apply uniformly to all n>=5. This is a natural complete structural description rather than an isolated computed example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
