---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Polar inclusion K°⊂B^d gives an asymmetric parallelotope in dual unit-vector basis w_i. Independent endpoint random variables T_i at 1/alpha_i and -1/beta_i with mean 0 yield E||∑T_i w_i||²=∑||w_i||²/(alpha_i beta_i)≤1. Since ||w_i||≥1, obtain ∑(alpha_i beta_i)^(-1)≤1. Two exact Cauchy–Schwarz steps and AM–GM yield the sharp quadratic and linear sums; equality forces alpha_i=beta_i=sqrt(d) and orthogonal u_i. Tightness of paired frame implies its d vectors sqrt(a_i²+b_i²)u_i form an orthogonal square matrix, so the polar is an axis-aligned box. Gaussian orthant vertex covariance is D+mm^T with D_ii=(1/a_i+1/b_i)²/4≥2, giving tr sqrt≥sqrt2 d by square-root operator monotonicity, with equality balanced. Independent endpoint probability/moment and equalities were algebraically recomputed. This covers all d>=2 under exactly d independent lines, not arbitrary 2d points.

## originality

PASS

Ivanov’s contemporaneous universal conjectures and the Bezdek–Litvak all-configurations linear conjecture are posed, not proved by the inspected bibliographic evidence. The line-paired asymmetric structural class (allowing unequal opposite radii) is more extensive than the equal-length cases advertised in the source account. The argument supplies new polar-parallelotope variance constraints and Gaussian box implication; Resultary searches returned this same record and no stronger proved all-dimensional paired-line classification. Best-of-knowledge pass: the plausible older parallelotope-moment bound and the unavailable full Ivanov source create significant prior-coverage risks, but literature inaccessibility alone does not fail O.

## value

PASS

The canonical cross-polytope combinatorial class is a substantive exact special case of two explicit difficult all-configuration conjectures and a natural vertex-index benchmark. All-dimensional sharp constants and equality rigidity for asymmetric line-paired vertices and paired tight frames furnish reusable structural bounds, not an unmotivated finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
