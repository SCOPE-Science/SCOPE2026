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

# Verification evidence
The theorem and proof are self-contained in `RESULT.md`. Reproduce with `g++ -std=c++17 -O3 verify_direct.cpp -o verify_direct && ./verify_direct` and `python3 verify_parametric.py`. The C++ verifier exhausts every length-two prefix subset for labeled alphabet sizes 2–5, derives the full compatible suffix set, and independently counts codebooks. The Python verifier checks the separate partition-based parameterization for sizes 2–35. Recorded outputs are in `verification_output.txt`; direct enumeration is finite and is not an infinite certificate. The exact proof supplies the all-parameter step. The source comparison has a residual priority risk because the 2023 Cai paper was not read in full. Independent audit has not been performed.
