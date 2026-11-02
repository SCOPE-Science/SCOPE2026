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

# Finite verification and reproducibility

`verify_bruteforce.py` is self-contained Python 3 code. Execute:

```sh
python3 verify_bruteforce.py
```

The checker enumerates all minimum-cardinality dominating configurations from board-square combinations using the actual rook adjacency relation, builds the jump graph by testing replacements, and checks order, size, degree distribution, and (for small square cases) all eccentricities. The recorded terminal marker was `ROOK_BRUTEFORCE_PASS`, together with `RECTANGLE_PASS` markers for \((2,3),(2,4),(3,4),(3,5)\). Recorded square counts \((|V|,|E|,\mathrm{radius},\mathrm{diameter})\) were \((6,12,2,2)\), \((48,234,3,3)\), \((488,3936,4,5)\), and \((6130,72100,5,7)\).

`verify_structural.cpp` is independent C++17 with no third-party dependencies. Execute:

```sh
c++ -O2 -std=c++17 verify_structural.cpp -o verify_structural
./verify_structural
```

It constructs minimum placements from independent row-function and column-function encodings, deduplicates their bit masks, forms exact jump adjacencies and breadth-first distances, and tests every orbit under row/column permutations and transpose. Its recorded terminal marker was `ROOK_STRUCTURAL_PASS`. For sizes \(2,3,4,5,6\) its computed vertex counts were \(6,48,488,6130,92592\), and edge counts \(12,234,3936,72100,1507680\). The respective observed radii and diameters were \((2,2),(3,3),(4,5),(5,7),(6,9)\).

These executions substantiate finite instances only. The proof in `RESULT.md`, including the permutation assignment argument and sharp extremal lower bound, is what covers every allowed board size. No separate external mathematical audit or proof-assistant certification is claimed.
