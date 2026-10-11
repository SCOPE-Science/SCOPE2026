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
# Reproducibility and limits

All tests use standard-library Python 3.10 or newer and have no network dependency. Run the two programs in the same directory as the supplied files:

```sh
python3 verify_morse.py
python3 verify_modular.py
```

The first program generated and exhaustively verified \(3468\) nonempty faces and the full face vector \((17,136,612,1122,952,476,136,17)\), the graph's \((17,8,3,4)\) intersection parameters, \(1711\) matched face pairs and the topological ordering of all \(15300\) directed incidences. It computed one critical zero-cell, five critical two-cells and forty critical three-cells. It computed the signed integral Morse boundary and checked a four-minor with determinant \(-1\), a five-minor with determinant \(-3\), and the modular ranks that force Smith factors \((1,1,1,1,3)\). Its canonical matrix digest is `2947ab3b904e0bdbad58376aa448307433649868212a401978108cedbd4f078a`.

The second program reconstructed faces independently by nonempty common-neighbor intersections, not by enumerating subsets of the seventeen facets, and recomputed all simplicial boundary ranks in three characteristics. In degree order from one through seven, these boundary ranks are \((16,120,492,595,357,119,17)\) in characteristic two, \((16,120,491,595,357,119,17)\) in characteristic three and \((16,120,492,595,357,119,17)\) in characteristic five. The corresponding reduced homology dimensions are \(35\) in degree three for the first and third fields, and \(1\) in degree two with \(36\) in degree three for the middle field.

`morse_boundary.json` stores all critical masks and the full \(5\)-by-\(40\) matrix in unambiguous row/column order. The rank information over fields is a cross-check only; the integral homotopy conclusion depends on the signed matrix, its determinants, the acyclic matching and the attaching-map argument. Exhaustion is limited to this finite graph. Bibliographic priority outside inspected sources and independent external validation are not asserted.
