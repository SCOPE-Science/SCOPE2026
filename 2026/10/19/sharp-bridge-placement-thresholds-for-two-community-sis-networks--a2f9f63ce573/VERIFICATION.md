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

The repaired RESULT.md closes a genuine proof gap in the frozen minimum: (lambda+1)hY>=(k+h)X does not alone imply lambda hY>=kX. Multiplying the former inequality by its exact row/column swap, cancelling XY and taking positive square roots gives lambda h>=k, with equality iff both incidence estimates are equalities. Perron positivity then forces, and is consistent with, unit degree on all occupied rows and columns. The frozen maximum can be reconstructed via the Schur complement and the Frobenius-norm bound from counting intersecting edge pairs; strictness for a nonstar follows from the incidence count, and the rank-one common-endpoint case saturates both bounds. The scalar root equation has a unique crossing because the positive resolvent coefficients decrease strictly. The two excess radii stay bounded (at most 1 for the matching and strictly less than 2 for the other extremum), so dividing their equations by n and n² respectively and taking limits establishes the asymptotics. For the stated deterministic map, linear domination gives subcritical decay. At criticality the positive Perron functional decreases strictly in the interior; a nonzero limit point would propagate to the interior by connectedness while preserving the limiting functional value, a contradiction. Above criticality the small positive subsolution, all-ones supersolution and strict radial subhomogeneity prove the unique interior equilibrium and convergence from nonzero data. The repair also distinguishes the exact algebraic witness from the bundled spectral computation, which does not simulate the map. The all-placement finding survives with its assumptions unchanged.

## originality

PASS

After proof repair the supported distinct result is the exact adjacency-radius optimization over all fixed-count cross-edge sets of two equal cliques, its equality classes and the joint asymptotic. The deterministic threshold and the idea of using topology to separate threshold regimes have prior overlap and are not claimed as standalone innovations.

## value

PASS

For the natural constrained joining of two complete graphs, the result identifies exact extremal radius values, rigidity of the equality cases, and the asymptotic scale on which the reciprocal radii separate. Community-local adjacency data and bridge counts alone cannot recover that distinction. This quantifies a structural ambiguity rather than presenting two arbitrarily chosen graphs or a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
