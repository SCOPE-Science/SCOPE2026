---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The triangle facet weights reduce Φ_K, by affine covariance and centering, to the equilateral angular logcosh sum F_t(θ)=sum_{j=0}^2 logcosh(t cos(θ-2πj/3)). For x_j the three cosines, x_j^3=(3/4)x_j+(cos(3θ))/4. Newton power sums obey P_m=A P_{m-2}+B P_{m-3} with nonnegative polynomial coefficients and even P_{2m} containing only even B powers. P6=2A^3+3B^2 forces strict cosh-series monotonicity in B² for t>0; hence maxima exactly at |cos3θ|=1 and minima at cos3θ=0. Their radial inverses give sharp reference John radius 2τ(c) and Loewner radius 4 arcosh(e^{c/2})/sqrt(3). Sixfold symmetry and uniqueness imply those extremal ellipses are disks. For arbitrary candidate ellipses, averaging the positive quadratic-form matrices over rotation and convexity of u^T A^-1 u preserve both inclusions, showing BM optimality of the concentric disks, not just a bound. The explicit sixth-order expansions establish 1+(2/405)c²+O(c³) and large c limit 2/sqrt(3)(1-log2/c+O(c^-2)). No polygonal direct covariogram convergence is assumed; smooth-body approximants give only convergence of the facet-defined functional under positive support distances. Independent numerical angular envelope and inverse-level tests at five levels confirmed all formulas within tolerance; the recurrence, not the finite grid, proves all angles and β>0.

## originality

PASS

The 2026 smooth-covariogram paper establishes the logcosh functional in smooth settings but does not give an all-level exact affine-triangle John/Löwner and BM contact profile; the present result makes the specific polygonal facet case mathematically explicit without claiming the invalid nonsmooth covariogram limit. No identical triangular angular theorem or sharp c² coefficient was identified in relevant Resultary/literature checks, with older Orlicz projection-body paper only partially inspected.

## value

PASS

The first nontrivial three-facet-normal instance of a natural Orlicz/projection-body transition is a canonical geometric test case; complete all-level affine ellipsoid contact geometry and the exact quadratic onset of anisotropy are nonroutine shape invariants. The all-triangle reduction and extremal contacts give a usable benchmark for convex-body asymptotics, without pretending it proves broad nonsmooth convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
