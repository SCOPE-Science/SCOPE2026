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

Exact spectral normalization gives (3/4)R=I-vvᵀ, and diag R=1 forces v_i²=1/4. Thus the three sign-multiplicity orbits, modulo global sign, exhaust the feasible covariances. For unit Gram vectors in R³, the distributional Laplacian of their maximum linear form has jump density ||u_i−u_j|| on the parts of the tie planes where the pair dominates; three distinct unit vectors cannot be collinear, so triple ties do not add surface mass. Euler homogeneity and Gaussian integration by parts convert this to the expected maximum. The plane Gaussian mass is its domination wedge probability divided by √(2π); this also covers correlations ±1. Substitution of the signed Gram entries yields same-sign distance √(8/3), opposite-sign distance √(4/3), and projected correlations 1/3 (all same), 1/√3 and 0 (one flip), −1 and 1 (balanced), respectively. As a check bypassing facets for the minimum, the balanced realization has common third coordinate 1/√3 and planar vertices ±√(2/3)e_1, ±√(2/3)e_2. Its mean maximum is √(2/3) times E max(|G_1|,|G_2|)=2/√π, by the half-sum of |G_1+G_2| and |G_1−G_2|. For the strict comparisons, arcsin(1/√3)>1/√3 and π<4 give the lower bound in lines 89–94, while 2 arcsin(1/3)>arcsin(1/√3) gives the upper orbit comparison. The independent-three-normal baseline follows by integration of 3xφ(x)Φ(x)^2 and gives the stated gap. The frozen code and recorded quadrature were inspected, not executed.

## originality

PASS

Supported for the sharp constrained minimum and its equality orbit, not for a new four-normal integration formula or the unconstrained tetrahedron maximum. The closest exact-object prior gives a positive but nonsharp gap; the general four-variable width formula provides objective values but not the constrained extremum and minimizer classification.

## value

PASS

This is the first nondivisible case in rank three of a previously defined exact-spectrum minimization family, not a slice selected from an arbitrary covariance matrix. It gives the exact positive gap and its unique optimizer, which the nonsharp divisibility theorem does not determine. The finite proof compares all feasible geometries, showing that a coplanar square Gram hull minimizes despite rank-three covariance, and distinguishes this constrained minimum from the regular-tetrahedron maximum. The individual closed forms are prior-formula evaluations, not a separate value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
