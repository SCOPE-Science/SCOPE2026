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

# Exact verification

Run `python3 verify.py` with Python 3 standard library only. The script constructs the ten-vertex pentagonal prism as \(C_5\square K_2\); labels all fifteen edges lexicographically; enumerates all \(2^{15}-1\) nonempty graph-edge subsets and independently all recursively generated matchings; and asserts identical 341-face sets and f-vector \((15,75,145,95,11)\).

Next it applies the exact bit-toggle matching at indices 0 through 14, verifies 165 disjoint pairs, constructs all 1,020 directed Hasse incidences, and topologically sorts the entire resulting 341-node graph. It identifies one critical vertex, five critical two-faces, five critical three-faces, and no other cells.

A signed recursive projection along gradient paths constructs the integral Morse boundary, whose explicit 5-by-5 matrix, rank three, and unit three-by-three minor are asserted. Independent simplicial boundary reductions modulo four primes return ranks \((14,61,82,11)\) in degrees one to four. These modular checks corroborate the homology ranks but are not a proof of absence of integral torsion. The integral unimodular minor and cell-attachment proof establish that conclusion.

Expected successful output begins `VERIFY_OK graph_vertices=10 graph_edges=15 faces=341`, followed by the exact Morse matrix and critical-face lists. The finite calculation is exhaustive for this graph; no claim is made about arbitrary wider prisms. Independent audit has not been performed.
