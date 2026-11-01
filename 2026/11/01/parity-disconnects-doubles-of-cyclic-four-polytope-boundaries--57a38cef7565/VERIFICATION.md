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

The universal conclusion is proved using Gale's four-dimensional evenness criterion, explicit paths in the doubled graph, and exact graph Euler characteristics. The calculation is integral and requires no computer algebra.

To replay computational corroboration, use Python 3 standard library and execute `python3 verify.py` in this directory. The code independently lists cyclic-polytope facets from exact moment-curve polynomial signs, Gale evenness, and cycle-edge unions; checks their equality; builds the entire doubled graph; enumerates its connected components; and verifies every vertex, edge, and circle-rank formula for \(n=5,6,\ldots,24,28,29,30,31,32\). The final printed line must be `ALL_VERIFY_OK`.

Finite computations do not certify infinitely many values of \(n\). The theorem's all-parameter quantification follows instead from the combinatorial path constructions and facet formula in the proof. No equivariant circle-homology module or higher-dimensional double classification is asserted.
