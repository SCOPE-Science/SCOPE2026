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

The star matrix preserves the diagonal and restricts to the lift t+c sin t. For c≤2 the lift on [0,π] is below 2π by π+2<2π; for 2<c≤c_* its maximum there occurs at arccos(−1/c)≤2π/3 and is at most 2π/3+c_*<2π. Reflection gives interval invariance, excluding modulo-wrapping branches. A nonfixed two-cycle must use one point x in (0,π) and one y in (π,2π), since each half has a strict displacement sign. Adding the return equations gives sin y=−sin x and forces y=2π−x or y=x+π. The symmetric equation c=2s/sin s increases from 2 to infinity since sin s−s cos s>0; the opposite-phase equation sin x=π/c gives zero, one or two solutions, with its unique c=π solution coinciding with the symmetric one. This gives exactly 0, 1 and 3 primitive cycles in the stated ranges, including the separate critical counts. The sine maximum yields t−π/2=±√(2(c−π)/π)+O((c−π)^(3/2)). The eigenvalues of the constant star matrix on the longitudinal and transverse subspaces are d+1 and 1. Multiplying the matching derivatives at both points gives the stated full-torus spectrum. Below π, 0<c cos s=2s cot s<2 on the symmetric branch, so both squared multipliers are below one; above π, both are greater than one. Opposite-phase cosines have opposite signs and yield 1−(c²−π²) and 1−(c²−π²)/(d+1)². Thus loss of hyperbolic attraction occurs at the longitudinal −1 crossing, with transverse multipliers still in (0,1); an endpoint multiplier of −1 is not by itself a nonlinear stability verdict at equality. At c=π all multipliers are 1 as claimed. Independent replay: python3 /workspace/independent_checks_oct19.py (star_check) evaluated the two-step star map on and off the diagonal, comparing 60 directional derivatives including the endpoints π and c_* for sampled dimensions. The supplied checker was inspected, not executed; no finite sample establishes exhaustion.

## originality

PASS

The scalar map, qualitative period doubling and star quotient are known. The supported distinction is the exact exhaustive zero-drift two-cycle split throughout the stated range combined with the full, dimension-dependent ambient stability classification. Closest catalogue coverage of the symmetric branch was found in a later listed, broader graph result; it does not contain the split opposite-phase cycles or their endpoint. Historical scalar equivalence for an uninspected source remains possible.

## value

PASS

The source's fixed-point regime leaves a natural large-step stability question. Exhausting the diagonal period-two states exhibits a concrete symmetry-breaking transition from one attractor to two, with full-dimensional basins rather than attraction merely inside the diagonal. The exact transverse spectrum shows that longitudinal loss of hyperbolicity is not preempted transversely. This is a useful dimension-uniform benchmark beyond small steps, not a claim about global attractors, other periods or off-diagonal cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
