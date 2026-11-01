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

# Reproduction

Compile `verify_kg73.cpp` as C++17, for example `g++ -std=c++17 -O2 verify_kg73.cpp -o verify_kg73`. Run `./verify_kg73` and `./verify_kg73 --reverse`; these write the six ASCII integer boundary matrices in the current working directory. Run `python3 verify_integral.py`, with SymPy installed, to check their exact Smith normal forms and differential compositions. Compare the output with `verification_output.txt`. No network access or third-party research paper is needed to reconstruct the certificate.

The generator enumerates all 1,278,686 faces, including empty, and all 639,283 forward or 639,293 reverse matched pairs. It checks all matched upper cells in a complete acyclicity traversal, computes the signed integer Morse boundary maps, and protects against signed 64-bit coefficient overflow. The Python checker computes Smith normal forms over the integer domain, not floating-point approximations. The six numerical boundary matrices are supplied as standalone evidence, not substituted from another example.

The calculation establishes integral homology only. It does not certify an integral homotopy decomposition or an infinite family. External independent audit has not been performed.
