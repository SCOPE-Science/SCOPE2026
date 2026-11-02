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

# Reproducibility and verification scope

Run `python3 verify.py` using Python 3 with the standard library. The program rebuilds the mandatory binary de Bruijn edges, computes the explicit sink-to-source matching and added walks for each order 3–16, extracts an Eulerian covering circle and checks its exact length and coverage. It also independently verifies a 50-degree polynomial-coefficient identity for the claimed generating function and exhaustively rules out shorter words at orders three and four. Successful output ends with `VERIFY_OK`.

A separate integer min-cost-flow calculation was carried out on the full de Bruijn digraph for orders 3–16 (including forbidden vertices and arcs), yielding exact supplementary costs `1,2,4,9,19,37,69,126,227,405,718,1268,2234,3930`. That separate test uses an external graph optimization library and is not a dependency of this package. All-order validity rests on the combinatorial lower bound, bijection, Eulerian construction, and generating-function derivation in `RESULT.md`, not on bounded computation.

This is reproducible self-review. An independent audit has not been performed. Historical priority beyond the inspected literature is not certified.
