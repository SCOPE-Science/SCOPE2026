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

# Reproduction and precise verification boundaries

Compile and run the complete standalone verifier with a standard C++17 compiler:

```sh
g++ -O3 -std=c++17 -o verify verify.cpp
./verify
```

No network, scientific libraries, external data or precomputed matrices are needed. The code constructs the twenty labeled vertices and thirty graph edges explicitly. It independently tests induced acyclicity by disjoint-set union and graph traversal for all 1,048,576 subsets, then exhaustively verifies a matching on every valid face. The topological sort verifies acyclicity across every face incidence, rather than using sampled gradient paths.

For the only nontrivial signed integral Morse boundary, the code uses increasing vertex order for simplicial orientations and recursive gradient-path elimination. It checks the 34-by-90 matrix's 125 signed unit entries, performs integer row/column transformations and checks that 24 unit pivots leave a zero residual. Thus the conclusion has no unidentified torsion or hidden nonzero differential. The recorded execution log is included as `VERIFY.log`, but the log alone is not a substitute for compiling and checking the source.

This exact finite proof covers the complex of induced forests of \(GP(10,2)\) only; it does not generalize to arbitrary graph families, compute an automorphism module, or provide an independent external audit. Known theoretical inputs are the elementary signed simplicial boundary, discrete Morse acyclicity-to-CW reduction and classification of maps between equal-dimensional simply connected sphere wedges by degrees. Independent audit status remains not performed.
