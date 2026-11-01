---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Affine coordinate change reduces each parallelepiped to uniform [-1,1]^d; the affine polynomial orthonormal basis {1,√3 y_i} gives reproducing kernel K(x,y)=1+3Σx_i y_i. For |f|≤1 the exact norm is max_x∫|K(x,y)|dμ(y), attained by sign K. Convexity in x forces a maximum at a cube vertex; symmetry makes all vertices extremal. Thus Λ_d=E|1+3ΣY_i| for independent uniform Y_i∈[−1,1], and nonnegative f defect equals (Λ_d−1)/2 (negative-part kernel integral). The Irwin–Hall clipped-cube CDF integrated at a=(3d+1)/6 yields the stated exact rational binomial formula. Jensen conditional on adding one symmetric uniform makes Λ_{d+1}>Λ_d strictly, while exact Λ4=75437/25920<3 and Λ5=46973/14580>3 give first f≥0 excursion below −1 at dimension 5. Fourier |z| representation and controlled sinc^d/cos expansions give Λ_d=√(6d/π)(1+13/(60d)+o(d−1)). Independent exact-Fraction checker computed all Λ1…12 and verified first five, strict growth in those dimensions and the crossing; the analytic derivation proves all d and the asymptotic.

## originality

PASS

PASS best of knowledge for the continuous uniform parallelepiped exact affine-projector norm, positivity cutoff and two-term asymptotic. Standard kernel and Irwin–Hall formulas are prior tools; the simplex, discrete Boolean cube and general manifold projector sources have different measures/objects and cannot entail this exact value without additional proof.

## value

PASS

Unweighted local least-squares affine projections on parallelepiped elements are canonical in approximation and numerical analysis. The sharp L∞ stability constant, precise first dimension of severe positivity loss and contrasting √d versus simplex d growth give a motivated geometry-dependent classification, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
