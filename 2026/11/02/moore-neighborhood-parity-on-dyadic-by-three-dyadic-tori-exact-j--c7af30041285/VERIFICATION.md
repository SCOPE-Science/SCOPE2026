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

# Reproduction and verification

Run `python3 moore_verify.py` from the directory containing this file and `moore_verify.py`. This standalone Python 3 script uses only built-in libraries. It constructs the eight-neighbor update matrices directly from coordinate displacements on \(\mathbb Z/M\mathbb Z\times\mathbb Z/(3d)\mathbb Z\), computes exact ranks of their powers over the binary field, and separately verifies the predicted nullities of \(T^{2^j}-I\).

The successfully reproduced `moore_verify_output.txt` contains fifteen `PASS` cases and a final `ALL_TESTS_PASSED cases= 15`. It covers all pairs \(M\in\{4,8,16,32\}\), \(d\in\{1,2,4,8\}\) satisfying \(3Md\le384\). A separate exhaustive check enumerates all \(2^{12}=4096\) binary configurations for \(M=4\), \(d=1\), finding exactly 256 initially periodic states, 768 states entering after one update, and 3072 entering after two updates, all eventually fixed.

The infinite-family Jordan classification is proved symbolically in `RESULT.md`. Finite computations cannot prove all instances, and no third-party independent verification has been carried out. A literature search does not certify historical novelty.
