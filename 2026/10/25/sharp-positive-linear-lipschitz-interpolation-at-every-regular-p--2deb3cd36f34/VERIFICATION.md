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

# Verification and reproducibility

Execute `python3 pentagon_extension_verify.py` with Python 3 and no third-party packages. The program computes exact rational intervals for the square roots and confirms seven strictly positive expressions: denominator, last coefficient, the two coefficient gaps, amplification above one, and two midpoint coupling margins. It also checks interval enclosures for normalization and saturation of all three vertex-distance orbits.

The independent finite consistency test enumerates the complete set of extreme one-Lipschitz functions on five original vertices, anchored at one vertex. A polytope extreme point has a connected graph of tight distance constraints and therefore contains a signed spanning tree. Exhaustively enumerating 125 labelled trees and 16 sign assignments each, then filtering with exact comparisons in \(\mathbb Q(\sqrt5)\), gives 70 distinct potentials. Their five extension rows satisfy 2,450 vertex–midpoint and midpoint–midpoint inequalities to the declared tight rational-interval tolerance. The final output is `PENTAGON_EXTENSION_CERTIFICATE_OK`.

The source proof establishes the lower bound for arbitrary signed linear extensions through symmetry averaging; the upper bound through a positive explicit operator and two transport plans. It is a proof for the one exact finite geometry, not a computational generalization to other polygons. Equality checks use exact displayed polynomial identities; the program's very small interval widths corroborate them. No independent audit has occurred.
