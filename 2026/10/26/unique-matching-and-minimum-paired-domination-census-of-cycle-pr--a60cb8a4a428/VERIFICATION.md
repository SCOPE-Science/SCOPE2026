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

# Verification

The finite checkers use distinct enumerations. Compile `verify_minima.cpp` with `g++ -O3 -std=c++17 verify_minima.cpp -o verify_minima` and run it from the package directory. This enumerates labelled vertex sets on \(C_n\square K_2\) for \(n=5,8,11,14,17\), checks domination directly, then checks whether the induced graph has a perfect matching, producing counts \(25,56,99,154,221\).

Run `python3 verify_shapes.py` to enumerate dominating matchings separately for \(n=5,8,11,14\), producing counts \(25,56,99,154\) and the unique two-column short gap in each matching. Both scripts completed with `VERIFY_OK`. These exhaustive finite checks do not prove the theorem for arbitrary \(n\); the all-length proof in RESULT.md does. No independent external audit was performed.
