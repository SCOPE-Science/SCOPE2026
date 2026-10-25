---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For q=t^h (t a prime power >=3, h>=2), the F_t-linear additive map s↦s^t-ms has kernel of dimension 0 or 1; every nonempty affine section of YZ^(t-1)=X^t has 1 or t rational points. The t-secant point sets are exactly cosets of one-dimensional F_t-subspaces. q+1 points and line capacity t require at least q/t+1 lines, attained by a parallel class plus Z=0. At equality, >=2 lines through infinity or a submaximal affine secant leave >=t-2 uncovered affine points even after the at-most-one contribution from the infinity line, hence exactly one infinity-line and all remaining maximal secants. When h=2, two nonparallel secants force each further secant to intersect their union, leaving at most t^2-t+2 < t^2 total affine points after infinity line: impossible. There are t+1 affine directions and t^2+1 infinity-lines, hence (t+1)(t^2+1) optimal covers. For h>=3, replacing the t u-direction cosets inside a 2-dimensional F_t-subspace by its v-direction cosets switches a parallel spread to a genuinely two-direction spread without changing cover size. Finite F_9 independent enumeration of the twelve maximal three-secants gives exactly four affine partitions and 40 optimal covers, corroborating h=2 but not proving infinite claims.

## originality

PASS

Compared mathematical implications against primary literature, Resultary semantic findings, aliases and broader formulations. Best-of-knowledge priority only. No identified broader prior theorem logically supplies all three ingredients. At h=2, two nonparallel affine lines intersect but alone do not imply all candidate optimal covers are parallel until the full incidence bound is applied.

## value

PASS

The problem is a natural exact finite-field rational-point covering invariant of a geometrically integral plane curve, with a sharp lower bound and nontrivial equality classification. The h=2 parallel-class rigidity, exact minimizer count and h>=3 switching boundary are structural finite-geometry information useful for organizing optimal covers and not a mere reparameterization of the standard affine spread facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
