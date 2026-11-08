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

Normalized axial beta density (d+1)(1-u)^d gives E[T²]=2/((d+2)(d+3)), and transverse ball sections give E[X_i²]=(d+1)/((d+2)(d+3)); orthogonal basis yields row kernel 1+a_d x·X+c_d tT. Convexity and rotational symmetry reduce global maximum to axial tips vs equatorial sphere. Symmetric-Z moment comparison gives equator B_d<=sqrt(a_d); the axial A_d>(d+3)/2 dominates for d>=3 since d²>=5, while d=2 follows from exact A_2=10561/4000>sqrt(20/3); d=1 coordinate-exchange symmetry. Integrating beta axial marginal exactly gives the formula. Kernel sign attains norm; indicator of negative kernel gives exact positive-input undershoot. Independent exact rational inequalities passed for d=1..150, and strict d=2 fraction was verified. No finite experiment is used to prove all dimensions. The asymptotic expansion is consistent with logarithmic expansion of exact norm.

## originality

PASS

Best-knowledge original combined exact full-volume Euclidean bicone norm, unique norming tips and negative excursion; generic finite-element stability theorems and nearby exact simplex/cross-polytope metric projections have different operators/measures. The beta integral and apex-vs-equator comparison do not follow from merely quoting broad boundedness of projectors.

## value

PASS

Full-volume rotational bipyramids are canonical pointed convex-body test domains for affine least-squares stability. Their exact sharp Lebesgue constant quantifies dimension-dependent amplification and loss of positivity, and the uniqueness of worst apex geometry is a substantive geometric property not supplied by a trivial covariance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
