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

An MMD pair can only be strongly resolved by one of its endpoints: a geodesic from a third resolving vertex would extend past an endpoint and produce a neighbor farther from the other endpoint. Conversely any shortest path can be extended as a contiguous subpath to a maximal geodesic, whose endpoints are MMD; a cover then resolves the original pair. Thus sdim=50-alpha(R). I independently reconstructed distances by simultaneous shortest-path relaxation from the two layer representatives, recovered the frozen distance rows and checked all 1225 pairs for mutual maximality. R has only the outer steps ±5,±7,±9,±11,±12 and inner steps ±9,±11 (125 and 50 edges). In the outer component rotate a nonempty independent set to contain 0: its 14 other available indices are partitioned into the five exhibited cliques, giving at most six. In the inner component the cycles t+9j for j=0,...,4 and t=0,5,10,15,20 close by an allowed step and partition the vertices (9 is invertible modulo 5); each supplies at most two independent vertices. The displayed witnesses realize both bounds. An independent take-or-skip bitset recurrence also gave independence numbers 6 and 10, and the complement directly resolved all 1225 pairs. Own replay: python3 /workspace/evidence/5/check_dimension.py. Frozen BFS and Floyd programs and outputs were inspected, not executed. The 2015 prediction comparison is correct; the published upper bound is not contradicted. The 2017 formulation is a bibliographic detail with the access limitation below.

## originality

PASS

The supported distinct contribution of the October record is the exact 34-versus-35 counterexample with matching structural optimality certificates. The closest primary theorem proves only an upper bound. A distinct November 22 Resultary result exactly covers the numerical value and the counterexample and goes further by classifying the bases; it is expressly credited. Its declared publication date is after the frozen source's October 18 publication date. It is not demonstrated prior coverage of the October finding, and the catalogue chronology does not establish independent discovery or wider priority. No earlier covering exact result was verified.

## value

PASS

This one 50-vertex case directly refutes a named equality for every k>=5 at k=6 rather than extending a table for its own sake. The compact clique and odd-cycle certificates explain why the value is exactly 34 and provide a witness any proposed replacement formula must fit. No full odd-order classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
