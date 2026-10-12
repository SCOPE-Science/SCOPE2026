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

The theorem is proved symbolically for every integer \(q\geq3\) by the equivalence to three-edge-path-free bipartite graphs, the classification of inclusion-maximal star forests, and a two-sort labeled exponential formula. The standalone checks do not establish its infinite quantifier on their own.

Run the Python-standard-library file with `python3 saturation_formula.py`. It prints the exact cardinality polynomials for \(3\leq q\leq8\) as CSV rows to stdout and terminates with `FORMULA_VERIFIED` on stderr. The provided `spectrum.csv` contains the CSV stdout.

Compile `brute_maximal.cpp` using `g++ -O3 -std=c++17 brute_maximal.cpp -o brute_maximal`. Run `./brute_maximal 3`, `./brute_maximal 4`, and `./brute_maximal 5`. Expected maximal-family counts and size distributions are respectively \(21\) at sizes \((3,4)\) with counts \((12,9)\); \(264\) at sizes \((4,5,6)\) with counts \((104,144,16)\); and \(3355\) at sizes \((5,6,7,8)\) with counts \((530,1800,1000,25)\). The exhaustive algorithm explicitly checks every absent column for extension. It does not inspect sizes \(q>5\); those follow from proof and the separate coefficient recurrence.

The two programs implement different checks: one counts star-forest components and partitions, while the other directly enumerates candidate column subsets and detects forbidden triples. The general theorem does not rely on an assumed absence of higher-order counterexamples.
