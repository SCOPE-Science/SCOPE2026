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

A shortest cube path flips distinct bits; a missing bit extends it, so maximal paths are exactly diameter geodesics with d+1 vertices. The elementary floor/ceiling volume bounds follow. The independent checker reconstructs Q4 from all five-vertex subsets with connected induced path and antipodal endpoints, then tests disjoint pairs and triples: 192 paths up to reversal, 31 disjoint from the canonical path, 2976 pairs and zero triples. This exhausts the path sets, since a shortest path in the cube is induced and its vertex set determines it up to reversal. The check separately validates the stated Q4/Q5/Q6 paths and uncovered sets {8,9,10,11,12,14}, {10,19}, {47}; the extra Q6 path includes 47 and completes the ten-path cover. The Q1–Q3 bounds are attained, including the two explicit Q3 paths. Independent replay: /workspace/branches/c3876b29-a911-49f0-b4d0-8230a63c51d0/qpack_independent_check.py and qpack_independent_check.out in the same directory. The frozen verifier was read, not executed; replay is bounded finite evidence, not Lean or expert attestation.

## originality

PASS

Credit the established invariant, volume bounds and Cartesian-product framework. The checked comparisons support the exact small-cube results, particularly the Q4 obstruction and polynomial, and the Q6 packing witness; the covering upper bound is a consequence of that witness, not a separate general theorem. No mathematical coverage of those claims was established in the inspected sources.

## value

PASS

This gives the first strict dimension for a natural bound, an exact count at that obstruction, and subsequent sharp constructions. The one-vertex deficit in Q6 connects two motivated packing and covering invariants and resolves the minimum cover there. These are small exact cases but not arbitrary instances or repeats of the volume calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
