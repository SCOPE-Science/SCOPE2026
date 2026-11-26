---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the dual group algebra a time step sends a site functional to its product with W=X+Y. Substitution X=W+Y carries the defining ideal to (W^L,Y^s-1), since L is a power of two and s divides L. Thus the time span is a module over F_2[W]/(W^L), free of rank s before any sensor restrictions. Modulo W each sensor is exactly the basis element Y^(i+j mod s). Missing a basis element prevents spanning; choosing one of each gives a matrix invertible modulo W and therefore invertible over the nilpotent extension. This proves the criterion for all sets, even for indefinite readings since W^L=0, and the linear dimension bound excludes fewer than L frames with s sensors. Each class has L sites, yielding L^s optimal sets and the claimed inclusion–exclusion formula at all cardinalities including k=0 and k=Ls. For r fixed the class-avoidance probability is the product of 1-rL/(Ls-i) over 0<=i<k. Its logarithm is -rk/s+O_r(k/s^2+k^2/(Ls^2)); both errors vanish uniformly for L>=s in the critical window. Consequently the empty-count factorial moments converge to those of Poisson(e^(-c)), giving the zero-empty probability, or equivalently the same result follows by finite Bonferroni bounds and then sending their truncation to infinity.

## originality

PASS

Known observability-rank criteria and occupancy arguments are credited as ingredients. The supported distinct contribution is the exact all-placement classification and resulting census and critical window for the specified two-dimensional torus. The closest CA results use different dynamics or occupancy events; none of the inspected statements evaluates this torus rank in terms of the claimed diagonal geometry.

## value

PASS

For a natural finite linear dynamics the result replaces a rank test on Ls initial coordinates by a complete geometric criterion. It establishes that the information lower bound is attainable, identifies every minimal set, and distinguishes deterministic optimum s from typical fixed-size sampling at s log s. The inclusion–exclusion and Poisson calculations are routine once the partition criterion is known, but together quantify the practical difference between designed and unstructured placement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
