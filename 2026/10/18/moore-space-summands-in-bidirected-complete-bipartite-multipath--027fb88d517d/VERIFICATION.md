---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Every multipath arc of bidirected K_{2,n} meets one of the two degree-limited central vertices. At most one selected incoming and one outgoing arc per central vertex means every simplex has at most four arcs; enumeration of all arc subsets of size 0..4 is fully exhaustive, not sampled. For n=3,4,5,6 the augmented face counts are 115,313,711,1417 and the signed acyclic discrete-Morse reductions leave critical cells in dimensions (1,2): (1,6), (2,3): (8,1), (2,3): (1,32), and 3:169. All matched incidences are units and the integral reduced boundary contents are 0,2,2,0, giving S1∨6 S2; 7 S2∨M(Z/2,2); M(Z/2,2)∨31 S3; 169 S3 respectively. Unimodular basis changes in wedges of simply connected spheres realize the Moore-space cofibers. The two source verifier algorithms were inspected: one signed gradient projection, another independent signed integral unit-pivot cancellation. Separately an independently written exhaustive face and F2 boundary-rank implementation recovered all four face vectors and Betti vectors. Full integer matching verification was examined in actual code, not asserted merely from prior PASS logs. Graph directed 2-/4-cycle closure forces any nonempty dynamical region to include all arcs, so each G_n is itself the unique dynamical module and is unstable.

## originality

PASS

Best-of-knowledge comparison of the exact claim against named closely related published results, semantic Resultary search and inspected primary scientific material; unsuccessful retrieval is not treated as evidence of absence.

## value

PASS

Four complete exact natural finite graph homotopy types with genuine integral 2-torsion, plus concrete unstable dynamical-module counterexamples to a published torsion-implies-stability conjecture, are mathematically motivated and not mere table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
