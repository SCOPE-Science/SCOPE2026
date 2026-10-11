---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The second variation reconstructs consistently from the source first-variation formula. At a geodesic sphere, δW=-∇²u-csc²(R)u Id and symmetry of normalized E_j give the stated δE_j. Differentiating A_{j-1}, subtracting the composed lower-quermassintegral second variation, and adding the Psi'' chain term cancels all index dependence except (k-l)d_{k+1}cot^k(R)/n and converts the zeroth-order term into variance about the mean. The round-sphere Laplace spectrum then gives kernel exactly degrees 0 and 1 and sharp next gap (n+2)csc²(R), attained by degree 2. The fetched verifier checks these coefficient cancellations for dimensions 2 through 12 and all index pairs; enumeration is only corroborative.

## originality

PASS

Originality passes. Luo--Wei--Zhou's full HTML gives the complete spherical Alexandrov--Fenchel inequalities, equality balls, and first-variation identities, but a full-text search finds no second-variation statement. Existing quantitative nearly-spherical work includes Euclidean/hyperbolic results and some spherical stability, but no checked source gives the all-pair exact Hessian, common Poincare form, kernel, and sharp degree-two gap.

## value

PASS

The full spherical Alexandrov--Fenchel family was only recently proved, so its exact quadratic stability structure at equality is an immediate natural next question. Showing every pair has the same shape Hessian up to a scalar and identifying the complete equality-mode kernel and sharp degree-two gap gives reusable local geometry beyond the global inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
