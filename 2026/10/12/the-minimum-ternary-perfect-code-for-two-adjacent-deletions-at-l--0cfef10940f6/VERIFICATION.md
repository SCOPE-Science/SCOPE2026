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

Run `python3 verify.py` in this directory. It verifies the explicit perfect-code partition and completely checks the absence of a covering code with at most seven codewords over the 243 possible ternary length-five words. Expected output starts `VERIFY_OK 243 27 witness 8 states 649`.

For a separate implementation, run `g++ -std=c++17 -O3 exhaustive_lower.cpp -o exhaustive_lower && ./exhaustive_lower`. The implementation uses integer bit masks; it reports `SEVEN_WORD_COVER_EXISTS? 0 NODES 735 STATES 649`. Both searches use a proven-safe necessary coverage bound and memoization, not a solver status. The result is a finite exhaustive certificate only.
