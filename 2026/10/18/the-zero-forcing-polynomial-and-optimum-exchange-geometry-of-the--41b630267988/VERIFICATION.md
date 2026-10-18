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

# Finite verification procedure

Run `python3 verify_python.py python_certificate.tsv` and separately compile `verify_cpp.cpp` with `g++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp`, then run `./verify_cpp cpp_certificate.tsv`. Both programs independently enumerate every one of the \(1048576\) twenty-vertex subsets and all minimum-set single-token exchanges; both compute the \(67\) symmetry orbits and all required shortest-path distributions. Compare each generated certificate byte-for-byte against `certificate.tsv` and compare stdout statistics to the included recorded outputs.

Both implementations were executed and yielded the same \(2611589\)-byte certificate, SHA-256 `5ad851a4887bdc203f66f1e52abd7c8a0fa879ff9273a9382ed373a1c145ef01`. The certificate contains every minimum set, all \(178560\) exchange edges and one full shortest-path distribution for each symmetry orbit representative, as well as the complete polynomial. The computations use independent force-closure algorithms, simultaneous versus sequential. The attached code is the reproducibility evidence; logs alone would not prove correctness.

The proof relies on exhaustive exact finite coverage and a specified automorphism group, not on an unproved computational conjecture. The graph is fixed to \(H(5,2)\). There is no claim of external independent audit or family-wide validity.
