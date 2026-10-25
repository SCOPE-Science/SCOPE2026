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

# Verification of the finite Kempe census

The structural quotient proof in `RESULT.md` is independent of computation. The labelled distance-shell and exact edge-count assertions have a complete finite witness in `verify.py`. Running `python3 verify.py` (Python 3 standard library, no downloaded modules or files) returned:

```
VERIFY_OK
states=120 edges=360 degree=6 radius=diameter=4
labeled_distance_shells=1,6,25,61,27
palette_quotient_states=20 edges=40 degree=4 radius=diameter=3
palette_quotient_shells=1,4,6,9; line graph of subdivided K5
```

The verifier builds the Petersen graph as the disjointness graph of all ten two-subsets of a five-set. It obtains the entire state set both by complete backtracking over three palette labels and by the explicit canonical partition into large star, small star and triangle followed by all palette permutations. It independently computes every Kempe move with (a) component breadth-first search and (b) disjoint-set union, checks equality of neighbour sets at all 120 vertices, checks undirectedness and degrees, identifies quotient states directly from colour classes, compares quotient adjacency with the line graph of the explicitly subdivided complete graph, and executes all-source breadth-first distances in both graphs. The reported shell totals exhaust their respective vertex sets, and all assertions passed.

The proof does not infer infinite or universal statements from finite enumeration. The computation is exact integer arithmetic and complete search for this specified graph, not a random sample. The code and theorem use the same palette quotient and same connected-component switch definition. No external or independent validation was performed.
