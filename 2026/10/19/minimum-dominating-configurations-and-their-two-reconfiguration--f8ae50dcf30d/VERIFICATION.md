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

# Reproducibility and exact finite verification

Graph: \(J(7,3)\), lexicographic ground triples of \(\{0,1,2,3,4,5,6\}\), vertex indices 00–34. Both verifiers enumerate all \(\binom{35}{4}=52360\) four-sets and all their possible one-for-one swaps; no randomized algorithm or time-limited search is used. The Python verifier uses a 35-bit closed-neighborhood union and a constructive geometric family. The independent C++ verifier tests pairs via the two-shadow condition, independently determines owner labels from unions of intersecting triples, and constructs its own reconfiguration graphs and all-root distance matrix.

With the files in a common directory, run:

```sh
python3 verify_python.py regenerated-python.tsv > regenerated-python.txt
g++ -O2 -std=c++17 -Wall -Wextra verify_cpp.cpp -o verifier
./verifier regenerated-cpp.tsv > regenerated-cpp.txt
cmp regenerated-python.tsv regenerated-cpp.tsv
cmp regenerated-python.tsv certificate.tsv
cmp regenerated-python.txt python-output.txt
cmp regenerated-cpp.txt cpp-output.txt
sha256sum certificate.tsv
```

Expected ASCII certificate has 5600 lines: 770 `D`, 2100 `S`, 2730 `J`, in canonical order. Expected SHA-256: `97ffabe0e4e0ab21199e85ecfea0697de63fb6b375a70e72197515d5aabade5b`. Both recorded logs are the actual output of the standalone sources; the certificate and logs were regenerated and compared byte-for-byte.

The verifier reconstructs every minimum dominating set and every possible move. Every-representative BFS computes the eccentricity of all 770 jumping configurations; component BFS checks slide radius 2 and diameter 3. The geometric classification, two orbit sizes, types, degree distributions and Kneser quotient are checked independently.

**Limits.** This is finite exhaustive proof for \(J(7,3)\), not infinite Johnson-graph certification. An independent external mathematical audit has not taken place, and inaccessible literature introduces a bounded originality risk. No arbitrary code path, graph instance, or precomputed log from another run is needed to regenerate the certificate.
