---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the assigned quartic Q_R, directly recomputed the four homogeneous partials at R=(1:2:3:4), verified all five prescribed points, and independently formed the rational lex Gröbner basis of the projective-gradient ideal at w=1. Its last eliminant is (2z+3)(4z-3)^4(8z+3)/4096, and solving at its three roots recovers exactly the five affine points. On w=0 the three projective charts have no common gradient zeros. At R, Taylor terms of degree <3 vanish and the cubic T=-(3/2)(84s²u-378s²v-252su²+567sv²+74u²v-37uv²) has no critical point on any chart of P²; the triple-point germ is ordinary, with smooth cubic exceptional divisor of self-intersection -3. At R_1,...,R_4 the affine Hessian determinants are 10762227/2, -530181288, 4921675101/2, and -121002336, all nonzero, proving A1. Smoothness of the strict transform on blowing up the moving triple-point section, local Hessian stability at node sections, and properness away from those sections furnish a nonempty Zariski-open parameter neighborhood with no residual singularities. This is an exact witness plus algebraic openness argument, not finite sampling as proof of all parameters.

## originality

PASS

Bauer--Malara--Szemberg--Szpond's exact 2018 family theorem gives a triple point and four further double points. The inspected theorem/projection discussion neither proves their ordinary/A1 analytic types nor generic singular-locus exhaustion. Quartic-monoid background does not by itself imply those family-specific facts; no returned published scientific finding mathematically dominates the combined result. An old-coordinate classical classification is still a risk.

## value

PASS

This identifies the actual generic singularity and resolution type of an early unexpected quartic surface: elliptic exceptional cubic of self-intersection -3 together with four A1 nodes and no others. The resolution basket is a natural invariant useful for geometry of the family and is not a perfunctory point-count or generic smoothness check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
