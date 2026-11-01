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

# Verification and reproducibility

`code/verify_scan.py` computes the original sequential update one visited vertex at a time and, independently, the transformed direct-sum update. It verifies equality on every binary initial state for even graph orders 4, 6, 8 and 10 and all admissible matching sizes. It also checks the full sweep order and fixed-population formula for each divisor of that order. The included output reports 7,728 examined states.

`code/verify_direct.cpp` uses a separate bitwise implementation of the graph update and enumerates **all** binary states for even orders from 4 to 16, all matching sizes. It detects least periods by actual recurrence and compares the counted divisor-fixed states and maximum period with the formulas. The included output reports 757,296 examined states. Compilation and invocation: `c++ -O2 -std=c++17 code/verify_direct.cpp -o verify_direct && ./verify_direct`; `python3 code/verify_scan.py` runs the first checker.

The results are finite test evidence, not an infinite-size proof. The proof for every even order and every characteristic-two field is the explicit invertible coordinate transformation and its direct-sum decomposition in RESULT.md. The published general framework and the narrower one-edge case have been compared; historical priority outside inspected material remains a limitation.
