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

For d>=2 and B any compact full-dimensional convex base, 0<=t<1, the frustum horizontal section at z is zB, yielding vol_d(P_t)=(1-t^d)vol_{d-1}(B)/d. Let r=h_B(u), l=-h_B(-u), w=r-l=h_{B-B}(u). The exact width W(u,s) over [t,1] has polar vertical-fiber length [2-(1+t)w]/(1-t) for w<=1, zero otherwise. The gauge layer-cake on C=(B-B)° gives ∫_C w=(d-1)/d vol C, hence polar volume [d+1-(d-1)t]/[d(1-t)] vol C. This proves the full base-independent product. Polynomial identities F_d(t)=(sum_{j<d}t^j)(d+1-(d-1)t), F_d′=2(1-t)sum_{j=0}^{d-2}binom(j+2,2)t^j and 2d-F_d=(1-t)^2 sum_{j=0}^{d-2}(j+1)(d-1-j)t^j give monotonicity and exact sharp quadratic gap constants. In d=3 applying the already-known planar Eggleston M2>=3/2 with triangle equality gives exact bound [2+t+t²−t³]/3 and equality classification (triangular bases at fixed t, tetrahedra at t=0). Independently checked both all-d polynomial identities symbolically for d=2..29; source verifier additionally compares 16 direct small-dimensional polar volumes but no infinite-domain conclusions follow from those samples. t=1 is only an affine-normalized limit, not a full-dimensional frustum.

## originality

PASS

Best-of-knowledge PASS for the exact arbitrary-base polar difference-body factorization, sharp interpolation gap and its 3D Eggleston lift. Known planar Eggleston inequality and related Santaló frustum formula are explicitly credited as distinct prior results.

## value

PASS

The Makai difference-body polar volume is a natural affine-invariant functional, and the complete arbitrary-base frustum factorization reduces a d-dimensional geometric problem to dimension d−1 with a universal sharp parameter law. Its exact quadratic stability at the prism limit and sharp 3D lower bound for an entire nonsymmetric base class supply reusable geometric information; Eggleston is a transparently acknowledged input, not repackaged novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
