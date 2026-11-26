---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The normal covector under the affine map is A^(1/2)u, of length sqrt(q). The hyperplane volume multiplier is sqrt(det A)/sqrt(q); the ball slice at signed distance (±1−t)/sqrt(q) gives the remaining power and hence the q^(−d/2) factor. Interior containment gives q>(1+|t|)^2. On the allowed interval h(x)=log(q−x²) is strictly concave, so [h(1−t)+h(1+t)]/2≤h(1), strictly unless t=0. The centered profile has log derivative (d−q)/(2q(q−1)), hence the unique optimum at q=d, with the stated constant. All-direction equality forces c=0,A=dI; equality of the spherical geometric mean forces all-direction equality by continuity and full support. For any other λ>1, a centered determinant-preserving perturbation along the first diagonal entry of diag(1,−1,0,…) with signed ε moving q towards d improves the section pair; λ>1 keeps strict containment for small ε. At (d,0) the first derivatives vanish and the log-pair Hessian is diagonal with entries −1/[2d(d−1)] and −(d+1)/(d−1). Substitution of q−d=εd uᵀHu+O(ε²) and t=εu·b and the fourth and second spherical moments reproduce both quadratic coefficients, uniformly by compactness of the sphere. The integrated deficit has strictly positive coefficients on tr(H²) and ||b||², including d=2.

## originality

PASS

Credit the affine section formula as existing coverage. Pairing that prior formula and optimizing its scalar profile gives the basic bound and directional equality by a short calculation, so those should not be treated as a new slice identity. The supported distinct content is the combined antipodal fixed-volume optimization, identification of the single universally pointwise-optimal reference scale (including feasible improving volume-preserving deformations off that scale), and the exact integrated translation/shape second variation. No retrieved stronger extremal or stability theorem subsumes that combination.

## value

PASS

The geometric comparison has a natural constraint and statistic: fixed enclosing volume, paired sections by the inner ball's two opposite supports. It identifies an exceptional radius, gives the exact directional equality condition even for translated bodies, and separates the shape and translation costs in the logarithmic averaged deficit. This is useful sharp local information about a natural extremum, not novelty in the affine section formula or a claim of global metric stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
