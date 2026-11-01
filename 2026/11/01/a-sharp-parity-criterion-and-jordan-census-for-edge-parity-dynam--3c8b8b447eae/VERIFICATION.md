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

# Reproduction and limits

The two independent source files are `verification/verify_hamming.py` and `verification/verify_hamming.cpp`; their captured output files have matching names with `_py.out` and `_cpp.out`. From the package root, run:

```
python3 verification/verify_hamming.py
g++ -std=c++17 -O2 -Wall -Wextra verification/verify_hamming.cpp -o verify_hamming
./verify_hamming
```

The Python code constructs each factor product, its edge set, the incident-vertex masks, and the line-graph neighbor matrices using bit vectors. It computes the first three powers and rank by binary elimination; it checks the formula in fourteen all-even tuple sizes, including \((4,4,4)\) with \(288\) edge vertices, then verifies a nonzero fixed-edge witness for seven odd-factor sizes. The independently written C++ code constructs line-graph adjacency directly by testing endpoint overlap of edges obtained from coordinate changes, checks seven even tuple sizes, and enumerates all binary configurations for \((2,2)\), \((2,2,2)\), and \((2,4)\), with \(4\), \(12\), and \(16\) edge vertices respectively. The exact resulting extinction-time populations are \((1,3,12,0)\), \((1,63,960,3072)\), and \((1,1023,15360,49152)\), in times zero through three.

The programs test samples, not the infinite parameter family. The universal assertions follow from the incidence-product proof in RESULT.md. The extension from binary fields to arbitrary finite characteristic-two fields is algebraic, because all matrices and rank arguments are defined over the prime field and remain valid under extensions. The code is self-contained with Python standard library and a C++17 compiler; no undisclosed external certificate or independent audit is claimed.
