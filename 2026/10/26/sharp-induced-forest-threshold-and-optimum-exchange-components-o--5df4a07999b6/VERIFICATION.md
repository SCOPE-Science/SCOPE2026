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

# Reproducibility

Build and execute the standalone source `verify_kneser_forest.cpp` with a C++17 compiler:

```
c++ -O2 -std=c++17 verify_kneser_forest.cpp -o verify
./verify
```

Observed output from the packaged verifier:

```
n=5 optimum=7 sets=20 components=5 edges=30 VERIFY_OK
n=6 optimum=7 sets=120 components=15 edges=420 VERIFY_OK
n=7 optimum=7 sets=525 components=42 edges=3045 VERIFY_OK
n=8 optimum=8 sets=168 components=8 edges=1680 VERIFY_OK
```

The program independently builds Kneser adjacency; tests all subsets of size \(f(G_n)\) and \(f(G_n)+1\) for each listed parameter; tests detected forests using a second DFS method; generates extremizers from both prescribed constructions; and constructs all optimum exchanges and connected components. This finite coverage does not verify every parameter and is not a replacement for the structural proof of the infinite family.
