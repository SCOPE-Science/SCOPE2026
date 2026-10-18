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

The classification has a self-contained C++17 enumerator and an independent Python 3 certificate checker. Execute the following commands in one directory containing the bundled files:

```sh
g++ -O2 -std=c++17 exhaustive.cpp -o exhaustive
./exhaustive representatives.tsv > reproduced_summary.txt
cmp summary.txt reproduced_summary.txt
python3 check_certificate.py representatives.tsv > reproduced_check_output.txt
cmp check_output.txt reproduced_check_output.txt
```

The C++ enumerator covers every \(a\)-by-\(b\) Boolean incidence matrix for \(a+b\le9\), checks connectivity, computes a complete canonical key under within-side permutations and swapping equally sized sides, and applies globally synchronized colour refinement. The resulting connected bipartite isomorphism counts for orders one through nine are \(1,1,1,3,5,17,44,182,730\); logical equivalence counts are \(1,1,1,3,5,17,44,182,728\). Two doubletons occur at nine vertices.

The Python checker separately verifies that the supplied canonical representatives are pairwise nonisomorphic and connected, redoes the stable-colour grouping, and verifies that the two pairs have four-cycle counts \((2,0)\) and \((6,4)\). The C++ sweep, rather than the Python checker, supplies completeness of the representative list. All comparisons are exact. This is reproducible computational evidence plus the mathematical coverage argument in `RESULT.md`, not an independently conducted audit or external certification.
