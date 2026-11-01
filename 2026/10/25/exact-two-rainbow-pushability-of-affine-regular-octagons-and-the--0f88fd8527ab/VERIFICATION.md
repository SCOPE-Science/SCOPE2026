---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Support elimination is exact: with q fixed, optimize p linearly under mass and two moment constraints, giving an extreme support <=3; then optimize q similarly without lowering global objective. By dihedral action first support reduces to 10 orbits, while the other is any of 92 nonempty supports of size <=3. Each support feasible set is a compact affine-polytope of dimension at most 2. For a quadratic objective, an interior local maximum can be strictly negative-definite stationary or else moved to a smaller-support boundary (if Hessian has nonnegative curvature or a flat stationary direction). The source exact Q(sqrt(2)) verifier was inspected; a separately programmed exact enumerator solved all 920 support pairs, reproduced 126 admissible interior stationary candidates and maximum 13/16-7sqrt(2)/32, independently reconfirming its per-support table. A separate exact enumeration of the 12 extreme individually-zero-mean laws and all 144 pairs gave max 1/2. The explicit 2+3 support witness satisfies mass and collective balance identities exactly.

## originality

PASS

Martínez-Sandoval and Olvera-Sampieri introduce collective-balance rainbow pushability and general facet-depth bounds, including centrally symmetric bounds, and pose further exact computations; inspected manuscript Sections 3–4 and problems do not compute regular-octagon optimum nor strict collective-versus-separate gap. Similar exact values on other polygons do not imply this 8-vertex probability.

## value

PASS

Rainbow pushability is a newly motivated natural facet-probability optimization. The regular octagon is the first nontrivial centrally symmetric eight-vertex test, and the sharp strict gap shows collective balance permits a genuinely different extremal law despite symmetry; complete exact value is mathematically informative for further classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
