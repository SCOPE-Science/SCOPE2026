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

The independent forest-subset/path-orientation enumerator generates exactly 59,203 distinct augmented faces and the given 10-entry f-vector. A separately implemented repeated-toggle matching has 29,464 pairs and 275 critical cells; full topological sorting processes all 333,390 Hasse incidences without a cycle. Independently constructed signed critical-to-critical differentials have sizes 17x59,59x101,101x98 and compositions zero. Exact integer unimodular row/column operations yield only unit Smith factors of ranks 5,53,4 and zero residual blocks, hence no torsion; reduced ranks in degrees 4–7 are 12,1,44,94. Removing the empty-face matching gives one 0-cell and no 1/2/3-cells, yielding 3-connectivity; Hurewicz yields pi_4=Z^12. The finite enumeration is exhaustive for this one Petersen graph.

## originality

PASS

Qualified best-of-knowledge originality: the exact 30-arc Petersen restriction, its integral Betti quadruple and all-prime torsion-free result were not found in the materially inspected primary texts or Resultary records. The complete directed-graph cycle-free definition is old; the remaining value is an exact new finite natural-graph calculation. Non-detection is not proof of priority.

## value

PASS

The Petersen graph is a canonical smallest ten-vertex cubic graph of girth five. Full bidirection is a natural non-polygonal test for multipath/cycle-free partial-injection topology. Its exact integral Betti groups in four consecutive dimensions, proof of all-prime torsion-freeness, and 3-connectivity give a mathematically motivated finite invariant, not merely a routine tiny-instance check. No general graph family or wedge-of-spheres type is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
