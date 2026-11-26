---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the stated generator, recovery is equivalent to membership in the helper span by the inclusion of kernels of the corresponding linear functionals. For an affine target, two evaluation helpers must complete a horizontal ternary line, giving (3^m−1)/2; an evaluation and an axis column give 2m+1. Replacing the origin by its systematic copy contributes one more pair exactly for z=0 and y≠0. Two systematic helpers contribute precisely at a nonzero allowed axis displacement. Neither origin position can use the other in a minimal pair. For an axis target two affine helpers differ along that axis: this gives 2·3^m for an unrestricted axis or 3^m for the restricted axis. Admitting the additional origin position adds two or one, respectively. Pure axis pairs and mixed axis/affine pairs cannot yield a different point at infinity. These cases exhaust the last-coordinate and direction possibilities. Only the origin has a projective duplicate. Three distinct projective classes yielding a repair pair form a 3-circuit, with three incidences and two nonzero ternary relations; a triple containing the duplicate positions and a third class cannot have a full-support relation. The summed incidence count is (2·3^m+1)B_m+(2m+2)3^m+4m+1. Independent replay `python3 /tmp/opencode/frozen-independent-checks.py recovery` tested full-support dependencies on position triples, agreeing on every position at m=2,3,4, with 78,443,2938 supports. The replay is finite; the case split supplies the universal proof.

## originality

PASS

The supported distinction is the exact positionwise minimal-pair spectrum for this systematic half-affine configuration. The underlying code, line-repair principle, and aggregate dual coefficient are not independently new. The closest distinct catalogue record counts the same kind of pairs for a different generator; its three-class enumeration does not determine this seven-row classification.

## value

PASS

The number of alternative minimal two-helper pairs at a specified position is a natural local repair invariant of this existing code. The exact spectrum distinguishes axes, affine positions and the duplicated origin, information unavailable from the aggregate dual coefficient or minimum locality alone. It does not claim disjoint repair availability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
