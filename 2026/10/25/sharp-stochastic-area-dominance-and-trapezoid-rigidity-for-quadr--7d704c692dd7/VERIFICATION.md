---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Horwitz's established center-line and squared-area cubic reduce via affine and linear parameterization to f_q(x)=(1−x²)(1+qx) for x uniform on (−1,1), |q|<1 and q=0 exactly for trapezoids. For 0<λ<max f_q the unique superlevel interval has midpoint c>0 and radius h. Equality of endpoint values yields λ=f_q(c)−h²(1+3qc), and exact algebra gives (1−h²)f_q(c)−λ=h²(c²+2qc+qc³)>0 for q>0. Thus h<sqrt(1−λ/max f_q); q=0 yields equality. Direct solve of four line tangencies for trapezoid center c gives det Q=r[1−4c²/(1−r)²]/4 and hence exactly B=sqrt(1−x²). Moments follow by tail integration/Beta function. Independent SymPy confirmed three polynomial identities and the trapezoid determinant, with twelve supporting finite superlevel comparisons. Endpoints are excluded zero measure, parallelograms excluded degeneracy.

## originality

PASS

Horwitz's primary 2010 paper provides the precise cubic squared-area profile, center-line parametrization and uniqueness/max-area statements; those are explicitly prior. The submitted theorem proves a new sharp distributional stochastic comparison across all quadrilateral shapes with strictness/equality at ANY threshold, not an area formula for each ellipse. A 2024 specialized Horwitz monograph appears relevant and was only inspected by description/table of contents, not full mathematical body; its contents remain a priority risk. Best-of-knowledge no equivalent complete stochastic law was found in the reviewed published summaries and accessible primary sections.

## value

PASS

A geometric probability invariant with a natural uniform-center measure and affine invariance; supplies sharp universal distribution and all positive moment inequalities with an exact rigidity class. This is not an arbitrary slice: center location canonically parametrizes all inellipses of any nonparallelogram quadrilateral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
