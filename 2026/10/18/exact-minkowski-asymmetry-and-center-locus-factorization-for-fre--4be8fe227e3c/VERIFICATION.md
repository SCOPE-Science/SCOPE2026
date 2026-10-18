---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The universal result is proved in `RESULT.md` by a factor-face containment argument. The decisive lower bound is the sum of the separate constraints \((h+1)t_i-1\ge s(A_i)\); equality forces all barycentric coordinates and independently forces each factor center to be optimal. The upper bound reflects each generating face into the scaled join and then uses convexity. This checks all quantifiers for \(k\ge2\) and full-dimensional compact convex factors of positive dimension.

The executable `checker.py` was run successfully using the dependencies in `requirements.txt`. It computes the asymmetry directly by linear programming on polytope facet and vertex descriptions, rather than calling the theorem. It passed six binary or higher-arity joins and five factor controls, including a nonsymmetric trapezoid and an asymmetric triangular prism with nonunique centers.

The computational checks are finite examples, not an exhaustive enumeration and not a substitute for the analytical argument. No independent mathematical audit has been performed. Bibliographic coverage may remain incomplete for historical general join identities under alternative terminology.
