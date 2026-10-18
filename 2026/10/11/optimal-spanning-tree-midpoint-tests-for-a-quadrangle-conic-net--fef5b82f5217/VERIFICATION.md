---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For a quadratic H restricted to an edge, phi prime at 1/2 equals H(v_j)-H(v_i). The four-vertex degree<=2 evaluation E has rank four and its two-dimensional kernel is the opposite-side conic pencil; the net is E inverse of the all-equal diagonal. Tested edges enforce constant E(H) on connected components, yielding exactly the net iff graph connected. If disconnected, surjectivity gives an outside polynomial, and adding a nonzero pencil member yields a genuine degree-two outside conic. Cayley gives 16 spanning trees; two opposite-pair members of the second pencil give six incidences. This is universal in the stated nondegenerate characteristic-ne-2 setting.

## originality

PASS

The originating quadrangle conic-net paper gives six-side criterion and reports a reduction to a four-side test, but the inspected accessible abstract and frozen result do not establish this optimal connected graph criterion. No independently retrieved Resultary theorem dominates the three-side classification. Full original paper unavailable this execution, so noncoverage of its full text is not claimed.

## value

PASS

This exactly minimizes a natural geometric membership test central to the originating net theory, classifies all minimal tests (16 trees), and gives a usable finite entanglement certificate. Excludes degenerate quadrangles and does not claim six entanglement incidences globally minimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
