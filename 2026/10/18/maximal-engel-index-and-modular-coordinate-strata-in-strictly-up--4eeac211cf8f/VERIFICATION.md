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

# Checks and reproducibility

The file `verify.cpp` is standalone C++17. Compile using `g++ -O3 -std=c++17 verify.cpp -o verify` and run `./verify` in a directory containing the extracted source.

Each enumerated matrix is built explicitly from its strictly upper-triangular entries. The test forms the commutator on all matrix-unit inputs of degree one, iterates it \(n-2\) times, checks the terminal \((1,n)\) coefficient individually, checks all other coefficients vanish, and compares the resulting maximal-index classification to the closed-form zero-pattern condition. All enumerated matrices in each test case are processed, not sampled.

Expected counts include \((q,n)=(2,3):6\), \((2,4):24\), \((2,5):320\), \((2,6):3072\), \((3,3):24\), \((3,4):540\), \((3,5):23328\), \((4,3):60\), \((4,4):2880\), and \((5,4):14000\). Characteristic-two arithmetic for \(q=4\) uses an explicit irreducible quadratic extension.

These finite checks validate the implementation on small fields and dimensions only. The all-dimensions and all-prime-powers statements are established by the independent symbolic proof in `RESULT.md`, whose key nontrivial identity is the terminal adjoint-power formula. The scope excludes lower Jordan-block enumeration and independent mathematical certification.
