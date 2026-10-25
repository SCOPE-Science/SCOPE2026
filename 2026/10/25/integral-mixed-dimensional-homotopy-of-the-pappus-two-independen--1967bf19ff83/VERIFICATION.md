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

# Executable verification

Run `python3 verify_pappus_ind2.py` with Python \(3.10\) or newer. No third-party Python packages, data files, or network access are required. The deterministic script builds the graph explicitly from the edge list, enumerates all \(262{,}144\) possible subsets, and checks the face predicate independently via induced connected components. It then constructs the complete sequential-toggle matching, forms the oriented Hasse digraph, and topologically sorts every face. Finally it evaluates the signed integral Morse boundary recursion, including every necessary matched gradient elimination.

Actual observed summary:

```
EDGES 27 PATH_TRIPLES 54 SUBSETS 262144
F_VECTOR [(0, 18), (1, 153), (2, 762), (3, 2394), (4, 4806), (5, 6027), (6, 4428), (7, 1728), (8, 308), (9, 27)]
FACES 20651 MATCHING_PAIRS 10320 RELATIONS 120222
CRITICAL [('0x1', 0), ('0x3330', 5), ('0x6622', 5), ('0x9912', 5), ('0xcc06', 5), ('0x12264', 5), ('0x18886', 5), ('0x21198', 5), ('0x2448a', 5), ('0x2cd02', 6), ('0x300cc', 5)]
SIGNED_MORSE_BOUNDARY [0, 0, 0, 0, 0, 0, 0, 0, 0] REDUCTION_CACHE 933
VERIFY_OK
```

The full face-poset acyclicity check and signed integer arithmetic are finite, exhaustive certificates, not approximations or random numerical experiments. Their conclusions apply to the specifically defined graph, not to an infinite graph class. The homotopy step from the Morse CW complex to the sphere wedge uses the standard Hurewicz theorem. No outside review or independent validation is claimed.
